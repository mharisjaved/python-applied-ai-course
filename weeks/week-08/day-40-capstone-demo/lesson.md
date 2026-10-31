# Day 40: Capstone Presentations and Python Readiness Assessment

**Week 8 · Session 40 of 60 · Planned 75 min** · Previous: [Day 39](../day-39-capstone-build/lesson.md) · Next: [Day 41](../../week-09/day-41-what-is-ai/lesson.md)

## Objectives

By the end of this lesson students can:

1. Demonstrate their capstone in 5 minutes: the problem, a live run with bad input and a restart that shows saved
   data, one function and one test.
2. Explain a function with four questions: what goes in, what comes out, what can go wrong, how do you know it works.
3. Ask a presenter useful technical questions and give specific, kind written feedback.
4. Show in the [Python readiness assessment](../../../assessments/final/python-readiness.md) that they can read,
   fix and write Python on their own: functions, files, CSV/JSON, a class and a small practical task.

**Prior knowledge:** Weeks 1–8; the capstone brief and their own finished MVP (Days 38–39 + homework).
**No new concepts.**

**Files:** `demo.ipynb` (format, explaining a function, six-prediction warm-up, feedback form) · `practice.ipynb`
(review set for early finishers and later revision) · `solutions.ipynb` · the
[readiness assessment](../../../assessments/final/python-readiness.md) (print the student part; answer key at the end)
· [capstone brief](../../../projects/05-python-capstone/README.md) (demo format, rubric).

## Timing

Day 40 holds a **50-minute assessment** and **about 8 minutes per presenter** (5 min demo + 2 min questions + 1 min
switch-over). Both cannot fit into 75 minutes for most classes, so choose a plan before the day:

- **Plan A (75 min, any class size, recommended):** assessment first, then as many presentations as fit (2–3).
  Schedule the remaining presentations in an extra slot or at the start of the next session (budget 8 min each).
- **Plan B (90-min session, up to 5 students):** presentations first, then the assessment (optional rows below).

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Setup: two warm-up predictions, rules, presentation order | core |
| 0:05–0:43 | Readiness assessment, sections A–E (paper) | core |
| 0:43–0:55 | Readiness assessment, section F (computer) | core |
| 0:55–0:58 | Switch to presentations: format and feedback form (demo sections 1 and 4) | core |
| 0:58–0:72 | Presentations: first 2 students (5 + 2 min each) | core |
| 0:72–0:75 | Exit ticket and what happens next | core |
| Plan B: 0:05–0:40 | Presentations: up to 5 students, *before* the assessment | optional (90-min session) |
| Plan B: +5 min | Demo section 2 (explaining a function) as a model before the first presenter | optional (90-min session) |

**For 60 min:** the assessment alone (setup 5 + 50 + 5 for collecting); all presentations move to the next slot.

## 1. Setup and warm-up (5 min)

Project demo section 3 and run only two predictions (the dict cell and the `int("4.5")` cell) to settle nerves.
(*`3 91`; `0`, because `int("4.5")` raises `ValueError`.*) Then:
- assessment rules: A–E on paper, no notes; F on the computer, Python and `help()` only, no notes, internet or AI;
- presentation order: draw names, or ask for volunteers first; write the order on the board;
- hand out the peer feedback forms (demo section 4: two stars and a wish).

## 2. Readiness assessment (50 min)

Print the student part of [python-readiness.md](../../../assessments/final/python-readiness.md) (everything above
the `---` line before the answer key). Logistics:
- **Section F** needs `expenses.csv`. Before the session, check that every student can reach the course
  `datasets/expenses.csv` from where they will run `transport_report.py` (or copy the file into their working
  folder). The task asks them to print a clear message if the file is missing, so a wrong path costs them the run,
  not the whole section.
- Collect the paper at 0:43; at 0:55 collect `transport_report.py` and a copy of its output (shared drive, LMS or
  a USB stick).
- Students who finish early sit quietly or open `practice.ipynb` (review set). They must not open it before
  handing in.
- Students with agreed extra time continue section F during the first presentation.

Mark it by Day 42 with the answer key and give each student their total, section scores and group (see
"Results and what to do next" in the assessment).

## 3. Presentations (concepts: the demo format and explaining code)

Before the first presenter (3 min), project demo section 1 (the format table) and section 4 (feedback form and
good questions). If you run Plan B, also model demo section 2: explain `parse_amount` with the four questions:

