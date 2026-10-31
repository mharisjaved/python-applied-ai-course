# Day 12: Iterating Strings, Lists and Dicts

**Week 3 · Session 12 of 60 · Planned 75 min** · Previous: [Day 11](../day-11-for-loops/lesson.md) · Next: [Day 13](../day-13-while-loops/lesson.md)

## Objectives

By the end of this lesson students can:

1. Loop over the characters of a string, the dicts in a list of dicts, and the key/value pairs of a dict with
   `.items()`.
2. Use `enumerate()` (with `start=1`) to get a position and an item together.
3. Build a new list from an old one with the **empty list + `.append()` in a loop** pattern (filter and transform).
4. Count how often things occur with a dict: `counts[key] = counts.get(key, 0) + 1`.
5. Find a maximum *and who has it* with a "best so far" variable, without `max()`.

**Prior knowledge:** `for`, `range`, accumulators (Day 11); string methods `.lower()`, `.split()` (Days 04, 07);
`.append()` (Day 07); dicts, `.get()`, `.items()`, list of dicts (Day 08); tuple unpacking `a, b = pair` (Day 07).

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: trace a Day 11 accumulator | core |
| 0:05–0:12 | Looping over a string: vowel counter | core |
| 0:12–0:24 | Lists of dicts, dict `.items()`, attendance report | core |
| 0:24–0:30 | `enumerate()` | core |
| 0:30–0:37 | Building a new list with `.append` | core |
| 0:37–0:45 | Counting with a dict, finding the maximum manually | core |
| 0:45–0:50 | Common mistakes (live debugging) | core |
| 0:50–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Demo section 8 (word frequency + most common word) in full, or Exercise 6 together | optional (90-min session) |

**60-minute version:** skip the `if/else` counting version in demo section 5 (show only `.get`), skip section 8,
and give 15 minutes of practice (Exercises 1–4).

## 1. Warm-up (5 min)

On the board, students trace and predict:

```python
total = 0
for n in range(3, 10, 3):
    total += n
print(total)
```

Answer: `18` (3 + 6 + 9). Ask: "Where must `total = 0` go and why?" (*Before the loop, or it resets every pass.*)
Then: "Yesterday we looped over lists and ranges. What else have we stored in Python that has many parts?"
(*strings, dicts, lists of dicts*). Today: loop over all of them.

## 2. Looping over a string (7 min)

**Intuition:** a string is a sequence of characters, so a `for` loop visits them one by one, like reading a word
letter by letter.

Live code (demo section 1):

```python
for letter in "Python":
    print(letter)          # P, y, t, h, o, n on separate lines
```

Vowel counter, combining Day 11's counter with `in` on a string:

```python
sentence = "Asha is learning Python"
vowels = 0
for letter in sentence.lower():
    if letter in "aeiou":
        vowels += 1
print("Vowels:", vowels)   # Vowels: 7
```

**Prediction question:** "Without `.lower()`, would the answer change?" (*Yes: the capital `A` is not in `"aeiou"`,
so it would be 6.*) Spaces are characters too; the loop visits them, the `if` just ignores them.

## 3. Lists of dicts and dict `.items()` (12 min)

**Why:** real data is usually *records*: one dict per student, product or question. A list of dicts is the most
common data shape in this course (and the Quiz Game project on Day 15 uses it).

Live code (demo section 2):

```python
students = [
    {"name": "Asha", "mark": 81},
    {"name": "Omar", "mark": 47},
    {"name": "Mei", "mark": 66},
]
for student in students:
    print(student["name"], "scored", student["mark"])
```

The loop variable `student` is a whole dict each time; use `[...]` lookups inside the body.

Then a single dict (demo section 2, attendance report). Days present out of 20:

```python
attendance = {"Asha": 19, "Bilal": 12, "Sara": 17, "Ken": 14}
for name in attendance:            # looping over a dict gives the KEYS
    print(name)
for name, days in attendance.items():   # .items() gives (key, value) pairs
    percent = days / 20 * 100
    print(f"{name:<6} {days:>2}/20  {percent:5.1f}%")
```

`for name, days in ...` is tuple unpacking (Day 07) done on every pass. Draw the pair `("Asha", 19)` being split
into two name tags.

**Prediction question:** "What does `for name in attendance:` print, names or numbers?" (*Names: looping over a
dict gives the keys.*) Mention `.values()` for "just the numbers".

## 4. `enumerate()` (6 min)

**Why:** sometimes we need the *position* too: "Question 3 of 10", a numbered list, row numbers.

```python
tasks = ["buy milk", "email Ken", "finish homework"]
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")
```

Output: `1. buy milk`, `2. email Ken`, `3. finish homework`.

**Prediction question** (demo section 3): the same loop *without* `start=1`. (*Numbering starts at 0. Computers count
from 0, humans from 1, so use `start=1` for anything people read.*)

## 5. Building a new list (7 min)

**Pattern** (it is an accumulator whose starting value is an empty list):

1. `result = []` before the loop
2. `result.append(...)` inside the loop (often inside an `if`)
3. use `result` after the loop

Live code (demo section 4): **filter** the students below 75% attendance, then **transform** prices by adding 10% tax.

