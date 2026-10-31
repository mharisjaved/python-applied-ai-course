# Day 21: Built-in Functions and Useful Methods

**Week 5 · Session 21 of 60 · Planned 75 min** · Previous: [Day 20](../../week-04/day-20-project-hangman/lesson.md) · Next: [Day 22](../day-22-comprehensions/lesson.md)

## Objectives

By the end of this lesson students can:

1. Replace a hand-written total/count/max/min loop with `sum`, `len`, `max`, `min`, and use `abs` and `round` on results.
2. Sort with `sorted(..., reverse=True)` and with a `key`: `key=len`, `key=str.lower`, or a small named function such as `by_score`.
3. Walk two lists side by side with `zip()` and explain what happens when the lists have different lengths.
4. Answer "did everyone…?" / "did anyone…?" with `all()` / `any()`, and check text with `.isdigit()` / `.isalpha()`.
5. Use `help()` to find out how a built-in (or their own function) is used.

**Prior knowledge:** `len/sum/min/max` (Day 06), `sorted()`, `.split()`, `" ".join()`, tuples and unpacking
(Day 07), dicts and lists of dicts (Day 08), truthiness (Day 09), finding a max by hand and `enumerate` (Day 12),
`.isdigit()` (Day 13), `.isalpha()` (Day 19, for Hangman), functions with parameters, `return` and docstrings (Days 16–17), keyword arguments (Day 17).

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: the "find the highest" loop vs `max()` | core |
| 0:05–0:10 | `abs()` and `round()` | core |
| 0:10–0:25 | `sorted()` with `reverse` and `key` (incl. own key function) | core |
| 0:25–0:32 | `zip()` and `enumerate()` | core |
| 0:32–0:40 | `any()`, `all()`, `.isdigit()`, `.isalpha()` | core |
| 0:40–0:43 | `help()` | core |
| 0:43–0:47 | Common mistakes (live debugging) | core |
| 0:47–0:52 | Real-world example: quiz leaderboard | optional (skip for 60 min, students meet it in Exercise 5) |
| 0:52–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +15 min | Exercise 6 (challenge) together, then "find `.isalnum()` with `help(str)`" | optional (90-min session) |

**For 60 min:** skip demo section 8 and shorten `help()` to one example; give Exercise 5 as homework.

## 1. Warm-up (5 min)

Show the Day 12 loop from demo section 1 (finding the highest mark by hand). Ask:
- "What does this loop do? How many lines is it?" (*Finds the biggest mark; five lines.*)
- "Which built-in from Week 2 does the same?" (*`max(marks)`.*)

Then the 🤔 cell: `print(max(marks), min(marks), sum(marks), len(marks))` → `91 58 449 6`.
Build the average live: `sum(marks) / len(marks)` → `74.83333333333333`, `round(average, 1)` → `74.8`.

**Message for the day:** Python ships with a toolbox of built-ins. Before writing a loop that totals, counts or
finds the biggest/smallest, check whether the tool already exists. Fewer lines means fewer places for bugs.

## 2. `abs()` and `round()` (5 min)

**Intuition:** `abs()` is "distance from zero". Use it when you care *how far off* something is, not the direction.

```python
budget = 250
spent = 287.5
difference = budget - spent      # -37.5
print(abs(difference))           # 37.5
```

**Prediction question** (demo section 2): `abs(3 - 10)` → `7`; `round(2.71828)` → `3`; `round(19.999, 1)` → `20.0`.

Key points:
- `round(x)` returns an `int`; `round(x, 2)` returns a `float` with 2 decimals.
- `round()` changes the **value**; `:.2f` in an f-string (Day 05) only changes how it is **displayed**. Round when
  you store or compare; format when you print.

## 3. `sorted()` with `reverse` and `key` (15 min)

Recap from Day 07: `sorted()` returns a **new** list; `.sort()` changes the list and returns `None`.
`reverse=True` is a **keyword argument** (Day 17), so it must be written by name.

**The capital-letter surprise** (demo section 3). Let students predict first:

```python
names = ["omar", "Zara", "asha", "Bilal", "mei"]
print(sorted(names))                 # ['Bilal', 'Zara', 'asha', 'mei', 'omar']
print(sorted(names, key=str.lower))  # ['asha', 'Bilal', 'mei', 'omar', 'Zara']
```

Python compares text character by character using character codes, and **all capitals come before all lowercase
letters**. That is why `Zara` beats `asha`.

**Explaining `key`:** "`key` is a function that makes a *sort label* for each item. Python sorts by the labels but
hands you back the original items." Draw it on the board:

