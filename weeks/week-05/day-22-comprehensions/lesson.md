# Day 22: Comprehensions

**Week 5 · Session 22 of 60 · Planned 75 min** · Previous: [Day 21](../day-21-built-in-functions/lesson.md) · Next: [Day 23](../day-23-reading-files/lesson.md)

## Objectives

By the end of this lesson students can:

1. Rewrite a *start empty → loop → append* block as a list comprehension and read one aloud.
2. Add an `if` filter at the end of a comprehension to keep only some items.
3. Build a dictionary with a dict comprehension, using `zip()` or `.items()` inside it.
4. Decide whether a comprehension or a normal loop is clearer, and move complicated logic into a named function.
5. Recognise and fix the three most common comprehension syntax errors.

**Prior knowledge:** building a list with `.append` in a loop and looping over `.items()` (Day 12), truthiness
(Day 09), `.split()` (Day 07), functions that return values (Day 17), `zip()`, `all()`, `.isdigit()` (Day 21).

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: the build-a-list loop | core |
| 0:05–0:20 | List comprehensions (transform) | core |
| 0:20–0:30 | Filtering with `if` | core |
| 0:30–0:38 | Dict comprehensions | core |
| 0:38–0:46 | When a normal loop is clearer | core |
| 0:46–0:50 | Common mistakes (live debugging) | core |
| 0:50–0:53 | Real-world example: sign-up clean-up | optional (skip for 60 min) |
| 0:53–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +15 min | Exercise 6 (challenge) and the loop-vs-comprehension discussion | optional (90-min session) |

**For 60 min:** skip demo section 7, show only two of the three common mistakes, and set Exercise 5 as homework.

## 1. Warm-up (5 min)

On the board, without a computer: "Write a loop that turns `["  asha ", "BILAL", "sara  ", "mEI"]` into
`['Asha', 'Bilal', 'Sara', 'Mei']`." Then show demo section 1.

Ask students to name the **three parts** of the pattern: (1) create an empty list, (2) loop, (3) append a
transformed item. Underline the expression inside `.append(...)`, because that is the part we keep.

Retrieval question: "What does `.strip().title()` do, and why can we chain them?" (*`strip` returns a new
string, and `title` is called on that new string, so they run left to right; Day 04.*)

## 2. List comprehensions (15 min)

**Why:** the build-a-list pattern is so common that Python has a short form for it. Shorter code is not the goal
in itself. The goal is code that says *what* it builds in one sentence.

```python
clean_names = [name.strip().title() for name in raw_names]
# ['Asha', 'Bilal', 'Sara', 'Mei']
```

Draw the mapping (it is also in demo section 2):

```
clean_names = []
for name in raw_names:                         ─┐
    clean_names.append(name.strip().title())  ─┐│
                                               ▼▼
clean_names = [ name.strip().title()   for name in raw_names ]
                └── what to keep ──┘   └──── the loop ────┘
```

**Read it aloud** every time: "name-strip-title, *for each* name *in* raw_names". Students who say it aloud make far
fewer syntax mistakes.

**Prediction question** (demo section 2, 🤔): `[n * 2 for n in [1, 2, 3]]` → `[2, 4, 6]`;
`[len(word) for word in ["hi", "hello", "hey"]]` → `[2, 5, 3]`; `[letter.upper() for letter in "abc"]` →
`['A', 'B', 'C']` (a string is a collection of characters, Day 12).

Two practical one-liners:

```python
[c * 9 / 5 + 32 for c in [18, 22.5, 30, -4]]     # [64.4, 72.5, 86.0, 24.8]
[int(part) for part in "12,7,30".split(",")]     # [12, 7, 30]
```

The second one fixes yesterday's `sum(["12", "30", "8"])` error. Tomorrow we read numbers from files as text, so
this conversion becomes a daily tool.

