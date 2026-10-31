"""Execute and check every course notebook.

Run from the course root:

    uv run python scripts/validate_notebooks.py                  # everything
    uv run python scripts/validate_notebooks.py weeks/week-01    # one folder
    uv run python scripts/validate_notebooks.py --write-outputs  # also save outputs into solutions

Checks performed:
  * valid notebook JSON (nbformat schema)
  * every cell executes top-to-bottom in a fresh kernel, offline (API keys removed)
  * cells tagged "raises-exception" really do raise (they demonstrate errors on purpose)
  * input() is answered from the notebook's metadata "course.mock_inputs" list
  * nothing that looks like a secret/API key is present
  * the run does not modify existing files (new files it creates are cleaned up)
  * each day folder has lesson.md, demo.ipynb, practice.ipynb, solutions.ipynb
    and the exercise numbers in practice and solutions match
"""

import argparse
import hashlib
import os
import re
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import nbformat
from nbclient.client import NotebookClient

ROOT = Path(__file__).resolve().parent.parent
SECRET = re.compile(r"sk-ant-[A-Za-z0-9_-]{10,}|sk-[A-Za-z0-9]{32,}|api_key\s*=\s*['\"][A-Za-z0-9_-]{16,}['\"]")
EXERCISE = re.compile(r"^#+\s*Exercise\s+(\d+[a-z]?)\b", re.IGNORECASE | re.MULTILINE)
DAY_FILES = ["lesson.md", "demo.ipynb", "practice.ipynb", "solutions.ipynb"]

SETUP_CELL = """
_course_mock_inputs = list({inputs!r})
def _course_input(prompt=""):
    if not _course_mock_inputs:
        raise RuntimeError("input() was called but the notebook metadata has no mock_inputs left")
    value = _course_mock_inputs.pop(0)
    print(f"{{prompt}}{{value}}")
    return value
get_ipython().kernel.raw_input = _course_input
del _course_input
"""


def snapshot(folder: Path) -> dict:
    return {
        p: hashlib.md5(p.read_bytes()).hexdigest()
        for p in folder.rglob("*")
        if p.is_file() and ".ipynb_checkpoints" not in p.parts and "__pycache__" not in p.parts
    }


def run_one(path_str: str, write_outputs: bool) -> tuple[str, list[str], float]:
    path = Path(path_str)
    problems = []
    start = time.time()
    raw = path.read_text(encoding="utf-8")
    if SECRET.search(raw):
        problems.append("possible secret/API key found")
    nb = nbformat.reads(raw, as_version=4)
    try:
        nbformat.validate(nb)
    except nbformat.ValidationError as exc:
        return path_str, [f"invalid notebook: {exc.message}"], 0.0

    inputs = nb.metadata.get("course", {}).get("mock_inputs", [])
    nb.cells.insert(0, nbformat.v4.new_code_cell(SETUP_CELL.format(inputs=inputs)))

    for key in ("ANTHROPIC_API_KEY", "OPENAI_API_KEY"):
        os.environ.pop(key, None)
    os.environ["COURSE_OFFLINE"] = "1"

    folder = path.parent
    before = snapshot(folder)
    client = NotebookClient(nb, timeout=180, kernel_name="python3", extra_arguments=["--log-level=ERROR"],
                            resources={"metadata": {"path": str(folder)}})
    try:
        client.execute()
    except Exception as exc:  # report the failing cell without a giant traceback
        lines = re.sub(r"\x1b\[[0-9;]*m", "", str(exc)).strip().splitlines()
        problems.append("execution failed: " + " | ".join(lines[-3:])[:600])
    finally:
        after = snapshot(folder)
        for p, digest in before.items():
            if after.get(p) != digest:
                problems.append(f"modified or deleted an existing file: {p.relative_to(ROOT)}")
        for p in set(after) - set(before):
            p.unlink(missing_ok=True)
        for d in sorted((d for d in folder.rglob("*") if d.is_dir()), reverse=True):
            if not any(d.iterdir()) and d not in {q.parent for q in before}:
                d.rmdir()

    nb.cells.pop(0)
    for cell in nb.cells:
        if cell.cell_type == "code" and "raises-exception" in cell.metadata.get("tags", []):
            if not any(o.get("output_type") == "error" for o in cell.get("outputs", [])) and not problems:
                problems.append("a cell tagged raises-exception did not raise: "
                                + cell.source.splitlines()[0][:60])

    is_reference = path.name == "solutions.ipynb" or "reference" in path.parts
    if write_outputs and is_reference and not problems:
        nbformat.write(nb, path)
    return path_str, problems, time.time() - start


def run_folder(paths: list[str], write_outputs: bool) -> list[tuple[str, list[str], float]]:
    # Notebooks sharing a folder run one after another so their temporary files never collide.
    results = []
    for p in paths:
        result = run_one(p, write_outputs)
        if any("Kernel died" in problem for problem in result[1]):
            result = run_one(p, write_outputs)  # rare port clash between parallel kernels: retry once
        results.append(result)
    return results


def check_structure(day: Path) -> list[str]:
    problems = [f"missing {name}" for name in DAY_FILES if not (day / name).exists()]
    if not problems:
        ids = {}
        for name in ("practice.ipynb", "solutions.ipynb"):
            nb = nbformat.read(day / name, as_version=4)
            text = "\n".join(c.source for c in nb.cells if c.cell_type == "markdown")
            ids[name] = EXERCISE.findall(text)
        if ids["practice.ipynb"] != ids["solutions.ipynb"]:
            problems.append(f"exercise numbers differ: practice={ids['practice.ipynb']} "
                            f"solutions={ids['solutions.ipynb']}")
        if not ids["practice.ipynb"]:
            problems.append("no '## Exercise N' headings found in practice.ipynb")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", default=["weeks", "projects"])
    parser.add_argument("--write-outputs", action="store_true", help="save executed outputs into solutions/reference notebooks")
    parser.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 2) // 2))
    args = parser.parse_args()

    notebooks, days = [], set()
    for p in args.paths:
        base = (ROOT / p).resolve()
        found = [base] if base.suffix == ".ipynb" else sorted(base.rglob("*.ipynb"))
        notebooks += [n for n in found if ".ipynb_checkpoints" not in n.parts]
        if base.is_dir():
            days |= {d for d in base.rglob("day-*") if d.is_dir()}
            if base.name.startswith("day-"):
                days.add(base)

    failures = 0
    for day in sorted(days):
        for problem in check_structure(day):
            failures += 1
            print(f"FAIL  {day.relative_to(ROOT)}: {problem}")

    by_folder: dict[Path, list[str]] = {}
    for n in notebooks:
        by_folder.setdefault(n.parent, []).append(str(n))
    with ProcessPoolExecutor(max_workers=args.jobs) as pool:
        futures = [pool.submit(run_folder, paths, args.write_outputs) for paths in by_folder.values()]
        results = [r for fut in futures for r in fut.result()]
        for path_str, problems, seconds in results:
            rel = Path(path_str).relative_to(ROOT)
            if problems:
                failures += 1
                for problem in problems:
                    print(f"FAIL  {rel}: {problem}")
            else:
                print(f"ok    {rel}  ({seconds:.1f}s)")

    print(f"\n{len(notebooks)} notebooks, {len(days)} day folders checked, {failures} problem(s).")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
