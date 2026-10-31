# Project 08: AI Text Assistant, the "Review Insights Assistant"

**Week 11 · Day 55 (+ homework)** · Builds on Days 51–54 · Lesson: [Day 55](../../weeks/week-11/day-55-project-ai-assistant/lesson.md)

## The problem

Fatima runs a small online shop that sells five products: wireless earbuds, a coffee maker, a backpack, a desk lamp
and running shoes. Customers leave short reviews (`datasets/reviews.csv`, 40 reviews). Fatima wants to know, every
week, **which products people are unhappy with and what they complain about**. Reading every review by hand does
not scale, so you will build a small program that uses an LLM to read them for her.

Two things make this harder than it sounds:
- **Privacy.** Some customers write their phone number or e-mail address into a review (see R33). Anything you put
  in a prompt leaves your computer when a real model is used, so personal data must be removed **before** a prompt
  is built.
- **Reliability.** The model answers with text. Sometimes the text is not the JSON you asked for, or uses a label
  you did not allow. Your program must check every reply and keep going when one is unusable.

Your program works **fully offline**: without an API key, `llm.py` answers with the course's mock model.

## What it should do

```
$ uv run app.py
Loaded 40 reviews. Analysing...

REVIEW INSIGHTS REPORT
Reviews analysed: 40 (failed: 0)

Sentiment per product:
  backpack: positive 4, negative 3, mixed 1
  coffee maker: positive 3, negative 3, mixed 2
  desk lamp: positive 3, negative 3, mixed 2
  running shoes: positive 4, negative 2, mixed 2
  wireless earbuds: positive 3, negative 3, mixed 2

Most common topics:
  quality: 11
  comfort: 6
  sound: 5
  battery: 5
  ease of use: 5

Top issues (topics in negative and mixed reviews):
  quality: 8
  support: 4
  sound: 3
  ease of use: 3
  delivery: 3

Stars and text disagree (check these by hand):
  R36 5 stars, negative: Oh great, another pair that died after one week.
```

(These numbers come from the offline mock model. With a real model they will be different.)

## Requirements

**Must**
1. Load the reviews from `datasets/reviews.csv` (with `csv` or pandas), with the rating as an `int`.
2. Redact personal data **before** anything is sent to a model: e-mail addresses → `[EMAIL]`, phone-like numbers
   → `[PHONE]`. Use string methods (`split`, `"@" in word`, counting digits); regular expressions are not needed.
3. For each review, ask the LLM (through `ask_llm`, the mock by default) for JSON:
   `{"sentiment": "positive|negative|mixed", "topics": [...], "summary": "..."}`. The review goes inside delimiters.
4. Validate **every** reply (JSON, keys, types, allowed sentiment). Retry once with a stricter prompt. A review
   that still fails is **counted** and skipped; the program never crashes because of a bad reply.
5. Print a report: sentiment counts per product, the most common topics, and the most common issues (topics of
   negative and mixed reviews).
6. Works offline, and `uv run pytest -q` passes in your folder.

**Should**
- A rating-vs-sentiment disagreement check: 4–5 stars but negative text, or 1–2 stars but positive text (R36 is
  sarcastic: 5 stars, "Oh great, another pair that died after one week").
- Save the results (and the failed IDs) to `results.json`.

**Could**
- "Draft a reply to this review": ask the model for a polite 2-sentence reply to a chosen review (redacted!).
- A small menu (`input()` loop in `main()`): show report, show one product, draft a reply, quit.
- Cache replies in a JSON file (review ID → reply) so a second run does not call the model again (saves money).

## Starter files

```
starter/
  llm.py        provided and complete: ask_llm() (real model with a key, mock model without one) and mock_llm()
  app.py        your program: 6 TODO functions + 2 "Should" TODOs; main() is provided
  test_app.py   21 tests for the Must requirements
```

Copy the `starter` folder to `projects/08-ai-text-assistant/my-work/` (the same depth, so the path to `datasets/`
in `app.py` still works), or work in `starter/` directly. From that folder:

```bash
uv run pytest -q      # most tests fail at the start: that is expected
uv run app.py         # runs at every stage, even before the TODOs are done
```

A few tests already pass with the starter (for example, "rejects text without JSON" passes because the unfinished
`parse_response` raises `ValueError` for everything). They protect you from breaking that behaviour later.

**Using the real model (optional):** put your key in `.env` in the course root (Day 53). Never paste it into code.
Run the program on 3–5 reviews first (`load_reviews()[:5]`) to check the cost. Your tests must keep using mocks.

## Build plan

| Step | Do | Checkpoint |
|------|----|------------|
| 1 | `load_reviews` (TODO 1) | the two `test_load_reviews_*` tests pass; `uv run app.py` says "Loaded 40 reviews" |
| 2 | `redact` (TODO 2), with `looks_like_email` / `looks_like_phone` helpers | the four `test_redact_*` tests pass; try `redact()` on R33 yourself |
| 3 | `build_prompt` (TODO 3) | print the prompt for R33: the review sits between tags and contains `[PHONE]` and `[EMAIL]` |
| 4 | `parse_response` (TODO 4) | all `test_parse_response_*` tests pass |
| 5 | `analyse_all` with retry and failure counting (TODO 5) | all `test_analyse_all_*` tests pass, including "never sends personal data" |
| 6 | `make_report` (TODO 6), then the Should features | all tests pass; your output matches the example run |

Work in this order and run the tests after every step. Commit (or save a copy) after each green step.

## Submission checklist

- [ ] `uv run app.py` runs offline and prints the report
- [ ] `uv run pytest -q` passes (all 21 tests, plus any you added)
- [ ] no API key anywhere in your files; `.env` is not in your submission
- [ ] at least **two tests of your own** (for example: a phone number with a `+` and dashes, a reply with a
      `"neutral"` label, an empty review text)
- [ ] a short `NOTES.md`: one limitation of your redaction, one limitation of the mock/LLM analysis, and what you
      would check before trusting the report

## Evaluation rubric (100 points)

| Criterion | Points | What we look for in this project |
|-----------|--------|----------------------------------|
| Works as specified | 40 | all Must requirements; report numbers correct for the mock; **privacy: no personal data in any prompt** (tested) |
| Code readability | 20 | small functions with one job each, clear names, docstrings, no copy-pasted blocks |
| Handles bad input / edge cases | 15 | **every reply validated**; one retry, then the failure is counted; bad CSV rows do not crash |
| Testing / evidence it works | 10 | given tests pass; at least two meaningful tests of your own, using mock models |
| Explanation / demo | 15 | you can explain the pipeline (input → redact → prompt → model → parse → report), why the mock exists, and one way the report could be wrong |

## Extension ideas

- Compare two prompts on the 40 reviews (Day 52): which one fails less often? Which disagrees with the stars more?
- Plot the sentiment counts per product with matplotlib (Day 45).
- Use pandas for the report (`value_counts`, `groupby`) and compare the code with your plain-Python version.
- Make redaction stronger (phone numbers written with spaces, such as `555 0142`) and add tests for each new case.
- With an API key: run the whole report with the real model and write down three differences from the mock.
