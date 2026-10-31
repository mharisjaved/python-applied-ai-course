# Day 39: Python Capstone, Build, Debug and Test

**Week 8 · Session 39 of 60 · Planned 75 min** · Previous: [Day 38](../day-38-capstone-planning/lesson.md) · Next: [Day 40](../day-40-capstone-demo/lesson.md)

## Objectives

By the end of this lesson students can:

1. Build in commit-sized steps (write → run → test → checkpoint) so that their app always runs.
2. Find bugs that do not crash by writing tests whose answers they worked out by hand, and read a traceback
   bottom-up to locate a crash.
3. Refactor a long function into small ones and prove with an `assert` that the output did not change.
4. Validate user input in two layers: a `parse_…` function that raises `ValueError`, and an `ask_…` loop.
5. Review a classmate's code with a checklist and act on the review of their own.

By the end of the session (with tonight's homework) every student has a **working, tested MVP**.

**Prior knowledge:** debugging and tracebacks (Day 28), pytest (Day 29), exceptions (Day 25), classes (Days 32–34),
CSV/JSON (Day 36), pipelines (Day 37), their approved plan and skeleton (Day 38). **No new syntax.**

**Files:** `demo.ipynb` (sample Budget Tracker module) · `practice.ipynb` (warm-up + toolbox) · `solutions.ipynb` ·
each student's own capstone project · [reference README](../../../projects/05-python-capstone/reference/README.md)
(the model README, shown at the end).

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:07 | Warm-up: practice Exercise 1 (read a traceback) + one-sentence stand-up | core |
| 0:07–0:22 | Mini-lesson: build loop, tests catch bugs, refactor, validation, checklist (demo 1–6) | core |
| 0:22–0:45 | Build block 1: class + tests, then storage (build-plan steps 3–4) | core |
| 0:45–0:55 | Peer code review with the checklist (pairs, 5 min each way) | core |
| 0:55–0:70 | Build block 2: act on the review; next MVP menu option | core |
| 0:70–0:75 | Progress check, model README, exit ticket | core |
| +15 min | Longer build block 2, or the README written in class | optional (90-min session) |

**For 60 min:** mini-lesson = demo sections 2–3 and 6 only (10 min); peer review 3 minutes each way.

## 1. Warm-up (7 min)

Students do practice **Exercise 1** (a traceback from a flashcard app) in pairs. Take answers:
*the last "File" line is where it happened (`models.py`, line 22, `accuracy`); both counts are 0 for a card never
studied; the fix is a decision (return `0.0`) made inside the function, plus a test.*

Then each student says one sentence: **"Yesterday I finished … Today I will … I am stuck on …"** (pairs, not the
whole class). Note who is stuck; visit them first in build block 1.

## 2. Mini-lesson (15 min)

Keep it brisk: the goal is to give tools, then get out of the way.

**The build loop (demo section 1).** A *commit-sized* step is one function, method or menu option: 10–20 minutes,
ending with the app running and the tests passing. Then a checkpoint: `git commit` if they use git, otherwise copy
the project folder. **Analogy:** climbing with ropes: you clip in after every few metres, so a slip costs metres,
not the whole climb.

**Tests catch bugs that do not crash (demo sections 2–3).** The budget module runs without errors but every answer
is wrong. **Prediction question:** "Income 1000, expenses 200 + 50 + 30: what should the balance be?" (*720. The
function says -720.*) Show `run_tests` reporting three FAILs, ask students to spot each bug by reading
(sign, `=` instead of `+=`, `return` indented inside the loop). Then `average_expense([])` → `ZeroDivisionError`:
read the traceback bottom-up, ask "which *value* caused it?", and point out that the fix is a **decision** (what is
the average of nothing?). Every fixed bug gets a test (`test_empty_data`).

**Refactoring (demo section 4).** Save the old output in `before`, split the long function into
`transactions_in_month`, `total_of_kind` and the existing `spending_by_category`, then `assert new == before`.
Refactoring changes structure, never behaviour, and the assert proves it.

**Validation in two layers (demo section 5).** `parse_amount` (raises `ValueError` with a friendly message, easy to
test) and `ask_amount` (loops; only the menu uses it). **Prediction question:** the user types `twelve`, `-5`,
nothing, `12.50`. What appears? (*Three messages, then `Saved amount: 12.5`.*)

**The review checklist (demo section 6).** Read the nine items. **Prediction question:** "How many items does
`f(l, c)` break?" (*At least four: names, docstring, print instead of return, a missing test for a hidden bug.*)

## 3. Common mistakes during the build

| Mistake | Error / symptom | How to explain it |
|---------|-----------------|-------------------|
| Writing three features before running anything | ten errors at once, no idea which change caused them | One step, run, test. If it breaks, the bug is in the last 20 lines |
| `return` indented inside the loop | wrong answer from the first item only | Trace two loop rounds on paper. When does the function end? |
| `totals[key] = amount` instead of adding | only the last amount per key survives | Day 12 counting pattern: `totals.get(key, 0) + amount` |
| Saving only when the user chooses "Quit" | data lost if the window is closed | Save after every change (as in the reference) |
| `TypeError: Object of type Habit is not JSON serializable` | dumping objects | JSON stores dicts/lists: give the class a `to_dict()` method |
| Tests import `main.py` and the menu starts | pytest waits for input or errors | `main()` must be called only under `if __name__ == "__main__":` |
| `except:` with no exception name, around everything | real bugs (typos, `NameError`) disappear silently | Catch the specific error you expect (`ValueError`, `FileNotFoundError`) |
| `ModuleNotFoundError: No module named 'models'` | terminal in the wrong folder | `pwd` / `ls`: run from the project folder |

## 4. Build block 1 (23 min)

Target: **build-plan step 3** (the class with ≥ 3 passing tests) and ideally **step 4** (save + load, missing
file → empty data, a save-then-load test; restart keeps data).

While circulating:
- Ask "show me your last passing test run" before looking at any code.
- Students stuck on a *skill* get a toolbox exercise: tests → practice Exercises 2–3; long function → Exercise 4;
  validation → Exercise 5; storage → Exercise 6. Ten minutes on the exercise, then back to their project.
- Anyone without a running skeleton: fix that first, nothing else.

The practice notebook is a toolbox (Exercise 1 was the warm-up for everyone):

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Read the traceback | locating a crash, deciding a fix | recall |
| 2 Write tests for working code | normal, edge and error cases | application |
| 3 Find the bugs with tests | test-driven debugging | modification |
| 4 Refactor a long function | splitting jobs, proving same output | modification |
| 5 Validate a date | parse function with clear errors | problem solving |
| 6 Safe load and save (challenge) | missing / damaged / wrong-type files | challenge |

## 5. Peer code review (10 min)

Pairs swap laptops. The reviewer runs `uv run python main.py` and `uv run pytest -q`, tries to break the app with
`abc`, an empty answer and `-1`, then goes through the checklist (demo section 6) and writes **two strengths and
two concrete suggestions** (e.g. "`ask_amount` is not used in menu option 3"). Then swap roles.
Rules: the reviewer does not type in the other person's code; suggestions must point at a line or a function.

## 6. Build block 2 (15 min)

Fix the review's suggestions first (they are usually quick wins for "bad input" points), then the next MVP menu
option. Remind students: "one option, run, test, checkpoint".

## 7. Progress check and exit ticket (5 min)

Show the [reference README](../../../projects/05-python-capstone/reference/README.md) for 1 minute as the model
for tonight's README: features, how to run, an example session, known limitations. (Show the README, not the code.)

**Exit ticket:** each student writes the build-plan **step number** they reached and **the next step** they will do
at home. Expected: step 4 reached (data survives a restart). Anyone below step 3 gets a message from you tonight
with one concrete next step.

## Homework (≈ 90 min, the main capstone finishing time)

1. Finish the MVP stories; tick them in `PLAN.md`; note any changes to the plan.
2. Try to break your app (every prompt: `abc`, empty, `-1`, huge numbers, unknown names; delete the data file).
3. Reach at least 5 passing tests, including an edge case and a `pytest.raises` case.
4. Write `README.md` (features, how to run, example session). Copy a real session from your terminal.
5. Rehearse the 5-minute demo **with a timer** (format in the brief). Code, tests and README are due at the
   start of Day 40.

## Next class

Day 40: capstone presentations (5 minutes + questions, peer feedback form) and the **Python readiness
assessment**, a 50-minute check of everything from Weeks 1–8 that decides what support each student gets in the
AI phase. Tell students it covers reading code, fixing bugs, writing functions, files/CSV/JSON, a small class and
one practical task, so the best revision is finishing the capstone honestly.

## Instructor notes

- **Your role today is unblocking, not teaching.** Use the questions in
  [INSTRUCTOR.md](../../../projects/05-python-capstone/INSTRUCTOR.md) and never type into a student's file.
- **Scope cuts are normal.** If a student is clearly behind at 0:45, agree a smaller MVP on the spot and write it in
  their `PLAN.md`. A small app that works beats a big app that crashes.
- **`run_tests` in the demo** is a teaching device that shows what pytest does. Students should use real pytest
  files in their projects; do not let them copy `run_tests` into the project.
- **Do not introduce** logging, `argparse`, type hints, dataclasses or other "professional" extras even if strong
  students ask. Point them to Could features or more tests instead.
- **Fast students:** Could features, or help as a second reviewer (explaining code to others is great practice for
  the demo). **Slow students:** one MVP story fully working and saved is the goal; skip Should/Could entirely.