```python
low_attendance = []
for name, days in attendance.items():
    if days / 20 * 100 < 75:
        low_attendance.append(name)
print(low_attendance)          # ['Bilal', 'Ken']
```

Key point: `.append()` *changes the list* and gives back nothing useful. Never write `result = result.append(x)`
(common mistakes, section 6).

## 6. Counting with a dict and finding a maximum (8 min)

**Counting (demo section 5).** Analogy: a tally sheet. The first time you see a fruit, write its name with a 1;
every next time, add a stroke.

```python
fruits = ["apple", "mango", "apple", "kiwi", "mango", "apple"]
counts = {}
for fruit in fruits:
    if fruit in counts:
        counts[fruit] += 1
    else:
        counts[fruit] = 1
print(counts)    # {'apple': 3, 'mango': 2, 'kiwi': 1}
```

Then show the one-line version using `.get(key, default)` from Day 08:
`counts[fruit] = counts.get(fruit, 0) + 1`. Read it as "the old count, or 0 if new, plus one".

**Finding the maximum manually (demo section 6).** `max(scores.values())` gives the highest value, but not *who*
has it. Use "best so far", like a judge holding the current winner's card:

```python
scores = {"Diego": 72, "Fatima": 94, "Zara": 88}
best_name = ""
best_score = -1                    # lower than any real score
for name, score in scores.items():
    if score > best_score:
        best_score = score
        best_name = name
print(best_name, best_score)       # Fatima 94
```

**Prediction question:** "What if two students tie for top score?" (*`>` keeps the first one found; `>=` would keep
the last.*)

## 7. Common mistakes (5 min)

Run the tagged cells in demo section 7:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `for name, days in attendance:` (forgot `.items()`) | `ValueError: too many values to unpack (expected 2)` | Looping over a dict gives only keys; each key is a string, not a pair |
| `counts[word] += 1` for a word not yet in `counts` | `KeyError` | You cannot add 1 to a count that does not exist yet. Use `.get(word, 0) + 1` |
| `result = result.append(x)` | `AttributeError: 'NoneType' object has no attribute 'append'` (next pass) | `.append` changes the list and returns nothing, so `result` is no longer a list |
| `best_score = 0` when all values could be negative | no error, wrong answer | Start below every possible value, or start with the first item |

## 8. Real-world example (optional, 5 min)

Demo section 8: word frequency in a short product review (`.lower()`, `.replace()` to remove commas and full stops,
`.split()`), then the most common word with the best-so-far pattern. This is exactly how a simple text-analysis
tool starts; mention that in Week 11 we will do text tasks with language models, and counting words is the
"before AI" baseline.

## 9. Practice (20 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the loops | strings, dicts, `enumerate` | recall |
| 2 Numbered shopping list | `enumerate(start=1)`, f-strings | application |
| 3 Fix the counters | `.items()`, `KeyError`, `.append` misuse | modification |
| 4 Class report | list of dicts → filtered list, grade counts | problem solving |
| 5 Word counter | counting with a dict + most common word | problem solving |
| 6 Letter bar chart (challenge) | counting letters, `sorted()`, string `*` | challenge |

While circulating, look for:
- `for name, mark in marks:` without `.items()`;
- counting dicts created *inside* the loop (same bug as yesterday's `total = 0`);
- `if letter == "aeiou"` instead of `in`;
- comparing a whole dict instead of a value (`if student > best`).

Expected outcome: everyone completes 1–3, most complete 4, many complete 5.

## 10. Recap and exit ticket (5 min)

Recap (students supply):
1. `for` works on strings (characters), lists (items) and dicts (keys; use `.items()` for pairs).
2. `enumerate(items, start=1)` gives position and item together.
3. New list: `[]` before, `.append()` inside. Count: `counts[k] = counts.get(k, 0) + 1`.
4. Maximum by hand: keep the best so far and replace it when you find something bigger.

**Exit ticket:** What does this print?

```python
counts = {}
for ch in "banana":
    counts[ch] = counts.get(ch, 0) + 1
print(counts)
```

Answer: `{'b': 1, 'a': 3, 'n': 2}` (keys appear in the order first seen).

## Homework (25 min)

Finish Exercise 5. Then: take any three sentences from a news article or book, count how many words have more than
5 letters, and build a list of those words.

## Next class

Day 13 introduces the **`while` loop**: repeat *until something happens*, when we do not know in advance how many
times. Today's loops all knew their length (the string, the list, the dict). Teaser: "How do we keep asking for a
PIN until the user types four digits?"

## Instructor notes

- Do not introduce list/dict comprehensions (Day 22), `Counter`, `zip` or `sorted(..., key=...)` (Day 21) even if
  strong students know them. Say "there is a shortcut we will learn later; today we learn what it does inside".
- Dict order: dicts keep insertion order (Python 3.7+). Say so only if a student asks why the output order matches.
- Do not modify a list while looping over it (e.g. `.remove()` inside the loop). If a student tries, show that items
  get skipped and steer them to "build a new list instead", today's pattern.
- Fast students: in Exercise 5, also ignore short words such as "the" and "a" with a list of stop words.
  Slow students: do Exercise 4 in two loops (first the passing list, then the grade counts).
