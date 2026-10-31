# Troubleshooting

Fix environment problems early: a student who cannot run code cannot learn. Ask them to read you the **last line**
of the error message first.

## Installing and running

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `uv: command not found` / `'uv' is not recognized` | Terminal opened before install; PATH not refreshed | Close **all** terminals and VS Code, reopen. Still failing: re-run the installer and read its last lines (it prints where uv was installed) |
| Windows: installer blocked ("running scripts is disabled") | PowerShell execution policy | Use the exact command in [environment.md](environment.md) (it includes `-ExecutionPolicy ByPass`) |
| Windows: typing `python` opens the Microsoft Store | Store "app execution alias" | Use `uv run python …` instead of `python …`, or disable the alias in *Settings → Apps → App execution aliases* |
| `error: No pyproject.toml found` | Running uv outside the project folder | `cd` into the folder that contains `pyproject.toml` (`ls` / `dir` to check) |
| `No such file or directory: hello.py` | Terminal is in a different folder | `cd` to the file's folder, or use VS Code's **Terminal → New Terminal** after opening the project folder |
| uv downloads fail | Proxy, firewall or offline | Try another network; if only the Python download fails, `uv python install 3.13` once on a working network |
| Anaconda/conda installed: wrong Python is used | `(base)` conda environment auto-activates | Always run through uv (`uv run …`). Optionally: `conda config --set auto_activate_base false` |
| Permission errors on Windows in OneDrive folders | Synced folders lock files | Keep the course project in a normal folder like `C:\code\python-class` |
| Odd errors with paths containing spaces or non-English characters | Some tools mishandle such paths | Use a simple path without spaces |

## Notebooks in VS Code

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Running cells requires the ipykernel package" | ipykernel not in the project | `uv add ipykernel`, then pick the `.venv` kernel again |
| `.venv` kernel not listed | VS Code has not noticed the new environment | Command Palette → **Developer: Reload Window**; or **Select Kernel → Select Another Kernel → Python Environments** |
| `ModuleNotFoundError: No module named 'pandas'` | Wrong kernel selected, or package not added | Check the kernel name (top right) is `.venv`; `uv add pandas` in the same project; restart the kernel |
| `NameError` for a variable you can see defined above | That cell was not run (or the kernel restarted) | Run cells top to bottom; when confused use **Restart** then **Run All** |
| A cell shows `[*]` forever | Infinite loop, or waiting for `input()` | Look for the input box at the **top** of VS Code; otherwise press **Interrupt** (■) |
| `input()` box does not appear | It appears in the command bar at the top of the window, not in the cell | Look up; press Enter to submit |
| `FileNotFoundError` when reading a dataset | Notebook working directory differs | VS Code runs notebooks from the notebook's own folder. Check with `from pathlib import Path; print(Path.cwd())`. Lessons use `Path("../../../datasets/…")` |
| Changes to my own `.py` module are ignored | Python caches imported modules | Restart the kernel after editing a module (Day 26) |
| Plots do not appear | Plot cell has no `plt.show()` or errored earlier | Add `plt.show()`; re-run the cell |

## Running tests (Week 6 onwards)

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `pytest: command not found` | Not using uv | `uv run pytest` |
| `ModuleNotFoundError` inside a test | Running pytest from the wrong folder | `cd` into the folder that contains both the module and `test_*.py`, then `uv run pytest` |
| `collected 0 items` | Test file or functions not named `test_…` | Rename: file `test_reports.py`, functions `def test_total():` |

## LLM / API (Week 11 onwards)

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Output says it came from the mock model | No `ANTHROPIC_API_KEY` found (this is the intended offline behaviour) | Only if you want the real API: create `.env` from `.env.example` in the project root and restart the kernel |
| `AuthenticationError` | Key mistyped, revoked or has extra spaces/quotes | Paste the key again with no quotes or spaces after `=` |
| `RateLimitError` | Too many requests at once (a whole class sharing one key) | Wait and retry; let students use the mock; demo the real API from one machine |
| `NotFoundError` mentioning the model | Misspelt `LLM_MODEL` | Use an exact model ID such as `claude-opus-5-5` or `claude-haiku-5-5` |
| `APIConnectionError` | No internet / blocked by firewall | Use the mock (it is the default when offline) |

## When nothing works

1. Ask the student to run `uv --version` and `uv run python --version` and show you the output.
2. Create a fresh test project: `uv init test-setup && cd test-setup && uv add ipykernel && uv run python -c "print('ok')"`.
3. If that works, the problem is in their original folder (wrong folder opened or wrong kernel), so compare.
4. Pair the student with a neighbour for the lesson and fix the setup during a break. Don't stall the class.
