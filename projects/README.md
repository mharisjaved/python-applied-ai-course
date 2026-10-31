# Projects: the Student Portfolio

Every student finishes the course with **nine projects they built themselves**, including two capstones they
designed. Support is reduced on purpose as the course goes on, so that by the end students can go from an idea to a
working, tested, documented program on their own.

| # | Project | When | Type | Support given | What it proves |
|---|---------|------|------|---------------|----------------|
| 01 | [Quiz Game](01-quiz-game/) | D15 (W3) | console script | starter with question bank + TODO skeleton | input, conditionals, loops, lists/dicts |
| 02 | [Hangman](02-hangman/) | D20 (W4) | console script | function plan made together on D19 | decomposition into functions |
| 03 | [Expense Tracker](03-expense-tracker/) | D30 (W6) | multi-file app + tests | module skeletons + failing tests | files, error handling, modules, pytest |
| 04 | [Inventory Manager](04-inventory-manager/) | D35 (W7) | multi-file app + tests | class skeletons + failing tests | classes and composition |
| 05 | [**Python Capstone**](05-python-capstone/) | D38–D40 (W8) | own choice | **plan template only** | independent Python application |
| 06 | [Data Analysis Report](06-data-analysis-report/) | D45 → D47 (W9–10) | notebook | section headings | cleaning, analysis, charts, written findings |
| 07 | [ML Predictor](07-ml-predictor/) | D50 (W10) | notebook | choice of 3 tasks + section headings | end-to-end scikit-learn workflow |
| 08 | [AI Text Assistant](08-ai-text-assistant/) | D55 (W11) | app + tests | LLM helper provided, TODO functions | LLM app with validation, privacy, offline mock |
| 09 | [**AI Capstone**](09-ai-capstone/) | D56–D60 (W12) | own choice | **plan template only** | independent AI application |

Each project folder contains:

- `README.md`: the **student brief** (share it): problem, requirements (Must / Should / Could), build plan, submission checklist, rubric, extensions.
- `starter/`: files students begin from (share it). Capstones have a plan template instead.
- `reference/`: a complete instructor implementation (**keep private**). From Project 03 on it has passing tests.
- `INSTRUCTOR.md`: session plan, common pitfalls, how to unblock without giving answers, grading notes (**keep private**).

## Shared rubric (100 points)

| Criterion | Points | What "full marks" looks like |
|-----------|--------|------------------------------|
| Works as specified | 40 | All *Must* requirements work; no crashes in a normal demo |
| Code readability | 20 | Clear names, small functions, comments where the *why* isn't obvious |
| Bad input & edge cases | 15 | Invalid input is handled with a helpful message; empty data doesn't crash |
| Evidence it works | 10 | Projects 01–02: example runs shown. Project 03+: tests that pass |
| Explanation / demo | 15 | Student can explain any part of their code and one decision they made |

Each brief adds 2–3 project-specific criteria. *Should* and *Could* items earn up to 10 bonus points (cap at 100).

**Independence rule:** students may use the course notes, cheatsheets, their old projects and documentation. AI
assistants may be used to *explain* errors or concepts, but not to write the project. Students must be able to
explain every line in the demo.

## Portfolio checklist (reviewed on Day 60)

Each student keeps one folder (ideally a Git repository) with a sub-folder per project, each containing:

- [ ] the code (runs with the command written in its README)
- [ ] a short `README.md`: what it does, how to run it, an example run or screenshot, what they would improve next
- [ ] tests (Projects 03, 04, 05, 08, 09) that pass with `uv run pytest`
- [ ] no API keys, passwords or personal data committed