Key points:
- Square brackets mean "the result is a list".
- The loop variable (`name`, `c`, `part`) only exists inside the comprehension. Give it a meaningful name, just as
  in a loop.
- The original list is not changed; a new list is created.

## 3. Filtering with `if` (10 min)

**Analogy:** a bouncer at the door. Each item walks up, and the `if` decides whether it gets into the new list.

```python
marks = [78, -5, 91, 105, 64, 0, 88]
valid_marks = [mark for mark in marks if mark >= 0 and mark <= 100]
# [78, 91, 64, 0, 88]
```

Anatomy: `[ keep this   for item in collection   if this is True ]`. The filter **always goes at the end**.

**Prediction question:** `[fruit for fruit in ["apple", "kiwi", "fig", "banana"] if len(fruit) > 3]` →
`['apple', 'kiwi', 'banana']`.

Transform **and** filter at once, which is very common with user input:

```python
entries = ["12", "abc", "7", "", "30"]
[int(entry) for entry in entries if entry.isdigit()]    # [12, 7, 30]
```

Order of work: the `if` is checked **first**, and only items that pass are transformed. That is why `int("abc")`
never runs. Ask students: "What would happen without the `if`?" (*`ValueError` on `"abc"`.*)

Close the loop with Day 21: `all([mark >= 50 for mark in valid_marks])` → `False` (the 0);
`any([mark > 90 for mark in valid_marks])` → `True`.

## 4. Dict comprehensions (8 min)

Curly brackets plus `key: value` build a dictionary:

```python
{name: len(name) for name in ["Asha", "Bilal", "Mei"]}        # {'Asha': 4, 'Bilal': 5, 'Mei': 3}
{name: score for name, score in zip(names, [88, 75, 93])}    # {'Asha': 88, 'Bilal': 75, 'Mei': 93}
```

With `.items()` we can filter or change an existing dictionary (demo section 4):

```python
cheap = {item: price for item, price in prices.items() if price < 10}
# {'apple': 0.5, 'pen': 1.2}
on_sale = {item: round(price * 0.9, 2) for item, price in prices.items()}
```

**Prediction question:** `{word: len(word) for word in ["hi", "hello", "hi"]}` → `{'hi': 2, 'hello': 5}`. Only two
entries, because **keys are unique** (Day 08), so the second `"hi"` overwrites the first.

## 5. When a normal loop is clearer (8 min)

This is the most important judgement of the day. Show the "works but unreadable" line in demo section 5:

```python
clean = [p.strip().lower().replace("-", " ").title() for p in raw_products if p.strip() != "" and not p.strip().isdigit()]
```

Ask: "What does this do?" Let students struggle for 20 seconds, then show the refactor with two small named
functions (`clean_product`, `is_product_name`):

```python
clean = [clean_product(p) for p in raw_products if is_product_name(p)]
# ['Usb Cable', 'Laptop Stand', 'Mouse Pad']
```

This is Week 4 decomposition paying off: **a comprehension that calls well-named functions reads like a sentence.**
The same goes for `if/elif/else` decisions: put them in `letter_grade(mark)` and write
`[letter_grade(mark) for mark in valid_marks]`.

**Prediction question:** `result = [print(name) for name in names]`: what is in `result`? (*The names are printed,
and `result` is `[None, None, None]`, because `print` returns `None`.*) Memorable rule:
**comprehensions build values; loops do actions.**

Rules to write on the board:

| Use a comprehension when… | Use a normal loop when… |
|---------------------------|-------------------------|
| you build a new list/dict from another collection | you print, save a file, or ask for input |
| one transform and at most one `if` | you need `elif`/`else`, `break`, or several steps |
| it fits on one line you can read aloud | you update something else: a total, a counter dict |

## 6. Common mistakes (live debugging, 4 min)

