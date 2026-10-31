# Project 09: AI Capstone (your own choice)

**Days 56–60 · individual · presented on Day 60**

Twelve weeks ago you wrote `print("Hello, World!")`. Now you will build a small AI application of your own
choice: a tool that a real person could use, that **works offline**, that is **tested**, and that is **honest about
its limits**. You choose the problem; the course gives you four options to start from.

The capstone proves you can **scope, build, test and present an AI application**: plain Python for the core,
a scikit-learn model or an LLM for the one part that needs AI, and the judgement to know when not to trust it.

## Choose an option

### A. ML-powered predictor app
Train a scikit-learn model **when the app starts** on `datasets/students.csv` or `datasets/apartments.csv` (or a
scikit-learn toy dataset). A command-line loop asks for the inputs and prints the prediction, a plain-language
explanation, and a confidence where the model has one. Example run (from the option A reference, local model):

```
Pass predictor (logistic regression)
Trained on 238 students. Test accuracy 82% (always guessing the most common result: 65%).
Answer each question, or type 'quit'.

Study hours per week: 3
Attendance (%): 60
...
Prediction: likely to FAIL (estimated chance of passing: 1%)
Why:
  - Study hours per week = 3.0 (average 8.9) lowers the chance
  - Attendance (%) = 60.0 (average 81.8) lowers the chance
  - Previous term score (0-100) = 50.0 (average 64.4) lowers the chance
This is an estimate from synthetic course data, not a judgement about anyone.
```

### B. LLM text tool
A tool that sends text to `ask_llm`, asks for **JSON**, validates it and falls back safely. Ideas: study-notes
summariser + quiz generator, course-feedback classifier, announcement or e-mail drafter with a fixed structure.
Use `reviews.csv`, your own **non-personal** sample texts, or text you write. Illustrative run (offline mock):

```
Notes quizzer | mode: offline mock
Paste a paragraph of notes (or 'quit'): A list is an ordered, changeable collection ...
Q1. Which of these can you change after creating it? a) tuple  b) list  c) string  d) int
...
(5 questions, all checked: 4 options each, answer among the options)
```

### C. Constrained Q&A assistant over `datasets/campus_faq.md`
Split the FAQ into sections, find the most relevant sections by **keyword overlap** (simple scoring, no
embeddings), and build a prompt that contains **only** those sections and tells the model to answer only from
them and to say "I don't know" otherwise. Always show which section was used. The mock answers with the
best-matching section's text. Example run (from the option C reference, offline mock):

```
Maple Grove FAQ assistant | 16 FAQ sections | mode: offline mock
You: How many books can I borrow?
Assistant: Students can borrow up to 6 books at a time for 14 days. Each book can be renewed twice online if nobody has reserved it.
Source: [S02] Library > How many books can I borrow?

You: Who won the football match?
Assistant: I don't know. The student FAQ does not cover that, so please ask at reception.
```

### D. Your own idea (approval required on Day 56)
Any problem where **one** part genuinely needs ML or an LLM, with data that exists today and contains no real
personal data of other people. Out of scope: web apps and GUIs, training neural networks, scraping, deployment.

## Requirements

**Must** (all options)
- A clear problem statement and target user (in the README and the approved plan).
- A named data source (dataset, FAQ file, or your own sample texts) that you have checked.
- Core logic in **modules** (not one long script), a `main()` CLI loop guarded by `if __name__ == "__main__":`.
- **At least 5 pytest tests** that pass offline with `uv run pytest -q` (no API key, no network).
- The AI part behind **one function**, with an offline mode: the mock (`COURSE_OFFLINE=1` or no key) for LLM
  options, a locally trained model for option A.
- Error handling: bad user input, missing data file, and (LLM) invalid JSON, refusal, missing key, API errors.
- `README.md`: what it does, how to run it offline **and** online, how to run the tests, an example run, and a
  **Responsible AI** section (limitations, privacy, bias, when not to trust it).
- A **5-minute demo** on Day 60.

**Should**
- Measurable success criteria from your plan, measured with a small evaluation loop; results in the README.
- At least one hallucination or sanity check in code (numbers from the data, quotes from the source, predictions
  in a sensible range).
- Personal data minimised: nothing sent that the task does not need; contact details redacted.
- Option A: test score compared with a baseline at start-up; no leakage features.

