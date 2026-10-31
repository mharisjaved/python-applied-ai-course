# Project 03: Expense Tracker

**Week 6 · Day 30** · Builds on Days 21–29 · Work alone · Suggested deadline: start of Day 32 (your instructor confirms)

## The problem

Bilal wants to know where his money goes. Every evening he types what he spent into a notes app, but at the end of
the month he still has to add everything up by hand, and he has no idea how much went on food versus transport.

You will build him a **console Expense Tracker**: it records expenses, **saves them to a file** so they are still
there tomorrow, and answers questions like "how much did I spend on food?" and "what did November cost?".
It must never crash, whatever he types.

Unlike the Quiz Game and Hangman, this program is split into **three modules plus tests**, like real Python projects:

| File | Its one job | Talks to the user? |
|------|-------------|--------------------|
| `storage.py` | turn lines of the file into expense dicts and back; load and save | no |
| `reports.py` | calculations on a list of expenses (totals, largest, by month) | no |
| `main.py` | the menu: asks questions, prints answers, calls the other two | **yes** |
| `test_storage.py`, `test_reports.py` | pytest tests for the two modules above | no |

## What it should do

```
Welcome to the Expense Tracker!
Loaded 9 expenses from expenses.txt.

=== Expense Tracker ===
1) Add an expense
2) List all expenses
3) Summary by category
4) Monthly total
5) Quit
Choose 1-5: 1
Date (YYYY-MM-DD, Enter for today): 2026-11-16
Category (e.g. food, transport, rent): Food
Description: Lunch, with Asha
  Please don't use commas.
Description: Lunch with Asha
Amount: abc
  Please type a number, for example 12.50
Amount: 7.5
Saved: Lunch with Asha (7.50)

Choose 1-5: 3
entertainment       9.00
food               82.60
health             14.30
rent              450.00
transport          31.80
utilities          38.75
TOTAL             626.45
Largest expense: November rent, 450.00 on 2026-11-01

Choose 1-5: 4
Month (YYYY-MM, Enter for this month): 2026-11
2026-11: 8 expenses, total 565.45

Choose 1-5: 5
Goodbye! Your expenses are saved in expenses.txt.
```

(The menu is printed before every `Choose 1-5:`; it is left out above to save space.)

**The data file** has one expense per line: `date,category,description,amount`, for example
`2026-11-03,food,Lunch with Sara,12.50`. We split lines with `.split(",")`, which is why descriptions may not
contain commas. (On Day 36 you will meet the `csv` module, which handles commas inside values properly. That is a
good improvement for later.)

## Requirements

**Must** (needed to pass)
- [ ] Three modules, `storage.py`, `reports.py` and `main.py`, each doing only its own job (table above).
- [ ] `storage.py`: `parse_line(line)` → dict (raises `ValueError` for a bad line), `format_line(expense)` → text,
      `load_expenses(path)` (missing file → empty list; bad lines skipped with a warning), `save_expense(path, expense)`
      (appends one line).
- [ ] `reports.py`: `total`, `total_by_category` (→ dict), `largest_expense`, `expenses_in_month(expenses, "2026-11")`.
- [ ] Menu with: add · list · summary by category · monthly total · quit.
- [ ] Data **persists**: quit, run again, and your expenses are still there.
- [ ] **Never crashes** on bad input: letters or negative numbers as the amount, an invalid date, an invalid menu
      choice, an empty description, a broken line in the file.
- [ ] Date defaults to **today** when the user just presses Enter (`date.today()`).
- [ ] At least **6 passing pytest tests**, including the 4 provided and at least **2 of your own**, one of which
      checks an error with `pytest.raises`.

**Should** (for a good grade)
- [ ] The list is **sorted by date** and printed as a neat **table** with headings and aligned amounts.
- [ ] Summary shows categories A–Z, the overall total and the largest expense.
- [ ] 10 or more tests, covering every function in `storage.py` and `reports.py`.
- [ ] Every function has a docstring; no function is longer than about 20 lines.

**Could** (extensions)
- [ ] Delete an expense (hint: load all, remove one, write them all back with mode `"w"`).
- [ ] Budget warnings: a dict like `{"food": 200}` and a warning when a category goes over.
- [ ] Export a month to its own file (`2026-11.txt`) or as CSV after Day 36.
- [ ] Monthly total for every month at once (`"2026-10": 61.00`, `"2026-11": 565.45`).