| item | label from `str.lower` |
|------|------------------------|
| `"Zara"` | `"zara"` |
| `"asha"` | `"asha"` |

Stress **no brackets**: `key=str.lower` *hands over the tool*; `key=str.lower()` tries to *use* it right now with
nothing to lower. Same with `key=len`.

```python
words = ["notebook", "pen", "calculator", "ruler"]
sorted(words, key=len)                 # ['pen', 'ruler', 'notebook', 'calculator']
sorted(words, key=len, reverse=True)   # ['calculator', 'notebook', 'ruler', 'pen']
```

**Your own key function.** A list of dicts cannot be sorted directly: should Python compare names or scores?
We write a one-line function that returns *the thing to sort by*:

```python
def by_score(student):
    """Sort key: return the student's score."""
    return student["score"]

for student in sorted(students, key=by_score, reverse=True):
    print(student["name"], student["score"])   # Ken 92 / Fatima 85 / Sara 78
```

`max(students, key=by_score)` uses the same idea and returns the **whole dict** of the best student.

**Prediction question:** "What would `sorted(students)` do without a key?" (*`TypeError: '<' not supported between
instances of 'dict' and 'dict'`. Python does not know what "smaller" means for a dict.*)

Naming convention for key functions: `by_score`, `by_price`, `by_length`. Reading `sorted(players, key=by_score)`
aloud then sounds like English.

## 4. `zip()` and `enumerate()` (7 min)

**Analogy:** the two rows of teeth on a zip. `zip(names, scores)` takes the first of each, then the second of each…

```python
for name, score in zip(["Asha", "Bilal", "Mei"], [88, 75, 93]):
    print(name, "scored", score)
```

`print(zip(...))` shows `<zip object at 0x...>`, a "pair dispenser" that hands out pairs one at a time. `list(...)`
empties it into a list so we can see the pairs: `[('Asha', 88), ('Bilal', 75), ('Mei', 93)]`.

**Prediction question (important):** `list(zip(["Asha", "Bilal", "Mei"], [88, 75]))` →
`[('Asha', 88), ('Bilal', 75)]`. **No error, Mei just disappears.** In real data this is a silent bug, so check
`len(a) == len(b)` when it matters (Exercise 4d).

`enumerate(items, start=1)` recap (Day 12): gives `(position, item)` pairs; `start=1` for human-friendly ranks.

## 5. `any()`, `all()` and checking text (8 min)

**Intuition:** `all()` = "did **everyone** say yes?", `any()` = "did **anyone** say yes?".

Start with truthiness (Day 09), a sign-up form:

```python
fields = ["Diego", "", "0300-1234567"]
all(fields)   # False: the email field is empty
any(fields)   # True
```

Then a list of booleans built with the Day 12 append pattern (demo section 5):

```python
passed = []
for mark in marks:
    passed.append(mark >= 60)
# [True, True, True, True, False, True] → all: False, any: True
```

Tell students tomorrow's comprehensions will shrink those three lines to one: a nice hook for Day 22.

**`.isdigit()` and `.isalpha()` recap** (🤔 predict each): `"4821"` → True; `"48 21"`, `"-5"`, `"3.5"` → False;
`"Fatima".isalpha()` → True; `"Mei Ling"` (space) and `"Zara2"` → False.

Key points:
- `.isdigit()` means "only 0–9". Fine for PINs, ages, quantities. **It rejects negatives and decimals**, so it cannot
  validate prices or temperatures. On Day 25 we will use `try/except` for that.
- These are **methods** (called on a string with a dot), while `len`, `sorted`, `any` are **functions** (the value goes
  inside the brackets). Students often write `isdigit(pin)`; point out the difference.

`split`/`join` recap: `" ".join(sorted(sentence.split(), key=len))` → `is fun and python useful`.

## 6. `help()` (3 min)

`help(round)` prints its signature `round(number, ndigits=None)` and a short description. Read it together:
"`ndigits=None` means the second argument is optional; that is a default value, like on Day 18."

Then `help(by_score)`: it shows **our own docstring**. That is the payoff for writing docstrings since Day 16.

If someone runs `help(sorted)` they will see `sorted(iterable, /, *, key=None, reverse=False)`. Say: "ignore `/` and
`*` for now. They mean `key` and `reverse` must be written by name."

## 7. Common mistakes (live debugging, 4 min)

