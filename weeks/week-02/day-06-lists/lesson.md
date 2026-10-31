# Day 06: Lists and Indexing

**Week 2 · Session 6 of 60 · Planned 75 min** · Previous: [Day 05](../../week-01/day-05-slicing-formatting/lesson.md) · Next: [Day 07](../day-07-list-methods-tuples/lesson.md)

## Objectives

By the end of this lesson students can:

1. Explain why one list is better than many separate variables, and create a list of numbers or strings.
2. Read items with positive and negative indexes and take slices, reusing the Day 05 string rules, and predict an `IndexError`.
3. Calculate count, total, highest, lowest and average with `len`, `sum`, `min`, `max`.
4. Change an item by index, and explain why this works for lists but not for strings.
5. Check whether a value is in a list with `in` / `not in`.
6. Read one value from a nested list with two indexes (preview only).

**Prior knowledge (Days 02–05):** variables and types, arithmetic and `round()`, `+=`, string methods and `len()`,
f-strings, string indexing/slicing (`[start:stop:step]`, negative indexes) and the `:.1f` format spec.
**Not yet known:** loops, `if`, comparison operators (`==`, `<`), functions. Everything today works without them.

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: string indexing retrieval | core |
| 0:05–0:12 | Why lists? List literals | core |
| 0:12–0:22 | Indexing and slicing lists | core |
| 0:22–0:32 | `len`, `sum`, `min`, `max`, average | core |
| 0:32–0:40 | Changing an item; `in` / `not in` | core |
| 0:40–0:44 | Nested list preview | core (cut first for 60 min) |
| 0:44–0:48 | Common mistakes (live debugging) | core |
| 0:48–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (challenge) together on the board | optional (90-min session) |
| +5 min | "Why does `7.1` print as `7.100000000000001`?" (Exercise 5 discussion) | optional (90-min session) |

**For 60 min:** skip the nested-list preview (demo section 7) and set Exercises 1–4 in class, 5–6 as homework.

## 1. Warm-up (5 min)

Write on the board and let students answer on paper first (demo section 0):

```python
word = "Python"
print(word[0], word[-1], word[1:4], len(word))
```

Answer: `P n yth 6`. Ask: "Why is `word[1:4]` only three letters?" (*The stop position is not included.*)
Tell them to keep these rules in their heads, because today they reuse every one of them.

## 2. Why lists? (7 min)

**Problem first** (demo section 1): five marks in five variables, then an average formula that names all five.
Ask: "What changes if a sixth student joins? What about 30 students?" (*New variable, longer formula, easy to
forget one.*) We need **one name for the whole group**.

```python
marks = [72, 85, 64, 90, 58]
print(marks)          # [72, 85, 64, 90, 58]
print(type(marks))    # <class 'list'>
```

> **Analogy:** a row of numbered lockers. The name tag `marks` (Day 02) is stuck on the **whole row**. Each locker
> has a number, the **index**, and the first locker is number **0**.

Draw the table from demo section 2 on the board (index row, value row, negative index row) and leave it up all lesson.

Key points:
- Square brackets, commas between items. `[]` is an empty list (useful later, when we fill lists up).
- Lists keep their **order**. A list of strings looks like `["Asha", "Bilal"]`.
- A list *can* mix types, but in practice keep one kind of thing per list (all marks, all names).

## 3. Indexing and slicing (10 min)

Live code (demo section 3). Ask for predictions before each run:

```python
students = ["Asha", "Bilal", "Sara", "Omar", "Mei"]
students[0]      # 'Asha'
students[-1]     # 'Mei'
students[1:3]    # ['Bilal', 'Sara']
students[::-1]   # ['Mei', 'Omar', 'Sara', 'Bilal', 'Asha']
```

The one new idea: **an index gives an item, a slice gives a new list**. Point at the square brackets in the output.

Playlist example (same section): "now playing" is `playlist[0]`, "up next" is `playlist[1:4]`.

**Prediction question:** "`students` has 5 items. What does `students[5]` give?" Most will say `Mei`. Run it:
`IndexError: list index out of range`. Valid indexes are `0` to `len - 1`. "Last item" is always `[-1]`.

## 4. Summarising a list: `len`, `sum`, `min`, `max` (10 min)

Demo section 4 uses a week of temperatures:

```python
temperatures = [31.5, 33.0, 29.8, 35.2, 34.1, 30.6, 32.4]
len(temperatures)   # 7
max(temperatures)   # 35.2
min(temperatures)   # 29.8
sum(temperatures)   # 226.6
```

**Prediction question:** "Python has no `average()`. How do we get one?" Let students build it:
`sum(temperatures) / len(temperatures)` → `32.4` with `:.1f`. Then the range: `max(...) - min(...)` → `5.4`.

Stress why this beats the section-1 formula: **it keeps working when the list grows.**

`min`/`max` on strings use alphabetical order (`min(students)` → `'Asha'`). `sum` on strings fails (section 6).

## 5. Changing items and membership (8 min)

**Changing an item** (demo section 5): assign to a position.

```python
marks = [72, 85, 64, 90, 58]
marks[2] = 68                 # [72, 85, 68, 90, 58]
marks[3] = marks[3] + 5       # [72, 85, 68, 95, 58]
```

Read the second line **right side first**: get `marks[3]` (90), add 5, store it back. `marks[3] += 5` is the same.

