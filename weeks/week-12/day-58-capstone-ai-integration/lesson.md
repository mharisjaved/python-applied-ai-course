# Day 58: AI Capstone: Integrate the AI and Test It Offline

**Week 12 · Session 58 of 60 · Planned 75 min** · Previous: [Day 57](../day-57-capstone-core/lesson.md) · Next: [Day 59](../day-59-capstone-reliability/lesson.md)

## Objectives

By the end of this lesson students can:

1. Put the AI part inside **one function** with the shape *prompt → ask → parse/check → fallback* (LLM options)
   or *train at start-up → check inputs → predict* (ML option).
2. Validate a model reply with `json.loads` **and** field checks, returning `None` for anything unusable.
3. Handle the four failure paths: invalid JSON, refusal message, missing key (→ mock), API error (→ mock).
4. Test every path offline by passing **fake model functions** through an `ask=ask_llm` parameter.
5. Measure a success criterion with a small evaluation loop and report the result honestly.

**Prior knowledge:** `sorted(key=...)` passes a function (Day 21), exceptions (Day 25), pytest (Day 29), `json`
(Day 36), scikit-learn fit/predict/evaluate (Days 46–49), `ask_llm` + `.env` + mock (Days 51–53), `json.loads`
validation and testing with mocks (Day 54), the core and stub from Day 57.

**Files:** `demo.ipynb` · `practice.ipynb` · `solutions.ipynb` · `example_app/` (Day 57's app plus `llm.py`, the
AI version of `summary.py`, and `test_summary.py`)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: checkpoint status + retrieval | core |
| 0:05–0:30 | Teaching: the one AI function (demo sections 1–7, 9; section 8 for option A students) | core |
| 0:30–0:45 | Practice Exercises 1–4 | core |
| 0:45–1:10 | Build time: integrate the AI into own capstone, mock first | core |
| 1:10–1:15 | Checkpoint (section 6) and exit ticket | core |
| +15 min | Exercises 5–6, then run your own evaluation loop | optional (90-min session) |

**60 min:** teach demo sections 1, 5, 6, 7 (15 min); practice Exercises 2–4 only; same checkpoint.

## 1. Warm-up (5 min)

Checkpoint status from Day 57: who has `pytest` green and `main.py` running with a stub? Pair anyone who is not
there with someone who is, for the first 5 minutes of build time.

Retrieval questions:
- "On Day 21 we wrote `sorted(students, key=get_score)`. What did we pass, a value or a function?" (*A function,
  without brackets.* Today we use the same idea for fake models.)
- "Why should the app never use `response.content[0].text`?" (*The first block can be a thinking block; join
  the text blocks instead.*)