**Could**
- Compare the mock with a real model on the same test cases.
- Save results to a CSV/JSON file; a chart of results (matplotlib) for the README.
- A second model (option A) or a second prompt version (B/C) compared on the same evaluation.

## Starting point

There is no starter code: it is your project. Start from:
- [PLAN-TEMPLATE.md](PLAN-TEMPLATE.md): fill it on Day 56 and get it approved.
- Your Project 08 `llm.py` (or the Day 53 helper) for options B, C and D. You will write your **own** `mock_llm`
  that answers in your app's JSON shape (Day 58).
- Suggested layout, inside your course workspace (the uv project you have used since Week 6):

```
capstone/
├── PLAN.md          from PLAN-TEMPLATE.md
├── README.md
├── main.py          CLI only: input(), print(), the loop
├── core.py          data loading, validation, logic (no AI)   (use a meaningful name)
├── ai.py            the ONE function that uses AI + prompt + parsing + fallbacks
├── llm.py           ask_llm + mock_llm (LLM options)
└── test_core.py, test_ai.py
```

Run: `uv run python main.py` · Tests: `uv run pytest -q` · Offline on purpose: `COURSE_OFFLINE=1 uv run python main.py`
(PowerShell: `$env:COURSE_OFFLINE="1"; uv run python main.py`).

## Build plan

| Day | Step | Checkpoint before you leave |
|-----|------|-----------------------------|
| 56 | Scope: option, user, input/output, success criteria, data & privacy check, risks, Must/Should/Could | plan approved |
| 57 | Core without AI: loading, validation, logic, tests; a **stub** for the AI function with the final return shape | ≥ 3 tests pass; app runs end to end with the stub |
| 58 | AI behind one function: mock first, parse/validate, fallbacks, fake-model tests; option A: train at start-up | app runs offline with AI; ≥ 2 fake/boundary tests; ≥ 5 tests total |
| 59 | Reliability: failure-case table, hallucination/sanity check, redaction, bias probe, README, demo script | README with Responsible AI; demo rehearsed offline |
| 60 | Present (5 min + questions) | submitted |

## Submission checklist

- [ ] `uv run pytest -q` passes from a fresh terminal, with **no** API key (≥ 5 tests).
- [ ] `COURSE_OFFLINE=1 uv run python main.py` (or `app.py`) runs end to end; the mode is printed at start-up.
- [ ] Bad input, an empty input and a missing data file do not crash the app.
- [ ] The AI part is one function; tests cover its fallback path.
- [ ] README: what it does · how to run offline/online · tests · example run · evaluation · Responsible AI.
- [ ] No `.env` file, no API key anywhere in the code or README.
- [ ] `PLAN.md` included; differences from the plan are explained in one or two sentences.

## Evaluation rubric (100 points)

| Criterion | Points | What earns full points in this project |
|-----------|--------|----------------------------------------|
| Works as specified | 40 | runs offline end to end (10) · core logic correct as planned (10) · **AI behind one function with offline mode and fallbacks** (15) · at least two success criteria met with evidence (5) |
| Code readability | 20 | clear names, small functions, core / AI / CLI separated into modules, docstrings where useful |
| Handles bad input / edge cases | 15 | user input validated; invalid model output, refusal, missing key/network, empty or missing data handled |
| Testing / evidence it works | 10 | ≥ 5 offline pytest tests (5) · fake-model or ML-boundary tests (3) · evaluation results in the README (2) |
| Explanation / demo | 15 | 5-minute demo within time (5) · explains own code and decisions (5) · **Responsible AI section** and limitations discussed honestly (5) |

Capstone-specific checks inside the rubric: the one-function AI boundary, the Responsible AI section, and
evaluation evidence. A smaller app that is robust, tested and honest scores higher than an ambitious app that
crashes or overclaims.

## Extension ideas (after the essentials)

- Option A: compare two models (logistic regression vs decision tree) and explain the choice; add a chart.
- Option B: a second prompt version, evaluated on the same 10 test texts; report both scores.
- Option C: better retrieval (synonym list, weighting rare words more), several FAQ files, an evaluation set of
  20 questions with expected sections.
- Any option: log anonymous usage counts to a CSV (no user text) and summarise them with pandas.
