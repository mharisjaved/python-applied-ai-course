# Week 7: Introductory OOP

**Goal:** students learn to model real things as objects: first by feeling the pain of dicts plus loose functions,
then by writing their own classes with attributes, methods that keep their state valid, and `__str__`. The week ends
with two cooperating classes, tests for them, and Project 04, a class-based Inventory Manager.

| Day | Topic | Lesson | Demo | Practice | Solutions |
|-----|-------|--------|------|----------|-----------|
| 31 | Objects, state and behaviour | [lesson](day-31-objects/lesson.md) | [demo](day-31-objects/demo.ipynb) | [practice](day-31-objects/practice.ipynb) | [solutions](day-31-objects/solutions.ipynb) |
| 32 | Classes, instances and constructors | [lesson](day-32-classes/lesson.md) | [demo](day-32-classes/demo.ipynb) | [practice](day-32-classes/practice.ipynb) | [solutions](day-32-classes/solutions.ipynb) |
| 33 | Attributes and methods | [lesson](day-33-methods/lesson.md) | [demo](day-33-methods/demo.ipynb) | [practice](day-33-methods/practice.ipynb) | [solutions](day-33-methods/solutions.ipynb) |
| 34 | Class design and composition | [lesson](day-34-composition/lesson.md) | [demo](day-34-composition/demo.ipynb) | [practice](day-34-composition/practice.ipynb) | [solutions](day-34-composition/solutions.ipynb) |
| 35 | 🏗 Project 04: Inventory Manager | [lesson](day-35-project-inventory/lesson.md) | [demo](day-35-project-inventory/demo.ipynb) | [practice](day-35-project-inventory/practice.ipynb) | [solutions](day-35-project-inventory/solutions.ipynb) |

**Assessment:** [Checkpoint 7](../../assessments/weekly/week-07-checkpoint.md) (start of Day 35, or Day 36 in a
60-minute timetable) · **Project:** [04 Inventory Manager](../../projects/04-inventory-manager/README.md)
([instructor notes](../../projects/04-inventory-manager/INSTRUCTOR.md)), due at the start of Day 37.

## Prepare before the week

- [ ] Mark Project 03 (Expense Tracker) so students get feedback before Day 31: Day 31 starts from their dicts.
- [ ] Run `uv run pytest -q` in `projects/04-inventory-manager/starter` (expect 3 passed, 7 failed) and in
      `reference` (expect 30 passed), so you know what students will see.
- [ ] Try the reference menu yourself (`uv run main.py` in a copy of `reference/`), including bad input.
- [ ] Print Checkpoint 7 without the answer key (everything above the `---` line).
- [ ] Decide whether the 90-minute options (inheritance preview on Day 34, extra build time on Day 35) fit your timetable.

## Common difficulties this week

| Difficulty | How to respond |
|------------|----------------|
| "What *is* `self`?" | Write `asha.describe()` and under it `Student.describe(asha)`; draw an arrow from `asha` to `self`. Repeat every time. |
| Passing `self` in the call, or forgetting it in the definition | Read the `TypeError` together: "takes 1 positional argument but 2 were given" counts the object before the dot. |
| `self.x` vs `x` inside methods | Ask "will this value still exist when the method has finished?" Only attributes (`self.`) survive. |
| Printing inside classes instead of returning | Repeat the Day 17 rule: classes return text, `main.py`/the caller prints. `__str__` must return. |
| Surprise that changing an object "through" a list changes it everywhere | Draw boxes and arrows (Day 07 name tags): lists hold the same objects, not copies. |
