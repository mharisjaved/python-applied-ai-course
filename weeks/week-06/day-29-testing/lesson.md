# Day 29: Testing with Assertions and pytest

**Week 6 · Session 29 of 60 · Planned 75 min** · Previous: [Day 28](../day-28-debugging/lesson.md) · Next: [Day 30](../day-30-project-expense-tracker/lesson.md)

## Objectives

By the end of this lesson students can:

1. Replace `print(f(x) == expected)` checks with `assert` and explain what happens when an assert fails.
2. Choose **normal**, **edge** and **error** test cases for a function from its docstring.
3. Check that a function raises an error with `with pytest.raises(ValueError):`.
4. Write a `test_*.py` file of `test_*` functions and run it with `uv run pytest` (`-q`, `-v`).
5. Read a pytest failure (`>` and `E` lines), decide whether the code or the test is wrong, and fix it.

**Prior knowledge:** functions and `return` (Day 17), print-checks (Day 19), `raise ValueError` and
`try/except` (Day 25), modules and imports (Day 26), `uv run` and dev dependencies (Day 27), tracebacks (Day 28).

**Files:** `demo.ipynb` (you) · `practice.ipynb` (students) · `solutions.ipynb` (you) · `grades.py` + `test_grades.py`
(demo code and its 11 tests, all passing) · `checkout.py` (practice code to test) · `solution_test_checkout.py`
(reference for practice Exercise 5; not collected automatically because its name does not start with `test_`)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: "you fixed a bug yesterday; how do you know nothing else broke?" | core |
| 0:05–0:12 | From print-checks to `assert` (demo 1) | core |
| 0:12–0:19 | Normal / edge / error cases (demo 2) | core |
| 0:19–0:24 | `pytest.raises` (demo 3) | core |
| 0:24–0:28 | Test functions (demo 4) | core |
| 0:28–0:42 | pytest in the terminal + reading a failure (demo 5–6, live break-and-fix) | core |
| 0:42–0:47 | Test-first bug fix + common mistakes (demo 7–8) | core |
| 0:47–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (challenge) together: write the tests first, then the function | optional (90-min session) |

For a 60-minute session: skip demo 4's manual calls (go straight to pytest), shorten demo 7 to the story only,
and set Exercise 5 step 5 as homework.

## 1. Warm-up (5 min)

Ask: "On Day 28 you fixed `count_passed`. How do you know the fix didn't break another case?" (*We would have to
re-run every check by hand and read every `True`.*) Then: "Programmers change code every day. Today we make the
computer re-check everything in one command."

## 2. From print-checks to `assert` (7 min)

**Intuition:** a print-check *reports*; an assert *insists*. It is silent when the claim is true and stops the
program loudly when it is false.

> **Analogy:** a smoke alarm. You don't want it to beep "all fine" every minute; you want silence until something
> is wrong, and then you want noise.

Live code (demo section 1):

```python
from grades import average, letter_grade, parse_marks
assert average([70, 80, 90]) == 80      # nothing happens
assert letter_grade(72) == "A"          # AssertionError
assert result == "A", f"expected A for 72, got {result}"   # AssertionError: expected A for 72, got B
```

**Prediction question:** "What will `assert letter_grade(72) == "A"` do?" Then point out that the bare
`AssertionError` has no message, which is why pytest (below) adds the details for us.

## 3. Normal, edge and error cases (7 min)

Show the table in demo section 2 and build it **with the class** from the docstring of `letter_grade`.

| Kind | Meaning | `letter_grade` examples |
|------|---------|-------------------------|
| normal | a typical input | 72 → `"B"` |
| edge | exactly on a boundary, just below it, empty input, extremes | 80, 79, 65, 64, 50, 49, 0, 100 |
| error | input that must be rejected | -1, 101 → `ValueError` |

**Prediction question:** "Which of these inputs would catch a programmer who wrote `score > 80` instead of
`score >= 80`?" Only 80. Most inputs give the same answer either way, which is exactly why edge cases exist.

## 4. Testing errors with `pytest.raises` (5 min)

```python
import pytest
with pytest.raises(ValueError):
    letter_grade(150)        # passes: the error happened
with pytest.raises(ValueError):
    letter_grade(90)         # Failed: DID NOT RAISE ValueError
```

Read it as "the indented code **must** raise `ValueError`". Students know `with` from files (Day 23); here it
means "watch this block for an error".

## 5. Test functions (4 min)

A test = a function named `test_…` with no parameters, containing asserts. One idea per test, and a name that
says the idea (`test_average_empty_list_is_zero`). Call three by hand in demo section 4 and ask: "Would you do
this for 200 tests?" That motivates pytest.

## 6. pytest in the terminal + reading a failure (14 min)

Open `test_grades.py` in VS Code. Point out: `import pytest`, `from grades import ...`, 11 small functions grouped
by the function they test. Then in the terminal:

```
cd weeks/week-06/day-29-testing
uv run pytest
```

Expected: a header (`rootdir:` is the course folder, because pytest found the course `pyproject.toml`), one dot per
test, and `11 passed`. Then `uv run pytest -v` (one line per test with `PASSED`) and
`uv run pytest -q` (dots and summary only). Run a single test with
`uv run pytest test_grades.py::test_letter_grade_boundaries`.

