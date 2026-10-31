# Day 27: Packages, uv and Project Environments

**Week 6 · Session 27 of 60 · Planned 75 min** · Previous: [Day 26](../day-26-modules-imports/lesson.md) · Next: [Day 28](../day-28-debugging/lesson.md)

## Objectives

By the end of this lesson students can:

1. Explain in one sentence why each project gets its own virtual environment (`.venv`).
2. Create a uv project outside the course folder, add and remove a dependency, and run a script with `uv run`.
3. Read a `pyproject.toml` line by line and say what `uv.lock` adds (exact versions of *every* package).
4. Rebuild a deleted `.venv` with `uv sync`, and explain why `.venv` is never shared.
5. Import from a package (a folder of modules with `__init__.py`) using `from package import module` and
   `from package.module import name`.

**Prior knowledge:** `uv run hello.py` (Day 01), writing and importing own modules, `__name__` (Day 26),
`pathlib` and `.read_text()` (Day 24), list comprehensions (Day 22).

**Files:** `demo.ipynb` (you) · `practice.ipynb` (students) · `solutions.ipynb` (you) · `shop/` (example package:
`__init__.py`, `prices.py`, `stock.py`)

**Before class:** run the terminal lab below once on the classroom machine. `uv add rich` needs internet; if
the room has none, pre-download it at home (uv keeps a cache) or demo from your laptop and let students do the lab
at home.

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: retrieval on Day 26 | core |
| 0:05–0:15 | Why environments? Demo 1–4 (which Python, where packages live, a missing package) | core |
| 0:15–0:37 | Terminal lab: `uv init` → `uv run` → `uv add rich` → `pyproject.toml` / `uv.lock` → `uv remove` / `uv sync` | core |
| 0:37–0:47 | Packages: the `shop` folder (demo 6–7) | core |
| 0:47–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (challenge) or `uv tree` + `uv add --dev pytest` in the lab project | optional (90-min session) |

