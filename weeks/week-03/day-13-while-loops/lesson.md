# Day 13: `while` Loops

**Week 3 · Session 13 of 60 · Planned 75 min** · Previous: [Day 12](../day-12-iterating-collections/lesson.md) · Next: [Day 14](../day-14-break-continue-nested/lesson.md)

## Objectives

By the end of this lesson students can:

1. Explain when to use `while` (repeat *until something happens*, number of repeats unknown) instead of `for`
   (one pass per item or a known count).
2. Write and trace a counter-controlled `while` loop, naming its three parts: initialise, condition, update.
3. Write a **sentinel** loop ("type q to quit") that collects values until a stop value is typed.
4. Recognise an infinite loop, stop it (Interrupt in VS Code, Ctrl+C in a terminal) and fix its cause.
5. Write a **validation loop** with `.isdigit()` that keeps asking until the input is valid, then converts it
   with `int()`.

**Prior knowledge:** `for`, `range`, accumulators (Day 11); building lists, counting (Day 12); `input()` and
`int()`, the `ValueError` from `int("abc")` (Day 03); `and/or/not` (Day 09); `len` on strings (Day 04).

**Files:** `demo.ipynb` (you, projected; it calls `input()`, and the answers used when the notebook is checked
automatically are stored in its metadata) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

**New today:** `while`, and the string method `.isdigit()`.

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: Day 12 retrieval | core |
| 0:05–0:15 | Why `while`; anatomy of a counter loop | core |
| 0:15–0:22 | Infinite loops and how to stop them (live) | core |
| 0:22–0:30 | Sentinel loop: "type q to quit" | core |
| 0:30–0:45 | `.isdigit()`, validation loop, PIN retry | core |
| 0:45–0:50 | Common mistakes; `for` vs `while` | core |
| 0:50–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (challenge) together, or students swap and try to break each other's validation loop | optional (90-min session) |

**60-minute version:** show the PIN retry (demo section 6) only as a reading exercise, keep the infinite-loop
demo to 3 minutes, and give 15 minutes of practice (Exercises 1–4).

## 1. Warm-up (5 min)

Retrieval from Day 12 (board): "What does this print?"

```python
counts = {}
for word in "to be or not to be".split():
    counts[word] = counts.get(word, 0) + 1
print(counts["to"], len(counts))
```

Answer: `2 4`. Then ask: "Every loop we wrote this week knew how many passes it would make. Can you think of a
situation where you do **not** know?" Collect answers: keep asking until the password is right, keep playing until
the player quits, keep saving until you reach a goal.

## 2. Why `while`, and its three parts (10 min)

**Intuition:** `for` is "do this for every plate on the table". `while` is "keep stirring **while** the soup is
not boiling": you check the condition, do the work, check again.

Live code (demo section 1), a savings goal:

```python
savings = 0
months = 0
while savings < 5000:
    savings += 650
    months += 1
print(months, savings)     # 8 5200
```

**Prediction question:** "How many months?" Let students estimate (5000 / 650 ≈ 7.7, so the loop needs 8).

Anatomy (demo section 2): count 1 to 5 with `while`, next to the `for` version.

```python
count = 1                  # 1. initialise
while count <= 5:          # 2. condition, checked BEFORE every pass
    print(count)
    count += 1             # 3. update: moves towards making the condition False
```

Draw the trace table with a column for "condition True?". Emphasise the condition is checked **before each pass**,
including the first.

**Prediction question** (demo section 2): `count = 10` then `while count <= 5:`. "How many times does the body
run?" (*Zero. The condition is False at the first check.*)

## 3. Infinite loops (7 min)

If nothing in the body makes the condition False, the loop never ends. **Live:** type this into a *new* cell
(it is shown as text in demo section 3, not as a runnable cell) and run it:

```python
count = 1
total = 0
while count <= 5:
    total += count       # forgot count += 1
```

Point at the `[*]` next to the cell: it is still running. Then:
- **VS Code notebook:** click **Interrupt** (■ at the top of the notebook). You get a `KeyboardInterrupt` error.
  If that does not work, **Restart** the kernel.
- **Terminal (`uv run …`):** press **Ctrl+C**.

Do *not* demo an infinite loop that prints: thousands of lines can freeze VS Code.

**Prediction question** (demo section 3, as text): `n = 2` and `while n != 10: n += 3`. "Does it stop?" (*No: n goes
2, 5, 8, 11, 14… and jumps over 10 forever.* With `n = 1` it would stop at 10, which is why this bug hides in
testing.) Lesson: prefer `<`/`<=` over `!=` in counter conditions.

## 4. Sentinel loops (8 min)

**Why:** we often collect input until the user says "stop". The stop value is called a **sentinel** (a guard who
says "this is the end").

Live code (demo section 4):

```python
shopping = []
item = input("Item (q to quit): ")      # ask once BEFORE the loop
while item != "q":
    shopping.append(item)
    item = input("Item (q to quit): ")  # ask again at the END of the body
print(shopping, len(shopping), "items")
```

With inputs `bread`, `milk`, `eggs`, `q` the output ends with `['bread', 'milk', 'eggs'] 3 items`.

Key point: the input line appears **twice**: once to get the first value, once at the end of every pass. Ask:
"What happens if we delete the second `input` line?" (*Infinite loop: `item` never changes.*) "What if the user
types `q` first?" (*Empty list: the body never runs.*)

## 5. Validation loops with `.isdigit()` (15 min)

