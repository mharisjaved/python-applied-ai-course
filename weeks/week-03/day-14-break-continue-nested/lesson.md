# Day 14: `break`, `continue`, Nested Loops and `random`

**Week 3 · Session 14 of 60 · Planned 75 min** · Previous: [Day 13](../day-13-while-loops/lesson.md) · Next: [Day 15](../day-15-project-quiz-game/lesson.md)

## Objectives

By the end of this lesson students can:

1. Use `break` to leave a loop early, and write a `while True` + `break` loop that asks for input only once.
2. Use `continue` to skip the rest of one pass (e.g. ignore invalid entries) and explain how it differs from `break`.
3. Write a nested loop and predict how many times the inner body runs (outer passes × inner passes).
4. Use `import random` with `randint`, `choice`, `shuffle`, and `seed` for reproducible results.
5. Build a number-guessing game with a random secret, hints and a limited number of attempts.

**Prior knowledge:** `for`, `range`, accumulators (Day 11); `enumerate`, counting with a dict (Day 12); `while`,
sentinel and validation loops, `.isdigit()` (Day 13); `" ".join()` (Day 07).

**Files:** `demo.ipynb` (you, projected; calls `input()`, answers for automatic checking are in its metadata) ·
`practice.ipynb` (students) · `solutions.ipynb` (you only)

**New today:** `break`, `continue`, `while True`, nested loops, and our **first `import`**: the `random` module
only. Importing in general and writing our own modules come on Day 26.

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: the duplicated `input()` from Day 13 | core |
| 0:05–0:13 | `break`; `while True` + `break` | core |
| 0:13–0:19 | `continue` | core |
| 0:19–0:28 | Nested loops: grid, pairs | core |
| 0:28–0:35 | `import random`: `randint`, `choice`, `shuffle`, `seed` | core |
| 0:35–0:47 | Live build: guessing game + "play again?" | core |
| 0:47–0:50 | Common mistakes | core |
| 0:50–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (dice duel) together, or the star-triangle pattern in demo section 3 | optional (90-min session) |

**60-minute version:** skip the dice-counting cell in demo section 4 and the star triangle in section 3, show
the "play again" wrapper (section 6) without typing it live, and give 15 minutes of practice (Exercises 1–3 + 5).

## 1. Warm-up (5 min)

Show Day 13's validation loop on the board:

```python
age_text = input("Your age: ")
while not age_text.isdigit():
    print("Please type a whole number.")
    age_text = input("Your age: ")
```

Ask: "Which line appears twice? What goes wrong if we change the prompt in one place and forget the other?"
Today's first tool removes the duplication.

## 2. `break` and `while True` (8 min)

**Intuition:** `break` is the emergency exit: leave the loop *now*, skip any remaining passes, and continue with the
first line after the loop.

Live code (demo section 1), searching for the first failing mark:

```python
marks = [72, 88, 45, 91, 38]
for mark in marks:
    if mark < 50:
        print("First fail found:", mark)
        break
    print(mark, "is fine")
print("Search finished")
```

**Prediction question:** "How many lines are printed, and is 38 mentioned?" (*`72 is fine`, `88 is fine`,
`First fail found: 45`, `Search finished`. 91 and 38 are never visited.*)

**`while True` + `break`:** a loop that would run forever, with the exit *inside* the body. The validation loop
becomes:

```python
while True:
    age_text = input("Your age: ")
    if age_text.isdigit():
        break
    print("Please type a whole number.")
age = int(age_text)
```

`input()` is now written once. Read it as "keep going until we `break` out". Both patterns are correct; use
whichever reads better. Mock inputs `abc`, `17` show one retry.

## 3. `continue` (6 min)

**Intuition:** a music playlist. `continue` = *skip this song* (go to the next one). `break` = *stop the playlist*.

Live code (demo section 2):

```python
readings = ["12", "", "15", "abc", "9"]
total = 0
for text in readings:
    if not text.isdigit():
        print(f"Skipping '{text}'")
        continue
    total += int(text)
print("Total:", total)       # Total: 36
```

**Prediction question:** "What is the total? How many 'Skipping' lines?" (*36; two.*) Point out that `continue`
avoids wrapping the rest of the body in an `else`, which keeps the "happy path" un-indented.

## 4. Nested loops (9 min)

**Intuition:** a clock. For every hour, the minute hand goes all the way round. The **inner loop runs completely for
each pass of the outer loop**.

Live code (demo section 3), a small times grid:

```python
for row in range(1, 4):
    line = ""
    for col in range(1, 6):
        line += f"{row * col:>4}"
    print(line)
```

Output: three lines, `   1   2   3   4   5` / `   2   4   6   8  10` / `   3   6   9  12  15`. Trace the first
row slowly: `row` stays 1 while `col` goes 1–5; *then* `row` becomes 2.

Pairs (demo section 3): every match in a small tournament.

```python
teams = ["Lions", "Tigers", "Bears"]
for home in teams:
    for away in teams:
        if home != away:
            print(home, "vs", away)
```

**Prediction question:** "How many matches?" (*3 × 3 = 9 combinations, minus the 3 where a team meets itself: 6.*)

Key point: `break` in the inner loop leaves **only the inner loop**. We will see this in the game's "play again"
wrapper.

