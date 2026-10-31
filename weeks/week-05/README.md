# Week 5: Practical Python Skills

**Goal:** students stop writing everything by hand and start using Python's toolbox: built-ins and comprehensions
for working with collections, files for reading and saving data, and exceptions for surviving bad input. By Friday
their programs read real text files, save results, and no longer crash on a typo from the user. These are the
skills Project 03 (Expense Tracker, Day 30) is built on.

| Day | Topic | Lesson | Demo | Practice | Solutions |
|-----|-------|--------|------|----------|-----------|
| 21 | Built-in functions & useful methods | [lesson](day-21-built-in-functions/lesson.md) | [demo](day-21-built-in-functions/demo.ipynb) | [practice](day-21-built-in-functions/practice.ipynb) | [solutions](day-21-built-in-functions/solutions.ipynb) |
| 22 | Comprehensions | [lesson](day-22-comprehensions/lesson.md) | [demo](day-22-comprehensions/demo.ipynb) | [practice](day-22-comprehensions/practice.ipynb) | [solutions](day-22-comprehensions/solutions.ipynb) |
| 23 | Reading text files | [lesson](day-23-reading-files/lesson.md) | [demo](day-23-reading-files/demo.ipynb) | [practice](day-23-reading-files/practice.ipynb) | [solutions](day-23-reading-files/solutions.ipynb) |
| 24 | Writing files & `pathlib` | [lesson](day-24-writing-files-pathlib/lesson.md) | [demo](day-24-writing-files-pathlib/demo.ipynb) | [practice](day-24-writing-files-pathlib/practice.ipynb) | [solutions](day-24-writing-files-pathlib/solutions.ipynb) |
| 25 | Exceptions & defensive input | [lesson](day-25-exceptions/lesson.md) | [demo](day-25-exceptions/demo.ipynb) | [practice](day-25-exceptions/practice.ipynb) | [solutions](day-25-exceptions/solutions.ipynb) |

**Assessment:** [Week 5 checkpoint](../../assessments/weekly/week-05-checkpoint.md), 15 minutes at the end of Day 25
(paper, individual). There is no project this week; the next one is
[Project 03: Expense Tracker](../../projects/03-expense-tracker/) on Day 30.

**Data files:** `day-23-reading-files/data/` (class diary, attendance log, shopping list, temperatures) and
`day-25-exceptions/data/` (messy marks file, step counts). They are small, original and deliberately messy
(blank lines, bad values). Notebooks only read them; Day 24 notebooks create new files in their own folder.

## Prepare before the week

- [ ] Run `uv run python scripts/validate_notebooks.py weeks/week-05` from the course root (all notebooks should say `ok`).
- [ ] Make sure students copy whole **day folders**, including `data/`, not just the notebooks.
- [ ] Open one Day 23 notebook on a Windows machine if possible and confirm `Zoë` displays correctly (it does with `encoding="utf-8"`).
- [ ] Check that VS Code runs notebooks from the notebook's own folder (default setting), so `data/...` paths work.
- [ ] Print one copy of the Week 5 checkpoint per student for Day 25.
- [ ] Have two or three students' Hangman projects (Day 20) ready: several homework tasks ask them to improve their own code.

## Common difficulties this week

| Difficulty | How to respond |
|------------|----------------|
| `key=len()` / `key=by_score()` with brackets (Day 21) | "Hand over the tool, don't use it yet." Say *pass the name* every time it comes up |
| Filter `if` placed before `for` in a comprehension, or one giant unreadable comprehension (Day 22) | Read it aloud; if it does not fit in one breath, move parts into a named function or use a loop |
| Double-spaced output and `"milk\n" != "milk"` (Day 23) | Show the list of raw lines so the `\n` becomes visible; strip first, then compare or split |
| `FileNotFoundError` for a file that "is right there" (Days 23–24) | Ask "where is Python standing?" Print `Path.cwd()` and compare with the path. Usually the `data` folder was not copied or the script was run from another folder |
| Losing data with `"w"`, or `"a"` cells run twice in a notebook (Day 24) | Keep the mode table on the board; demonstrate only on throw-away files |
| Bare `except:` or one huge `try` around everything (Day 25) | Run the typo example from demo section 7; insist on naming the exception and keeping `try` blocks small |
