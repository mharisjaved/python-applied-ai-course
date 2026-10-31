# Week 2: Data Structures & Decisions

**Goal:** by Friday every student can store related values in lists, tuples, dictionaries and sets, change and
inspect them without loops, and make programs decide with `if/elif/else`. The week ends with a tested
ticket-price calculator and **Checkpoint 2**. Day-by-day objectives are in the [roadmap](../../COURSE-ROADMAP.md).

| Day | Topic | Lesson | Demo | Practice | Solutions |
|-----|-------|--------|------|----------|-----------|
| 06 | Lists & indexing | [lesson](day-06-lists/lesson.md) | [demo](day-06-lists/demo.ipynb) | [practice](day-06-lists/practice.ipynb) | [solutions](day-06-lists/solutions.ipynb) |
| 07 | List methods, tuples & mutability | [lesson](day-07-list-methods-tuples/lesson.md) | [demo](day-07-list-methods-tuples/demo.ipynb) | [practice](day-07-list-methods-tuples/practice.ipynb) | [solutions](day-07-list-methods-tuples/solutions.ipynb) |
| 08 | Dictionaries & sets | [lesson](day-08-dicts-sets/lesson.md) | [demo](day-08-dicts-sets/demo.ipynb) | [practice](day-08-dicts-sets/practice.ipynb) | [solutions](day-08-dicts-sets/solutions.ipynb) |
| 09 | Booleans, comparisons & conditionals | [lesson](day-09-conditionals/lesson.md) | [demo](day-09-conditionals/demo.ipynb) | [practice](day-09-conditionals/practice.ipynb) | [solutions](day-09-conditionals/solutions.ipynb) |
| 10 | Decision problems + weekly review | [lesson](day-10-decisions-practice/lesson.md) | [demo](day-10-decisions-practice/demo.ipynb) | [practice](day-10-decisions-practice/practice.ipynb) | [solutions](day-10-decisions-practice/solutions.ipynb) |

**Assessment:** [Checkpoint 2](../../assessments/weekly/week-02-checkpoint.md), 20 min at the end of Day 10
(answer key below the `---` line; print only the questions). No project this week: lists, dicts and conditionals
all come together in the Quiz Game on Day 15.

**What students build this week:** class-marks report (D06) → shopping-list operations (D07) → contact book and
student record (D08) → grade calculator (D09) → ticket-price calculator with a test table (D10).

**No loops, no functions this week.** Everything is done with indexes, methods and built-ins
(`len/sum/min/max/sorted/in`). Testing means changing an input value and re-running the cell. That friction is
the motivation for loops (Day 11) and functions (Day 16), so do not shortcut it.

## Prepare before the week

- [ ] Note the weakest Checkpoint 1 question in `PROGRESS.md` and revisit it in the Day 06 warm-up (indexing and
      slicing matter most this week).
- [ ] Copy each day's `demo.ipynb` and `practice.ipynb` to students (never `solutions.ipynb`).
- [ ] Run every notebook once yourself: `uv run python scripts/validate_notebooks.py weeks/week-02`.
- [ ] Day 09 and Day 10 demos call `input()`: in VS Code the input box appears at the top of the window.
- [ ] Print Checkpoint 2 (questions only) for Day 10.

## Common difficulties this week and how to respond

1. **Off-by-one again (Days 06–07).** "The third item" is index 2; `[1:3]` stops before 3. Draw the locker table
   (index row + value row) for every new list until it becomes automatic.
2. **`my_list = my_list.sort()` (Day 07).** The list becomes `None`. Keep the rule on the board all week:
   *methods that change a list give back `None`*; use `sorted()` when you need a new list.
3. **Two names, one list (Day 07).** `b = a` does not copy a list. Use the Day 02 name-tag drawing: one list, two
   tags. `.copy()` makes a second list.
4. **`KeyError` and `{}` vs `set()` (Day 08).** Keys must match exactly (capitals!). Teach `in` and
   `.get(key, default)` as the safe options; an empty set is `set()`, `{}` is a dict.
5. **Silent logic bugs (Days 09–10).** Wrong `elif` order, `>` vs `>=`, `day == "Sat" or "Sun"`. These give no
   error, so insist on a test table with boundary rows and an "Actual" column students actually fill in.
