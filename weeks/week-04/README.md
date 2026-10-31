# Week 4: Functions

Students stop writing programs as one long script. They learn to package code into named functions, pass
information in with parameters and get results back with `return`, understand where variables live, and plan a
program as a set of small, checked functions before writing it. The week ends with Project 02 (Hangman), built
function by function from a plan made together on Day 19.

| Day | Topic | Lesson | Demo | Practice | Solutions |
|-----|-------|--------|------|----------|-----------|
| 16 | Why functions; define & call | [lesson](day-16-functions-intro/lesson.md) | [demo](day-16-functions-intro/demo.ipynb) | [practice](day-16-functions-intro/practice.ipynb) | [solutions](day-16-functions-intro/solutions.ipynb) |
| 17 | Parameters, arguments & return values | [lesson](day-17-parameters-return/lesson.md) | [demo](day-17-parameters-return/demo.ipynb) | [practice](day-17-parameters-return/practice.ipynb) | [solutions](day-17-parameters-return/solutions.ipynb) |
| 18 | Scope, defaults & composition | [lesson](day-18-scope-defaults/lesson.md) | [demo](day-18-scope-defaults/demo.ipynb) | [practice](day-18-scope-defaults/practice.ipynb) | [solutions](day-18-scope-defaults/solutions.ipynb) |
| 19 | Problem decomposition + Hangman plan | [lesson](day-19-decomposition/lesson.md) | [demo](day-19-decomposition/demo.ipynb) | [practice](day-19-decomposition/practice.ipynb) | [solutions](day-19-decomposition/solutions.ipynb) |
| 20 | 🏗 Project 02: Hangman + Checkpoint 4 | [lesson](day-20-project-hangman/lesson.md) | [demo](day-20-project-hangman/demo.ipynb) | [workbench](day-20-project-hangman/practice.ipynb) | [solutions](day-20-project-hangman/solutions.ipynb) |

**Assessment:** [Checkpoint 4](../../assessments/weekly/week-04-checkpoint.md) (first 18 min of Day 20) ·
**Project:** [02 Hangman](../../projects/02-hangman/README.md) (brief) ·
[instructor guide](../../projects/02-hangman/INSTRUCTOR.md) · due at the start of Day 22.

## Prepare before the week

- [ ] Run every Week 4 notebook once with *Restart → Run All* (no network or packages needed).
- [ ] Play the reference game: `cd projects/02-hangman/reference && uv run hangman.py`; then run the starter and
      confirm it prints 14 × `False`.
- [ ] Read the Project 02 brief and instructor guide; decide how students get the starter (shared drive, repo, chat).
- [ ] Print or prepare a form for Checkpoint 4 (questions only, everything above the `---` line).
- [ ] Have each student's Quiz Game (Project 01) at hand: Day 16 and its homework use it as the "before" picture.
- [ ] Plan board space on Day 18 for the two "whiteboards" (global and local scope) and on Day 19 for the
      Hangman function table.

## Common difficulties and how to respond

1. **"Defining runs the function."** Students expect output from a `def` cell. Keep repeating the recipe-card
   picture: writing the card is not cooking. The Day 16 exit ticket diagnoses it.
2. **Print vs return.** The biggest one. Every time `None` appears in output, ask "where is the `return`?" Use the
   waiter-vs-receipt analogy (Day 17) and the "can a check use it?" test (Day 19).
3. **Expecting a function to change a global.** Draw the two whiteboards (Day 18). Insist on "pass in, return
   out, store the result" and ban `global`, even when students find it online.
4. **Wanting to code before planning.** On Day 19 and 20, ask for the stub and the checks first. A student who
   can't write the check doesn't yet know what the function should do.
5. **Testing only by playing the game.** Slow and unreliable. Point back to the build order: checkable functions
   first, then input, then glue (Day 20 demo).
