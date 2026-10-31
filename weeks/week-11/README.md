# Week 11: Generative AI and Python Applications

Students learn how LLM applications work and build one: prompt templates, prompt design measured on a test set,
calling Claude through a small `ask_llm()` helper without ever exposing a key, and turning free-text replies into
validated data that is tested with mock models. **Everything runs offline:** without an API key, `llm.py` answers
with a deterministic, keyword-based mock model; the real API is optional and the instructor's choice.

| Day | Topic | Lesson | Demo | Practice | Solutions |
|-----|-------|--------|------|----------|-----------|
| 51 | How LLM apps work | [lesson](day-51-how-llms-work/lesson.md) | [demo](day-51-how-llms-work/demo.ipynb) | [practice](day-51-how-llms-work/practice.ipynb) | [solutions](day-51-how-llms-work/solutions.ipynb) |
| 52 | Prompt design and reliability | [lesson](day-52-prompt-design/lesson.md) | [demo](day-52-prompt-design/demo.ipynb) | [practice](day-52-prompt-design/practice.ipynb) | [solutions](day-52-prompt-design/solutions.ipynb) |
| 53 | Calling an LLM API | [lesson](day-53-llm-api/lesson.md) | [demo](day-53-llm-api/demo.ipynb) | [practice](day-53-llm-api/practice.ipynb) | [solutions](day-53-llm-api/solutions.ipynb) |
| 54 | Parsing, validation and mocks | [lesson](day-54-parsing-validation/lesson.md) | [demo](day-54-parsing-validation/demo.ipynb) | [practice](day-54-parsing-validation/practice.ipynb) | [solutions](day-54-parsing-validation/solutions.ipynb) |
| 55 | 🏗 Project 08 + Checkpoint 11 | [lesson](day-55-project-ai-assistant/lesson.md) | [demo](day-55-project-ai-assistant/demo.ipynb) | [practice](day-55-project-ai-assistant/practice.ipynb) | [solutions](day-55-project-ai-assistant/solutions.ipynb) |

- **Project:** [Project 08: Review Insights Assistant](../../projects/08-ai-text-assistant/README.md)
  ([instructor notes](../../projects/08-ai-text-assistant/INSTRUCTOR.md)), started on Day 55, finished as homework.
- **Checkpoint:** [Checkpoint 11](../../assessments/weekly/week-11-checkpoint.md), first 20 minutes of Day 55.
- **Shared files:** `llm.py` (identical copy in Days 52–55 and the project) holds `ask_llm()` and the mock; its
  docstring lists every mock rule. Day 54 adds `review_analyser.py`, `mock_model.py` and 14 pytest tests.
- **Data:** `datasets/reviews.csv` (40 reviews; R05 one word, R31 mixed, R33 fictional contact details, R36 sarcasm).

## Prepare before the week

- [ ] Decide whether you will show the real model at all. If yes: create an API key, set a spending limit, choose
      the model (`claude-haiku-5-5` is far cheaper than the default `claude-opus-5-5`), and put both in `.env` in
      the course root (Day 53 lesson, section 4). Run `uv run python weeks/week-11/day-53-llm-api/llm.py` once.
- [ ] Never open `.env` on the projector. Check that `.gitignore` contains `.env`.
- [ ] Run `uv run pytest -q` in `weeks/week-11/day-54-parsing-validation/` and in
      `projects/08-ai-text-assistant/reference/` (14 and 25 tests pass, offline).
- [ ] Read the rules at the top of `llm.py` so you can predict the mock's answers during the demos.
- [ ] Print Checkpoint 11 (questions only) for Day 55.

## Common difficulties and how to respond

1. **"Is the mock the real AI?"** No. Repeat every day: the mock follows a few fixed rules so that everyone gets the
   same answers offline; real models are more capable and less predictable. That is exactly why we validate.
2. **Keys pasted into notebooks.** Stop it immediately and kindly; explain revoking. Keys live only in `.env`.
   Students do not need keys for anything in this course.
3. **`json.load` vs `json.loads`, and `ValueError` vs `KeyError`.** Draw "load = file, loads = string" on the
   board, and show `issubclass(json.JSONDecodeError, ValueError)`.
4. **Passing a function vs calling it** (`ask=model.ask` vs `ask=model.ask()`). Link it to `key=len` from Day 21:
   "we hand over the tool, the function uses it".
5. **Trusting one good-looking output.** Bring every discussion back to measuring: the Day 52 test set, the Day 54
   tests, the Project 08 privacy test.
