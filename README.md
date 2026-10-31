# Python + Applied AI: 12-Week Teaching Course

A complete, day-by-day course for beginners: **8 weeks of Python foundations** followed by **4 weeks of applied
AI** (data analysis, scikit-learn, LLM applications). 60 sessions of ~75 minutes, each with instructor notes, a live
demo notebook, student exercises and solutions. Students build **nine portfolio projects**, including two capstones
they design themselves.

## Before each class (5 minutes)

1. Open [PROGRESS.md](PROGRESS.md) → **Next class** link.
2. Read that day's `lesson.md` (objectives, timing, explanations, questions to ask, common mistakes).
3. Open `demo.ipynb` in VS Code, select the `.venv` kernel, **Restart → Run All** once to check it works, then
   **Clear All Outputs** so students can predict before you run each cell.
4. Have `practice.ipynb` ready to share with students; keep `solutions.ipynb` to yourself.
5. After class, update PROGRESS.md (taught date + anything to reinforce).

## Course map

| Weeks | Phase | Ends with |
|-------|-------|-----------|
| 1–2 | Python basics: types, strings, collections, decisions | Checkpoints 1–2 |
| 3 | Loops | Project 01: Quiz Game |
| 4 | Functions | Project 02: Hangman |
| 5 | Built-ins, comprehensions, files, exceptions | Checkpoint 5 |
| 6 | Modules, uv, debugging, testing | Project 03: Expense Tracker |
| 7 | Classes and objects | Project 04: Inventory Manager |
| 8 | CSV/JSON, pipelines | **Python Capstone** + readiness assessment |
| 9 | What AI is, NumPy, pandas, visualisation | Project 06: Data Analysis Report |
| 10 | Machine learning with scikit-learn | Project 07: ML Predictor |
| 11 | LLM applications (offline mock + optional API) | Project 08: AI Text Assistant |
| 12 | Final project weeks | **AI Capstone** + final assessment |

Full day-by-day plan: [COURSE-ROADMAP.md](COURSE-ROADMAP.md) (the single source of truth for the schedule).

## Folder guide

| Folder / file | What's inside |
|---------------|---------------|
| [COURSE-ROADMAP.md](COURSE-ROADMAP.md) | Schedule settings + all 60 days: topic, new concepts, objectives, prerequisites, output |
| [PROGRESS.md](PROGRESS.md) | Material status and teaching status per day; next class |
| `weeks/week-NN/day-DD-topic/` | `lesson.md` (your notes) · `demo.ipynb` (teach live) · `practice.ipynb` (students) · `solutions.ipynb` (you) |
| `weeks/week-NN/README.md` | The week at a glance, prep checklist, common difficulties |
| [projects/](projects/README.md) | Nine project briefs, starters, reference implementations, grading rubric |
| [assessments/](assessments/README.md) | Weekly checkpoints, Python readiness assessment, final AI assessment (with answer keys) |
| [concepts/](concepts/) | One-page cheatsheets for revision (Python and AI) |
| [datasets/](datasets/README.md) | Small synthetic datasets used from Week 8 on |
| [setup/](setup/environment.md) | Installation (students and instructor), what to share, API keys, troubleshooting |
| [references/source-map.md](references/source-map.md) | How your `learn-python` notes map onto this course |
| `scripts/` | `validate_notebooks.py` (run/check all notebooks), `make_datasets.py` (regenerate data) |

Compared with the originally proposed layout, two folders were added: `datasets/` (one shared copy of the data
instead of duplicates in every day folder) and `scripts/` (the validator, so you can re-check notebooks after editing).

> **Published version:** instructor-only material is not in this repository: `solutions.ipynb` and `solution_*.py`
> files, project `reference/` implementations, and assessment answer keys (`assessments/answer-keys/`). Links to
> them in lesson notes will not resolve here.

## Setup

```bash
uv sync                                                   # instructor environment
uv run python scripts/validate_notebooks.py weeks/week-01 # check a week's notebooks
```

Student setup, what to share with students, and API-key handling: [setup/environment.md](setup/environment.md).

## Key decisions and assumptions

- **Schedule:** 5 sessions/week × 75 min from Monday 2026-10-12. Lessons are numbered by day, so a different
  timetable just shifts dates. Each lesson marks optional segments for 60- or 90-minute sessions.
- **Audience:** complete beginners. Concepts are introduced in a strict order and later lessons never use
  anything not yet taught (e.g. no functions before Day 16, no `assert` before Day 29).
- **Python first, AI second:** 40 sessions of Python before any AI so students can actually write the code the AI
  weeks need. Advanced Python (decorators, generators, inheritance hierarchies, async) is out of scope.
- **No paid services required:** all LLM lessons run on an offline mock by default; a real Claude API key is optional
  (`.env.example`). No GPUs; datasets are small and synthetic.
- **Original material:** your `learn-python` notes were used only to map topics and their order; no Udemy exercises
  or solutions are reproduced.
