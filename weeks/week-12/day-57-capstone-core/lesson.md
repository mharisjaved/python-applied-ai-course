# Day 57: AI Capstone: Build the Core First

**Week 12 · Session 57 of 60 · Planned 75 min** · Previous: [Day 56](../day-56-capstone-scoping/lesson.md) · Next: [Day 58](../day-58-capstone-ai-integration/lesson.md)

## Objectives

By the end of this lesson students can:

1. Explain why the non-AI core is built and tested before the AI part ("make it work without AI").
2. Split a capstone into `main.py` (CLI), core module(s) (data + logic) and **one** AI boundary function.
3. Write pure core functions (parameters in, value out, no `input`/`print`) that validate their input.
4. Test the core with tiny hand-made data, first with `assert`, then with pytest in `test_*.py`.
5. Write a stub for the AI function that already returns the final shape, so the app runs end to end today.

**Prior knowledge:** functions and return (Days 16–18), exceptions and `raise` (Day 25), modules and
`__name__` (Day 26), pytest and `pytest.raises` (Day 29), `csv` (Day 36), pipelines with `main()` (Day 37),
baselines (Day 46), the approved plan (Day 56).

**Files:** `demo.ipynb` · `practice.ipynb` · `solutions.ipynb` · `example_app/` (the worked example as real
files: `spending.py`, `summary.py`, `main.py`, `test_spending.py`)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: plan status + retrieval questions | core |
| 0:05–0:25 | Teaching: core first (demo sections 1–8, terminal run of `example_app`) | core |
| 0:25–0:35 | Practice Exercises 1–3 | core |
| 0:35–1:08 | Build time: own core + tests + stub | core |
| 1:08–1:15 | Checkpoint (section 6) and exit ticket | core |
| +15 min | Practice Exercises 4–6, or pairs run each other's tests | optional (90-min session) |

**60 min:** teach demo sections 1, 3, 5 and 7 (12 min), skip the practice notebook except Exercise 1 and go
straight to build time.

## 1. Warm-up (5 min)

Plan status: hands up, *approved / approved with changes / not yet*. "Not yet" students sit near you for the
first build minutes.

Retrieval questions:
- "What does pytest look for?" (*Files named `test_*.py`, functions named `test_*`.*)
- "What is the difference between `print` and `return`?" (*print shows text; return hands a value back to the caller.*)
- "On Day 46, what was a baseline?" (*The simplest possible prediction, e.g. always the most common class. A model must beat it.*)

## 2. Teaching: build the core first (20 min)

**Why (demo section 1).** Draw the three layers on the board:

```
main.py      input() and print() only
core .py     load, clean, calculate, validate    ← most bugs live here
AI function  ONE function that talks to the model ← today: a stub
```

> **Analogy:** a restaurant kitchen. The core is the prep station (washing, cutting, weighing): boring,
> reliable, checkable. The AI is the guest chef who arrives later. If the chef is ill, the prep is done and a
> simple dish can still be served (the stub/fallback).

Three reasons: the core is **deterministic** (exact tests possible), it is **free and fast** to run hundreds of
times, and you **always have a demo**.

**Loading (demo section 2).** `parse_amount` is small and strict; the `[raises-exception]` cell shows it
refusing `-4`. The loader catches that error and counts skipped rows. Point out that descriptions are never
loaded: Day 56's privacy decision became code.

**Pure functions (demo section 3).** Define it: only parameters in, a value out, no `input`, `print` or files.
**Prediction question:** `category_totals(filter_month(sample, "2026-09"))`. (*`{'rent': 650.0, 'food': 20.0}`;
transport is October.*)

**Checking as you go (demo section 4).** Tiny hand-made data means we *know* the right answers, so exact `assert`s
work. **Prediction question:** what should `category_totals([])` return? (*`{}`: decide edge cases before
coding.*)

**The stub (demo section 5).** `write_summary(totals)` uses a template but returns exactly
`{"summary": ..., "tips": [..., ...]}`, the shape the AI version will return tomorrow.
**Prediction question:** "Tomorrow the inside calls a model. Which other functions change?" (*None.*)

**From notebook to files (demo section 7).** Switch to the terminal and run the worked example:

```
cd weeks/week-12/day-57-capstone-core/example_app
uv run pytest -q
uv run python main.py
```

Expected: `8 passed`, then the app asks for a month; type `2026-09` and see the totals table, a template summary
and two tips (`The biggest category was food (660.87).`), then `quit`. Open `test_spending.py` and show that a
test is just the notebook `assert` inside a `test_` function, with `SAMPLE` data at the top.

**Option-specific cores.** Show this table; every student should find their row:

| Option | The core (no AI) | The stub for the AI function |
|--------|------------------|------------------------------|
| A ML predictor | load + clean data, choose features (no leakage!), validate user inputs, format output | return the **baseline** (most common class or the mean): Day 46's "dumbest model" |
| B LLM text tool | load/clean texts, length checks, format results, count/aggregate | keyword rules or a template with the final JSON-like shape |
| C FAQ assistant | split the FAQ into sections, keywords, scoring, retrieval of the top sections | return the best section's answer text |
| D own idea | whatever is deterministic | the simplest non-AI answer with the final shape |

## 3. Common mistakes

| Mistake | Error / symptom | How to explain it |
|---------|-----------------|-------------------|
| `print` instead of `return` in a core function (demo section 8) | `TypeError: ... 'NoneType' and 'int'` | the function shows the value but hands back `None` |
| Comparing unrounded money (demo section 8) | `AssertionError` on `0.1 + 0.2 == 0.3` | floats are binary; round to cents in the core |
| `input()` inside a core function | tests hang waiting for typing | only `main()` talks to the user |
| Only testing on the big real file | "is 1929.2 right?" nobody knows | tiny hand-made data with known answers + one real-file test |
| Test file cannot import the module | `ModuleNotFoundError` | run `uv run pytest` **from the folder** that contains both files |
| Model call or API key needed to import a module | tests fail offline | nothing AI-related runs at import time |

## 4. Practice (10 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Where does it belong? | main / core / AI layers | recall |
| 2 From print to return | pure function, edge case | application |
| 3 Validate input in the core | `raise ValueError`, `pytest.raises` | application |
| 4 Logic on records | list of dicts, reuse, tests | application |
| 5 The AI boundary as a stub | keyword stub with final shape | modification |
| 6 A loader that survives bad rows (challenge) | `csv.DictReader` on lines, skip/count | challenge |

Look for: Exercise 2 forgetting the empty list (`ZeroDivisionError`); Exercise 3 putting checks in a test
instead of in `parse_rating`; Exercise 5 checking complaint words before suggestion words (order matters).

## 5. Build time (33 min)

Students build **their own** core. Put this order on the board:

1. Folder layout: `main.py`, one or two core modules, the AI module with the stub, `test_core.py`.
2. Loader + validation function(s), each with one normal and one error test.
3. The main logic functions with tiny-data tests (and one real-data test).
4. The stub AI function with the final return shape + one test of that shape.
5. `main()` with a `while` loop, `quit`, and `try/except` around bad input; run it end to end.

Circulate with the checkpoint list below. Unblock with questions, not code: "What does this function return
for an empty list?", "Can you test this without typing anything?", "Which line here needs the network?"

## 6. Checkpoint and exit ticket (7 min)

**Checkpoint** (tick per student, keep the list for grading notes):
- [ ] `uv run pytest -q` passes with **at least 3 tests** on their own core.
- [ ] `uv run python main.py` runs end to end using the stub, and `quit` works.
- [ ] The AI boundary is **one** named function that already returns the final shape.
- [ ] No API key and no network needed for anything so far.

**Exit ticket:** "Your AI function will return `{"label": ..., "reason": ...}`. Write the stub in 3 lines for a
comment classifier."

Possible answer:
```python
def classify(comment):
    if "please" in comment.lower():
        return {"label": "suggestion", "reason": "asks for something"}
    return {"label": "praise", "reason": "no keywords matched"}
```

## Homework (40 min)

Finish the checkpoint items. Then add **two more tests** (aim for 5 on the core before Day 58), and write the first
two sections of your README: *What it does* and *How to run it*.

## Next class

Day 58 replaces the inside of the stub with the real AI: a model trained at start-up (option A) or `ask_llm`
with a mock first (B/C), JSON validation, fallbacks for refusals and bad replies, and **tests with fake models**.
Today's stub becomes the fallback.

## Instructor notes

- Students will want to start with the AI ("the fun part"). Hold the line: no `ask_llm` until the core
  checkpoint is green. The stub makes the app feel complete, which helps motivation.
- Option C students have the biggest core (splitting + retrieval). Point them to `split_sections` thinking:
  `## ` lines are topics, `### ` lines are questions, everything else is answer text. Do not show the reference.
- Option A students sometimes put `train_test_split` and `fit` in `main()`. Training belongs in a function in
  the core/AI module (`train_model(data)`), called once at start-up.
- `ModuleNotFoundError` in tests is nearly always the working folder. Ask them to `ls` (or `dir`) first.
- If someone's data turns out unusable today, switch them to a course dataset immediately; do not let them
  lose a second session.
- Do not introduce fixtures, `parametrize`, mocking libraries or classes-for-everything. Plain test functions
  and small dicts are enough and are what the rubric expects.