1. **What goes in?** Text typed by the user.
2. **What comes out?** A float rounded to 2 decimals, *returned*, not printed.
3. **What can go wrong?** Empty text, a word, zero, a negative number → `ValueError` with a friendly message.
4. **How do you know it works?** Run `test_parse_amount()`.

**Prediction question** (Plan B, demo section 2): "If `parse_amount("0")` did *not* raise, what would the test
do?" (*`assert False, ...` would fail with the message `0 was not rejected`.*)

Running the presentations:
- Show a visible timer; give a signal at 4:00 and stop at 5:00. Questions get 2 minutes.
- Ask every presenter at least one question from [INSTRUCTOR.md](../../../projects/05-python-capstone/INSTRUCTOR.md)
  ("walk me through this function", "why JSON?", "change this limit and run it"). This doubles as the authorship
  check.
- The audience fills in one feedback line per presenter. Collect the forms and give each presenter theirs at the
  end of the slot.
- Score the "Explanation / demo" criterion (15 points) during the questions; score the rest from the submission
  afterwards (grading procedure in INSTRUCTOR.md).

## 4. Common mistakes in demos

| Mistake | Symptom | How to prevent or handle it |
|---------|---------|-----------------------------|
| Starting with code instead of the problem | the audience does not know why the app exists | First sentence: "This is for … who needs to …" |
| Messy or empty data file | the demo shows "no items yet", or crashes on old test data | Prepare a clean data file with 3–5 realistic records before class |
| Running out of time in the code tour | no time for the decision and the "next step" | Pick **one** function and **one** test; rehearse with a timer |
| Reading the code line by line | listeners get lost | Use the four questions instead |
| "It worked at home" | `ModuleNotFoundError` or failing tests on the day | Run `uv run python main.py` and `uv run pytest -q` before the session starts |
| Tiny terminal font | nobody can read the output | Zoom the VS Code terminal before your turn |

If an app crashes live, let the presenter restart once and explain what happened; that is a debugging
demonstration in itself. Grade the explanation, not the luck.

## 5. Practice (review set)

`practice.ipynb` is a short review of Weeks 1–8 for early finishers, for students waiting to present in the
overflow slot, and as targeted revision for students in the "ready with support" group.

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the output | slicing, aliasing, scope, `sorted(key=)` | recall |
| 2 Fix the class | `>=` vs `>`, `__str__` must return, refusing duplicates | modification |
| 3 Count by a column | dict counting on `students.csv` | application |
| 4 CSV → JSON summary | load → analyse → save pipeline | problem solving |
| 5 A reading log class | class with validation and `__str__` | application |
| 6 Two questions about the dataset (challenge) | pass rates, top 5 with a key function, correlation vs causation | challenge |

Exercises 3, 4 and 6 use `students.csv`, the dataset of Week 9, which is a gentle bridge into Day 41–42.

## 6. Exit ticket (3 min)

Each student writes:
1. One thing in their capstone they are proud of.
2. One Python topic they will revise before Week 9, and how (e.g. "functions: redo Day 37 Exercise 4").

There is no single correct answer. Check later that the topic matches their assessment results; if it does not, say
so when you return the marks.

## Homework (20 min)

1. If your presentation is in the overflow slot: rehearse once more with a timer.
2. Small fixes to the capstone are allowed until the start of Day 41 if your instructor agreed. Note them in
   `PLAN.md`.
3. Optional: Day 40 practice Exercises 3–4 with `students.csv`: you will meet this dataset again on Day 42.

## Next class

[Day 41](../../week-09/day-41-what-is-ai/lesson.md) starts the AI phase: what AI, machine learning and generative AI
are, the difference between hand-written rules and rules learned from examples, and where AI goes wrong. The
CSV/JSON, functions and tests from this week are the tools every AI week builds on.

## Instructor notes

- **Plan the timing before the day.** Count your students: 8 minutes each for presentations. If the overflow slot
  is the start of Day 41, tell the students on Day 39 so nobody is surprised, and keep it to 30 minutes at most.
- **Nerves:** let anxious students choose a later slot, and allow a pre-recorded terminal session as a fallback if
  the live run fails for technical reasons (they still answer questions live).
- **Fairness in the assessment:** the same conditions for everyone; extra time only where agreed. Do not help with
  content during the assessment; clarifying the wording of a question is fine.
- **Groups after marking:** "Ready", "Ready with support", "Needs a revision plan" (thresholds and actions are in the
  assessment). Tell students their group privately and frame it as the support they will get, not a label.
- **What not to do today:** no new content, no previews of NumPy/pandas beyond one sentence. Celebrate: they have
  built five projects and finished the Python phase.
