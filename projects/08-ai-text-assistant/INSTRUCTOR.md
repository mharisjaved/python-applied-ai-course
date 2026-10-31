# Project 08 Instructor Notes: Review Insights Assistant

Student brief: [README.md](README.md) · Session plan: [Day 55 lesson](../../weeks/week-11/day-55-project-ai-assistant/lesson.md)

## Timing plan

Day 55 is 75 minutes, and Checkpoint 11 takes the first ~20 of them, so the project is **started in class and
finished as homework** (about 2–3 hours in total). Suggested deadline: the start of Day 57, so it does not
compete with capstone scoping on Day 56.

| When | What |
|------|------|
| Day 55, 0:23–0:33 | Kick-off: brief, example run, the privacy problem in R33, starter tour (demo notebook) |
| Day 55, 0:33–0:70 | Build steps 1–3 in class (load, redact, prompt). Prototype in `practice.ipynb`, then move code into `app.py` |
| Day 55, 0:70–0:75 | Everyone runs `uv run pytest -q` and writes down how many tests pass; homework = steps 4–6 |
| Homework | Steps 4–6 (parse, analyse with retry, report), Should features, two own tests, `NOTES.md` |
| Day 56 (5 min) | Quick check of who is stuck at which step; pair stuck students with finished ones |

Most students finish steps 1–3 in class. Steps 4–5 reuse Day 54 code almost directly; step 6 is counting with
dicts and `Counter` (Weeks 3, 6).

## Expected results with the mock

`reference/` prints exactly the example run in the README (40 analysed, 0 failed, only R36 flagged as a
disagreement). Students whose sentiment counts differ usually changed the prompt in a way the mock reads
differently:
- no `"mixed"` in the prompt → the mock never answers `mixed` (and some ties become `neutral`, which validation
  must reject → retries → failures);
- no delimiters → the review text is mixed into the instructions;
- no "only" → the reply has a sentence and a code fence around the JSON (fine if `parse_response` cuts out the
  `{...}`).
These are good teaching moments, not bugs in the mock. `llm.py` lists the mock's rules in its docstring.

## Common pitfalls and how to unblock (without giving the answer)

| Symptom | Likely cause | Ask the student… |
|---------|--------------|------------------|
| `FileNotFoundError` for the CSV | copied the folder to a different depth, or ran from another folder | "Print `DATA_PATH.resolve()`. Where does it point?" |
| `test_redact_replaces_phone_and_keeps_punctuation` fails with `[PHONE]` missing the dot | replaced the whole word instead of the core | "What is `word` and what is `core` for `555-0142.`?" |
| `100 km` became `[PHONE]` | digit rule too loose | "How many digits does a phone number have at least?" |
| prompt still contains the e-mail | redacted in `analyse_all` but `build_prompt` uses the raw text, or the other way round | "Which function builds the text that is sent? Does it see the raw review?" |
| every review fails | `json.loads(reply)` on the fenced reply, or comparing `"Positive"` with `"positive"` | "Print one raw reply. What is around the JSON?" |
| program stops at the first bad reply | `except` around the whole loop instead of around one review | "If review 3 fails, should review 4 still run? Where must the `try` be?" |
| endless loop | `while True` retry | "How many attempts did we agree on, on Day 54?" |
| report test fails on spacing | wrote `backpack : positive 4` or a table | "The test looks for this exact line; compare character by character." |
| tests call the real API | student removed `ask=` from the tests or set `ask_llm` inside `analyse_all` | "Which model does the test pass in? Is it used?" |

Rule of thumb: point to the failing **test name**, ask them to read the assertion, then ask one of the questions
above. Do not type in their file.

## Privacy discussion (5 minutes during kick-off)

Show R33 (fictional data). Ask: "If we send this to a real model, where does the phone number go?" (*To another
company's servers; it may be logged.*) The redaction is simple and imperfect; that is fine for this project as long
as students can name a case it misses (phone numbers with spaces, names, addresses). Better to hide too much
(a date such as `2026-10-13` looks like a phone number to this rule) than too little.

## Grading notes

- Use the rubric in the README. The privacy test (`test_analyse_all_never_sends_personal_data_to_the_model`)
  and "every reply validated" carry most of the project-specific weight: a report that looks right but crashes on
  one bad reply, or leaks R33's contact details, cannot get full marks for "Works as specified" / "Handles bad
  input".
- Accept different but reasonable report layouts **only if** the required lines in the tests are present.
- Own tests: look for tests that use a mock model on purpose (a broken reply, a `"neutral"` label, a review with
  personal data). Tests that only re-check the given tests' cases earn little.
- `NOTES.md` is part of "Explanation": a student who writes "the mock cannot detect sarcasm except by a fixed
  rule" or "a 3-star review counted as negative because of the word refund" has understood the limits.
- In the demo (2–3 minutes per student), ask: "What happens if the model answers `neutral`?" and "How do you know
  no phone number reached the model?"

## Reference solution

`reference/app.py` (Must + Should + the "draft a reply" Could, with an `input()` loop in `main()`),
`reference/test_app.py` (25 tests; 21 are the starter's tests, plus disagreements, `save_results` with pytest's
`tmp_path` folder, the full-run R36 check and `draft_reply`). Check:

```bash
cd projects/08-ai-text-assistant/reference && uv run pytest -q     # 25 passed
uv run app.py                                                       # press Enter at the prompt to quit
```

The `input()` loop in `main()` was tested by hand (`R13`, an unknown ID, then Enter). `uv run app.py` writes
`results.json` next to `app.py`; it is a program output and can be deleted.
