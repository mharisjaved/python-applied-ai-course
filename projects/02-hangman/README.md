# Project 02: Hangman

**Week 4 · Day 20 · Individual project · Due at the start of Day 22**

Build the classic word-guessing game as a console program, **one small function at a time**. This project proves
you can take a plan (the one we made together on Day 19) and turn it into a clean program made of functions that
each do one job.

## The problem

Your younger cousin Mei wants a word game for the family laptop. The computer secretly picks a word. Mei sees
one `_` for each letter and guesses letters one at a time. Every correct letter appears in all the places it
belongs. Every wrong letter adds a piece to the drawing. Six wrong guesses and the drawing is complete: game over.
Guess every letter first and Mei wins. Then the game offers another round.

Mei is eight: she *will* type numbers, two letters at once, capital letters, and the same letter twice. Your game
must handle all of that politely.

## What it should do

An example run (the gallows picture is printed before every guess; most turns are cut here to save space):

```
$ uv run hangman.py
Welcome to Hangman! Guess the word before the drawing is finished.

  +---+
  |   |
      |
      |
      |
=========
Word:         _ _ _ _ _ _
Guessed:
Lives left:   6
Guess a letter: e
Sorry, there is no 'e'.

  +---+
  |   |
  O   |
      |
      |
=========
Word:         _ _ _ _ _ _
Guessed:      e
Lives left:   5
Guess a letter: 7
Please type exactly one letter (a-z).
Guess a letter: o
Yes! 'o' is in the word.
   ...
Word:         p _ t h o _
Guessed:      e h o p t
Lives left:   5
Guess a letter: o
You already guessed 'o'. Try a different letter.
Guess a letter: n
Yes! 'n' is in the word.
   ...
Word:         p y t h o n
Guessed:      e h n o p t y
Lives left:   5
You win! The word was 'python'.
Play again? (y/n): n
You won 1 of 1 game(s). Thanks for playing!
```

Your messages and layout may be different. The behaviour must match.

## Requirements

**Must** (needed for a working game)

1. The secret word is chosen at random from a list of words (`random.choice`).
2. Before each guess, show the word's progress with `_` for hidden letters, e.g. `_ y _ h _ n`.
3. Guesses are validated with a re-ask loop: exactly **one letter**, **not already guessed**. Capital letters and
   extra spaces are accepted (`" A"` counts as `a`). Invalid guesses never cost a life.
4. The player has **6** wrong guesses. The game ends with a win or lose message that **reveals the word**.
5. The program is built from **at least 5 small functions, each with a docstring**, for example `choose_word`,
   `display_progress`, `is_word_guessed`, `is_valid_guess`, `get_guess`, `play_round`, `play_game`.
   Functions that calculate something **return** it; only a few functions use `input()` or `print()`.
6. After a game, ask whether to play again (`y`/`n`, re-asking on anything else).

**Should** (for a polished game)

7. Show the letters guessed so far and the number of lives left.
8. Show an ASCII gallows (the pictures are provided in the starter) **or** a simple lives bar like `[####--]`.
9. Keep score across games and show it at the end.

**Could** (extra ideas, pick any)

- Categories or difficulty levels (e.g. short words for *easy*, long words for *hard*).
- A hint that reveals one random hidden letter, at the cost of a life.
- Two-player mode: player 1 types the secret word, then the screen is scrolled away with `print("\n" * 50)`.
- Allow guessing the whole word at once.

## Starter files and how to run them

Copy `starter/hangman.py` into your own project folder (the one you use with `uv`), then run:

```
uv run hangman.py
```

The starter already contains the **function plan from Day 19** as stubs (a `def` line, a docstring and a `TODO`),
the word list, the gallows pictures, and a `run_checks()` function full of Day 19 checks.

At the bottom of the file there is a switch:

```python
CHECK_ONLY = True   # True: only run the checks. False: play the game.
```

- While `CHECK_ONLY` is `True`, running the file prints one `True`/`False` line per check. At the start all
  14 lines say `False`. That is expected.
- Fill in the functions until every check prints `True`. Then set `CHECK_ONLY = False` and play.
- Prefer notebooks? The Day 20 workbench (`weeks/week-04/day-20-project-hangman/practice.ipynb`) has the same
  functions and checks. Develop a function there, then copy it into `hangman.py`.

## Build plan

Work in this order. Don't move on until the checkpoint of the step is reached.

| Step | What to do | Checkpoint |
|------|------------|------------|
| 1 | Copy the starter, run it | 14 lines of `False`, no errors |
| 2 | Write `display_progress`, `is_word_guessed`, `is_valid_guess`, `choose_word` (one at a time, re-running after each) | every check prints `True` |
| 3 | Write `get_guess` (a `while` loop around `input()` that uses `is_valid_guess`). To try it, temporarily add `print(get_guess(["a"]))` as the last line of `run_checks()` | typing `7`, `ab` and `a` (already guessed) is refused with a helpful message; `B` is accepted as `b` |
| 4 | Write `play_round`. Tip: temporarily set `WORDS = ["cat"]` so you know the answer | you can win **and** lose one round with `CHECK_ONLY = False` |
| 5 | Write `ask_play_again` and finish `play_game` | you can play two games in a row and quit |
| 6 | *Should* features (status, gallows or lives bar, score), then tidy up | every function has a docstring; checks still all `True` |

If you add a new calculating function (for example a lives bar), add checks for it to `run_checks()`.

## Submission checklist

- [ ] `hangman.py` runs with `uv run hangman.py` and `CHECK_ONLY = False`.
- [ ] With `CHECK_ONLY = True`, every check prints `True`.
- [ ] At least 5 functions, each with a one-line docstring; no `global` keyword.
- [ ] `example_runs.txt` next to `hangman.py`, with two runs copied from your terminal: **one win and one loss**,
      including at least one invalid guess and one repeated guess.
- [ ] You can explain any function in your file and one decision you made.

## Evaluation rubric (100 points)

| Criterion | Points | What full marks looks like for Hangman |
|-----------|--------|----------------------------------------|
| Works as specified | 40 | All Must requirements work; a full game can be won and lost; play again works; no crashes |
| Code readability | 20 | Clear names, small one-job functions with docstrings, comments only where the *why* isn't obvious |
| Bad input & edge cases | 15 | Numbers, several letters, empty input, capitals and repeated letters are all handled without losing a life |
| Evidence it works | 10 | `example_runs.txt` shows a win and a loss with invalid input; all checks print `True` |
| Explanation / demo | 15 | You can explain any part of your code and why one function returns instead of prints |

**Project-specific criteria** (assessed inside the categories above):

1. **Decomposition:** at least 5 functions, each with one job; calculating functions return values; the game loop
   lives in a function, not at the top level of the file.
2. **No hidden state:** functions get what they need through parameters (reading constants like `MAX_WRONG` is
   fine); a new game starts with an empty list of guessed letters.
3. **Checks:** `run_checks()` passes and covers any new calculating function you added.

*Should* and *Could* items earn up to 10 bonus points (total capped at 100).

## Extension ideas

- Read the word list from a text file (you'll learn how on Day 23: come back and add it).
- Keep a "best streak" of consecutive wins.
- Build **Tic-Tac-Toe** for two players with the same method: plan table first, checkable functions
  (`is_winner(board, mark)`, `is_full(board)`) before the input loop.
