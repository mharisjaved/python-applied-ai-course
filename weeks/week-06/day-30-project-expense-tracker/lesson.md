# Day 30: Project 03, Expense Tracker

**Week 6 · Session 30 of 60 · Planned 75 min** · Previous: [Day 29](../day-29-testing/lesson.md) · Next: [Day 31](../../week-07/day-31-objects/lesson.md)

## Objectives

By the end of this session students can:

1. Explain the job of each module in a multi-file program (`storage.py`, `reports.py`, `main.py`) and why only
   `main.py` talks to the user.
2. Turn a line of a text file into a dict and back (`parse_line` / `format_line`) and check the round trip.
3. Load a data file that contains a broken line without crashing, and append new records to it.
4. Make the provided pytest tests pass one TODO at a time, and add tests of their own.
5. Complete Checkpoint 6.

**Prior knowledge:** everything from Weeks 5–6: `sorted(key=)` / `max(key=)` (Day 21), comprehensions (Day 22),
reading and writing files with `with open(...)` and `pathlib` (Days 23–24), `try/except ... as error`, `raise`
(Day 25), modules and `date` (Day 26), `uv run` (Day 27), tracebacks (Day 28), `assert` and pytest (Day 29).

**Files:** `demo.ipynb` (design + worked example on a reading log) · `practice.ipynb` (warm-ups on a workout log)
· `solutions.ipynb` · `reading_log.txt` (6 lines, one broken). Project:
[README.md](../../../projects/03-expense-tracker/README.md) (student brief) ·
[INSTRUCTOR.md](../../../projects/03-expense-tracker/INSTRUCTOR.md) · `starter/` · `reference/`. Checkpoint:
[week-06-checkpoint.md](../../../assessments/weekly/week-06-checkpoint.md).

**Before class:** in `projects/03-expense-tracker/reference` run `uv run pytest -q` (21 passed) and try the app with
`sample_expenses.txt` copied to `expenses.txt` (see INSTRUCTOR.md). Print the checkpoint.

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: retrieval on modules and tests | core |
| 0:05–0:15 | Read the brief together; run the reference app | core |
| 0:15–0:27 | Demo: module plan + reading-log worked example (demo 1–5) | core |
| 0:27–0:58 | Build: practice Exercises 1–3 (5 min), then project build steps 1–3 | core |
| 0:58–0:60 | Stand-up: "how many tests pass?" | core |
| 0:60–0:75 | Checkpoint 6 | core |
| +15 min | More build time (steps 4–5), with demo 6–7 (safe input, "Enter for today") shown first | optional (90-min session) |

For a 60-minute session: skip the practice warm-ups and demo 4, and give the checkpoint at the start of Day 31.

## 1. Warm-up (5 min)

Quick-fire, hands up:
1. "`import storage` works in `main.py`. What must be true about the two files?" (*same folder*)
2. "What does `if __name__ == "__main__":` protect?" (*code that should run only when the file is run directly*)
3. "A pytest function must start with…?" (*`test_`*) "…and the file?" (*`test_…py`*)
4. "`with pytest.raises(ValueError): f(x)`: when does this test fail?" (*when `f(x)` does NOT raise `ValueError`*)

## 2. The brief (10 min)

Open the [README](../../../projects/03-expense-tracker/README.md) on the projector. Read the story and the module table aloud;
then **run the reference app** (`cd projects/03-expense-tracker/reference`, copy `sample_expenses.txt` to
`expenses.txt`, `uv run main.py`). Show: the warning about line 8 at start-up, list (2), summary (3), month (4), adding
an expense with deliberate mistakes (`abc`, `-5`, a comma in the description), quitting and restarting to prove the
data was saved. Then `uv run pytest -v` in the same folder.

Go through **Must / Should / Could** and the rubric. Stress the two habits that get marks: *never crashes* and
*tests*. Show the build plan: steps 1–3 today in class, 4–6 as homework.

## 3. Demo: the design and a worked example (12 min)

Demo section 1: the module diagram. **Key idea:** `input()` makes a function impossible to test automatically,
so all talking lives in `main.py`, and `storage`/`reports` become pure functions that pytest checks in a second.
**Prediction question:** "Which module does 'keep asking until the amount is a number' belong in?" (*`main`: it
calls `input()`.*)

Demo sections 2–5 use a **reading log** (`date,book,pages`), deliberately not expenses, so students adapt the ideas
instead of copying code:

```python
entry = parse_entry("2026-11-02,Atomic Habits,35\n")
# {'date': '2026-11-02', 'book': 'Atomic Habits', 'pages': 35}
parse_entry(format_entry(entry)) == entry     # True: the round trip
load_entries("reading_log.txt")               # Warning: skipped line 5: invalid literal for int() ... -> 5 entries
entries_in_month(log, "2026-1")               # [] because of month + "-"
```

