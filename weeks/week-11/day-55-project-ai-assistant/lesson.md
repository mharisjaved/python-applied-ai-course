# Day 55: Project 08, AI Text Assistant + Checkpoint 11

**Week 11 · Session 55 of 60 · Planned 75 min** · Previous: [Day 54](../day-54-parsing-validation/lesson.md) · Next: [Day 56](../../week-12/day-56-capstone-scoping/lesson.md)

## Objectives

By the end of this lesson students can:

1. Show what they learned this week in Checkpoint 11 (LLM basics, prompts, keys, JSON validation, mocks).
2. Turn a written brief into the pipeline input → **redact** → prompt → model → parse → report, and name the
   function for each step.
3. Remove e-mail addresses and phone-like numbers from text with string methods, and name a case their rule misses.
4. Use failing tests as a to-do list: make them pass one function at a time.
5. Start Project 08 (steps 1–3 in class) with a clear plan for finishing it as homework.

**Prior knowledge:** everything from Days 51–54; `csv.DictReader` (Day 36), counting with dicts and `Counter`
(Days 12, 26), `.isdigit()` (Day 13), `strip(chars)` and `split`/`join` (Days 04, 07), pytest (Day 29).

**Files:** `demo.ipynb` (kick-off) · `practice.ipynb` (prototype the hard parts before moving them into `app.py`) ·
`solutions.ipynb` · `llm.py` (same helper as Days 52–54). Project:
[projects/08-ai-text-assistant/](../../../projects/08-ai-text-assistant/README.md) (brief, `starter/`, `reference/`,
[INSTRUCTOR.md](../../../projects/08-ai-text-assistant/INSTRUCTOR.md)). Checkpoint:
[week-11-checkpoint.md](../../../assessments/weekly/week-11-checkpoint.md).

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:03 | Plan for today | core |
| 0:03–0:23 | Checkpoint 11 (paper or a blank notebook, no internet) | core |
| 0:23–0:33 | Project kick-off: brief, data, privacy, starter (demo 1–5) | core |
| 0:33–0:70 | Build: prototype in `practice.ipynb` (Exercises 1–3), move into `app.py`, run the tests | core |
| 0:70–0:75 | Wrap-up: how many tests pass? homework plan | core |
| +15 min | Build time for steps 4–5, or pair code review of `redact` | optional (90-min session) |

**60-min version:** checkpoint 15 minutes (drop questions 7 and 10, mark out of 8 and rescale), kick-off 5 minutes
(demo sections 1 and 3 only), build 32 minutes.

## 1. Plan for today (3 min)

Say it plainly: quiz first while minds are fresh, then we start the project; it is finished at home. Write the
homework deadline on the board (suggested: start of Day 57).

## 2. Checkpoint 11 (20 min)

Hand out [week-11-checkpoint.md](../../../assessments/weekly/week-11-checkpoint.md) (questions only, without the
answer key). Closed book, no running code. Collect, mark with the 10-point guide after class, and return on Day 56
with the two most common mistakes discussed in 3 minutes.

## 3. Project kick-off (10 min)

Demo sections 1–5:
1. **The brief in one picture** (demo section 1): Fatima's shop, 40 reviews, "what are people unhappy with?"
   Draw the pipeline with the new **redact** box *before* the prompt. Show the README's example run.
2. **The data** (demo section 2): reviews per product, average rating per product. Ask: "Which product would you
   look at first?" (*Hard to say: every average is 3.2–3.4 stars. Stars do not say* why*; the text does.*)
3. **Privacy** (demo section 3): print R33. Ask: "If we send this to a real model, where do the phone number and
   e-mail address go?" (*To another company's servers.*) Show the two ideas for detection on single words:
   `"@" in word` and counting digits. Do **not** write the full `redact` function; that is Exercise 2.
4. **The starter** (demo section 4): list the TODO functions and the test names. The tests are the to-do list.
5. **The smallest version** (demo section 5): one review end to end with the mock in six lines. "`analyse_all` is
   this, in a loop, with checks."

## 4. Build time (37 min)

