# Project 05: Python Capstone

**Milestone project 5 of 9 · Week 8 · Days 38–40** ([plan](../../weeks/week-08/day-38-capstone-planning/lesson.md) ·
[build](../../weeks/week-08/day-39-capstone-build/lesson.md) · [demo](../../weeks/week-08/day-40-capstone-demo/lesson.md))
· Proves you can plan and ship a complete Python application on your own.

## The problem

For seven weeks you have built programs from a brief and a starter. This time **you** decide what to build. You
will choose an application that is useful to a real person (you, a friend, a teacher, a small club), plan it, build
it, test it and present it in a 5-minute demo.

There is **no starter code**. You start from a plan ([PLAN-TEMPLATE.md](PLAN-TEMPLATE.md)) that your instructor
approves on Day 38. Everything you need has been taught in Weeks 1–8: functions, files, exceptions, modules,
pytest, classes, CSV and JSON.

## Choose your project

| Option | What it is | Suggested features (MVP first, then extras) | Data hint |
|--------|-----------|---------------------------------------------|-----------|
| **(a) Personal Budget Tracker** | Track income and spending against monthly budgets | add income/expense with date, category, amount · balance · spending per category · *extras:* monthly budget per category with a warning when it is exceeded, month-by-month summary, CSV export | transactions are a flat table → CSV; budgets → JSON |
| **(b) Student Gradebook** | A teacher records students' scores and sees results | add students · record scores per subject · student average + letter grade · class report · *extras:* weighted assessments (tests 60%, homework 40%), students below a pass mark, CSV export | students with varying subjects are nested → JSON |
| **(c) Flashcard Study App** | Study with question/answer cards | decks of cards · add/edit cards · study session in random order · count right/wrong per card · *extras:* "weakest cards" practice, statistics per deck, import cards from CSV | decks containing cards → JSON |
| **(d) Habit Tracker** | Build habits by ticking them off each day | add habits · mark a habit done today · today's checklist · completion % this week · *extras:* current streak, best streak, weekly report | habits with lists of dates → JSON |
| **(e) Library Lending System** | A small club library lends books to members | add books and members · borrow and return · who has what · *extras:* due dates and an overdue list, max 3 books per member, search by title/author | books and members (two classes) → JSON |
| **(f) Your own idea** | Anything of a similar size, **approved by your instructor** | examples: workout log, film watch-list with ratings, plant-watering schedule, tournament scoreboard, pet-care planner | your choice, justified in your plan |

Choosing (a) after Project 03? Fine, but it must go **beyond** your Expense Tracker (income, budgets, a class,
CSV or JSON). Too big for three days: anything with a graphical window, a website, internet access, a database or
several users at once. Too small: a single calculation (a calculator, a unit converter).

## Requirements

**Must** (needed for a pass, every option):
1. A **menu-driven console app** that loops until the user quits, started with `uv run python main.py`.
2. At least **3 modules** (`.py` files, `main.py` included), each with one clear job.
3. At least **5 functions** (outside classes), **each with a docstring**.
4. At least **1 class** you designed, with `__init__`, `__str__` and at least two other methods, one of which
   changes the object's state and rejects invalid values with `raise ValueError`.
5. Data **saved to and loaded from CSV or JSON**, so changes survive closing and restarting the app.
6. **Input validation and exception handling:** the app **never crashes**, whatever the user types (letters
   instead of numbers, empty input, out-of-range values, unknown names, unknown menu options), and it starts
   normally when the data file is **missing** (first run).
7. At least **5 pytest tests** that pass with `uv run pytest -q`, including at least one edge case and one error
   case (`pytest.raises`).
8. A **`README.md`**: what the app does, how to run it and its tests, a feature list, and an **example session**.
9. A **5-minute demo** on Day 40 (format below).

**Should** (expected for a good grade):
- Logic separate from input/output: only `main.py` calls `input()` and `print()` for the menu; other modules
  take values as parameters and **return** results, so they can be tested.
- A damaged data file gives a clear message instead of a crash.
- Tests for every module except `main.py`, and a save-then-load test.
- Confirmation before deleting anything; tidy, aligned output (f-string formats).
- Your `PLAN.md` kept up to date: stories ticked off, changes noted.

**Could** (if your MVP is finished and tested):
- A second class and composition (one object holding a list or dict of others).
- Search, filter or sort options; a statistics or report screen; export a report to CSV.
- Import data from a CSV file; dates with `datetime`; a backup copy before overwriting the data file.

Rules: Python and its standard library only (`csv`, `json`, `pathlib`, `random`, `datetime`…), plus `pytest`.
AI assistants may *explain* errors and concepts but must not write your project (see the
[independence rule](../README.md)). You must be able to explain every line.

## Starter files and how to run them

There is no starter. Create your own uv project (Day 27) **outside** the course folder, for example next to your
other projects:

```
uv init my-capstone
cd my-capstone
uv add pytest
```

Suggested layout (rename to fit your app):

