# Day 20: Project 02, Hangman (+ Checkpoint 4)

**Week 4 · Session 20 of 60 · Planned 75 min** · Previous: [Day 19](../day-19-decomposition/lesson.md) · Next: [Day 21](../../week-05/day-21-built-in-functions/lesson.md)

## Objectives

By the end of this lesson students can:

1. Show what they have learned about functions in Checkpoint 4 (define/call, parameters, `return` vs `print`, scope, defaults, checks).
2. Build a program in the right order: checkable functions first, then input functions, then the glue that calls them.
3. Turn the Day 19 Hangman plan into working functions, each with a docstring and with checks that print `True`.
4. Run their game with `uv run hangman.py`, using the `CHECK_ONLY` switch to run checks without starting the game.

**Prior knowledge:** everything from Days 11–19, especially the Hangman plan and stubs from Day 19 (Exercise 5),
`random.choice` (Day 14), `while` validation loops (Day 13), `.isalpha()` (Day 19).

**Files:** `demo.ipynb` (you, projected: Rock, Paper, Scissors built function by function) · `practice.ipynb`
(students: the Hangman *workbench*) · `solutions.ipynb` (you only) ·
[Project brief](../../../projects/02-hangman/README.md) · [Instructor guide](../../../projects/02-hangman/INSTRUCTOR.md) ·
[Checkpoint 4](../../../assessments/weekly/week-04-checkpoint.md)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:03 | Settle, hand out Checkpoint 4 | core |
| 0:03–0:21 | **Checkpoint 4** (individual, closed notes) | core |
| 0:21–0:29 | Demo: building Rock, Paper, Scissors function by function | core |
| 0:29–0:34 | Project launch: brief, starter tour, `CHECK_ONLY` switch | core |
| 0:34–0:70 | Build Hangman (Must requirements first) | core |
| 0:70–0:75 | Show-and-tell + what to finish at home | core |
| +15 min | Longer build; pairs swap laptops and try to break each other's input validation | optional (90-min session) |

**For 60 min:** skip the demo (students saw the same workflow on Day 19; the demo notebook can be read at home)
and build for 29 minutes. Never cut the checkpoint short; move it to the start of Day 21 instead if you must.

### Why the checkpoint comes first

- **Project time always overruns.** A quiz scheduled for the end gets squeezed or skipped; at the start it gets
  its full 18 minutes.
- **It is a warm-up for the build.** The questions (return vs print, scope, defaults, checks) are exactly the
  ideas students need ten minutes later.
- **Fresh attention and fair conditions.** Students write the checkpoint before the energy of the build, and
  nobody is tempted to keep coding instead of finishing the quiz.
- Students who finish the checkpoint early read the project brief quietly. That is useful, not idle, time.

## 1. Checkpoint 4 (3 + 18 min)

Hand out the questions part of [week-04-checkpoint.md](../../../assessments/weekly/week-04-checkpoint.md)
(everything above the `---` line). Paper or a shared form; no notebooks, no notes. Collect at 0:21 sharp.

Mark it after class with the answer key at the end of the file. Note the weakest question in `PROGRESS.md` and
spend 5 minutes of Day 21's warm-up on it (see `assessments/README.md`).

## 2. Demo: building function by function (8 min)

Use `demo.ipynb`. The example is **Rock, Paper, Scissors**, deliberately *not* Hangman, so the project stays the
students' own work. The point is the **order** of building:

1. **The plan** (demo section 1): the same table as Day 19, including the "checkable?" column.
2. **Checkable functions first** (sections 2–3): `decide_winner` gets its stub and checks before any body. The
   first body forgets draws. **Prediction question:** "which check still prints `False`?" (*the `paper`/`paper`
   draw*). Fix, re-run all checks. Then `is_valid_choice`, and the `KeyError: 'Rock'` cell showing why validation
   matters.
3. **Random** (section 4): check that the result is **allowed** (`in CHOICES`), not its exact value.
4. **Input functions** (section 5): try by hand with good *and* bad answers (`lizard`, ` Rock`).
5. **Glue** (section 6): `play_round` and `play_game` mostly call already-checked functions, so the first full
   run usually just works.
6. **Into a `.py` file** (section 7): the `CHECK_ONLY` switch. Say: "your starter works exactly like this".

Keep it to 8 minutes. Run the cells; don't type them live.

## 3. Project launch (5 min)

Open the [student brief](../../../projects/02-hangman/README.md) on the projector and point at:

- the **Must / Should / Could** lists ("Must first; Should only when every Must works");
- the **build plan** with a checkpoint after each step;
- the **rubric**, especially "≥ 5 small functions with docstrings" and "example runs".

Then the starter: students copy `projects/02-hangman/starter/hangman.py` into their own project folder and run
`uv run hangman.py`. They should see **14 lines of `False`**. Explain:

