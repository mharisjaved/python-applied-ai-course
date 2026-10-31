# Project 01: Quiz Game

**Milestone project 1 of 9 · Week 3 · Day 15** ([lesson](../../weeks/week-03/day-15-project-quiz-game/lesson.md))
· Proves you can combine input, conditionals, loops, lists and dicts into a working program.

## The problem

Your school's study club runs a quiz night every month, and the questions are read out from paper. They want a
small program that anyone can run on a laptop: it asks multiple-choice questions, says straight away whether the
answer is right, keeps the score, and gives a result at the end. You are going to build it, with **your own
questions on a theme you choose** (a subject you study, a sport, films, geography, a hobby…).

It is a console program: a single file, `quiz_game.py`, run in the terminal with `uv run quiz_game.py`.

## What it should do

An example run (yours can look different, but it must do the same things):

```
============================================
            WELCOME TO THE QUIZ GAME
============================================
10 questions. Answer each one with a, b, c or d.

Question 1 of 10: What is the smallest prime number?
   a) 0
   b) 1
   c) 2
   d) 3
Your answer: C
Correct!

Question 2 of 10: Which planet is known as the Red Planet?
   a) Venus
   b) Mars
   c) Jupiter
   d) Mercury
Your answer: e
Please type a, b, c or d.
Your answer: a
Wrong. The correct answer was b) Mars.

...

--------------------------------------------
You scored 8/10 (80%).
Excellent! You really know your stuff.
--------------------------------------------
Play again? (y/n): n
Thanks for playing! Goodbye.
```

## Requirements

**Must** (needed for a pass):
1. At least **8 questions** stored in a **list of dicts**. Each dict has the question text, four options `a`–`d`
   and the correct letter (the starter shows the format).
2. Ask every question with `input()`, showing the question number and the four options.
3. Accept `a`, `b`, `c` or `d` in **upper or lower case**. Anything else is **not** marked wrong: the program says
   what is allowed and **asks again** (a validation loop). The program never crashes, whatever is typed.
4. Give **immediate feedback** after each answer and keep a **score**.
5. **Shuffle** the questions with `random.shuffle` so every game has a different order.
6. At the end, print the score, the **percentage**, and a **message tier**: 80% or more "Excellent", 50% or more
   "Good effort", otherwise "Keep practising" (your own wording is fine).
7. Ask **"Play again? (y/n)"**. `y` starts a new game with the score back at 0; `n` ends the program politely.

**Should** (expected for a good grade):
- When an answer is wrong, show the **correct letter and its text**.
- Validate the play-again answer too (accept `Y`/`N`, ask again for anything else).
- A clear welcome message with instructions, and consistent, tidy output (blank lines, aligned options).
- Questions on **your own theme** (replace or extend the starter's general-knowledge bank).

**Could** (pick one or two if you finish early):
- **Best score** of the session, shown after each game.
- **Lives:** the game ends early after 3 wrong answers.
- **Streak bonus:** an extra point for every 3 correct answers in a row.
- **Categories:** each question has a `"category"` key, and the player chooses a category at the start.
- **Choose the length:** ask how many questions to play (validated number, at most the size of the bank).

Rules: use only what we have learned so far (Weeks 1–3). **No functions (`def`) yet**: they start on Day 16, and
next week you will see how they would tidy up this program.

## Starter files and how to run them

```
projects/01-quiz-game/
├── README.md            ← this brief
└── starter/
    └── quiz_game.py     ← a question bank + TODO comments. It already runs.
```

1. Copy `starter/quiz_game.py` into your own course project folder (the one you created on Day 01).
2. In the VS Code terminal, from that folder, run: `uv run quiz_game.py`
3. You should see a welcome line and one example question. Now open the file and read the TODOs.

How to read one question from the bank (these lines are in the starter):

```python
first = questions[0]           # the first dict in the list
first["question"]              # 'Which planet is known as the Red Planet?'
first["options"]["b"]          # 'Mars'  (a dict inside the dict)
first["answer"]                # 'b'
```

Stop a running program with **Ctrl+C**.

## Build plan

Work in small steps and **run the program after every step**. Each step ends with a checkpoint.

| Step | Build | Checkpoint |
|------|-------|------------|
| 1 | Plan: write the steps of the program as comments in your file (Day 15 lesson) | your plan has 6–10 comment lines in the right order |
| 2 | Loop over the questions and print each one with its options (TODO 1) | all questions appear, numbered, with options a–d |
| 3 | Ask for an answer, compare with the correct letter, print feedback, keep a score (TODO 2, 4) | you can play a whole game and the score is right |
| 4 | Validation loop for a/b/c/d, case-insensitive (TODO 3) | `x`, an empty answer and `maybe` ask again; `B` and ` c ` are accepted |
| 5 | Shuffle + final score, percentage, message (TODO 5) | two runs give different orders; you have seen all three messages |
| 6 | Play-again loop (TODO 6), your own questions (TODO 7), then Should/Could features | a second game starts at score 0; `n` ends the program |

**Testing tip:** play once answering everything correctly (100%), once everything wrong (0%) and once getting
exactly half right (50%). Do the messages match the tiers?

## Submission checklist

- [ ] `quiz_game.py` runs with `uv run quiz_game.py` from start to finish without an error.
- [ ] At least 8 questions of your own theme, stored as a list of dicts.
- [ ] Every Must requirement works (tick them off one by one above).
- [ ] Comments explain the main parts (question bank, game loop, validation, result, play again).
- [ ] Clear variable names (`score`, `choice`, `question`, not `x`, `a2`, `thing`).
- [ ] **Evidence:** copy the terminal output of **two example runs** into a file `example_runs.txt`: one with at
      least one invalid answer and a wrong answer, and one where you play again.
- [ ] Be ready to explain any line of your code in 2 minutes.

Deadline: **before the start of Day 17**, unless your instructor says otherwise.

## Evaluation rubric (100 points)

| Criterion | Points | Full marks when… |
|-----------|--------|------------------|
| Works as specified | 40 | all 7 Must requirements work (about 5 points each); Should features add the last few points |
| Code readability | 20 | clear names, comments for each part, consistent indentation, no unused leftover code |
| Handles bad input / edge cases | 15 | any text at any prompt is handled; invalid answers never cost a point; play-again input is validated |
| Shows example runs that prove it works | 10 | `example_runs.txt` shows both runs described in the checklist |
| Explanation / demo | 15 | you can explain how the validation loop and the play-again loop work, and change a small thing live |

Project-specific checks inside those criteria:
- **Data structure (in "Works as specified"):** the questions are a list of dicts and the game loop works for any
  number of questions (no `10` typed into the code; use `len(questions)`).
- **Fair scoring (in "Handles bad input"):** the score resets for every new game, and the percentage is computed
  from the number of questions asked.
- **Your own content (in "Works as specified"):** at least 8 questions on your theme, with exactly one correct option
  each.

## Extension ideas

- Shuffle the **options** too (hint: shuffle a list of the option texts and rebuild the letters).
- A two-player mode: players take turns, and the program announces the winner.
- Difficulty levels: easy questions first, then harder ones worth 2 points.
- After the game, list the questions the player got wrong so they can revise them.
- Next week, once you know functions, refactor your quiz into small functions. It is a great before/after
  example for your portfolio.
