# Project 02: Hangman, instructor guide (keep private)

**Files:** `README.md` (student brief, share it) · `starter/hangman.py` (share it) ·
`reference/hangman.py` (complete solution, **keep private**) · Day 20 lesson:
[weeks/week-04/day-20-project-hangman/lesson.md](../../weeks/week-04/day-20-project-hangman/lesson.md)

## Session plan

| When | What | Notes |
|------|------|-------|
| Day 19, last 10 min of teaching | Plan Hangman together (pseudocode + function table) | Students write stubs and checks in Day 19 Exercise 5 |
| Day 20, 0:00–0:21 | Checkpoint 4 | First, so it is not squeezed by the build (reasons in the Day 20 lesson) |
| Day 20, 0:21–0:34 | Rock, Paper, Scissors demo (build order) + project launch | Demo is *not* Hangman on purpose |
| Day 20, 0:34–0:70 | Build | Circulate with the questions below |
| Day 20, 0:70–0:75 | Two show-and-tells + "how many checks are `True`?" | Note students below 8 of 14 |
| Homework (40–60 min) | Finish Must (+ Should), `example_runs.txt` | Due at the start of Day 22 |
| Day 22, first 5 min | Collect submissions; 2–3 students demo | Grade with the rubric in the brief |

Realistic expectations: in 36 minutes of class most students get the four calculating functions and `get_guess`
done; `play_round`/`play_game` are usually finished at home.

## Why a `CHECK_ONLY` switch (and not something else)

The game must run with `uv run hangman.py`, and the file has to **end by calling the game**: we cannot use
`if __name__ == "__main__":` until Day 26. So running the file always starts the game, and checks need a safe home.
Options considered:

| Option | Problem for beginners |
|--------|----------------------|
| A block of checks students comment/uncomment | Easy to uncomment half of it; indentation and `#` mistakes; checks "disappear" in the final file |
| A separate `check_hangman.py` that imports `hangman` | Importing runs the game (no `__name__` guard yet) and `import` of own modules is Day 26 |
| Checks only in a notebook | Two copies of every function that slowly drift apart; the submitted file contains no evidence |
| **`CHECK_ONLY = True/False` + `if`/`else` at the bottom** (chosen) | Uses only Day 09 syntax; one obvious switch; checks live in the submitted file as evidence |

The switch also sets up Day 26 nicely: `if __name__ == "__main__":` is "Python's built-in version of our switch".
The Day 20 workbench notebook is offered as an *optional* place to develop the calculating functions; the
functions are then copied into `hangman.py`, where `run_checks()` confirms they still work.

The starter's calculating functions are **docstring-only stubs** (they return `None`), so all 14 checks start as
`False`: the same "red first" experience students will later get from failing tests (Week 6). Running the starter
with `CHECK_ONLY = False` prints the welcome line and stops; it never crashes or loops forever.

## How the reference was tested

There are no automated tests before Week 6, so the reference was hand-tested by piping input (no network, no
packages):

```
cd projects/02-hangman/reference
uv run python -m py_compile hangman.py
# all 14 checks print True:
uv run python -c "exec(open('hangman.py').read().replace('CHECK_ONLY = False', 'CHECK_ONLY = True'))"
# a forced word ("python" via seed 2): invalid input (P repeated, ab, 7, empty), a win, an invalid y/n answer,
# a second game ("function") lost with 6 wrong letters, then quit:
printf 'p\nP\nab\n7\n\ny\nz\nt\nh\no\nn\nmaybe\ny\nq\nx\nj\nw\nk\nz\nn\n' | \
  uv run python -c "import random; random.seed(2); exec(open('hangman.py').read())"
```

Each of the 12 words in `WORDS` was also played to a win with `WORDS` temporarily reduced to that one word
(input: the word's distinct letters, then `n`). All runs finished with the final score line.
You can test a student's game the same way: `printf 'a\ne\n...\nn\n' | uv run hangman.py`.

## Common pitfalls

| Pitfall | Symptom | Unblocking question (don't type the fix) |
|---------|---------|------------------------------------------|
| `display_progress` prints | checks `False`, `Word: None` in the game | "What does your function give back? Where is the `return`?" |
| Trailing space from `+= letter + " "` | `False` though it "looks right" | "Print it between `[` and `]`. What do you see at the end?" |
| `return True` inside the `is_word_guessed` loop | win after one correct letter | "After checking the first letter, how do you know about the others?" |
| `guess.isalpha` without `()` | `7` accepted | "Is `isalpha` being *called*?" |
| No `.lower()` / `.strip()` in `get_guess` | `A` or `" a"` counted as wrong | "What exactly is inside `guess` when Mei types a capital A?" |
| `guessed_letters = []` at the top of the file | second game remembers old letters | "Where should a *new* game get its empty list?" |
| Wrong guess counted twice for repeated letters | lives drop on a repeat | "What does `is_valid_guess` say about a repeated letter? Is it called?" |
| `<=` instead of `<` in the loop condition | a 7th wrong guess is allowed | "Trace the last life on paper: what is `wrong_guesses` when the loop checks?" |
| Replay by calling `play_game()` inside `play_game()` | works, but the score resets | "How did we repeat things on Day 13? Which loop fits 'until the player says no'?" |
| Loop condition with `or` instead of `and` | game never ends after winning | "Say the condition in English: keep going while … *and* …" |
| `random.seed(...)` inside `choose_word` | same word every game | "What does seeding do? Do we want that in a real game?" |
| `CHECK_ONLY` still `True` | "the game doesn't start" | "What does the switch at the bottom say?" |

General unblocking routine: (1) "Which check is `False`?" (2) "What should it return for that input? Work it out
on paper." (3) "Put a `print` inside your function to see what it is doing." Only after that, point at a line.

Students who are completely stuck on `play_round`: give them the Day 19 pseudocode on paper and ask them to
turn **one line** at a time into code. Students who finished Exercise 6 (`simulate_game`) in the workbench
already have the loop: ask them to add `show_status` and `get_guess` to it.

## Grading notes

Grade with the rubric in the brief (shared rubric + 3 project-specific criteria). A fast routine, about 5 minutes
per student:

1. Run with `CHECK_ONLY = True`: count the `True`s (evidence, 10).
2. Set `CHECK_ONLY = False` and play: type `7`, `ab`, an empty line, a capital letter, a repeated letter; win
   once (temporarily shorten `WORDS` if needed), lose once, answer `maybe` then `n` to "play again" (works 40,
   bad input 15).
3. Read the file: count functions with docstrings, look for `print` inside calculating functions, `global`, game
   logic at the top level (readability 20).
4. Ask one question from the list below during the demo (explanation 15).

Suggested deductions: missing docstrings −1 each (max −5); fewer than 5 functions −8; `global` used −3; a crash
on bad input −5 per crash type; reveals the word only on a win −3; no `example_runs.txt` −5.

Explanation questions: "Why does `is_valid_guess` return `True`/`False` instead of printing a message?" · "What
happens to `guessed_letters` when a game ends?" · "Why can't you check `get_guess` with `print(... == ...)`?" ·
"What would you change to allow 8 wrong guesses?" (*only `MAX_WRONG`*: a good answer shows they understand
constants).

Bonus (max +10, total capped at 100): Should items +2 each; each Could feature +2 to +4 depending on effort.

**Independence:** if two submissions are suspiciously similar, ask each student to explain and modify one
function live (for example "make `display_progress` show `*` instead of `_`"). That is a fairer test than
comparing files.