- `CHECK_ONLY = True` (bottom of the file) runs `run_checks()` only. The game does not start.
- Each `TODO` function turns some `False` lines into `True`.
- When every line is `True`: set `CHECK_ONLY = False` and play.
- The workbench notebook (`practice.ipynb`) has the same functions and checks, for students who prefer to
  develop in a notebook and then copy the function into `hangman.py`.

## 4. Build (36 min)

Students work individually (helping each other with *questions* is fine; sharing code is not, see the
independence rule in `projects/README.md`).

Suggested order, written on the board:
1. `display_progress` → `is_word_guessed` → `is_valid_guess` → `choose_word` (checks turn `True`)
2. `get_guess` (try it by hand: temporarily add `print(get_guess(["a"]))` as the last line of `run_checks()`,
   type some bad guesses and a repeated `a`, then delete the line)
3. `play_round` (tip: temporarily set `WORDS = ["cat"]` so you know the answer)
4. `ask_play_again` + `play_game`
5. Should: `show_status` with gallows/lives and guessed letters

The workbench exercises map onto the Must/Should requirements:

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 `choose_word` | `random.choice`, checking a random result | Must |
| 2 `display_progress` | loop over a string, build a list, `" ".join` | Must |
| 3 `is_word_guessed` | early `return False` inside a loop | Must |
| 4 `is_valid_guess` | combining conditions, `.isalpha()` | Must |
| 5 `lives_bar` | string repetition, default parameter | Should |
| 6 `simulate_game` (challenge) | the game loop's logic without `input()` | challenge |

**While circulating**, check in this order: (1) does the file run? (2) how many checks print `True`? (3) is
`play_round` a loop that ends both ways? Use the unblocking questions in
[INSTRUCTOR.md](../../../projects/02-hangman/INSTRUCTOR.md) instead of typing fixes.

Expected outcome by 0:70: everyone has most checks `True`; most have a playable round; fast students are on
*Should* features.

## 5. Common mistakes on Hangman day

| Mistake | What you see | How to explain it |
|---------|--------------|-------------------|
| `display_progress` prints instead of returning | output looks right, checks say `False`, `Word: None` | A check (and `show_status`) needs a returned value |
| Trailing space in `display_progress` | `False` for a result that "looks" right | Print it between brackets to see the space; use `" ".join` |
| `return True` inside the loop of `is_word_guessed` | game declares a win after one correct letter | Return `True` only after the loop has checked every letter |
| `guess.isalpha` without `()` | digits accepted as guesses | Without `()` the method doesn't run |
| Uppercase input not matching | `A` counted as wrong | Lowercase in `get_guess` (`.strip().lower()`) |
| `guessed_letters = []` outside `play_round` | the second game starts with old letters | Each game needs its own fresh list: create it inside `play_round` |
| `while wrong_guesses <= MAX_WRONG` | 7 wrong guesses allowed | Trace the last life on paper |
| "Play again" by calling `play_game()` inside itself | works, but the score resets and calls pile up | Use a `while` loop controlled by `ask_play_again()` |
| `CHECK_ONLY` still `True` | "my game doesn't start" | Flip the switch at the bottom of the file |

## 6. Show-and-tell and wrap-up (5 min)

Two volunteers run their game on the projector (one win, one invalid guess). Ask each: "which function are you
proudest of, and what does it return?"

**Exit check** (instead of an exit ticket): each student runs `uv run hangman.py` with `CHECK_ONLY = True` and
shows you (or posts in chat) how many checks print `True`. Note anyone below 8 out of 14: they need help at the
start of Day 21 or in office hours.

## Homework (project week: 40–60 min)

Finish every **Must** requirement (and any **Should** you like), then follow the submission checklist in the
brief, including the example runs file. **Due at the start of Day 22.** Optional: one *Could* feature.

## Next class

Day 21 starts Week 5 with **built-in functions** (`sorted(key=...)`, `zip`, `any`/`all`, `help`): now that
students write their own functions, they learn which ones Python already provides. `.isalpha()` (from Day 19) is
recapped there.

## Instructor notes

- The checkpoint is low-stakes retrieval practice. Don't grade it harshly; use it to plan Day 21's warm-up.
- The reference solution is in `projects/02-hangman/reference/` (keep it private). It also passes all 14 checks.
- Do not introduce `if __name__ == "__main__":` today. The `CHECK_ONLY` switch does the same job for now and
  makes Day 26 easy to motivate ("Python has a built-in version of our switch").
- Students who finish everything: suggest a *Could* feature, or the Tic-Tac-Toe extension in the brief (planned
  the same way: table first, checkable functions first).
- Students who are far behind: help them reach a playable game with only the Must functions; the Should items
  are bonus points.
