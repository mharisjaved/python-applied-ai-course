# Project 05: Python Capstone (instructor notes)

Student brief: [README.md](README.md) · Plan template: [PLAN-TEMPLATE.md](PLAN-TEMPLATE.md) ·
Sessions: [Day 38](../../weeks/week-08/day-38-capstone-planning/lesson.md),
[Day 39](../../weeks/week-08/day-39-capstone-build/lesson.md), [Day 40](../../weeks/week-08/day-40-capstone-demo/lesson.md) ·
Reference: [reference/](reference/) (option b, Student Gradebook; **keep the code private**)

## Timing plan

| When | What | Notes |
|------|------|-------|
| Day 36–37 homework | Students read the brief and pick two favourite options | Ask on Day 37 who is unsure; give them the option table again |
| Day 38, 0:00–0:35 | Kickoff + planning demo (recipe box) | See the Day 38 lesson |
| Day 38, 0:35–0:65 | Students fill in `PLAN.md`; you approve plans in 2–3 minute conversations | Approve in the order students raise a hand; have the scope questions below ready |
| Day 38, 0:65–0:75 | Walking skeleton: `uv init`, files, menu with `TODO`s, one test | Every student must leave with `uv run python main.py` working |
| Day 38 homework (≈ 30 min) | Finish the skeleton; write the class's `__init__` and `__str__` | |
| Day 39 | Build session: class + tests, storage, first MVP options; peer review at mid-point | Target by the end: build-plan step 4 (data survives a restart) |
| Day 39 homework (≈ 90 min) | Remaining MVP stories, README, rehearse demo | The real finishing time. Say so explicitly |
| Day 40 | Readiness assessment + presentations | See the Day 40 lesson for the two timing options |
| By Day 41 | Small fixes allowed (if you agree); grading | Grade from the submission at the start of Day 40 plus the demo |

Realistic expectations: 3 sessions + ~2 hours of homework is enough for a 3–5 story MVP. Most students
over-plan Could features and under-plan validation and storage; steer them on Day 38.

## Approving plans (Day 38)

Read the plan with the student, using the approval checklist at the end of the template. Questions that work:

- "Tell me the one thing a user does most often in your app." (That story must be in the MVP.)
- "If you were ill on Day 39, what would you cut?" (Their answer is the Should/Could list.)
- "Show me one record of your data file." (No concrete record = no data design yet.)
- "Which method of your class refuses bad values?" (Ensures the validation Must is designed, not bolted on.)

| Plan problem | Typical example | What to do |
|--------------|-----------------|------------|
| Too big | "A school system with students, teachers, timetables, fees and logins" | Keep one noun and two verbs: "students and their fees: record a payment, show who owes money". The rest becomes Could |
| Too small | "Converts temperatures" | Add state that is saved and changed over time: "a weather log that records daily temperatures and shows weekly averages" |
| No real class | Data kept only in dicts | Ask "which *thing* has data and rules?" (the card, the habit, the book). Its rule becomes a method that raises `ValueError` |
| Wrong data format | Flashcard decks in CSV with `;`-joined lists inside a cell | Show the Day 38 demo section 3 argument; nested → JSON |
| Logins / passwords | "Users log in" | Not in scope (and storing passwords properly is beyond the course). Replace with "choose your name from a list" |
| Copy of Project 03/04 | Expense tracker with a new name | Require two of: a class, budgets, income, JSON/CSV, monthly view |

Write your initials and the date on the approved plan. Unapproved students start the skeleton anyway (it is the
same for every option) while you come back to them.

## Option-specific notes

| Option | Hard part | Suggest |
|--------|-----------|---------|
| (a) Budget | Months and dates | Store dates as text `YYYY-MM-DD`; month = `date[:7]` (Day 36 Exercise 6). Round money only for display |
| (b) Gradebook | Average of a student with no scores (`ZeroDivisionError`) | "What should the average be when there are no scores?" Return `None` and handle it in the report |
| (c) Flashcards | Testing random order | Keep "check the answer" and "update the counts" in methods that tests can call directly; only the menu uses `random` |
| (d) Habits | Streaks | Streaks are a Could. MVP: done-dates stored as `YYYY-MM-DD` strings; "done today" = `str(date.today()) in habit.done_dates` (Day 26 `datetime`) |
| (e) Library | Two cooperating classes, due dates | MVP without dates (who has which book). For due dates, ISO text compares correctly: `due < str(date.today())` |
| (f) Own idea | Scope | Use the scope questions above; insist on a concrete data record before approving |