Students work in this order (it is the README's build plan):

| Step | Where | Done when |
|------|-------|-----------|
| 1 `load_reviews` | `app.py` directly (it is Day 36 code) | `test_load_reviews_*` pass |
| 2 `redact` | prototype in practice Exercise 2, then copy into `app.py` | `test_redact_*` pass |
| 3 `build_prompt` | practice Exercise 3, then `app.py` | prompt for R33 shows `[PHONE]` and `[EMAIL]` inside the tags |
| 4–6 | homework (practice Exercise 4 prepares step 5) | all 21 tests pass |

**Reading a failing test** (show once on the projector, 1 minute; example output of a typical redaction bug):

```
FAILED test_app.py::test_redact_replaces_phone_and_keeps_punctuation
>       assert redact("Call me at 555-0142.") == "Call me at [PHONE]."
E       AssertionError: assert 'Call me at [PHONE]' == 'Call me at [PHONE].'
```

The test **name** says what should happen, the `>` line is the check, the `E` line shows *what we got* on the left
and *what was expected* on the right (Day 29). Here the full stop was lost: the whole word was replaced.

Circulate with [INSTRUCTOR.md](../../../projects/08-ai-text-assistant/INSTRUCTOR.md)'s pitfall table. Look for:
- redaction that replaces the whole word including the full stop (the punctuation test fails);
- `build_prompt` that uses the raw text (the privacy test fails later; point it out now);
- students who start with the report "because it is the fun part". Redirect: the tests define the order.

Practice notebook overview:

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Know your data | counting per product, finding risky reviews | warm-up |
| 2 Redaction prototype | string methods, helper functions, edge cases | core project step |
| 3 One review end to end | prompt with delimiters, mock, parse | core project step |
| 4 Keep going, keep count | `try/except` in a loop, counting failures | prepares step 5 |
| 5 Stars vs text (challenge) | the "Should" disagreement check | challenge |

## 5. Common mistakes during the build

Collect these on the board as they appear; most come back in the homework.

| Mistake | Error / symptom | How to explain it |
|---------|-----------------|-------------------|
| Running `app.py` from another folder, or copying `starter/` to a different depth | `FileNotFoundError` for `reviews.csv` | `DATA_PATH` is relative to `app.py`; print `DATA_PATH.resolve()` |
| Replacing the whole word in `redact` | `[PHONE]` without its full stop; punctuation test fails | strip punctuation to get the *core*, replace only the core |
| Counting digits in the whole text instead of the word | `10 km` or every review becomes `[PHONE]` | the rule is about one word at a time |
| Redacting outside `build_prompt` only | privacy test fails in step 5 | redact *inside* `build_prompt`, so no caller can forget it |
| `try` around the whole loop | one bad reply stops all analysis | the `try` belongs around **one** review |
| Rating left as text | `'5' >= 4` → `TypeError` in the disagreement check | `int(row["rating"])` when loading |

## 6. Wrap-up (5 min)

Everyone runs `uv run pytest -q` in their project folder and says the number of passing tests (no judgement: the
goal is to know where to continue). Homework: steps 4–6, the Should features, two own tests, `NOTES.md`.

**Exit question:** "Why does `build_prompt` call `redact` itself, instead of trusting that the caller did it?"
*Answer: then no code path can ever send unredacted text to the model, whoever calls `build_prompt`.*

## Homework (2–3 hours, due start of Day 57)

Finish Project 08 following the README build plan and submission checklist.

## Next class

Day 56 starts the **AI Capstone**: students choose and scope their own AI application. Project 08's structure
(load → protect → model behind a function → validate → report, all testable with a mock) is the template for any
LLM-based capstone. Ask students to bring one idea for a capstone that uses either an ML model (Week 10) or an LLM
(Week 11).

## Instructor notes

- Return checkpoints on Day 56; spend 3 minutes on the two most common mistakes.
- If many students struggle with redaction, show the *helper function* shape on the board
  (`def looks_like_phone(word):` → count digits → return a bool) without the body.
- Strong students: Could features (draft a reply, menu, caching), then the "compare two prompts" extension.
- Students with an API key may try the real model on 5 reviews **after** the tests pass; remind them the tests must
  keep using mocks and the key stays in `.env`.
