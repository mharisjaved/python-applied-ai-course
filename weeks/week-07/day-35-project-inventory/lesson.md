# Day 35: Project 04, Inventory Manager

**Week 7 · Session 35 of 60 · Planned 75 min** · Previous: [Day 34](../day-34-composition/lesson.md) · Next: [Day 36](../../week-08/day-36-csv-json/lesson.md)

## Objectives

By the end of this session students can:

1. Turn a written brief into a class design (`Product`, `Inventory`) and explain which class owns which job.
2. Work through a starter's TODOs with a **test-first loop**: run the tests, read the first failure, write the code,
   run again.
3. Implement methods that validate input with `raise ValueError` and a menu that turns those errors into friendly
   messages with `try/except`.
4. Show evidence that their program works: passing pytest tests and a short example run.
5. Complete Checkpoint 7 on this week's OOP concepts.

**Prior knowledge:** classes, methods, validation, `__str__` (Days 32–33), composition and testing classes (Day 34),
multi-file programs and `uv run pytest` (Days 26–30, Project 03), `try/except` input loops (Day 25).

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (warm-up exercises for students who get stuck or finish
early, and homework) · `solutions.ipynb` (you only) · project: [projects/04-inventory-manager](../../../projects/04-inventory-manager/README.md)
(brief), [INSTRUCTOR.md](../../../projects/04-inventory-manager/INSTRUCTOR.md) · checkpoint:
[week-07-checkpoint.md](../../../assessments/weekly/week-07-checkpoint.md)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:20 | Checkpoint 7 (paper or notebook, individual) | core |
| 0:20–0:28 | Brief walkthrough and design on the board (demo 1–2) | core |
| 0:28–0:36 | Test-first workflow and menu pattern (demo 3–6) | core |
| 0:36–0:70 | Build time: Must steps 1–3 of the build plan | core |
| 0:70–0:75 | Stand-up: "what works, what is next", homework | core |
| +15 min | More build time, or practice.ipynb Exercises 2 and 5 for students who finished the Must steps | optional (90-min session) |

**For 60 min:** move Checkpoint 7 to the first 20 minutes of Day 36 and keep everything else.

Project 04 needs about **3–4 hours** in total: this session plus homework. Submission is due at the start of
Day 37 (see the brief).

## 1. Checkpoint 7 (20 min)

Hand out [week-07-checkpoint.md](../../../assessments/weekly/week-07-checkpoint.md) **without** the answer key
(everything below the `---` line). Closed book, no laptops, 18 minutes plus 2 to collect. Mark it after class with
the key; return it on Day 36 and go over the two most-missed questions in 5 minutes.

## 2. Brief and design (8 min)

Open the [project brief](../../../projects/04-inventory-manager/README.md) on the projector and read the story and
the example run together. Then do the noun/verb exercise from Day 34 **with** the class (demo section 1):

| From the brief | Becomes |
|----------------|---------|
| product, name, price, quantity | class `Product` with three attributes |
| restock, sell, value of the stock | `Product` methods |
| the shop's stock, find by name, low-stock report, total value | class `Inventory` (it **has** many products) |
| menu, asking the user, printing | `main.py` only: classes never call `input()` |
| saving to a file (Should) | `storage.py` only |

Key design messages:
- `Product` checks its own rules (no negative stock, no selling more than you have).
- `Inventory` stores products in a **dict keyed by lowercase name**, so "pen", "Pen" and " PEN " are the same
  product (demo section 4).
- `main.py` is the only file that talks to the user. That's why the classes can be tested without typing anything.

## 3. Workflow demo (8 min)

Show the starter folder structure (demo section 2), then demonstrate **the loop** in the notebook with the part the
starter already gives away (`restock`), so nothing is spoiled (demo section 3):

1. write (or read) a test,
2. run it and watch it fail (red),
3. write the smallest code that makes it pass,
4. run again (green), then the next TODO.

In the terminal, show once from the starter folder:

```
cd projects/04-inventory-manager/starter
uv run pytest -q          # 3 passed, 7 failed at the start
uv run main.py            # the menu runs; most options say "not written yet"
```

Then quickly show demo sections 4–6: lowercase dict keys with `.get()`, sorting objects with a `key=` function, and
the menu's `try/except ValueError as error` turning a method's error into `Sorry: ...`.