## Common pitfalls and how to unblock without giving the answer

| Symptom | Likely cause | What to ask or suggest |
|---------|--------------|------------------------|
| `ModuleNotFoundError: No module named 'models'` | Running from another folder, or a typo in the file name | "Which folder is your terminal in? What does `ls` show?" |
| Tests cannot import the app; the menu starts when running pytest | `main()` called without the `__name__` guard | "What happens when Python *imports* `main.py`?" (Day 26) |
| Data disappears after restart | Saving only on "Quit", or saving to a path relative to another folder | "Add one item, close the terminal window instead of choosing Quit. Is it saved?" Suggest saving after each change |
| `TypeError: Object of type Card is not JSON serializable` | Dumping objects instead of dicts | "What types can JSON store? (Day 36) Which method could turn your object into a dict?" |
| Loaded numbers behave like text (`"5" + 1`) | CSV values never converted | "What type does `DictReader` give you?" |
| Crash on first run | Loading a file that does not exist yet | "What should the app show the very first time?" (Day 36 `load_json` pattern) |
| Duplicate `input()` logic everywhere | No input helpers | "You ask for a number in four places. Which day showed `ask_int`?" (Project 04 / Day 25) |
| A 60-line `main()` | Menu options written inline | Day 39 demo section 4 (refactoring). "One function per menu option" |
| Tests that only check "no crash" | `assert result` or no assert | "What exact value do you expect? Put that number in the test" |

General moves, in order: ask what *should* happen vs what *does* happen → ask for a temporary `print` of the
variables → cut the problem down (one item, one test) → point to the day/demo section → as a last resort sketch
the *shape* (comments or a function signature) on paper, never type into their file.

## AI assistants and authorship

The [independence rule](../README.md) applies. During the demo questions, every student gets at least one of:
"Walk me through this function line by line", "Why did you choose JSON here?", "Change the menu text / the limit
in this method now and run it". A student who cannot explain their own code loses the explanation points and is
asked to a 5-minute follow-up; if they still cannot explain it, treat the affected parts as not their work.

## Using the reference

- `reference/` is a complete option (b) implementation: `models.py` (`Student`, `Gradebook`), `storage.py` (JSON
  load/save, CSV export), `reports.py` (averages, grades, top students), `main.py` (menu, input helpers), 23 tests.
- **Show its `README.md` as the model README** on Day 39 (after plans are approved). Keep the code private: students
  who chose the gradebook should design their own; their plan must include at least one feature the reference lacks
  (weighted assessments, pass-mark list, several tests per subject…).
- Its tests are good examples for Day 39 questions ("what does a save-then-load test look like?"): show
  `test_storage.py` on screen if a student is stuck on testing files.

Run it (from the course root):

```
cd projects/05-python-capstone/reference
uv run pytest -q                       # 23 passed
uv run python main.py                  # interactive
printf '1\n4\nsara lopez\n5\n9\n0\n' | uv run python main.py   # read-only pipe test: list, show, report, bad option, quit
```

The app saves `gradebook.json` after every change, so a pipe test that adds or edits data changes the sample file.
Run such tests on a copy of the folder.

## Grading notes

Procedure per submission (≈ 10 minutes, plus the demo):

1. Read `PLAN.md`: which stories are MVP? What changed?
2. `uv run pytest -q`: count tests, read two of them. Do they check exact results? Is there a `pytest.raises`?
3. Run the app. Try: a letter where a number is expected, an empty answer, `-5`, an unknown name, menu option `9`.
4. Add an item, quit, restart: is it still there? Then **rename the data file** and start again: fresh start
   without a crash? (Rename it back afterwards.)
5. Check the structure Musts: 3 modules, 5 documented functions, a class with `__init__`, `__str__`, two
   methods and a `raise`.
6. Read the README: could a classmate run it from these instructions?

Partial credit for "Works as specified" (40): ≈ 25 for the MVP stories (split evenly), 10 for persistence, 5 for the
menu flow. A crash on bad input costs "bad input" points, not "works" points, unless it happens in normal use.
Missing structure Musts (fewer than 3 modules, no class) cost up to 10 points of "readability and structure". A
student with fewer than 5 tests gets 2 points per passing meaningful test in "Testing".

Use the [readiness assessment](../../assessments/final/python-readiness.md) together with the capstone grade when
deciding who needs support in Week 9: a good capstone with a weak assessment usually means the student needed a lot
of help; a weak capstone with a good assessment usually means poor time management.
