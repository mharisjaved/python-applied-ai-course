# Project 01: Quiz Game (instructor notes)

Student brief: [README.md](README.md) · Session plan: [Day 15 lesson](../../weeks/week-03/day-15-project-quiz-game/lesson.md) ·
Reference solution: [reference/quiz_game.py](reference/quiz_game.py) (do not share before the deadline)

## Timing plan

| When | What | Notes |
|------|------|-------|
| Day 14 homework | Students read the brief, write 3 questions about it and pick a theme | Collect questions at the start of the kickoff |
| Day 15, 0:00–0:15 | Checkpoint 3 | Scan the loop questions during build time to see who needs help first |
| Day 15, 0:15–0:38 | Kickoff: how to work on a project, brief walk-through, planning demo | See the Day 15 lesson |
| Day 15, 0:38–0:68 | Build time (30 min) | Target by the end of class: build-plan step 3 (a playable game with a score) |
| Day 15, 0:68–0:75 | Mini show-and-tell | 2–3 students, 2 minutes each |
| Homework (≈ 60 min) | Steps 4–6, own questions, `example_runs.txt` | Due before Day 17 |
| Day 16, first 5 min | "Look at your quiz: which lines are repeated?" | Motivates functions; no grading yet |
| Day 17 | Submissions due; demo/explanation slots during practice time | 2 minutes per student, see grading notes |

Realistic expectations: most students finish Musts 1–4 in class and the rest at home. A student who has a
working step 3 at the end of Day 15 is on track.

## Before the session

- Run `uv run quiz_game.py` in `starter/` on the classroom machine so you know what students will see.
- Have the reference open in a separate window (not projected).
- Write the build-plan table from the README on the board; students tick steps off as they go.

## Common pitfalls and how to unblock without giving the answer

| Symptom | Likely cause | What to ask or suggest |
|---------|--------------|------------------------|
| Every answer is "Wrong" even when correct | Comparing `"B"` with `"b"`, or `" b"` with `"b"` | "Print the answer between brackets, `print("[" + choice + "]")`. What do you see?" Then: "Which string methods from Day 04 help?" |
| Score is 0 or 1 at the end | `score = 0` inside the question loop | "Trace two questions on paper. When is `score` set back to 0?" (Day 11 accumulator) |
| Invalid input is counted as a wrong answer | The `if` check runs before/without the validation loop | "What should happen to `x` *before* we decide right or wrong?" |
| Program hangs after an invalid answer | The validation loop does not ask again inside its body | "Inside your `while`, what changes the variable in the condition?" (Day 13) |
| `TypeError: 'NoneType' object is not subscriptable` | `questions = random.shuffle(questions)` | "What does `shuffle` give back? Look at Day 14 demo section 7." |
| `KeyError: 'Question'` or `'A'` | Key spelled differently from the bank, or using the typed letter without `.lower()` | "Print `q.keys()`. Which spelling does the dict use?" |
| Percentage is always 0 | `score // len(questions) * 100` | "What does `//` do with 7 and 10?" (Day 03) |
| Second game continues the old score, or ends at once | Score not reset inside the outer loop; play-again variable never reset | "Which variables belong to *one game*? Where does one game start in your code?" |
| Options printed as `{'a': 'Venus', …}` | Printing the whole options dict | "How did we loop over a dict's pairs on Day 12?" |
| Question numbering starts at 0 | `enumerate` without `start=1` | "Who reads these numbers, Python or a person?" |

General unblocking moves (in this order):
1. Ask the student to **say what the program should do** at this point, then **what it actually does**.
2. Ask them to add a temporary `print` of the variables involved (e.g. `print("DEBUG", choice, q["answer"])`).
3. Ask them to **cut the problem down**: test with 2 questions by temporarily slicing `questions[:2]` (Day 06).
4. Point to the day and demo section that covers the pattern (Days 11–14). Do not type in their file.

If a student is completely stuck, give them a **skeleton of comments** (the plan), not code. The planning exercise
in Day 15 practice (Exercise 4) is the model.

## Fast and slow students

- **Fast:** Could features. Lives and streak bonus are the most instructive (extra counters + `break`). Categories
  require a new key and a filtered list (Day 12 pattern). Shuffling options is the hardest extension.
- **Slow:** accept a version without play-again in class; it is the last Must. Make sure validation (Must 3) works
  before they add anything else, because it is the core skill of the week.

## Grading notes

Use the rubric in the README. Quick procedure per submission (≈ 5 minutes):

1. Read the question bank: list of dicts? ≥ 8 questions? own theme? exactly one correct letter each?
2. Run it twice by hand: once with invalid inputs (`x`, empty, `B`, ` c `), once choosing play again.
3. Run it non-interactively by piping answers, so it plays to the end without you typing. From the student's
   folder (10-question bank shown; adjust the number of answers to their bank size):

   ```
   printf 'a\nB\nx\n\n c \nd\na\nb\nc\nd\na\nb\nmaybe\ny\na\na\na\na\na\na\na\na\na\na\nYES\nn\n' | uv run quiz_game.py
   ```

   It must finish without an error. If it ends with `EOFError`, it asked for more answers than you piped: check
   whether invalid answers wrongly consumed a question, or whether play-again is not validated.
4. Read `example_runs.txt` (10 points).
5. During the 2-minute explanation, ask one of: "Show me where an invalid answer is handled", "Where is the score
   reset for a new game?", "Change the pass mark for 'Excellent' to 90%."

Partial credit guide for "Works as specified" (40): roughly 5 points per Must requirement; up to 5 more for Should
features. A program that crashes on some input loses the "bad input" points, not the "works" points, unless the
crash happens in normal play.

Things **not** to penalise: functions (`def`) used by a student who knew them before (ask them to explain; do not
award extra points either); a different but sensible message wording; options stored as separate keys
(`"a": …, "b": …`) instead of a nested dict.

Red flags: code using concepts far beyond the course with no ability to explain it (discuss with the student before
grading); questions copied from the starter with no own theme (lose the "own content" check).

## How the reference was tested

The reference contains no functions (they start on Day 16), so there is no `main()` or pytest file. It was tested
by hand and by piping input:

```
cd projects/01-quiz-game/reference
printf 'a\nB\nx\n\n c \nd\na\nb\nc\nd\na\nb\nmaybe\ny\na\na\na\na\na\na\na\na\na\na\nYES\nn\n' | uv run python quiz_game.py
```

This plays two full games (with invalid answers `x`, an empty line, `maybe` and `YES`), validates both prompts and
ends with `Thanks for playing! Goodbye.` and exit code 0. To check the scores and the three message tiers, the
shuffle was switched off for a test run so the answer order is known:

```
printf 'b\nc\nd\na\nb\nc\nb\nd\nc\na\nn\n' | uv run python -c "import random; random.shuffle = lambda seq: None; exec(open('quiz_game.py').read())"
```

This gives `You scored 10/10 (100%)` and `Excellent!`. Answering 5 and 8 correctly gave 50% ("Good effort") and
80% ("Excellent"), and all wrong gave 0% ("Keep practising"). Both `starter/quiz_game.py` and
`reference/quiz_game.py` pass `uv run python -m py_compile`, and the starter runs to the end without input.
(The `random.shuffle = …` trick is an instructor testing shortcut; do not show it to students.)
