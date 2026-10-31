# Day 54: Parsing, Validation and Mocks

**Week 11 · Session 54 of 60 · Planned 75 min** · Previous: [Day 53](../day-53-llm-api/lesson.md) · Next: [Day 55](../day-55-project-ai-assistant/lesson.md)

## Objectives

By the end of this lesson students can:

1. Ask a model for JSON and turn the reply into a dict with `json.loads`, also when extra text surrounds it.
2. Validate a parsed reply: required keys, types (`isinstance`), allowed values, non-empty text, and clean it.
3. Handle `json.JSONDecodeError`, invalid values and API errors without crashing, and retry **once** with a
   stricter prompt.
4. Write a `MockLLM` class with predictable (and predictably broken) behaviour.
5. Test LLM-dependent code offline by passing a mock model into the function, and run the tests with pytest.

**Prior knowledge:** `raise ValueError`, `try/except` (Day 25), pytest and `pytest.raises` (Day 29), classes,
methods and `__str__` (Days 32–33), `json.load`/`json.dump` with files (Day 36), passing a function as an argument
like `key=len` (Day 21), `ask_llm` and API errors (Day 53), prompts with delimiters (Day 52).

**Files:** `demo.ipynb` · `practice.ipynb` · `solutions.ipynb` · `llm.py` (from Day 53) · `review_analyser.py`
(the finished analyser built in the demo) · `mock_model.py` (the `MockLLM` class) · `test_review_analyser.py`
(14 pytest tests).

**New today:** `json.loads` / `json.dumps` (strings instead of files), `json.JSONDecodeError`, `isinstance()`,
`str.rfind()`.

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: `json.load` vs a string, `raise ValueError` | core |
| 0:05–0:13 | Text → data with `json.loads` (demo 1) | core |
| 0:13–0:23 | Asking for JSON; when parsing fails; two fixes (demo 2–3) | core |
| 0:23–0:33 | Validating fields (demo 4) | core |
| 0:33–0:40 | Retry once + API errors: `analyse_review` (demo 5) | core |
| 0:40–0:50 | `MockLLM` and testing with pytest (demo 6–7) | core |
| 0:50–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +15 min | Exercise 6 (challenge), demo 8 on all 40 reviews, or the structured-output aside | optional (90-min session) |

**60-min version:** skip demo section 3's prompt-only fix (show only `parse_json_reply`), show the test file in
the terminal instead of writing tests live, and set Exercise 5 as homework.

## 1. Warm-up (5 min)