**Why:** on Day 03, `int(input(...))` crashed with `ValueError` when the user typed `twenty`. A program should
**keep asking** instead of crashing.

`.isdigit()` (new) returns `True` when **every** character is a digit 0–9 and the string is not empty.

**Prediction round** (demo section 5, vote on each): `"42"` (*True*), `"4.5"` (*False*, the dot), `"-3"` (*False*,
the minus), `""` (*False*, empty), `" 7"` (*False*, the space; `.strip()` first if needed).

Validation loop, same shape as the sentinel loop:

```python
age_text = input("Your age: ")
while not age_text.isdigit():
    print("Please type a whole number, like 19.")
    age_text = input("Your age: ")
age = int(age_text)        # safe now: we know it is all digits
print(f"Next year you will be {age + 1}.")
```

Mock inputs `twenty`, `-5`, `19`: two retries, then `Next year you will be 20.`

Point out the honest limitation: `.isdigit()` rejects negative numbers and decimals. For ages and quantities
that is exactly what we want. Day 25 shows the general tool (`try/except`).

**PIN retry** (demo section 6, the roadmap's output for today): the condition combines a check and a counter.

```python
correct_pin = "2468"
attempts = 0
entered = ""
while entered != correct_pin and attempts < 3:
    entered = input("PIN: ")
    attempts += 1
if entered == correct_pin:
    print(f"Unlocked after {attempts} attempt(s).")
else:
    print("Card blocked.")
```

Trace it with mock inputs `1111`, `2468`: *Unlocked after 2 attempt(s).* Then ask "What would the output be with
`1111`, `0000`, `9999`?" (*Card blocked.*) Note the `if` **after** the loop decides *why* the loop ended.

## 6. Common mistakes and `for` vs `while` (5 min)

Run the cells in demo section 7:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `while count = 5:` | `SyntaxError: … Maybe you meant '==' or ':='` | `=` assigns, `==` compares (Day 09). We always want `==`; `:=` is not part of this course |
| `int("twenty")` without validating first | `ValueError: invalid literal for int()` | This is why we validate with `.isdigit()` first |
| `if text.isdigit:` (no parentheses) | no error, always true | Without `()` the method is not called; the method itself counts as "truthy" |
| forgetting the update / the second `input()` | infinite loop | Something in the body must change the condition |

Decision table (demo section 8) to leave on the board:

| Use `for` when… | Use `while` when… |
|-----------------|-------------------|
| you have a collection to walk through | you repeat until a condition changes |
| you know the number of repeats (`range`) | the number of repeats depends on the user or the data |

## 7. Practice (20 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Trace the while loops | predicting passes and final values | recall |
| 2 Growing plant | counter loop with a goal | application |
| 3 Fix the infinite loops | finding the missing/wrong update | modification |
| 4 Score collector | sentinel loop + accumulators | problem solving |
| 5 Ticket quantity | validation loop with `.isdigit()` and a range check | problem solving |
| 6 The 3n + 1 puzzle (challenge) | `while` with `if/else` inside, counting steps | challenge |

Exercises 4 and 5 call `input()`: students type the answers themselves when they run the cell.

While circulating, look for:
- the missing "ask again" line at the end of the body (the cell shows `[*]` forever: teach them to Interrupt);
- `int(input(...))` before validating;
- `while age_text.isdigit():` (the condition the wrong way round: loops while the input is *valid*);
- in Exercise 5, `int()` on the text *before* checking `.isdigit()` in the condition.

Expected outcome: everyone completes 1–3, most complete 4, many complete 5.

## 8. Recap and exit ticket (5 min)

Recap (students supply):
1. `while condition:` repeats as long as the condition is true; it is checked before every pass.
2. Three parts: initialise, condition, update. No update → infinite loop → Interrupt / Ctrl+C.
3. Sentinel and validation loops: ask once before the loop, ask again at the end of the body.
4. `.isdigit()` checks text **before** `int()` converts it.

**Exit ticket:** What does this print?

```python
n = 20
steps = 0
while n > 1:
    n = n // 2
    steps += 1
print(n, steps)
```

Answer: `1 4` (20 → 10 → 5 → 2 → 1).

## Homework (20 min)

Finish Exercise 5. Then write a small "menu" program cell: show `1) Balance  2) Deposit  q) Quit`, keep asking for
a choice until the user types `q`, and print a different message for each valid choice and `Unknown option` for
anything else. (No real balance is needed.)

## Next class

Day 14 adds `break` (leave a loop early), `continue` (skip to the next pass), `while True` loops, nested loops and
the `random` module, and we build a number-guessing game. Teaser: "Today we wrote `input()` twice in every
validation loop. Tomorrow we will see a way to write it once."

## Instructor notes

- **Do not teach `break` or `while True` today**, even when students ask how to avoid the duplicated `input()` line.
  Say "tomorrow". Today's priming-read pattern makes the condition visible, which is the point.
- Students coming from other languages may ask about `do…while`: Python does not have it.
- If a student's notebook is stuck on an `input()` box (they ran another cell while one was waiting), they must
  answer or press Escape, then Interrupt. Show this once to the whole class; it happens to everyone.
- `.isnumeric()` and `.isdecimal()` exist; do not go there. `"²".isdigit()` being `True` is trivia, skip it.
- Fast students: make Exercise 5 also reject leading zeros such as `"07"`. Slow students: give them the skeleton
  of the sentinel loop on the board (ask, `while`, body, ask again) and let them fill in the body.