## Starter files and how to run them

The `starter/` folder contains `storage.py`, `reports.py` and `main.py` with numbered `TODO` comments, two test
files and `sample_expenses.txt` (10 lines, one deliberately broken). Everything **runs** as given: the menu works,
but most options do nothing useful yet.

**Option A: work inside the course folder** (works offline, uses the course environment):

```
cd projects/03-expense-tracker/starter
uv run main.py
uv run pytest
```

**Option B: make it your own uv project** (recommended for your portfolio; needs internet once):

```
cd ~/python-projects
uv init expense-tracker
cd expense-tracker
uv add --dev pytest
```

Then copy the six starter files into `expense-tracker/` (replace the generated `main.py`) and use the same
`uv run main.py` / `uv run pytest` commands.

⚠️ **The provided tests fail until you complete the TODOs.** `uv run pytest` on the starter shows `4 failed`.
That is expected: your job is to turn them green.

Want to start with data? Copy `sample_expenses.txt` to `expenses.txt`. When the app starts you will see a warning
about line 8. That is the broken line, and your program should skip it, not crash.

## Build plan

Work in this order, and **run the tests after every step**.

1. **`parse_line` and `format_line`** (TODO 1–5). *Checkpoint:* `uv run pytest test_storage.py` → 2 passed.
   Add a test for `format_line`.
2. **`load_expenses` and `save_expense`** (TODO 6–7). *Checkpoint:* copy `sample_expenses.txt` to `expenses.txt`,
   run `uv run main.py`, choose 2: you see 9 expenses and one warning. Add an expense, quit, restart: it is still there.
3. **`reports.py`** (TODO 8–11). *Checkpoint:* `uv run pytest` → 4 passed. Add tests for `largest_expense` and
   `expenses_in_month` (including the `"2026-1"` trap).
4. **Safe input in `main.py`** (TODO 12–13). *Checkpoint:* try to crash your program: `abc`, `-5`, `0`,
   `2026-02-30`, a description with a comma, menu choice `7`. Nothing crashes.
5. **Summary and monthly total** (TODO 15–16), then the **table** (TODO 14, Should).
   *Checkpoint:* your output matches the example run above.
6. **Tidy up:** docstrings, names, remove debug prints, run `uv run pytest -v` one last time. Then try a Could.

Stuck? Use Day 28's process: reproduce → read the traceback bottom-up → print the values → fix one thing → re-run
the tests.

## Submission checklist

- [ ] `storage.py`, `reports.py`, `main.py`, `test_storage.py`, `test_reports.py` (and `pyproject.toml` + `uv.lock`
      if you used Option B). Do **not** submit `.venv`.
- [ ] `uv run pytest -v` output pasted into a file `test_results.txt`, all passing.
- [ ] A short `NOTES.md`: how to run it, which Should/Could items you did, and one bug you found and how.
- [ ] You can explain any function in your code in your own words.

## Evaluation rubric (100 points)

| Criterion | Points | What earns full marks |
|-----------|--------|------------------------|
| Works as specified | 40 | all Must items; data persists between runs |
| Code readability | 20 | clear names, small functions with docstrings, each module does only its own job |
| Handles bad input / edge cases | 15 | no crash for any input in build step 4 or for a broken file line |
| Testing | 10 | ≥ 6 passing tests incl. own tests and a `pytest.raises` test (10+ tests for full marks) |
| Explanation / demo | 15 | can explain how a line travels from the file to the summary, and why `main.py` is the only module that uses `input()` |

Project-specific criteria (included in the rows above):
- **Separation of jobs** (within readability): no `input()` or `print()` in `reports.py`; no file code in `main.py`.
- **Round trip** (within works as specified): `parse_line(format_line(e)) == e` for every expense.
- **Month filter** (within edge cases): `"2026-1"` does not match October or November.

## Extension ideas

- Replace `split(",")` with the `csv` module after Day 36, so descriptions may contain commas.
- A "search" option: all expenses whose description contains a word.
- Show the summary as a simple bar chart made of `#` characters, one `#` per 10 spent.
- Keep a second file of monthly budgets and show "spent / budget / left" per category.