Then contrast with strings: `word[0] = "J"` → `TypeError: 'str' object does not support item assignment`.
Lists are **mutable** (can change), strings are **immutable** (Day 04). Keep it at that level today; Day 07 builds on it.

**`in` and `not in`** (demo section 6) ask yes/no questions, so they produce a `bool`:

```python
"Omar" in students       # True
"Zara" not in students   # True
"omar" in students       # False  (case matters)
"Om" in students         # False  (must be a whole item)
"Om" in "Omar"           # True   (on a string, `in` finds a piece of text)
```

**Prediction question:** the last three lines. The difference between `in` on a list and `in` on a string surprises
almost everyone; take a moment on it.

## 6. Preview: nested lists (4 min)

Demo section 7: a seating plan, a list of rows.

```python
seating = [["Asha", "Bilal", "Sara"], ["Omar", "Mei", "Diego"]]
seating[1]       # ['Omar', 'Mei', 'Diego']
seating[1][0]    # 'Omar'
len(seating)     # 2 (rows, not people)
```

Read indexes left to right: "row 1, then seat 0". This is only a preview; tables of data return in Week 9. Do not
assign exercises beyond Exercise 6 on it.

## 7. Common mistakes (4 min)

Run demo section 8 and read the **last line** of each error together:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `marks(0)` | `TypeError: 'list' object is not callable` | Round brackets mean "call a function". Lists use square brackets |
| `marks[5]` on a 5-item list | `IndexError: list index out of range` | Counting starts at 0, so the last index is `len - 1`. Use `[-1]` |
| `sum(["72", "85"])` | `TypeError: unsupported operand type(s) for +: 'int' and 'str'` | The marks are text. Remove the quotes (or convert, Day 03) |
| `max([])` | `ValueError: max() iterable argument is empty` | There is no biggest item in an empty list |
| `word[0] = "J"` on a string | `TypeError: 'str' object does not support item assignment` | Strings cannot change. Build a new one: `"J" + word[1:]` |
| `["Fatima" "Ken", "Zara"]` (missing comma) | **no error**: list has 2 items, `'FatimaKen'` | Python glues neighbouring strings. Check `len()` when the count looks wrong |

The missing comma is the most important one: no error message, just wrong data.

Bridge into practice with demo section 9, the class-marks report (expected: 6 students, average `75.8`, highest
`95`, lowest `58`). It is the model for Exercise 2.

## 8. Practice (22 min)

Students open `practice.ipynb`.

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the output | index/slice/`in` on a list | recall |
| 2 Class marks report | `len`, `sum`, `min`, `max`, average | application |
| 3 Fix the broken code | five classic list/string mistakes | modification |
| 4 Update the playlist | change an item, slice, `in`/`not in` | application |
| 5 A week of temperatures | independent report + correcting an item | problem solving |
| 6 Gradebook with nested lists (challenge) | two indexes | challenge |

While circulating, look for:
- typing numbers again instead of using the list (`sum(marks) / 8`): ask "what if a mark is added?";
- off-by-one: "the third song" written as `playlist[3]`, `[1:3]` for "positions 1, 2 and 3";
- Exercise 3e: students trying to change the string. Nudge: "you can't change it, but can you build a new one from slices?";
- Exercise 5: the range printed as `7.100000000000001`. Tell them to use `:.1f` and promise a short explanation.

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

## 9. Recap and exit ticket (5 min)

Ask students to supply the recap:
1. A list stores many values in order under one name; indexes start at 0, `[-1]` is the last item.
2. Slicing works exactly as for strings and returns a new list.
3. `len`, `sum`, `min`, `max` summarise a list; average is `sum(x) / len(x)`.
4. Lists can be changed by index; strings cannot.

**Exit ticket:** what does this print?

```python
queue = ["Ken", "Zara", "Diego", "Fatima"]
queue[1] = "Ali"
print(queue[1:3], len(queue), "Zara" in queue)
```

Answer: `['Ali', 'Diego'] 4 False`.

## Homework (20 min)

1. Finish Exercises 5–6.
2. "My week in a list": make a list of 7 numbers about your own week (hours of sleep, minutes of exercise, money
   spent…). Print the total, the average (1 decimal place), the best and worst day's value, and the weekend values
   using a slice.

## Next class

Day 07 makes lists **grow and shrink**: `.append`, `.insert`, `.remove`, `.pop`, plus sorting and counting.
Teaser to end on: "Our report says the highest mark is 95, but **who** got it?" Tomorrow `.index()` answers that.
We also meet **tuples** (lists that cannot change) and a surprise: two names on the same list.

## Instructor notes

- Do **not** introduce list methods today, even if students ask how to add an item; say "tomorrow". Keeping today
  about indexes keeps the cognitive load low.
- If asked about `+` on lists: `[1, 2] + [3]` gives `[1, 2, 3]`. Fine to answer, not needed for exercises.
- Comparisons (`==`, `<`) come on Day 09. Today every yes/no question is answered with `in`, so solutions are
  checked by comparing printed output with the expected output.
- Floating-point artefacts (`7.100000000000001`): say "computers store most decimals approximately; always format
  money and measurements with `:.2f` or `:.1f`". Do not go into binary representation.
- Fast students: ask them to explain *in words* the difference between `"Om" in students` and `"Om" in "Omar"`.
  Slow students: let them draw the locker table for each list before writing any index.