**Live break-and-fix (the most important 5 minutes today):**
1. In `grades.py` change `if score >= 80:` to `if score > 80:` and save.
2. `uv run pytest` → `1 failed, 10 passed`. Read the failure together:
   - the `>` line: `assert letter_grade(80) == "A"` (only the first failing assert in a test is reported);
   - the `E` line: `AssertionError: assert 'B' == 'A'` (left side = what the function returned, right side = expected);
   - the last line: `FAILED test_grades.py::test_letter_grade_boundaries`.
3. Undo the change, run again: `11 passed`.

Then show demo section 6 (a notebook-written test file with a **wrong expectation**: `letter_grade(85) == "B"`).
**Prediction question:** "Is the code wrong or the test?" The docstring says 80+ is an A, so the **test** is
wrong. A failing test means "code and test disagree"; the specification decides who is right.

`pytest.main(["-q", "test_grades.py"])` is the notebook equivalent of the terminal command. Students should
prefer the terminal, which is what they will use in the project.

## 7. Test-first bug fix and common mistakes (5 min)

Demo section 7 tells the story: a user reports `count_words("")` gives 1. Step 1: write tests that reproduce the
bug (they fail). Step 2: fix (`.split()` instead of `.split(" ")`). Step 3: run all tests. The tests stay, so the
bug cannot return unnoticed.

| Mistake | Symptom | How to explain it |
|---------|---------|-------------------|
| Test function not named `test_…` | "no tests ran" / fewer tests than expected | pytest only collects `test_*` names |
| Test file not named `test_*.py` | file silently ignored | rename it |
| `assert x = 5` | `SyntaxError` | `==` compares |
| Comparing floats with `==` | fails with `0.30000000000000004` | `round(…, 2)` or `pytest.approx` (demo 8) |
| `print` instead of `assert` in a test | test always passes | a test must be able to fail |
| `assert f(0) == ValueError` | the `ValueError` crashes the test | use `pytest.raises` |
| `ModuleNotFoundError` for the code under test | test file in a different folder | keep `test_x.py` next to `x.py` |
| Running `pytest` instead of `uv run pytest` | command not found / wrong Python | always `uv run` |

## 8. Practice (23 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Pass or fail? | predicting asserts (floats, `in` on dicts, list order) | recall |
| 2 Cases for `split_bill` | normal/edge/error table → asserts, `pytest.raises` | application |
| 3 Test functions for `is_valid_username` | boundary values 3/12 characters | application |
| 4 Let the tests find the bug | writing tests that expose a bug, then fixing | modification |
| 5 Your first pytest file | `test_checkout.py`, `uv run pytest -v`, reading a failure | problem solving |
| 6 Tests first (challenge) | writing tests before the function | challenge |

While circulating, look for: edge cases that are really normal cases ("what's special about this input?"),
`assert f(x) == ValueError`, test functions that are defined but never called (Exercises 3–4), files saved as
`test-checkout.py` or outside the folder, and students who forget to **undo** the deliberate break in Exercise 5.

Expected outcome: everyone completes 1–4, most complete 5, fast students do 6.

## 9. Recap and exit ticket (5 min)

1. `assert` is silent when true and raises `AssertionError` when false.
2. Good tests cover normal, edge and error cases; `pytest.raises` checks errors.
3. `uv run pytest` runs every `test_*` function in every `test_*.py` file. Read failures via `>` and `E`.

**Exit ticket:** write one pytest test for `apply_discount(price, percent)` (from `checkout.py`) checking that a
discount of 150% raises `ValueError`.

Answer:

```python
def test_apply_discount_over_100_raises():
    with pytest.raises(ValueError):
        apply_discount(20, 150)
```

## Homework (25 min)

Finish Exercise 5. Then write a `test_*.py` file with at least four tests (one error case) for two functions you
wrote earlier, for example your Day 26 `gradetools.py` or a Hangman helper from Day 20, and run it with
`uv run pytest -v`.

## Next class

Day 30 is **Project 03: Expense Tracker**, a multi-file program (`storage.py`, `reports.py`, `main.py`) that saves
expenses to a file, with `test_storage.py` and `test_reports.py`. Everything from this week comes together:
modules and imports (Day 26), `uv run` (Day 27), debugging (Day 28) and pytest (today). Checkpoint 6 is at the
end of the session.

## Instructor notes

- Do **not** introduce fixtures (`tmp_path`, `conftest.py`), parametrize, mocking, coverage or test classes. They
  are all useful later, but today plain functions with asserts are enough. If a student asks about many similar
  cases, the answer for now is "several asserts in one test, or several small tests".
- `pytest.raises(ValueError, match="between 0 and 100")` exists for checking the message. Mention it only to fast
  students.
- The pytest header says `rootdir: …/python-course` and creates `.pytest_cache/` in the course folder (ignored by
  Git). That is normal: pytest found the course `pyproject.toml`. In their own uv project it will be their project folder.
- In their own uv projects (Day 27) students need `uv add --dev pytest` once before `uv run pytest` works.
- `pytest.main([...])` in a notebook imports the test file once per kernel. If you edit a test file and run it
  again from the same notebook, restart the kernel first (same rule as Day 26). The terminal has no such problem.
- Some students think tests are a waste of time. Point back to Day 28: every bug they fixed could be locked out
  forever with one three-line test.
- Fast students: Exercise 6, then add tests for `parse_marks` edge cases (`"78,,92"`, `" 78 "`): what *should*
  happen? Writing the test forces the decision.
- Slow students: Exercises 1, 2 and 4 are the core. Make sure they see one red failure and one green run in the
  terminal before they leave.