## 4. Build time (34 min)

Students follow the build plan in the brief. Expected progress by the end of class:
- **everyone:** `Product` TODOs 1–5 done, Product tests green;
- **most:** `Inventory` TODOs 6–9 done;
- **fast:** all tests green, menu options 2–6 written, starting their own tests.

Circulate with these questions instead of answers (more in [INSTRUCTOR.md](../../../projects/04-inventory-manager/INSTRUCTOR.md)):
- "Which test is failing first? Read me its last line."
- "Does this method change state, or return an answer, or both?"
- "Where is the check? Is it *before* the change?"
- "Is this `print` inside a class? Should it be?"

Students who are stuck on a concept (not on the project) use `practice.ipynb`. Each exercise practises one project
technique on different data, so it unblocks without giving the project code away:

| Exercise | Skill | Level | Unblocks |
|----------|-------|-------|----------|
| 1 Lowercase keys | dict lookups with `.lower()` and `.get()` | recall/predict | TODO 6–7 |
| 2 Parse lines safely | `split`, `float`/`int`, `try/except` per line | application | Should: `storage.py` |
| 3 Which plants need water? | filter objects, `sorted(key=)` with a named function | application | TODO 10 |
| 4 A report string | aligned f-string columns, `"\n".join`, return not print | application | TODO 12 |
| 5 An `Order` class (challenge) | composition with validation and merging lines | challenge | Could: `Order` |

Give students only the `starter/` folder; share `reference/` after the submission deadline (it makes a good
code-review exercise on Day 37).

## 5. Common mistakes today

| Mistake | Error / symptom | How to explain it |
|---------|-----------------|-------------------|
| running commands from the wrong folder | `uv run main.py` → `Failed to spawn: main.py`; pytest one level up → `import file mismatch` (starter and reference both have `test_inventory.py`) | `cd` into your own project folder first, then run |
| `sell` changes `quantity` before checking | test "changes nothing" fails | check first, change second |
| `report()` prints instead of returning | menu prints the table and then `None` | the menu prints; the class returns text |
| `find` without `.strip().lower()` | test with `"  GLUE STICK "` fails | keys are stored lowercase, so look them up lowercase |
| `low_stock` returns names instead of products | `AttributeError: 'str' object has no attribute 'name'` in the test | return the `Product` objects; the caller decides what to show |
| `except:` with no exception type in the menu | real bugs are hidden | catch `ValueError` only |

## 6. Stand-up and homework (5 min)

Three or four students say in one sentence what works and what is next. Recap the week in three sentences
(students supply them): a class is a template and `self` is the object being worked on; methods check first and
change second; composition means one object holds others and lets them do their own jobs.

**Exit ticket** (sticky note, collected at the door): "My test count is __ passed / __ failed. The next TODO I will
do is __. One thing I am unsure about is __." Use the notes to plan the first 5 minutes of Day 36: if many students
name the same TODO, explain its *idea* on the board.

Then:

**Homework (2–3 hours across Days 35–36):** finish the Must requirements (all starter tests green, menu complete,
at least 4 tests of your own), then the Should requirements. Submit at the start of Day 37 using the checklist in the
brief. The practice notebook's Exercises 2 and 5 prepare the Should and Could parts.

## Next class

Day 36 introduces `csv` and `json`. The inventory text file students save today (`name,price,quantity` per line)
is a CSV file in disguise. Tomorrow they will see how the `csv` module does the splitting for them, and a "Could"
extension is to export the inventory with `csv.DictWriter`.

## Instructor notes

- Collect the checkpoint before the project starts, otherwise students keep working on it.
- Do not live-code `sell` or the `Inventory` methods for the class. If more than a third of the room is stuck on the
  same TODO after 10 minutes, do a 3-minute board explanation of the *idea* (e.g. "check, then change, then
  return") without writing the code.
- Students who copy the reference from a classmate are easy to spot in the explanation part of the rubric: ask them
  to explain why `find` returns `None` instead of raising.
- Strong students: point them at the Could list (categories, an `Order` class) and at writing more error-case tests.
- Weak students: it is fine to submit only the Must part. Make sure they get `Product` fully working and tested; that
  alone covers most of the week's learning objectives.
