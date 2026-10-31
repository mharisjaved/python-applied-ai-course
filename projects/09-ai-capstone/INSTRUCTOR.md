# Project 09: AI Capstone, instructor notes

## Timing plan

| Day | Teaching | Build time | Your job while students build |
|-----|----------|------------|-------------------------------|
| 56 | 20 min scoping (demo) | 35 min plan + practice | approve plans with the checklist (Day 56 lesson, section 6); 2–3 min each |
| 57 | 20 min core first | 33 min | check that nobody calls the AI yet; unblock tests and imports |
| 58 | 25 min AI boundary | 25 min | check mocks answer in the app's own JSON shape; fallbacks exist |
| 59 | 23 min reliability | 25 min + 7 min rehearsal | read Responsible AI drafts; push for one handled failure in each demo |
| 60 | none | presentations + assessment | grade the demo/explanation rows live; collect peer feedback |

Expect about 4 × 30–35 min of in-class build time plus 3 × 40–60 min of homework. Scope plans for **that**.

Keep a tracking sheet: *plan approved · D57 checkpoint · D58 checkpoint · D59 checkpoint · presentation slot*.
Anyone missing two checkpoints in a row gets a 5-minute rescue conversation: cut the scope, not the quality.

## Plan approval

Use the checklist in the Day 56 lesson. Typical changes you will ask for:
- "AI does the calculation" → code calculates, the AI words / predicts / retrieves.
- "Success = it works / users like it" → a number and how it is measured.
- Real personal data (classmates' messages, family finances, health) → synthetic data or a course dataset.
- Two AI features → choose one; the other becomes a *Could*.
- Option D with no data yet → today, in class, or switch to the closest option.

## How to unblock without giving the answer

| Stuck on | Ask / suggest |
|----------|---------------|
| Where to start the core | "Which function would you test first with three hand-made records?" |
| Tests cannot import the module | "Which folder is your terminal in? Run `ls`." |
| Option C splitting | "What do the `## ` and `### ` lines mean? Loop over lines and keep the current topic in a variable." |
| Option C retrieval | "For one question, list its words and one section's words. How many are shared? Turn that into a score." |
| Option A explanation | "How far is this input from the average student? Which direction does the coefficient push?" |
| Writing the mock | "If a perfect model answered *your* prompt, what JSON would it send? Make the mock build that from the prompt." |
| Fallbacks | "Draw the four failure paths (no key, API error, refusal, bad reply). Where is each one handled?" |
| Testing the AI part | "Pass a fake function as `ask`. What should happen if it returns `'not json'`?" |
| Hallucination check | "What claim can the reply make that you can check with code: a number, a section ID, a quote?" |

Show the **worked example** (`weeks/week-12/day-57…` and `day-58…/example_app`) freely; it is a different
problem. Show the **references** only to students who are completely blocked, and then only one function.

## Common pitfalls

- **Too much scope.** The most common failure. Cut early; a robust small app scores higher (see rubric).
- **AI first, core never.** Enforce the Day 57 rule: no model calls until core tests are green.
- **Mock that ignores the prompt** (always returns the same text): the pipeline is never really exercised. The mock
  should read the prompt and answer in the app's JSON shape.
- **Keys in code or committed `.env`.** Check every submission with a search for `sk-ant` and `api_key=`.
- **Untrusted parsing.** `json.loads(reply)["label"]` without checks crashes on the first odd reply.
- **Option A leakage** (`final_score` predicting `passed`) and **no baseline**.
- **Option C sending the whole FAQ** to the model, or showing no source. Both miss the point of the option.
- **AI-written code the student cannot explain.** Ask about specific lines during build time, not only on Day 60.

## Use of AI assistants by students

Decide your policy before Day 56 and say it clearly. Suggested: assistants may be used for explanations and
debugging hints, **not** to write whole functions; students must be able to explain every line. The
"Explanation/demo" row (15 points) and the Day 60 questions check this.

## Grading notes

Grade with the rubric in [README.md](README.md). For every submission:
1. Fresh terminal, **no key**: `uv run pytest -q`, then run the app with `COURSE_OFFLINE=1`. Grading never needs the
   real API. If a student's online mode differs from offline, grade offline and note it.
2. Try three things: an empty input, a nonsense input, and (LLM) a quick look at the fallback test.
3. Compare with `PLAN.md`; reasonable, explained scope changes are fine.
4. Read the Responsible AI section: specific limitations score; "it may have bugs" does not.

Guidance per row:
- *Works as specified (40):* the 15 points for the AI boundary need **one** function, an offline mode, and at least
  two handled failure paths (e.g. bad JSON + refusal, or bad input + out-of-range for option A).
- *Readability (20):* deduct for one long script, unclear names, logic inside `main()`.
- *Edge cases (15):* full marks only if the app survives the three checks above and documents the rest.
- *Testing (10):* tests must pass offline; tests that call the real API score 0 for that part.
- *Explanation (15):* demo within 5 minutes, clear answers about their own code, honest limitations.

## Reference implementations

Both read the course datasets via `Path(__file__).parent / "../../../../datasets/<file>"`, so run them from their
own folder inside the course repository.

| Folder | Files | Run | Tests |
|--------|-------|-----|-------|
| `reference/option-c-faq-assistant/` | `faq.py` (split, keywords, retrieval, redaction) · `llm.py` · `assistant.py` (one AI function `answer_question` + CLI) · `evaluate.py` · `test_faq.py` · `README.md` | `uv run python assistant.py` · `uv run python evaluate.py` | `uv run pytest -q` → 15 passed |
| `reference/option-a-ml-predictor/` | `predictor.py` (load, train, check, explain, `predict_pass`) · `app.py` (CLI) · `test_predictor.py` · `README.md` | `uv run python app.py` | `uv run pytest -q` → 9 passed |

How they were checked (offline, no key): pytest in each folder; the CLIs were pipe-tested, e.g.
`printf 'How many books can I borrow?\n\nWho won the football match?\nquit\n' | COURSE_OFFLINE=1 uv run python assistant.py`
and `printf '3\n60\n6\n50\n4\nn\n' | uv run python app.py`. Option C's `evaluate.py` gives 9/12 offline; the three
misses are deliberate examples of keyword-retrieval limits (synonyms, a shared word "late") for the Day 59
discussion. The online path of `ask_llm` follows the course pattern but was not run here (no key in the
authoring environment); test it once with your own key before Week 12 if you plan to demo online.

## Day 60 logistics

See the Day 60 lesson: Plan A (≤ 6 students, one session) or Plan B (two sessions), the question bank, the peer
feedback form and the course feedback form. Day 60 is planned for 1 January; move it and record the date in
`PROGRESS.md`.