**Prediction question (demo 4):** "Why `month + "-"`?" Show that `startswith("2026-1")` matches both October and
November. This exact trap is a test in the project.

Differences to point out for the project: **4** values per line instead of 3; the amount is a `float`; the category is
lowercased; `parse_line` also checks the date with `date.fromisoformat` and rejects amounts ≤ 0.

## 4. Build time (31 min)

Students first do practice Exercises 1–3 (about 5 minutes; skip them for confident students), then open
`projects/03-expense-tracker/starter/`:

```
cd projects/03-expense-tracker/starter
uv run pytest            # 4 failed: the starting point
```

Students who prefer their own uv project follow Option B in the README (needs internet for `uv add --dev pytest`).

Build order (from the README): TODO 1–5 (`parse_line`, `format_line`) → `uv run pytest test_storage.py` →
TODO 6–7 (load/save) → try the app → TODO 8–11 (`reports.py`) → `uv run pytest` all green → own tests.

While circulating, ask "what does your test output say?" before looking at code. Typical problems are listed in
[INSTRUCTOR.md](../../../projects/03-expense-tracker/INSTRUCTOR.md#common-pitfalls-and-how-to-unblock-without-giving-the-answer).
Most frequent today:
- running from the wrong folder → `ModuleNotFoundError: No module named 'storage'`;
- `amount` left as a string (forgot `float`), so the `assert` shows `'12.50'` vs `12.5`;
- `save_expense` with `"w"` (overwrites) or without `"\n"` (everything on one line);
- `total_by_category` assigning instead of adding.

**Stand-up (2 min):** everyone says how many tests pass. Aim: storage tests green for most students by the end.

## 5. Common mistakes

| Mistake | Error / symptom | How to explain it |
|---------|-----------------|-------------------|
| `parse_line` returns the parts list, not a dict | `assert [...] == {...}` fails | the test shows the expected shape: read the `E` line |
| No try/except in `load_expenses` | app crashes at start-up on line 8 | one bad line should be skipped, not fatal |
| `print` inside `reports.py` instead of `return` | test gets `None` | print vs return (Day 17) |
| Comma allowed in the description | the next load skips that line | why `ask_text` refuses commas; the `csv` module (Day 36) fixes this properly |
| Tests use the real `expenses.txt` | tests pass or fail depending on what you typed in the app | tests use strings, small lists and `sample_expenses.txt` only |
| Copying the reading-log code unchanged | `expected 3 values, got 4` | the expense format has 4 values |

## 6. Checkpoint 6 (15 min)

Hand out [week-06-checkpoint.md](../../../assessments/weekly/week-06-checkpoint.md) (paper, closed notes, no computer).
Collect it and mark it with the answer key before Day 31; return it with one comment per student. If the build ran
long, give it at the start of Day 31 instead.

Exit ticket today = the checkpoint.

## Homework (2–3 hours over the next days)

Finish build steps 4–6 (safe input, summary, monthly total, table, own tests, `NOTES.md`). Submit by the
deadline in the README (suggested: start of Day 32). Practice Exercises 4–6 are optional extra help if the reports
or tests are hard.

## Next class

Week 7 starts **object-oriented programming**. Day 31 looks at "objects, state and behaviour": students will
model a bank account with a dict plus functions and feel where it gets messy, exactly like an expense dict passed
to many functions today. Teaser: "What if an expense could *format itself*, so `expense.format_line()` replaced
`format_line(expense)`?"

## Instructor notes

- Do **not** introduce `csv`, `json`, classes, `tmp_path` or other fixtures for this project. The brief deliberately
  uses `split(",")`; the comma limitation is a teaching point for Day 36.
- Run the reference only from inside its folder, and delete `expenses.txt` there afterwards. Never run pytest from
  `projects/03-expense-tracker/` itself: starter and reference both have `test_storage.py`, so pytest stops with
  "import file mismatch".
- The starter's 4 tests fail **on purpose**. Say so out loud, or some students will think the starter is broken.
- Struggling students: aim for build steps 1–3 and a working "add + list"; that is most of the Must list. Point them
  to practice Exercises 2–4, which mirror the project on simpler data.
- Fast students: Should items, then a Could (delete an expense or budget warnings), and more edge-case tests
  (amount `0`, `"2026-02-30"`, a description with spaces only).
- Grading guidance and timing for the following days are in [INSTRUCTOR.md](../../../projects/03-expense-tracker/INSTRUCTOR.md).
