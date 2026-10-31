# Capstone plan: *app name*

Copy this file into your project folder as `PLAN.md` and replace every *italic* hint. Keep answers short: a plan
is a tool for building, not an essay. Your instructor approves it on Day 38; keep it up to date afterwards.

**Student:** *name* · **Option:** *(a)–(f)* · **Date:** *YYYY-MM-DD*
**Approved:** ☐ *(instructor initials and date)*

## 1. Problem statement

*2–3 sentences: who has which problem today, and how your app will help.*
*Example: "Mei's study group keeps vocabulary on paper and never knows which words they still get wrong. The app
stores flashcards, quizzes them in random order and shows which cards they miss most."*

## 2. Users

*Who will use it, how often, and what they already know (can they be trusted to type a date correctly?).*

## 3. User stories

One story = one thing a user can do, written as **As a … I want … so that …**. Write 5–8. Mark each as **Must**
(the app is useless without it), **Should** or **Could**.

| # | User story | Priority | Done |
|---|-----------|----------|------|
| 1 | As a *…*, I want to *…* so that *…* | Must | ☐ |
| 2 | | | ☐ |
| 3 | | | ☐ |
| 4 | | | ☐ |
| 5 | | | ☐ |
| 6 | | | ☐ |

## 4. MVP (minimum viable product)

**MVP** = the smallest version that is already useful. Test: "If I could only work on this for one day, what must
it do?" Usually 3–5 Must stories, **including saving and loading**.

- MVP stories: *#…, #…, #…*
- Nice-to-have (only after the MVP works and is tested): *#…, #…*

## 5. Data

- What is stored: *e.g. each card has a front, a back, times right, times wrong*
- Format: **CSV / JSON** (circle one). Why: *one sentence (flat table → CSV; nested or settings → JSON)*
- File name: *e.g. `cards.json`*
- One example record exactly as it will look in the file:

```
*paste one example record here*
```

- If the file is **missing** (first run): *e.g. start with an empty deck*
- If the file is **damaged**: *e.g. show a warning and start empty*

## 6. Design

**Modules** (at least 3):

| File | Its one job | Contains |
|------|-------------|----------|
| `main.py` | menu and user input | `main()`, `ask_…()`, one function per menu option |
| `models.py` | *…* | class *…* |
| `storage.py` | *…* | `load_…()`, `save_…()` |
| *…* | | |

**Class(es)** (at least 1):

| Class | Attributes (state) | Methods (behaviour) | What it must refuse (`raise ValueError`) |
|-------|-------------------|---------------------|------------------------------------------|
| *…* | *…* | `__init__`, `__str__`, *…* | *…* |

**Functions** (at least 5 outside classes), each with the one-line docstring you will write:

| Function | Module | Docstring |
|----------|--------|-----------|
| `load_…(path)` | storage | *"Return … from the file at path, or … if it does not exist."* |
| | | |
| | | |
| | | |
| | | |

**Menu sketch:**

```
=== app name ===
1. …
2. …
0. Quit
```

## 7. Test ideas

At least 5 tests. For each important function or method: a normal case, an edge case and an error case.

| Function / method | Normal case | Edge case | Error case (`pytest.raises`) |
|-------------------|-------------|-----------|------------------------------|
| *…* | *…* | *e.g. empty list, 0, exactly the limit* | *e.g. negative amount → ValueError* |
| | | | |
| | | | |

## 8. Risks

*What might go wrong, and your plan B.*

| Risk | Plan B |
|------|--------|
| *e.g. dates are tricky* | *store them as text `YYYY-MM-DD`; text comparison still sorts them correctly* |
| *e.g. the Could features take too long* | *drop them; the MVP is what is graded* |

## 9. Schedule

| When | Task | Estimate | Done |
|------|------|----------|------|
| Day 38 | Plan approved; uv project; walking skeleton runs; 1 test | 75 min | ☐ |
| Day 39 | Class + tests | *…* | ☐ |
| Day 39 | Storage (save/load, missing file) + save-then-load test | *…* | ☐ |
| Day 39 | First MVP menu options with validation | *…* | ☐ |
| Homework | Remaining MVP stories; try to break it; more tests | *…* | ☐ |
| Homework | README + example session; rehearse demo (timer!) | *…* | ☐ |
| Day 40 | 5-minute demo | 5 min | ☐ |

## Approval checklist (instructor)

- [ ] The problem and user are clear and real
- [ ] The MVP is buildable in about 4–5 hours by this student (cut it if not)
- [ ] All Musts are covered: menu, 3 modules, 5 functions, a class with validation, CSV/JSON, validation and
      exceptions, 5 tests, README
- [ ] The data format fits the data, with a sensible missing-file behaviour
- [ ] Not a copy of an earlier project (Project 03/04 ideas must clearly go further)
