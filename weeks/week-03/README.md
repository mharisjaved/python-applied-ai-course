# Week 3: Control Flow

Students learn to make Python **repeat** work: `for` loops over ranges and collections, `while` loops that run
until something changes, and `break`/`continue` to steer them. By Friday they combine everything from Weeks 1–3
into their first independent program, the **Quiz Game** (Project 01).

| Day | Topic | Lesson | Demo | Practice | Solutions |
|-----|-------|--------|------|----------|-----------|
| 11 | `for` loops and `range`, accumulators | [lesson](day-11-for-loops/lesson.md) | [demo](day-11-for-loops/demo.ipynb) | [practice](day-11-for-loops/practice.ipynb) | [solutions](day-11-for-loops/solutions.ipynb) |
| 12 | Iterating strings, lists and dicts; `enumerate`; counting | [lesson](day-12-iterating-collections/lesson.md) | [demo](day-12-iterating-collections/demo.ipynb) | [practice](day-12-iterating-collections/practice.ipynb) | [solutions](day-12-iterating-collections/solutions.ipynb) |
| 13 | `while` loops, sentinels, validation with `.isdigit()` | [lesson](day-13-while-loops/lesson.md) | [demo](day-13-while-loops/demo.ipynb) | [practice](day-13-while-loops/practice.ipynb) | [solutions](day-13-while-loops/solutions.ipynb) |
| 14 | `break`, `continue`, nested loops, `random` | [lesson](day-14-break-continue-nested/lesson.md) | [demo](day-14-break-continue-nested/demo.ipynb) | [practice](day-14-break-continue-nested/practice.ipynb) | [solutions](day-14-break-continue-nested/solutions.ipynb) |
| 15 | 🏗 Project 01: Quiz Game + Checkpoint 3 | [lesson](day-15-project-quiz-game/lesson.md) | [demo](day-15-project-quiz-game/demo.ipynb) | [practice](day-15-project-quiz-game/practice.ipynb) | [solutions](day-15-project-quiz-game/solutions.ipynb) |

**Assessment and project:**
[Checkpoint 3](../../assessments/weekly/week-03-checkpoint.md) (start of Day 15, 15 min) ·
[Project 01 brief](../../projects/01-quiz-game/README.md) ·
[Project 01 instructor notes](../../projects/01-quiz-game/INSTRUCTOR.md) (due before Day 17)

## Prepare before the week

- [ ] Run all five demo notebooks once (Restart → Run All). Days 13–15 call `input()`: have answers ready.
- [ ] Practise **Interrupt** and **Restart** in VS Code with a silent infinite loop (Day 13 section 3) so you can
      show it calmly.
- [ ] Run `uv run quiz_game.py` in `projects/01-quiz-game/starter/` and read the reference solution.
- [ ] Print Checkpoint 3 for Day 15 (or prepare a blank notebook per student).
- [ ] Assign the Project 01 brief as reading for Day 14 homework.

## Common difficulties this week

| Difficulty | How to respond |
|------------|----------------|
| Accumulator reset inside the loop, or result printed inside the loop | Trace table on the board with *before / inside / after* columns; compare with a shop till |
| `range` stop value (`range(1, 10)` for 1–10) and `randint` including both ends | Say the rule every time it appears: "range stops *before* stop; randint includes both" |
| Infinite `while` loops and notebooks stuck on `input()` | Normalise it: show Interrupt/Restart once to everyone; ask "what changes the condition?" |
| `for name, value in d:` without `.items()`, and `KeyError` when counting | Print one item of the loop to *see* its shape before unpacking it |
| Confusing `break` and `continue` | Playlist analogy: skip this song vs stop the playlist; Day 14 practice Exercise 1 |
