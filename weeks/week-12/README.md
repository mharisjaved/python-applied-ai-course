# Week 12: Final AI Capstone

Students scope, build, test and present their own AI application in five sessions. Every session is a short
teaching segment on one technique (shown on a worked example, the *Spending Summary Assistant*), followed by
supervised build time and a checkpoint. The week ends with presentations, the final assessment and course feedback.

| Day | Topic | Materials |
|-----|-------|-----------|
| 56 | Choose and scope: options, measurable success criteria, data & privacy check, risks, plan approval | [lesson](day-56-capstone-scoping/lesson.md) · [demo](day-56-capstone-scoping/demo.ipynb) · [practice](day-56-capstone-scoping/practice.ipynb) · [solutions](day-56-capstone-scoping/solutions.ipynb) |
| 57 | Build the core first: modules, pure functions, pytest, AI stub | [lesson](day-57-capstone-core/lesson.md) · [demo](day-57-capstone-core/demo.ipynb) · [practice](day-57-capstone-core/practice.ipynb) · [solutions](day-57-capstone-core/solutions.ipynb) · [example_app](day-57-capstone-core/example_app/) |
| 58 | Integrate the AI behind one function: mock first, fallbacks, fake-model tests, evaluation | [lesson](day-58-capstone-ai-integration/lesson.md) · [demo](day-58-capstone-ai-integration/demo.ipynb) · [practice](day-58-capstone-ai-integration/practice.ipynb) · [solutions](day-58-capstone-ai-integration/solutions.ipynb) · [example_app](day-58-capstone-ai-integration/example_app/) |
| 59 | Reliability and responsible AI: failure table, hallucination checks, redaction, bias probes, README, demo script | [lesson](day-59-capstone-reliability/lesson.md) · [demo](day-59-capstone-reliability/demo.ipynb) · [practice](day-59-capstone-reliability/practice.ipynb) · [solutions](day-59-capstone-reliability/solutions.ipynb) |
| 60 | Final presentations, final assessment, course feedback, next steps | [lesson](day-60-final-presentations/lesson.md) · [demo](day-60-final-presentations/demo.ipynb) · [practice (final review)](day-60-final-presentations/practice.ipynb) · [solutions](day-60-final-presentations/solutions.ipynb) |

**Project:** [09 AI Capstone](../../projects/09-ai-capstone/README.md) (brief, rubric,
[plan template](../../projects/09-ai-capstone/PLAN-TEMPLATE.md), [instructor notes](../../projects/09-ai-capstone/INSTRUCTOR.md),
reference implementations for options A and C) ·
**Assessment:** [final assessment](../../assessments/final/ai-final-assessment.md) on Day 60 (replaces a weekly checkpoint).

## Prepare before the week

- [ ] Run both references offline: `cd projects/09-ai-capstone/reference/option-c-faq-assistant && uv run pytest -q`
      and the same in `option-a-ml-predictor`; try `uv run python assistant.py` / `uv run python app.py`.
- [ ] Run both `example_app/` folders (Days 57 and 58): `uv run pytest -q` and `uv run python main.py`.
- [ ] Decide whether you will show the real API at all. If yes: `.env` with a key in the course root, and
      `LLM_MODEL=claude-haiku-5-5` if cost matters. Rehearse the offline switch (`COURSE_OFFLINE=1`) anyway.
- [ ] Print the plan approval checklist (Day 56 lesson, section 6) and make a tracking sheet: plan approved,
      Day 57/58/59 checkpoints, presentation slot.
- [ ] Check the calendar: Day 60 is planned for 1 January (likely a holiday). Book the replacement session(s),
      two if you have more than 6 students (Day 60 lesson, Timing).

## Common difficulties this week

| Difficulty | How to respond |
|------------|----------------|
| Scope too big ("a chatbot that knows everything", web app, own neural network) | Use the approval checklist; cut to a Must list that fills ~80 % of four sessions. Offer the closest option A–C. |
| Students start with the AI and have no working app on Day 58 | Day 57 rule: no `ask_llm` until the core tests are green and the stub runs end to end. |
| App crashes on the first odd reply or input | The fallback table (Day 58) and the failure-case table (Day 59): every row becomes a test. |
| No API key, worried about grades or cost | Every requirement can be met offline; grading runs the app with the mock or the local model. |
| Code written by an AI assistant that the student cannot explain | Ask about specific lines during build time, not only at the presentation; "Explanation" is 15 % of the grade. |