Run the tagged cells in demo section 7 and read the last line together:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `sorted(words, key=len())` | `TypeError: len() takes exactly one argument (0 given)` | Brackets *call* `len` now, with nothing inside. Pass the name only |
| `sorted(students, key=by_score())` | `TypeError: by_score() missing 1 required positional argument: 'student'` | Same mistake with our own function |
| `sum(["12", "30", "8"])` | `TypeError: unsupported operand type(s) for +: 'int' and 'str'` | Numbers stored as text. Convert with `int()` first (very common after reading files on Day 23) |
| `sorted(["Asha", 7, "Mei"])` | `TypeError: '<' not supported between instances of 'int' and 'str'` | Python cannot decide whether 7 is "smaller" than a name |
| `ranked = scores.sort()` | no error, `ranked` is `None` | `.sort()` changes the list in place and returns nothing. Use `sorted()` |

## 8. Real-world example: quiz leaderboard (5 min, optional)

Demo section 8 ranks five Quiz Game players. Point out the structure: one small key function per sort
(`by_score`, `by_seconds`), one function to print the table, one for the summary. Expected output:

```
=== Quiz Leaderboard ===
1. Zara      91
2. Mei       88
3. Asha      82
4. Diego     75
5. Bilal     67
Average score: 80.6
Fastest: Diego (80 s)
Gap between 1st and last: 24
```

Ask: "Why does `by_score` (written for `students`) also work for `players`?" (*It only needs a `"score"` key.*)

## 9. Practice (18 min)

Students open `practice.ipynb`.

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the output | all of today's built-ins | recall |
| 2 Replace the loops | `sum/max/min/len/round` | application |
| 3 Sort it out | `key=str.lower`, `key=len`, own key function, `max(key=)` | application |
| 4 Fix the broken code | `key` without brackets, `sum` of strings, `.sort()` → `None`, `zip` length | modification |
| 5 Leaderboard report | `zip` + `sorted(key=)` + `enumerate` + formatting | problem solving |
| 6 Username checker (challenge) | `.isalpha/.isdigit`, `all()`, early `return` | challenge |

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

While circulating, look for:
- `key=by_price()` with brackets (the most common error today);
- sorting `names` and `scores` separately in Exercise 5, which breaks the pairs. Ask "who has 92 now?";
- `round(sum(x)) / len(x)` with the bracket in the wrong place;
- `isdigit(text)` written as a function instead of `text.isdigit()`.

## 10. Recap and exit ticket (5 min)

Ask students to complete each sentence:
1. Before writing a loop to total/count/find the max, I check for a **built-in**.
2. `key=` takes a function **name without brackets**; it says *what to compare*.
3. `zip()` pairs lists and **stops at the shorter** one.
4. `all()` = everyone, `any()` = anyone.

**Exit ticket:** what does this print?

```python
cities = ["Rome", "oslo", "Lima", "berlin"]
print(sorted(cities, key=len, reverse=True)[0])
print(sorted(cities, key=str.lower)[0])
print(any(["", 0, "no"]))
```

Answer: `berlin` (6 letters is the longest), `berlin` (alphabetically first when case is ignored), `True`
(`"no"` is a non-empty string, so it is truthy).

## Homework (20 min)

Finish Exercise 5 (and 6 if you like a challenge). Then take your Hangman code from Day 20 and find **one** loop that
a built-in could replace (e.g. checking whether all letters have been guessed with `all()`). Write the old and new
version in a markdown cell.

## Next class

Day 22 introduces **comprehensions**: building a new list (or dict) in one line. Today's "append `True`/`False`
in a loop, then `all()`" pattern becomes `all([mark >= 60 for mark in marks])`, and `zip()` will help build
dictionaries in one line.

## Instructor notes

- **Lambda is not taught in this course.** If a student has seen `key=lambda s: s["score"]` online, say: "that is a
  shortcut for a one-line function. We write the named function because it is easier to read and test." Do not
  demonstrate it.
- `round()` uses "round half to even": `round(2.5)` is `2`, `round(3.5)` is `4`. If a student hits this, explain
  it is deliberate (it avoids always rounding up in large statistics) and move on. Do not go into floating-point
  representation.
- `any([])` is `False`, `all([])` is `True`. Mention only if asked. Sorting is **stable** (equal keys keep their order,
  Exercise 3b): a good question for fast students.
- Do not introduce `map`, `filter`, `reversed` or `dict(zip(...))`; `.isalnum()` appears only as the Exercise 6 bonus.
- Slow students: let them skip `zip` in Exercise 5 by sorting a ready-made list of `(name, score)` tuples.
  Fast students: ask them to break score ties by name (hint: sort by name first, then by score: stability does the rest).