```
my-capstone/
├── PLAN.md          ← your copy of PLAN-TEMPLATE.md, approved on Day 38
├── README.md        ← created by uv init; you fill it in
├── main.py          ← menu, input helpers, one function per menu option
├── models.py        ← your class(es)
├── storage.py       ← load/save CSV or JSON
├── reports.py       ← calculations and text reports (no input(), no print())
├── test_models.py
├── test_storage.py
├── test_reports.py
└── data.json        ← created by your app the first time it saves
```

`uv init` creates a `main.py` that prints a greeting. Replace it with a **walking skeleton**: a menu where every
option already exists but only prints `TODO`. It runs from the first minute, and you replace one `TODO` at a time.

```python
"""Habit Tracker: tick off daily habits and see your progress."""

MENU = """
=== Habit Tracker ===
1. Today's checklist
2. Mark a habit done
0. Quit"""


def main():
    """Show the menu until the user quits."""
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            print("TODO: show today's checklist")
        elif choice == "2":
            print("TODO: mark a habit done")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print(f"'{choice}' is not on the menu.")


if __name__ == "__main__":
    main()
```

Run the app with `uv run python main.py` and the tests with `uv run pytest -q`. Put test files next to your
modules (as in Projects 03 and 04).

## Build plan

Work in small steps. After **every** step the app runs and the tests pass.

| Step | When | Build | Checkpoint |
|------|------|-------|------------|
| 1 | Day 38 | Plan: fill in `PLAN.md` from the template | instructor has approved it (initials on your plan) |
| 2 | Day 38 | Walking skeleton: uv project, empty modules with docstrings, menu with `TODO`s, one trivial test | `uv run python main.py` shows the menu; `uv run pytest -q` shows `1 passed` |
| 3 | Day 39 | Your class, with tests written alongside it | `uv run pytest -q` passes with ≥ 3 tests |
| 4 | Day 39 | Storage: save + load, missing file → empty data, a save-then-load test | add something, quit, restart: it is still there |
| 5 | Day 39 + homework | The remaining MVP menu options, one at a time, with validation | every MVP story ticked in `PLAN.md`; you cannot make it crash |
| 6 | Homework before Day 40 | README with an example session; rehearse the demo with a timer | a classmate can run your app from the README alone; demo ≤ 5 minutes |

## The demo (Day 40, 5 minutes + 2 minutes of questions)

| Time | What to show |
|------|--------------|
| 0:00–0:30 | The problem and the user: "This is for … who needs to …" |
| 0:30–3:00 | Live run of your main user story. Include **one bad input** handled gracefully, then quit and restart to show the data was **saved** |
| 3:00–4:15 | Code tour: open one function and one test and explain them; say which file does what |
| 4:15–5:00 | One decision you made (e.g. CSV or JSON, why), one thing you would add next |

## Submission checklist

- [ ] `PLAN.md` approved on Day 38, updated with what changed
- [ ] `uv run python main.py` runs from a fresh terminal in your project folder
- [ ] ≥ 3 modules, ≥ 5 functions with docstrings, ≥ 1 class with `__init__`, `__str__` and 2+ methods
- [ ] Data saved and loaded with CSV or JSON; **delete the data file and start the app**: it still works
- [ ] Tried to break it: letters for numbers, empty input, out-of-range values, unknown menu option, unknown name
- [ ] `uv run pytest -q` passes with ≥ 5 tests (including an edge case and a `pytest.raises` error case)
- [ ] `README.md` with description, how to run, features, example session
- [ ] No leftover debug prints, no personal data of real people, no passwords or keys
- [ ] Demo rehearsed with a timer

Deadline: **code, tests and README by the start of Day 40.** Small fixes after the demo are allowed until the start
of Day 41 if your instructor agrees.

## Evaluation rubric (100 points)

| Criterion | Points | Full marks when… |
|-----------|--------|------------------|
| Works as specified | 40 | every MVP story in your approved plan works (≈ 25); data survives a restart (10); the menu flow is complete and clear (5) |
| Code readability and structure | 20 | ≥ 3 modules with clear jobs; logic separated from input/printing; small functions with docstrings; good names; the class models something real |
| Handles bad input / edge cases | 15 | no crash on any input; missing data file → fresh start; helpful messages; empty data (no items yet) handled |
| Testing | 10 | ≥ 5 meaningful tests that pass, including an edge case and an error case; tests check results, not just "it runs" |
| Explanation / demo | 15 | demo follows the format and fits 5 minutes; you explain one function, one test and one design decision; you answer questions about your own code; README is complete |

Project-specific checks inside those criteria:
- **Plan followed (in "Works as specified"):** the app delivers the approved MVP. Changing the plan is fine,
  *if the README or PLAN.md says what changed and why*.
- **Data format choice (in "Explanation / demo"):** you can explain why you chose CSV or JSON for your data.
- **Persistence edge cases (in "Bad input"):** first run without a data file works, and quitting never loses
  saved data.

*Should* and *Could* features earn up to 10 bonus points (total capped at 100).

## Extension ideas (after Day 40)

- Add a second class and composition, or a search/sort feature driven by `sorted(key=...)`.
- In Week 9 you will learn pandas and matplotlib: load your app's CSV/JSON data and draw a chart of it.
- In Week 12 your **AI capstone** may extend this project, e.g. flashcards or habit tips generated by a language
  model. Keep your code tidy now and it will be easy to extend then.