Run the tagged cells in demo section 6:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `[mark if mark >= 50 for mark in marks]` | `SyntaxError: expected 'else' after 'if' expression` | An `if` before `for` looks like a different kind of expression to Python. **Filter `if` goes at the end** |
| `{name, len(name) for name in names}` | `SyntaxError: did you forget parentheses around the comprehension target?` | A dict needs `key: value`, a colon |
| `[student.title() for s in students]` | `NameError: name 'student' is not defined` | The expression must use the loop variable's name |
| missing `]` | `SyntaxError: '[' was never closed` | Count your brackets |

Notebook warning: if the "wrong" name happens to exist from an earlier cell, there is **no error**, just a list
full of that old value. Another reason to use distinct, meaningful loop variable names.

## 7. Real-world example: cleaning sign-up data (3 min, optional)

Demo section 7 cleans a messy form export in four short lines: names (strip + title + drop blanks), marks (only
digits, then only ≤ 100), Celsius → Fahrenheit, then a username dictionary and a "passed" list from `.items()`.

```
['Asha Khan', 'Bilal Ahmed', 'Sara Ali', 'Mei Chen']
[78, 91, 64]
[54.5, 86.0, 28.4, 69.8]
```

Point out that the marks are filtered in **two named steps** rather than one long line.

## 8. Practice (17 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the output | reading comprehensions, truthiness filter | recall |
| 2 Loop → comprehension | converting the append pattern | application |
| 3 Filter it | `if` at the end, `isdigit` + `int` | application |
| 4 Fix the broken code | the four common syntax/name errors | modification |
| 5 Data clean-up one-liners | list + dict comprehensions on realistic data | problem solving |
| 6 Survey cleaner (challenge) | comprehension vs loop for counting; judging readability | challenge |

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

While circulating, look for:
- a colon left at the end: `[x for x in items:]`;
- filtering on `name != ""` without stripping, which lets `"   "` through (Exercise 5a);
- square brackets where a dict was asked for (Exercise 5d);
- students who write everything as one giant comprehension. Ask them to read it aloud in one breath.

## 9. Recap and exit ticket (5 min)

Recap (students supply the endings):
1. `[expression for item in collection]` replaces *empty list → loop → append*.
2. The filter `if` goes **at the end**.
3. `{key: value for ...}` builds a dictionary.
4. Comprehensions build values; loops do actions.

**Exit ticket:** rewrite as one line, then say what it prints.

```python
words = ["Data", "", "AI", "python", ""]
result = []
for word in words:
    if word != "":
        result.append(word.lower())
print(result)
```

Answer: `result = [word.lower() for word in words if word != ""]` → `['data', 'ai', 'python']`.

## Homework (20 min)

Finish Exercise 5. Then find one build-a-list loop in your Hangman project (Day 20), for example collecting the
letters of the secret word that have not been guessed yet, and decide: comprehension or loop? Rewrite it if a
comprehension is clearer, and write one sentence justifying your choice.

## Next class

Day 23: **reading text files**. Every line of a file arrives as text with a `\n` at the end, so tomorrow we will
constantly write things like `[line.strip() for line in lines if line.strip() != ""]` and `int(...)` conversions.
Today's filters are exactly what we need.

## Instructor notes

- **Do not teach** nested comprehensions, set comprehensions, generator expressions (round brackets), or the
  conditional expression `x if condition else y`. If a strong student asks about the `else` in the error message,
  show it privately; for the class, "put decisions in a function" is the rule.
- `map()`, `filter()` and `lambda` are out of scope. Comprehensions replace them in this course.
- A trap worth mentioning to strong students: if you filter two parallel lists **separately** (e.g. drop bad marks
  but keep all names), `zip()` will pair the wrong items afterwards. Filter pairs, not separate lists.
- Slow students: let them write the loop first, then translate line by line using the board mapping. That is a
  legitimate strategy, not cheating.
- Fast students: Exercise 6, then ask them to explain *why* `sorted(set(...))` is needed for a predictable output.
- Avoid the word "Pythonic" as a justification. Readability for the next person is the argument.
