# Week 6: Working Like a Python Developer

Students move from single notebooks to how real Python code is organised: modules and packages, project
environments managed by uv, systematic debugging and automated tests with pytest. The week ends with Project 03,
a multi-file Expense Tracker with its own tests, which is the template for every later project.

| Day | Topic | Materials |
|-----|-------|-----------|
| 26 | Modules and imports | [lesson](day-26-modules-imports/lesson.md) · [demo](day-26-modules-imports/demo.ipynb) · [practice](day-26-modules-imports/practice.ipynb) · [solutions](day-26-modules-imports/solutions.ipynb) |
| 27 | Packages, uv and project environments | [lesson](day-27-packages-uv/lesson.md) · [demo](day-27-packages-uv/demo.ipynb) · [practice](day-27-packages-uv/practice.ipynb) · [solutions](day-27-packages-uv/solutions.ipynb) |
| 28 | Debugging and tracebacks | [lesson](day-28-debugging/lesson.md) · [demo](day-28-debugging/demo.ipynb) · [practice](day-28-debugging/practice.ipynb) · [solutions](day-28-debugging/solutions.ipynb) |
| 29 | Testing with assertions and pytest | [lesson](day-29-testing/lesson.md) · [demo](day-29-testing/demo.ipynb) · [practice](day-29-testing/practice.ipynb) · [solutions](day-29-testing/solutions.ipynb) |
| 30 | 🏗 Project 03: Expense Tracker | [lesson](day-30-project-expense-tracker/lesson.md) · [demo](day-30-project-expense-tracker/demo.ipynb) · [practice](day-30-project-expense-tracker/practice.ipynb) · [solutions](day-30-project-expense-tracker/solutions.ipynb) |

**Project:** [Project 03: Expense Tracker](../../projects/03-expense-tracker/README.md)
([instructor notes](../../projects/03-expense-tracker/INSTRUCTOR.md)) · **Checkpoint:**
[Checkpoint 6](../../assessments/weekly/week-06-checkpoint.md) (end of Day 30 or start of Day 31)

Supporting files live in the day folders: `textutils.py`, `name_demo.py` (Day 26), the `shop/` package (Day 27),
`buggy_grades.py` (Day 28; keep the bugs in the provided copy), `grades.py` + `test_grades.py` and `checkout.py`
(Day 29), `reading_log.txt` (Day 30). Files named `solution_*.py` are instructor references.

## Prepare before the week

- [ ] Day 26: run `uv run textutils.py` and `uv run name_demo.py` in their folder; both print without errors.
- [ ] Day 27: check that the classroom has internet for `uv add rich`, or pre-run the lab at home (uv caches packages).
      Decide where students create projects **outside** the course folder (e.g. `~/python-projects`).
- [ ] Day 28: VS Code's **Python Debugger** extension works: open `buggy_grades.py`, press F5, it stops on the
      `ZeroDivisionError`.
- [ ] Day 29: `cd weeks/week-06/day-29-testing && uv run pytest` → `11 passed`.
- [ ] Day 30: `cd projects/03-expense-tracker/reference && uv run pytest -q` → `21 passed`; starter → `4 failed`
      (by design). Print Checkpoint 6.

## Common difficulties this week

1. **"I changed my module but nothing happened."** The notebook cached the old import. Restart the kernel (Day 26).
   This comes up every day this week; make it a class mantra.
2. **Wrong folder, wrong Python.** `ModuleNotFoundError` usually means the terminal is in another folder or the
   notebook kernel is not the project's `.venv`. Ask "where are you?" (`pwd`) and "which kernel?" before anything else.
3. **`uv init` inside the course folder** adds a workspace entry to the course `pyproject.toml`. Undo it by deleting
   the folder and the `[tool.uv.workspace]` lines it added, then create projects elsewhere.
4. **Guessing instead of debugging.** When a student changes random lines, stop them and walk the six steps from
   Day 28 together: reproduce → read → locate → hypothesise → check → fix.
5. **Tests that cannot fail** (prints instead of asserts, test functions never called, or only "normal" cases). Ask
   "which bug would this test catch?". If the answer is "none", it needs an edge case.