- "What does `ask_llm` do when there is no API key?" (*Returns the mock's reply.*)

## 2. Teaching: the one AI function (25 min)

**The plan (demo section 1).** Write on the board and keep it there all session:

```
write_summary(totals, ask=ask_llm)
   prompt  -> ask -> parse/check -> result
                        │ refusal / None
                        └──────────> fallback (yesterday's stub)
```

**The helper and an app-specific mock (demo section 3).** The helper is the Day 53 `ask_llm` unchanged, plus
`load_dotenv()` at the top so `LLM_MODEL` from `.env` is read before `MODEL` is set. The interesting part is
`mock_llm`: it reads the numbers *from the prompt* and replies in our JSON shape, so the whole pipeline runs
offline. Every LLM capstone writes its own mock this way: "what would a sensible reply to *my* prompt look like?"

**The prompt (demo section 4).** Only totals, fixed costs marked, JSON shape given, "do not invent numbers".
**Prediction question:** "Where is rent, and what follows its amount?" (*Second in the list, after food; then
`(fixed)`.*) Point out that the role and its limits ("general budgeting tips, never financial-product advice")
are the first lines of the prompt. If you have a key, run the `reply = ask_llm(...)` cell online once so students
see that real wording differs from the mock. Never present mock output as real model output.

**Parse and check (demo section 5).** `parse_summary` returns a dict or `None`. Run the six hand-written replies.
**Prediction question:** "Which survive?" (*1 and 3; the fence is stripped. 2 is chatty, 4 has one tip, 5 an empty
summary, 6 is a list.*) Message: valid JSON is not the same as a usable answer.

**Fallbacks and fakes (demo section 6).** Two layers of safety:

| What goes wrong | Where it is handled | What the user gets |
|-----------------|---------------------|--------------------|
| no API key, or `COURSE_OFFLINE=1` | inside `ask_llm` | the mock's reply |
| wrong key, rate limit, no network, server error | `call_model`: `except anthropic.AuthenticationError` … `APIStatusError` | the mock's reply + a note |
| the model declines (refusal) | `reply == REFUSAL_MESSAGE` | the template, `source` says so |
| chatty text, broken JSON, wrong fields | `parse_summary` returns `None` | the template, `source` says so |

Then define the three fakes and ask: **"Predict the `source` of each."** (*ai, template (not valid JSON),
template (declined).*) Explain `ask=ask_llm`: *a function is a value; the default is the real one, tests pass a
fake one.* This matches Day 54's `analyse_review(text, ask=ask_llm)`; a Week 11 `MockLLM(...).ask` method works as
a fake too: it has the same one-parameter shape `ask(prompt)`.

**Tests (demo section 7).** The same checks as pytest functions; then the terminal:

```
cd weeks/week-12/day-58-capstone-ai-integration/example_app
uv run pytest -q          # 15 passed
uv run python main.py     # "AI mode: offline mock"; type 2026-11, then quit
```

Point out `os.environ["COURSE_OFFLINE"] = "1"` at the top of `test_summary.py`: tests must never spend money
or depend on the network, even by accident.

**Option A (demo section 8, 3 min, or only with A students during build time).** Train once at start-up
(`train_price_model`), one boundary function `predict_price` that checks inputs and returns a dict. Expected
output: typical error about `22.4k`, `{'price_k': 177.4}`, then `177.4 -> 236.5` for 70 vs 100 m². Good ML tests:
data loads, beats the baseline, bad inputs raise, predictions move in a sensible **direction**.

**Evaluation (demo section 9).** Five test cases, three checks, `Passed 5/5`. Ask the 🤔 question: why does 5/5
with the mock prove nothing about the model? (*We wrote the mock. Offline we test the pipeline; online the same
loop measures the model.*) Students report real numbers in their README with date and model name.

## 3. Common mistakes

| Mistake | Error / symptom | How to explain it |
|---------|-----------------|-------------------|
| `json.loads(reply)` with no `try` (demo section 10) | `JSONDecodeError` crashes the app | parsing returns `None`; the caller picks a fallback |
| `ask=fake_good()` (demo section 10) | `TypeError: fake_good() missing 1 required positional argument` | pass the function, do not call it |
| fake that prints instead of returning | `AttributeError: 'NoneType' object has no attribute 'strip'` | a fake returns a string, exactly like a model |
| `data["label"]` on model JSON | `KeyError` on a reply missing a field | `.get()` + check, return `None` |
| tests call the real API | slow, costs money, red without Wi-Fi | fakes + `COURSE_OFFLINE=1` at the top of the test file |
| catching `anthropic.APIStatusError` before `RateLimitError` | the specific branch never runs | most specific exception first (Day 53) |
| model trained inside the prediction function (option A) | every prediction retrains; slow | train once at start-up, pass the model in |

## 4. Practice (15 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Which replies are usable? | JSON vs usable | predict |
| 2 Parse and check the reply | `json.loads` + field checks | application |
| 3 The one AI function | boundary with fallbacks | application |
| 4 Test it with fake models | fakes + test functions | application |
| 5 A small evaluation | accuracy, baseline thinking | independent |
| 6 Option A, a model trained at start-up (challenge) | ML boundary + direction test | challenge |

Look for: label checked before `.lower()` (Exercise 2); `ask=fake()` (Exercise 4); students who think the
offline 6/8 in Exercise 5 measured Claude. It measured the keyword mock, which is the **baseline**.

## 5. Build time (25 min)

Order for every LLM capstone (B, C, D):
1. Write your app's `mock_llm` so it replies in **your** JSON shape. Run the app fully offline.
2. `build_prompt` (only the data needed), `parse_...` (returns dict or `None`), and the boundary function with
   fallbacks. The Day 57 stub becomes the fallback.
3. Fake-model tests: good reply, not JSON, refusal, one wrong-field case.
4. Only then, if you have a key: run once online and compare with the mock.

Option C students: the prompt must contain **only** the retrieved sections and the "I don't know" rule; the mock
returns the best section's answer text. Option A students: `train_model()` at start-up, `predict(model, inputs)`
as the boundary, report test score vs baseline at start-up. For a confidence, classifiers such as `LogisticRegression` have
`model.predict_proba(row)[0][1]`: the probability of class 1 (regression models have no such method).

## 6. Checkpoint and exit ticket (5 min)

**Checkpoint:**
- [ ] The app runs end to end **offline** with the AI function in place (mock or local model).
- [ ] At least **two fake-model tests** (or, option A, input-check and direction tests) pass with `uv run pytest -q`.
- [ ] A bad reply (not JSON) cannot crash the app; you can show the test that proves it.
- [ ] Total tests: aim for ≥ 5 (the capstone minimum).

**Exit ticket:** "Write a fake model that makes `classify_comment` take the refusal path, and the line that
calls it."

Answer:
```python
def fake_refusal(prompt):
    return REFUSAL_MESSAGE

classify_comment("Nice course", ask=fake_refusal)
```

## Homework (40 min)

Finish the checkpoint. Write your evaluation loop over 5–10 test cases for your main success criterion and
record the offline result (and the online one, if you have a key) in your README under *Evaluation*.

## Next class

Day 59 hardens the app: a failure-case table, hallucination checks (numbers must come from the data, answers
must quote a source), privacy (redaction), bias questions, the README's Responsible AI section and a 5-minute
demo script with an offline backup plan.

## Instructor notes

- The most valuable minute today is the fallback table in section 2. Students who understand "where is each
  failure handled?" build robust apps; the rest build apps that crash in the demo.
- Students without a key are not disadvantaged: grading never requires the real API. Students with a key
  should still develop **mock first** and go online only once the tests are green.
- If you demo online, mention cost and rate limits (Day 53); `claude-haiku-5-5` via `LLM_MODEL` in `.env` is the
  much cheaper choice for a class.
- Do not introduce `unittest.mock`, `monkeypatch`, fixtures or structured-output mode as the main path. Strong
  students may try `output_config` with a JSON schema (Day 54 aside), but must keep the `parse_...` checks
  because the mock and the fallback still go through them.
- Fast students: add the API-error `try/except` (`call_model`) and a test that the template fallback still
  returns two tips. Slow students: get the mock path working end to end; fakes can come in homework.