For a 60-minute session: skip demo 5 (the course's own lock file) and demo 8, and set Exercise 4 as homework.

## 1. Warm-up (5 min)

1. "Three ways to import `ceil` from `math`?" (*`import math` → `math.ceil`; `from math import ceil`; `import math as m` → `m.ceil`*)
2. "What is `__name__` inside a file that was imported?" (*the module's name, not `"__main__"`*)
3. "Where did `textutils` come from, and where did `math` come from?" (*our folder · Python itself*). Today adds a
   third source: packages downloaded from the internet.

## 2. Why environments? (10 min)

**Problem first.** Tell the story in demo section 4: Sara's new expense app needs pandas 2.2, but her old thesis
code only works with pandas 1.5. With one shared Python, installing one breaks the other. A second problem is
"it works on my machine": a classmate runs your code with different versions and it crashes.

> **Analogy:** each project gets its own **toolbox** (`.venv`). `pyproject.toml` is the *shopping list* you
> wrote ("a hammer, at least size 3"). `uv.lock` is the *receipt*: the exact brand and model of every tool
> bought, including the screws the hammer needed. With the receipt, anyone can rebuild an identical toolbox.

Live (demo sections 1–3):
- `sys.executable` ends in `.venv/bin/python` (Windows `.venv\Scripts\python.exe`): the notebook runs the course's environment.
- `random.__file__` is inside Python's own folder; `pytest.__file__` is inside `.venv/.../site-packages`.
- `import rich` → `ModuleNotFoundError`. **Prediction question:** "How do we fix this?" Many will say
  `pip install rich` in the notebook. The answer is `uv add rich` in the terminal, inside the right project.

## 3. Terminal lab: your own uv project (22 min)

Students type along. Do it **outside the course folder**: if you run `uv init` inside the course folder, uv adds
the new project to the *course* project (it prints "Adding … as member of workspace" and edits the course
`pyproject.toml`).

```
cd ~                        # Windows PowerShell: cd ~ works too
mkdir python-projects
cd python-projects
uv init budget-buddy
cd budget-buddy
```

Open the folder in VS Code (*File → Open Folder*, or `code .`). `uv init` created `pyproject.toml`,
`.python-version`, `README.md`, `.gitignore` and `main.py` (uv older than 0.6 calls it `hello.py`).

```
uv run main.py
```

Output: `Hello from budget-buddy!`. The first `uv run` also created `.venv/` and `uv.lock`. Point out that
`main.py` already uses Day 26's `if __name__ == "__main__":`.

```
uv add rich
```

uv installs `rich` **and** `markdown-it-py`, `mdurl`, `pygments`. **Prediction question:** "We asked for one
package. Why four?" (*rich needs the others: dependencies of dependencies.*) Now replace `main.py` with:

```python
from rich import print
from rich.table import Table


def main():
    print("[bold green]Budget Buddy[/bold green] is running!")

    table = Table(title="November budget")
    table.add_column("Item")
    table.add_column("Amount", justify="right")
    table.add_row("Rent", "450.00")
    table.add_row("Food", "180.50")
    table.add_row("Transport", "42.00")
    print(table)


if __name__ == "__main__":
    main()
```

`uv run main.py` prints a green title and a boxed table. `Table(...)` creates a table *object* and
`.add_row(...)` is a method, just like `"text".upper()`. We will build our own objects in Week 7.

**`pyproject.toml` line by line** (open it after `uv add rich`):

| Line | Meaning |
|------|---------|
| `[project]` | section header: facts about this project |
| `name = "budget-buddy"` | the project's name |
| `version = "0.1.0"` | **your project's** version (not Python's, not rich's) |
| `description`, `readme` | a one-line summary and the file that explains the project |
| `requires-python = ">=3.13"` | the oldest Python this project accepts |
| `dependencies = ["rich>=15.0.0"]` | packages the app needs to **run**, with a *minimum* version. `uv add` / `uv remove` edit this list |

Optional: `uv add --dev pytest` adds a `[dependency-groups]` section with `dev = ["pytest>=…"]`. These are tools
for developing, not for running the app. We use pytest on Day 29.

**`uv.lock`** (open it, scroll, do not edit): a `[[package]]` block for *every* installed package with its
**exact** `version`, its `source` (PyPI), its own `dependencies`, and download URLs with a `hash`, a fingerprint
uv uses to check the download was not changed. The project itself appears with `source = { virtual = "." }`.
Rule: commit `pyproject.toml` and `uv.lock`; never edit `uv.lock` by hand; never commit `.venv` (`.gitignore`
already lists it).

Then show removal and rebuilding:

```
uv remove rich        # rich and its 3 helpers are uninstalled; pyproject is back to dependencies = []
uv add rich           # back again
```

Delete the `.venv` folder in VS Code's Explorer, then:

```
uv sync               # rebuilds .venv exactly from uv.lock
uv run main.py        # works again
```

Message: `.venv` is disposable; `pyproject.toml` + `uv.lock` are the real information. Demo section 5 shows the
same two files for the course itself: 8 packages requested, 77 pinned (the exact count may change if the course
dependencies are updated).

## 4. Packages: folders of modules (10 min)

Show the `shop/` folder tree (demo section 6). A **package** is a folder with an `__init__.py`; Python runs
`__init__.py` once on first import. The dot in `shop.prices` means "the `prices` module inside the `shop` folder",
like a path.

```python
import shop
print(shop.SHOP_NAME)                        # Corner Shop
from shop import prices
print(prices.add_tax(10))                    # 11.5
from shop.prices import apply_discount
print(apply_discount(80, 25))                # 60.0
import shop.stock
print(shop.stock.restock_list({"milk": 3, "bread": 12, "eggs": 4, "rice": 20}))   # ['eggs', 'milk']
```

Clarify the two meanings of "package": a folder of modules (today's `shop`), and something you install with
`uv add` (a folder of modules that someone published, like `rich`). Same idea, different source.

## 5. Common mistakes (included in the timing above)

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `import prices` (module inside a package) | `ModuleNotFoundError: No module named 'prices'` | it lives in `shop/`: `from shop import prices` |
| `from shop import add_tax` | `ImportError: cannot import name 'add_tax' from 'shop'` | `add_tax` is in `shop/prices.py`, not in `__init__.py` |
| `pip install rich` | installs into the wrong Python, `pyproject.toml` unchanged | `uv add rich` inside the project folder |
| `python main.py` instead of `uv run main.py` | `ModuleNotFoundError: No module named 'rich'` | only `uv run` guarantees the project's `.venv` |
| `uv init` inside the course folder | course `pyproject.toml` gets a `[tool.uv.workspace]` section | delete the folder and those lines; create projects elsewhere |
| `uv add` in the wrong folder | package added to the wrong project | check the prompt or `pwd`; look for `pyproject.toml` |

## 6. Practice (23 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Environment detective | `sys.executable`, `importlib.metadata.version` | recall |
| 2 Which uv command? | choosing `init / add / run / sync / remove / --dev` | recall |
| 3 Read a `pyproject.toml` | minimum versions vs exact versions, dev dependencies | reasoning |
| 4 A receipt from the `shop` package | importing from a package | application |
| 5 Your own uv project | the terminal lab, written up as answers | application |
| 6 A package inside your project (challenge) | creating a package and importing it from `main.py` | challenge |

While circulating, look for: a notebook kernel that is not the course `.venv` (Exercise 1 prints `False`),
projects created inside the course folder, `pip install` habits from online tutorials, and `from shop import add_tax`.

Expected outcome: everyone finishes 1–4 and the lab; most write up Exercise 5; fast students do 6.

## 7. Recap and exit ticket (5 min)

1. One project = one `.venv`; uv creates and fills it.
2. `uv init` · `uv add` · `uv remove` · `uv run` · `uv sync`.
3. `pyproject.toml` = what you asked for (minimum versions). `uv.lock` = exactly what was installed.
4. A package is a folder of modules with `__init__.py`: `from shop.prices import add_tax`.

**Exit ticket:** "Omar sends you his project folder: `main.py`, `pyproject.toml`, `uv.lock`. There is no `.venv`.
What do you type to run it, and why will you get the same package versions as Omar?"

Answer: `uv sync` then `uv run main.py` (or just `uv run main.py`, which syncs first). `uv.lock` pins the exact
version of every package, so uv installs the same versions he has.

## Homework (20 min)

Finish Exercise 5's answers. In `budget-buddy`, add a fourth table row with your own expense and run it.
Optional: Exercise 6.

## Next class

Day 28 is about what to do when code breaks: reading a traceback from the bottom up, the most common error types,
print debugging and the VS Code debugger (breakpoints, stepping, the Variables panel). Teaser: the traceback you
saw for `import rich` today has the same structure as every Python error, and tomorrow we learn to read it fully.

## Instructor notes

- Do **not** go into `pip`, `venv`/`virtualenv`, conda, `requirements.txt`, publishing packages, relative imports
  (`from . import prices`) or `__init__.py` re-exports. If asked: "uv does those jobs for us; you will meet the
  others in other people's projects, and the ideas are the same."
- `sys.path` (the list of folders Python searches for imports) can be shown to curious students with
  `print(sys.path[:3])`. The notebook's own folder is in it, which is why Day 26's `import textutils` worked.
- Windows: `.venv\Scripts\python.exe` instead of `.venv/bin/python`. If `uv` is "not recognised", the terminal was
  opened before installation, so close and reopen VS Code.
- If `uv add` fails behind a proxy or without internet, students can still do Exercises 1–4 and read
  `pyproject.toml` / `uv.lock` in the course folder. Do the lab at home.
- Version numbers in this lesson (rich 15.0.0, pytest 9.1.1) are whatever was newest when the course was written;
  students will see newer numbers. That is fine and illustrates `>=`.
- Fast students: `uv tree` prints the dependency tree; ask them to explain why `pygments` appears under rich.
- Slow students: make sure everyone finishes `uv init` → `uv add rich` → `uv run main.py`. That sequence is what
  Project 03 and the capstones rely on.