- "On Day 36 we used `json.load(file)`. Our model's reply is a **string**, not a file. What do we need?"
  (*A function that reads JSON from a string: today's `json.loads`.*)
- "Write a function that raises `ValueError` if a mark is not between 0 and 100." (one volunteer at the board;
  this is the pattern for today's validation.)

## 2. Text → data (8 min)

**Why:** Day 52 got one-word answers. Real tasks need several values at once (sentiment *and* topics *and* a
summary). JSON is the format both models and Python understand.

Live code (demo section 1):

```python
reply = '{"sentiment": "positive", "topics": ["battery", "sound"], "summary": "Great earbuds."}'
data = json.loads(reply)        # "load string" -> dict
data["topics"][0]               # 'battery'
json.dumps(data)                # dict -> string (the opposite)
```

JSON rules that differ from Python: **double quotes only**, `true`/`false`/`null`, no trailing comma.

**Prediction question:** `json.loads("{'sentiment': 'positive'}")`? (*`JSONDecodeError`: single quotes are not JSON.*)

## 3. Asking for JSON, and when parsing fails (10 min)

Live code (demo section 2): a prompt that says "Return JSON with keys..." gets this from the mock (real models do it
too, sometimes):

````
Here is the analysis you asked for:
```json
{"sentiment": "negative", "topics": ["quality", "design"], "summary": "Zip broke within a month of daily use."}
```
````

`json.loads(reply)` → `JSONDecodeError: Expecting value: line 1 column 1`. Two fixes, use **both** (demo section 3):
1. **Prompt:** "Return **only** a JSON object..." (the mock then returns bare JSON).
2. **Code:** `parse_json_reply(reply)` takes the text from the first `{` to the last `}` (`find`/`rfind`) and only
   then calls `json.loads`. If there is no `{`, it raises `ValueError` itself.

Key point: `json.JSONDecodeError` is a kind of `ValueError` (`issubclass` from Day 53), so one `except ValueError`
catches "not JSON at all" and "broken JSON" alike.

Aside for strong students only: the API can also *force* a JSON shape (structured output via `output_config` on
`client.messages.create`). We validate ourselves because that works with every model and with the mock.

## 4. Validating fields (10 min)

**Valid JSON is not the same as valid data.** Demo section 4 parses four replies that are perfect JSON but useless:
a missing key, `"sentiment": "neutral"` (not allowed), `"topics": "battery"` (a string, not a list), and an empty
summary.

`validate_analysis(data)` checks, in order, and raises `ValueError` with a clear message at the first problem:

| Check | Code |
|-------|------|
| it is a dict | `isinstance(data, dict)` (new: "is this value of this type?") |
| required keys | `for key in REQUIRED_KEYS: if key not in data` |
| allowed sentiment | `sentiment.strip().lower() in ALLOWED_SENTIMENTS` |
| topics is a list of non-empty strings | `isinstance(topics, list)`, loop over items |
| summary non-empty | `summary.strip() != ""` |

It returns a **clean copy** (lowercase, stripped, at most 3 topics), so the rest of the program can trust the data.

**Prediction question:** "`isinstance(['a'], list)`, `isinstance('a', list)`, `isinstance(True, str)`?"
(*`True`, `False`, `False`.*)

## 5. Retry once, and API errors (7 min)

`analyse_review(review, ask=ask_llm)` (demo section 5, also in `review_analyser.py`):

```python
for prompt in [build_prompt(review), build_strict_prompt(review)]:
    try:
        reply = ask(prompt)
    except anthropic.APIConnectionError: ...  return None
    except anthropic.APIStatusError as error: ...  return None
    try:
        return validate_analysis(parse_json_reply(reply))
    except ValueError as error:
        print("Unusable reply:", error)
return None
```

- The loop over two prompts **is** the retry: second attempt = same prompt + "Return ONLY the JSON object".
- **Retry once, not forever.** A `while True` retry can loop (and bill) endlessly. After two failures we return
  `None` and the caller counts it.
- API errors are not retried here: the SDK already retried 429/5xx twice (Day 53).
- `ask=ask_llm` is a default parameter whose value is a **function** (like `key=len`). Normally it is the real
  helper; a test passes a mock instead. This one design decision makes the code testable.

## 6. `MockLLM` and testing (10 min)

**Why:** we cannot test with the real model: it costs money, needs a network and gives different answers. And we
need to test what happens when the model misbehaves, which a good model rarely does on demand.

Live code (demo section 6): build `MockLLM` (Week 7 OOP):
- `__init__(self, fail_first=0, bad_reply=...)` stores the settings, plus `calls = 0` and `prompts = []`;
- `ask(self, prompt)` counts the call, records the prompt, returns `bad_reply` for the first `fail_first` calls,
  then `mock_llm(prompt)`.

Pass the **method** without brackets: `analyse_review(text, ask=model.ask)`. Then check `model.calls`
(1, 2 or 2 for `fail_first` 0, 1, 5) and `model.prompts[1]` (the stricter prompt).

Demo section 7 runs test functions in the notebook, then the same tests from `test_review_analyser.py` in the
terminal:

```bash
cd weeks/week-11/day-54-parsing-validation
uv run pytest -q          # 14 passed
```

## 7. Common mistakes (shown during the demo)

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `json.load(reply)` on a string | `AttributeError: 'str' object has no attribute 'read'` | `load` = file, `loads` = string |
| `json.loads` on text with a fence | `JSONDecodeError: Expecting value` | cut out the `{...}` first, ask for "only JSON" |
| `data["sentiment"]` before checking | `KeyError` | validate keys first, then read |
| `except KeyError` around `json.loads` | the `JSONDecodeError` still crashes | catch `ValueError` |
| `while True:` retry | endless loop / endless bill | retry once, then give up and count it |
| `ask=model.ask()` with brackets | `TypeError` (missing prompt) | pass the method, do not call it |

## 8. Practice (20 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Will it parse? | JSON rules, `json.loads`, error types | predict |
| 2 Find the JSON | `find`/`rfind`, `json.loads`, raising `ValueError` | apply |
| 3 Validate a support ticket | required keys, `isinstance`, allowed values (new domain) | apply |
| 4 Fix the analyser | `loads` vs `load`, wrong `except`, endless retry, order of checks | modify / fix |
| 5 Test with `MockLLM` | tests that use a mock model | independent problem |
| 6 A scripted mock (challenge) | a new mock class for exact test scenarios | challenge |

Circulate and look for: `isinstance(x, "list")` (a string instead of the type); validation that returns `False`
instead of raising; tests that create one `MockLLM` and reuse it across tests (the call count keeps growing).

## 9. Recap and exit ticket (5 min)

Recap:
1. Ask for "only JSON", then still cut out the `{...}` and `json.loads` it.
2. Valid JSON is not valid data: check keys, types, allowed values; raise `ValueError`; return a clean copy.
3. Retry once with a stricter prompt; after that return `None` and count the failure.
4. Pass the model into the function (`ask=...`) so tests can use a `MockLLM` that fails on purpose.

**Exit ticket:** what does `analyse_review("Love it!", ask=MockLLM(fail_first=1).ask)` return, and how many times
was the model asked? *Answer: a dict with `"sentiment": "positive"`; asked twice (one broken reply, one retry).*

## Homework (25 min)

Finish Exercise 5 and move your tests into a new file `test_my_analyser.py` in this folder; run `uv run pytest -q`.
Read the Project 08 brief ([projects/08-ai-text-assistant/README.md](../../../projects/08-ai-text-assistant/README.md))
before Day 55.

## Next class

Day 55 is project day: the **Review Insights Assistant** combines everything from this week (redaction of personal
data, a JSON prompt, validation with retry, counting failures, a report) on all 40 reviews, offline with the mock.
It also includes Checkpoint 11.

## Instructor notes

- Keep `review_analyser.py` on screen when explaining section 5: it is the reference shape for Project 08.
- Do not introduce JSON Schema libraries, pydantic, dataclasses or regex. `isinstance` and `if` are enough.
- Students sometimes ask "why not just fix the reply with more string tricks?" Because every trick handles one
  failure we have seen; validation catches the ones we have not seen yet.
- `pytest.raises` was introduced on Day 29. If your group skipped it, show one example (`with pytest.raises(ValueError):`)
  before Exercise 5.
- Fast students: Exercise 6, then add a check that topics are at most 20 characters long. Slow students: in
  Exercise 3, give them the list of checks from the section 4 table to follow.
