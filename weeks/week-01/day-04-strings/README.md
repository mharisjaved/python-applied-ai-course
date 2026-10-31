# Week 1: Getting Started with Python

**Goal:** by Friday every student can run Python from VS Code, store values in variables, calculate with numbers
the user types in, clean and slice text, and print neatly formatted output. The week ends with a formatted
receipt and **Checkpoint 1**. Day-by-day objectives are in the [roadmap](../../COURSE-ROADMAP.md).

| Day | Topic | Lesson | Demo | Practice | Solutions |
|-----|-------|--------|------|----------|-----------|
| 01 ✅ | Environment & Hello World | [lesson](day-01-environment/lesson.md) | [demo](day-01-environment/demo.ipynb) | [practice](day-01-environment/practice.ipynb) | [solutions](day-01-environment/solutions.ipynb) |
| 02 | Variables & basic data types | [lesson](day-02-variables/lesson.md) | [demo](day-02-variables/demo.ipynb) | [practice](day-02-variables/practice.ipynb) | [solutions](day-02-variables/solutions.ipynb) |
| 03 | Numbers, operators & input | [lesson](day-03-numbers-input/lesson.md) | [demo](day-03-numbers-input/demo.ipynb) | [practice](day-03-numbers-input/practice.ipynb) | [solutions](day-03-numbers-input/solutions.ipynb) |
| 04 | Strings & string operations | [lesson](day-04-strings/lesson.md) | [demo](day-04-strings/demo.ipynb) | [practice](day-04-strings/practice.ipynb) | [solutions](day-04-strings/solutions.ipynb) |
| 05 | Indexing, slicing & formatting + review | [lesson](day-05-slicing-formatting/lesson.md) | [demo](day-05-slicing-formatting/demo.ipynb) | [practice](day-05-slicing-formatting/practice.ipynb) | [solutions](day-05-slicing-formatting/solutions.ipynb) |

**Assessment:** [Checkpoint 1](../../assessments/weekly/week-01-checkpoint.md), 15 min at the end of Day 05
(answer key below the `---` line; print only the questions). No project this week: the first project is the Quiz
Game on Day 15.

**What students build this week:** `hello.py` (D01) → profile card (D02) → bill splitter (D03) → username and
email generator (D04) → formatted receipt (D05).

## Prepare before the week

- [ ] Every student has VS Code + uv working ([setup/environment.md](../../setup/environment.md)); stragglers
      from Day 01 are fixed before Day 02 ([setup/troubleshooting.md](../../setup/troubleshooting.md)).
- [ ] Before Day 02: students run `uv add ipykernel` in their `python-class` project and can select its `.venv`
      kernel in VS Code.
- [ ] Copy each day's `demo.ipynb` and `practice.ipynb` to students (never `solutions.ipynb`).
- [ ] Run every notebook once yourself: `uv run python scripts/validate_notebooks.py weeks/week-01`.
- [ ] Print Checkpoint 1 (questions only) for Day 05.

## Common difficulties this week and how to respond

1. **"My notebook won't run" (Day 02 onwards).** Almost always the wrong kernel. Top right → *Select Kernel* →
   the `.venv` of their project. If a cell seems stuck with `[*]`, an `input()` box may be waiting at the top of
   the VS Code window.
2. **`input()` returns text (Day 03).** `"20" * 2` giving `2020` is the week's key surprise. Keep asking "what
   type is it?" and get students to check with `type()` instead of guessing.
3. **"I called the method but nothing changed" (Day 04).** Strings are immutable: `name.strip()` returns a new
   string. The fix is always to keep it: `name = name.strip()`.
4. **Off-by-one (Day 05).** Counting starts at 0 and the slice `stop` is not included. Have students write the
   index numbers under the letters on paper before predicting.
5. **Reading errors.** Train the habit from Day 02: read the **last line** first (`NameError`, `TypeError`,
   `ValueError`, `IndexError`) and say in plain words what it means before changing any code.
