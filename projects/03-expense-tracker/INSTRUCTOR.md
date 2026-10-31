# Project 03: Expense Tracker (instructor notes)

Student brief: [README.md](README.md) · Session plan: [Day 30 lesson](../../weeks/week-06/day-30-project-expense-tracker/lesson.md)
· Checkpoint: [week-06-checkpoint.md](../../assessments/weekly/week-06-checkpoint.md)

## What this project assesses

The first **multi-file** program: modules with one job each (Day 26), running with `uv run` (Day 27), debugging
(Day 28) and pytest (Day 29), on top of files (Days 23–24), exceptions (Day 25), dicts/lists and `sorted(key=)`
(Day 21). No classes, no `csv`/`json` (Days 32 and 36).

## Timing plan

| When | What |
|------|------|
| Day 30, 0:05–0:15 | Read the brief together; run the reference app (below) so students see the goal |
| Day 30, 0:15–0:27 | Demo notebook: the module plan and a worked example on a *different* file format (reading log) |
| Day 30, 0:27–0:60 | Build steps 1–3 (storage + reports until the provided tests pass) |
| Day 30, 0:60–0:75 | Checkpoint 6 (or move it to the start of Day 31) |
| Homework (2–3 h) | Build steps 4–6: safe input, summary, month, table, own tests, NOTES.md |
| Day 31, first 10 min (optional) | Stand-up: everyone shows `uv run pytest -v`; collect blockers |
| Start of Day 32 (suggested) | Submission |

**Running the reference live:**

```
cd projects/03-expense-tracker/reference
cp sample_expenses.txt expenses.txt      # Windows: copy sample_expenses.txt expenses.txt
uv run main.py
uv run pytest -v                          # 21 passed
```

Point out the warning about line 8 on start-up: the app *survives* a broken line. Delete `expenses.txt`
afterwards so the reference folder stays clean (it is never needed by the tests).

## How the reference was checked

- `cd projects/03-expense-tracker/reference && uv run pytest -q` → `21 passed`. The tests never modify
  `sample_expenses.txt`; the save test writes `test_save_tmp.txt` next to the tests and deletes it in `finally`.
- `main.py` was run with scripted input (`printf '2\n3\n4\n2026-11\n...' | uv run main.py`) covering every menu
  option, invalid month `2026-13`, invalid date `2026-02-30`, a description with a comma, amounts `abc` and `-5`,
  menu choice `9`, and a restart to confirm the added expense was saved.
- Starter: imports without errors, the menu runs, `uv run pytest` → `4 failed` (by design).

## Common pitfalls and how to unblock (without giving the answer)

| Symptom | Likely cause | Ask / hint |
|---------|--------------|------------|
| `ModuleNotFoundError: No module named 'storage'` | running from the wrong folder, or file named `Storage.py` | "Which folder is your terminal in? Is `storage.py` next to `main.py`?" |
| Test says `assert {} == {...}` | the TODO still returns the stub value | "Which function does this test call? What does it return right now?" |
| `amount` is `'12.50'` (a string) in the dict | forgot `float()` | "Print `type(expense['amount'])`. What should it be?" |
| `total_by_category` gives `{'food': 8.4}` | assigning instead of adding | Day 28 Exercise 3 again: print the dict inside the loop |
| `"2026-1"` matches October and November | `startswith(month)` without the `"-"` | "Which dates start with `2026-1`?" |
| Every expense lands on one line in the file | wrote `format_line(...)` without `"\n"` | "Open `expenses.txt`. What separates two expenses?" |
| Expenses vanish after restart | `"w"` instead of `"a"` in `save_expense` | "What does mode `w` do to an existing file (Day 24)?" |
| App crashes on start with a `ValueError` | `load_expenses` calls `parse_line` without try/except | "What should happen to *one* bad line?" |
| `input()` or `print()` inside `reports.py` | mixing jobs | "Could you test this function with pytest? Why not?" |
| Test file creates `expenses.txt` in the folder | test uses the real data file | tests read `sample_expenses.txt` and write only to a temp file they delete |
| Same expense appears twice after adding | appended to the list **and** reloaded the file | "Where does the new expense get into `expenses`?" |
| pytest: "import file mismatch" | ran `pytest` in `03-expense-tracker/` (collects starter **and** reference) | run inside one folder only |

Strong-student questions worth asking: "What happens if the file does not end with a newline and you append?"
(the new expense joins the last line, making a broken line). "Why keep the date as text, not a `date`?" (sorting
and month filtering work on strings; the file stores text anyway).

## Grading notes

Use the rubric in the README. Practical procedure (about 10 minutes per student):

1. `uv run pytest -v`: count passing tests and look for at least one `pytest.raises` test and own tests (Testing, 10).
2. Run the app on `sample_expenses.txt` (copied to `expenses.txt`): every menu option, then the "try to crash it"
   list from build step 4 (Works 40, Bad input 15).
3. Quit and restart: are the new expenses still there? Missing persistence costs most of the "Works" marks.
4. Read the code: `reports.py` has no `input`/`print`; `main.py` has no `open`; functions have docstrings and
   one job (Readability 20).
5. Ask two questions (Explanation 15), e.g. "Walk me through what happens to the line `2026-11-03,food,Lunch,12.50`
   from the file to the summary." and "Why does `expenses_in_month` add a `-`?"

Typical grade bands: all Must + tests passing ≈ 70–80; Must + Should ≈ 85–95; a Could or exceptional tests for
the rest. A program that crashes on `abc` as the amount cannot score more than 7/15 on bad input.

Academic honesty: the reference solution is in this repository. If students have access to it, rely more on the
explanation questions; students who copied usually cannot explain `get_amount` as a `key=` function or the `"-"`
in the month filter.
