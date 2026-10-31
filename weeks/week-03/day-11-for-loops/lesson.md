# Day 11: `for` Loops and `range`

**Week 3 · Session 11 of 60 · Planned 75 min** · Previous: [Day 10](../../week-02/day-10-decisions-practice/lesson.md) · Next: [Day 12](../day-12-iterating-collections/lesson.md)

## Objectives

By the end of this lesson students can:

1. Explain the problem a loop solves (repeating work without copy-paste) and trace a `for` loop over a list,
   saying the loop variable's value on every pass.
2. Write a `for` loop with a colon and an indented body, and say which lines run once per item and which run once
   after the loop.
3. Use `range(stop)`, `range(start, stop)` and `range(start, stop, step)` and predict the numbers produced
   (the stop value is never included).
4. Use the **accumulator pattern** (create before the loop, update inside, use after) to total and count values,
   including counting only the values that pass an `if` test.

**Prior knowledge:** lists, `len`, `sum` (Day 06); list methods (Day 07); `if/elif/else` and comparisons (Day 09);
f-strings and `:.2f`/`:>4` formats (Days 04–05); `+=` (Day 03). Students have not seen any kind of repetition.

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

**New small tools today:** `list(range(...))` to *see* the numbers a range produces (introduce it as "turn the
range into a list so we can look inside"; it works like `set()` from Day 08), and `print(..., end=" ")` to keep
printing on one line (demo section 5). Both are named here so later days may use them.

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:07 | Warm-up: retrieval + "the copy-paste problem" | core |
| 0:07–0:20 | First `for` loop: loop variable, indentation, trace table | core |
| 0:20–0:32 | `range`: counting, start/stop/step, multiplication table | core |
| 0:32–0:45 | Accumulator pattern: total, count, count with a condition | core |
| 0:45–0:50 | Common mistakes (live debugging) | core |
| 0:50–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (challenge) together, or demo section 6 (weekly expenses) in full | optional (90-min session) |

**60-minute version:** skip demo section 6 (real-world example), cut the warm-up to 3 minutes and give students
15 minutes of practice (Exercises 1–4).

## 1. Warm-up (7 min)

Retrieval questions from Week 2 (on the board, 2 minutes):
- "`marks = [72, 45, 88]`. What is `marks[-1]`? What is `len(marks)`?" (*88; 3*)
- "Write an `if` that prints `Pass` when `mark >= 50`, otherwise `Fail`."

Then pose the problem (demo section 1). Show five marks printed with five `print` lines, each checking pass/fail.
Ask: **"What if the class had 300 students? What if a new student joins tomorrow?"** Let them say "copy-paste
300 times" and "change the code every time". That pain is the motivation for today: *write the instruction once,
let Python repeat it for each item*.

## 2. The first `for` loop (13 min)

**Intuition:** a `for` loop is like a teacher calling the register: "for each student in the list, say their name".
The teacher repeats the same action, and only the name changes each time.

Live code (demo section 2):

```python
marks = [72, 45, 88, 91, 60]
for mark in marks:
    print(mark)
print("Done")
```

Output: the five marks on separate lines, then `Done` once.

Read it aloud in English: "**for each** mark **in** marks, print the mark". Point at each part:

| Part | Meaning |
|------|---------|
| `for` … `in` … `:` | the loop header, ending with a colon (same as `if`) |
| `mark` | the **loop variable**: a name tag that moves to the next item on every pass |
| `marks` | the collection we walk through |
| indented lines | the **body**: runs once per item |
| first line back at the left margin | runs **once**, after the loop has finished |

Build a **trace table** on the board for the first three passes (pass | `mark` | printed). This is the same
tracing skill as Day 02, now with a column for each pass.

**Prediction question** (demo section 2): add `if mark >= 50: print(mark, "pass")` inside the loop. "How many
lines are printed?" (*4 pass lines; 45 fails the test and prints nothing.*)

**Prediction question:** move `print("Done")` *into* the body. "How many times does `Done` appear now?" (*5.*)
Indentation is not decoration: it decides what repeats.

Key points:
- The loop variable name is your choice; pick the singular of the list name (`for mark in marks`,
  `for name in names`). Say it so students adopt the habit.
- After the loop, the loop variable still holds the **last** item. Mention it only if asked.

## 3. `range`: loops that count (12 min)

**Why:** sometimes there is no list; we just want to repeat something *n* times or count 1, 2, 3, … `range`
produces the numbers for us.

Live code (demo section 3):

```python
for i in range(5):
    print("Hello", i)          # i is 0, 1, 2, 3, 4
print(list(range(1, 6)))      # [1, 2, 3, 4, 5]
print(list(range(0, 21, 5)))  # [0, 5, 10, 15, 20]
print(list(range(10, 0, -1))) # [10, 9, 8, ..., 1]
```

The three forms:

| Form | Produces | Memory hook |
|------|----------|-------------|
| `range(stop)` | 0, 1, …, stop − 1 | "stop numbers, starting at 0" |
| `range(start, stop)` | start, …, stop − 1 | "up to but **not including** stop" (like slicing on Day 05) |
| `range(start, stop, step)` | start, start + step, … | negative step counts down |

**Prediction questions** (demo section 3, vote first): `list(range(2, 11, 3))` → `[2, 5, 8]` (11 is never reached)
and `list(range(3))` → `[0, 1, 2]` (three numbers, but not 1–3).

Connect to slicing: `marks[1:4]` stops *before* index 4, and `range(1, 4)` stops before 4. Same rule.

Real use (demo section 3): a multiplication table.

```python
number = 7
for i in range(1, 11):
    print(f"{number} x {i:>2} = {number * i:>3}")
```

Output starts `7 x  1 =   7` and ends `7 x 10 =  70`. The `:>2`/`:>3` formats (Day 05) line the columns up.

Countdown: `for n in range(5, 0, -1): print(n)` then `print("Lift off!")` after the loop.

## 4. The accumulator pattern (13 min)

**Intuition:** a shopping-basket total at a till. The total starts at 0 *before* the first item, the cashier adds
each item's price *while scanning*, and you read the final total *after* the last item.

Live code (demo section 4):

```python
marks = [72, 45, 88, 91, 60]
total = 0                  # 1. create the accumulator BEFORE the loop
for mark in marks:
    total = total + mark   # 2. update it INSIDE the loop
print("Total:", total)     # 3. use it AFTER the loop -> Total: 356
```

Trace on the board: `total` goes 0 → 72 → 117 → 205 → 296 → 356. Then show the short form `total += mark`.

**Counting** is the same pattern with `+= 1`. **Counting with a condition** puts the update inside an `if`:

```python
passed = 0
for mark in marks:
    if mark >= 50:
        passed += 1
print(passed, "of", len(marks), "passed")   # 4 of 5 passed
```

**Prediction question** (demo section 4): "What if `total = 0` is moved *inside* the loop?" (*It is reset on every
pass, so only the last mark survives: `Total: 60`.*) Run it to confirm. This is the most common accumulator bug.

Key points:
- Three steps, three places: **before / inside / after**. Write them on the board and leave them up.
- "Doesn't `sum()` already do this?" Yes, for a plain total. But `sum()` cannot count only the passes, add only
  the expenses over a budget or total the squares; the pattern can. Today we practise the pattern.
- Average = total / count, computed **after** the loop.

## 5. Common mistakes (5 min)

Run the tagged cells in demo section 5 and read the last line of each error:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `for mark in marks` with no colon | `SyntaxError: expected ':'` | Every block header (`if`, `for`) ends with `:` |
| Body not indented | `IndentationError: expected an indented block` | Python needs to know which lines repeat |
| `range(times)` where `times = "3"` came from `input()` | `TypeError: 'str' object cannot be interpreted as an integer` | Convert first: `int(times)` (Day 03) |
| `range(1, 10)` to print 1–10 | no error, 10 is missing | Stop is excluded: use `range(1, 11)` |
| `total = 0` inside the loop | no error, wrong answer | Reset on every pass. Accumulators go *before* the loop |

Stress the last two: **the most dangerous bugs give no error message**. Checking the output against a value you
worked out by hand is part of programming.

## 6. Real-world example (optional, 5 min)

Demo section 6: one week of expenses, total, average per day, and how many days went over a daily budget of 1000.
It uses every idea from today in eight lines. If time is short, let students read it as homework.

## 7. Practice (20 min)

Students open `practice.ipynb`.

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the loops | trace `for` and `range` output | recall |
| 2 Times table | `range(start, stop)` + f-string alignment | application |
| 3 Fix the loop | colon, indentation, off-by-one, misplaced accumulator | modification |
| 4 Marks report | total, average, conditional counts | problem solving |
| 5 Countdown and even numbers | `range` with a step | application |
| 6 Savings plan (challenge) | two accumulators in one loop | challenge |

While circulating, look for:
- `print` of the total **inside** the loop (it prints a running total five times);
- `range(1, 10)` when they meant 1–10;
- `marks = marks + mark` (using the list name instead of the accumulator), which gives a `TypeError`;
- dividing by a hard-coded `5` instead of `len(marks)`.

Expected outcome: everyone completes 1–3, most complete 4–5, fast students try 6.

## 8. Recap and exit ticket (5 min)

Ask students to supply the three recap sentences:
1. A `for` loop runs its indented body once for each item; the loop variable holds the current item.
2. `range(start, stop, step)` counts from start up to **but not including** stop.
3. Accumulator: create before, update inside, use after.

**Exit ticket:** What does this print?

```python
total = 0
for n in range(1, 5):
    total = total + n
print(total)
```

Answer: `10` (1 + 2 + 3 + 4; 5 is not included). Students who write `15` need the stop rule again tomorrow.

## Homework (20 min)

Finish Exercises 5–6. Then write a loop that prints the 12 times table (`12 x 1` to `12 x 12`) and, after the loop,
the total of all twelve answers (expected total: 936).

## Next class

Day 12 loops over **other collections**: the characters of a string, the keys and values of a dict, and positions
with `enumerate()`. We will also *build* new lists and *count* things with a dict. Teaser: "How would you count how
many times each word appears in a sentence?"

## Instructor notes

- Do **not** introduce `while`, `break`, `continue`, `enumerate` or looping over strings/dicts today. Each has its
  own day, and today's goal is the for-loop mental model plus the accumulator.
- If someone asks about `for i in range(len(marks))`: it works, but looping over the items directly is clearer.
  We will meet `enumerate()` tomorrow for when we need positions.
- Slow students: have them trace on paper with a table before running anything. Fast students: ask them to rewrite
  Exercise 4 so it also counts *distinctions* (≥ 80) and *fails* in the same loop.
- Notebook reminder: an accumulator cell that is run twice keeps adding if the `total = 0` line is in another cell.
  Keep the initialisation in the **same cell** as the loop.