## 5. The `random` module (7 min)

**Why:** games, quizzes, simulations and (in Week 10) splitting data for machine learning all need randomness.
Python ships with **modules**: toolboxes of extra code. `import random` opens the toolbox; we use its tools with
`random.` in front.

Live code (demo section 4):

| Tool | Does | Example |
|------|------|---------|
| `random.randint(a, b)` | whole number from a to b, **both included** (unlike `range`!) | dice: `randint(1, 6)` |
| `random.choice(items)` | one random item | pick a student |
| `random.shuffle(items)` | mixes the list **in place**, gives back nothing | shuffle quiz questions |
| `random.seed(n)` | makes the "random" sequence repeat exactly | demos, testing |

Run `random.randint(1, 6)` several times (different each time). Then run the cell with `random.seed(42)` first:
the same three numbers every time. Explain: computers produce *pseudo*-random numbers from a starting value; the
seed fixes the start. **Use a seed while testing; remove it when people play for real.**

**Prediction question:** "Can `randint(1, 6)` ever give 6?" (*Yes, both ends are included. `range(1, 6)` stops at
5: say this out loud, students mix them up.*)

## 6. Live build: guessing game (12 min)

Type demo section 5 together, one feature at a time, running after each step:
1. secret with `random.seed(7)` + `randint(1, 20)` (the seed makes the secret 11 for the demo);
2. `while True` loop with `input`, `int`, and "too low / too high";
3. `break` on the correct guess, and a guess counter;
4. `continue` for non-digit input, so it does not count as a guess.

Mock inputs `10`, `ten`, `15`, `12`, `11` → *Correct! You needed 4 guesses.*

Then demo section 6 wraps the game in a **"Play again?" outer loop**. Ask: "The `break` for a correct guess: which
loop does it leave?" (*Only the inner game loop; we still reach the "Play again?" question.*) This outer/inner
structure is exactly what the Quiz Game needs tomorrow.

## 7. Common mistakes (3 min)

Run the tagged cells in demo section 7:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `randint(1, 6)` without `random.` | `NameError: name 'randint' is not defined` | The tool lives inside the module: `random.randint` |
| `cards = random.shuffle(cards)` then `cards[0]` | `TypeError: 'NoneType' object is not subscriptable` | Like `.append`, `shuffle` changes the list and gives back nothing |
| `break` outside any loop | `SyntaxError: 'break' outside loop` | `break`/`continue` only make sense inside a loop |
| `continue` before the counter update in a `while` loop | infinite loop | The update is skipped, so the condition never changes |

## 8. Practice (20 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the output | `break`, `continue`, nested loop counts | recall |
| 2 First heatwave day | `break` + a "found" flag | application |
| 3 Step counter | `continue` to skip invalid entries | application |
| 4 Cinema seating plan | nested loops building rows, `join` | problem solving |
| 5 Guessing game with limited attempts | `random`, `while`, `break`, `continue` | problem solving |
| 6 Dice duel (challenge) | `random` + counters over 10 rounds | challenge |

Exercise 5 is the session's output; make sure everyone starts it, even if they skip Exercise 4.

While circulating, look for:
- the attempts counter increased for invalid input (should not be);
- `random.randint(1, 50)` *inside* the loop, so the secret changes every guess;
- after the loop, no way to tell "won" from "ran out of attempts" (suggest a `won = False` flag);
- `break` placed before the "Correct!" message, so the message never prints.

Expected outcome: everyone completes 1–3, most complete 5, fast students do 4 and 6.

## 9. Recap and exit ticket (5 min)

Recap (students supply):
1. `break` leaves the loop now; `continue` skips to the next pass.
2. `while True` + `break` puts the exit test in the middle of the body.
3. Nested loops: the inner loop runs completely for every outer pass; `break` leaves only the inner loop.
4. `random.randint(a, b)` includes both ends; `shuffle` changes the list in place; `seed` makes results repeatable.

**Exit ticket:** What does this print?

```python
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue
        print(i, j)
```

Answer: six lines: `1 1`, `1 3`, `2 1`, `2 3`, `3 1`, `3 3`.

## Homework (30 min)

Finish Exercise 5 and play it without the seed. Then **read the Project 01 brief**
([projects/01-quiz-game/README.md](../../../projects/01-quiz-game/README.md)) and write down three questions you
have about it. Bring a theme idea for your own quiz questions.

## Next class

Day 15 is **project day**: the Quiz Game. It combines everything from Weeks 1–3: a list of dicts for the
questions, a `for` loop to ask them, a validation loop for a/b/c/d, `random.shuffle`, and today's "play again"
wrapper. Checkpoint 3 opens the session.

## Instructor notes

- Do **not** teach `for … else` / `while … else`; it confuses beginners. Use a flag variable instead.
- Do not show `import random as r`, `from random import randint` or other modules. One module, one way, today.
- "Is it really random?" Pseudo-random is fine for games, not for passwords. Do not go further.
- If students ask how to leave *both* loops at once: use a flag variable checked by the outer loop. Day 17's
  `return` will be a cleaner answer.
- Fast students: in Exercise 5, add a "warmer/colder" hint or let the player choose the difficulty (range and
  attempts). Slow students: start Exercise 5 from the unlimited version in demo section 5 and add only the
  attempts limit.
