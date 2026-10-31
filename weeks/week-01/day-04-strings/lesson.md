# Day 04: Strings and String Operations

**Week 1 · Session 4 of 60 · Planned 75 min** · Previous: [Day 03](../day-03-numbers-input/lesson.md) · Next: [Day 05](../day-05-slicing-formatting/lesson.md)

## Objectives

By the end of this lesson students can:

1. Write strings with single, double and triple quotes (choosing quotes so an apostrophe works) and use `\n` and `\t`.
2. Join strings with `+`, repeat them with `*` and count characters with `len()`.
3. Clean and transform text with `.strip() .lower() .upper() .title() .replace()`, and search it with `.count() .find() .startswith() .endswith()`.
4. Explain why `name.upper()` does not change `name`, and keep a result by reassigning (`name = name.upper()`).
5. Build messages with f-strings, including an expression inside the braces (`f"{qty * price}"`).

**Prior knowledge (Days 01–03):** variables, `str` vs numbers, `type()`, reassignment; `input()` returns a `str`;
`int()` `float()` `str()`; `TypeError` from `"5" + 5`; `print` with commas.

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: Day 03 retrieval | core |
| 0:05–0:12 | Making strings: quotes, `\n`, `\t`, triple quotes | core |
| 0:12–0:18 | `+`, `*` and `len()` | core |
| 0:18–0:28 | Methods that change text | core |
| 0:28–0:34 | Methods that search text | core |
| 0:34–0:38 | Strings never change (immutability) | core |
| 0:38–0:45 | f-strings | core |
| 0:45–0:48 | Common mistakes (live debugging) | core |
| 0:48–0:51 | Real-world example: username generator | core |
| 0:51–0:71 | Practice exercises 1–5 | core |
| 0:71–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (challenge) together, then the "two spaces in the middle" edge case | optional (90-min session) |
| +5 min | Students turn Exercise 5 into `username.py` and run it with `uv run` | optional (90-min session) |

**60-min session:** warm-up 2 min, show triple quotes only briefly, skip `.startswith()` in the demo (it is in
Exercise 1), skip demo section 8 (Exercise 5 is the same program), and give 15 min of practice (Exercises 1–4).

## 1. Warm-up (5 min)

On the board, students answer on paper:

```python
answer = "8"           # what input() gave us
print(int(answer) + 2)
print(answer * 2)
print(17 % 5)
```

Answers: `10`, `88`, `2`. Ask: "Which would crash, `answer + 2` or `int(answer) + 2`?" (*`answer + 2`, a
`TypeError`.*) Then: "Why did `answer * 2` give `88` and not an error?" Leave it open: today explains it.

## 2. Making strings (7 min)

**Why:** most data people type is text: names, emails, addresses, messages, reviews. Before we can analyse text
we need to write it correctly and clean it.

Live code (demo section 1):

```python
place = "Mei's cafe"                     # double quotes, so the apostrophe is fine
print("Name:\tAsha\nCity:\tLahore")      # two lines, values lined up by a tab
```

Key points:
- `'...'` and `"..."` make the **same** kind of string. Choose the one that does not appear inside the text.
- A backslash starts an **escape sequence**: `\n` = new line, `\t` = tab. Two characters in the code, one in the string.
- Triple quotes `"""..."""` let a string span several lines (a menu, a message, a poem).

**Prediction question:** "How many lines does `print("Name:\tAsha\nCity:\tLahore")` print?" (*Two.*)

## 3. Joining, repeating and measuring (6 min)

Live code (demo section 2):

```python
first_name = "Mei"
last_name = "Lin"
print(first_name + last_name)              # MeiLin
full_name = first_name + " " + last_name   # Mei Lin
print("-" * 20)                            # --------------------
len(full_name)                             # 7
```

**Prediction questions:** "How do we get a space between the names?" and "Is `len(full_name)` 6 or 7?" (*7: the
space is a character.*)

Close the warm-up loop: text times a number **repeats** the text, so `"8" * 2` is `"88"` and Day 03's
`"20" * 2` was `"2020"`. And `+` only joins **two strings**: `"Age: " + 20` is a `TypeError` (Day 03).

## 4. Methods that change text (10 min)

**Intuition:** a **method** is a tool that belongs to a value. You write the value, a dot, the tool's name and
parentheses: `city.upper()`. Compare with `len(city)`, which is a function written *around* the value. Students
will mix these up; say it out loud.

Live code (demo section 3):

```python
city = "  kArAcHi "
city.strip()      # 'kArAcHi'    spaces removed at both ends (not in the middle)
city.upper()      # '  KARACHI '
city.lower()      # '  karachi '
city.title()      # '  Karachi '
"0300-123-4567".replace("-", "")   # '03001234567'
city.strip().title()               # 'Karachi'
```

Key points:
- `.strip()` is the most useful method of the day: users type stray spaces all the time.
- **Chaining** runs left to right: first `strip`, then `title`. Read the dots like "and then".
- `.replace(old, new)` replaces **every** occurrence.

## 5. Methods that search text (6 min)

Live code (demo section 4):

```python
sentence = "the cat sat on the mat"
sentence.count("at")            # 3
sentence.find("sat")            # 8    position where it starts, counting from 0
sentence.find("dog")            # -1   not found (no error!)
"omar@example.com".endswith(".com")          # True
"report_october.pdf".startswith("report")    # True
```

Key points:
- `.find()` returns a **position**, and positions start at **0**. Do not explain more; it is tomorrow's topic.
- `.startswith()` and `.endswith()` return a `bool` (Day 02), a yes/no answer. On Day 09 we will use such answers
  to make decisions.
- Strings are **case-sensitive**. **Prediction question:** "How many p's in `"Python"`?" (*`0`. Lowercase first:
  `"Python".lower().count("p")` is `1`.*)

## 6. Strings never change (4 min)

Live code (demo section 5). **Prediction question:** "What does the last line print?"

```python
name = "zara"
name.upper()
print(name)          # zara
```

Explain: `.upper()` builds a **new** string `'ZARA'` and returns it. Nobody kept it, so it is lost. The original
string cannot be changed: strings are **immutable**. To keep the result, reassign: `name = name.upper()`.

> **Analogy:** a method is a photocopier with filters. You put the original in, and you get a *changed copy*
> back. The original stays as it was. If you want the copy, pick it up (give it a name).

This connects to Day 02's name tags: `name = name.upper()` moves the tag `name` onto the new string.

## 7. f-strings (7 min)

**Why:** show the problem first (demo section 6):

```python
print("Hello,", name, "!")                 # Hello, Zara !       (unwanted space)
print("Total: " + str(total) + " each")    # works, but needs str() and many +
```

The fix: put `f` before the opening quote and variables inside `{ }`:

```python
print(f"Hello, {name}!")                            # Hello, Zara!
print(f"{quantity} x {item} = {quantity * price}")  # 3 x notebook = 7.5
print(f"{item.upper()} has {len(item)} letters")    # NOTEBOOK has 8 letters
```

Key points:
- Anything inside `{ }` is **evaluated** as Python: variables, maths, method calls. Numbers need no `str()`.
- The result is an ordinary string, so it can be stored: `receipt_line = f"{quantity} x {item}"`.
- From today on, f-strings are our standard way to build messages.

**Prediction question:** "What does `print("Welcome, {student}!")` show?" (*The braces literally: the `f` is missing.*)

## 8. Common mistakes (live debugging, 3 min)

Run demo section 7.

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `'It's sunny'` | `SyntaxError: unterminated string literal` | The apostrophe closes the string. Use `"It's sunny"` |
| `"Age: " + 20` | `TypeError: can only concatenate str (not "int") to str` | `f"Age: {age}"` or `str(age)` |
| `word.len()` | `AttributeError: 'str' object has no attribute 'len'` | `len` is written around the value: `len(word)` |
| `"Welcome, {student}!"` | none: braces printed | Missing `f` |
| `nickname.strip()` alone | none: spaces still there | Keep the result: `nickname = nickname.strip()` |
| `name.upper` (no parentheses) | none: shows `<built-in method upper ...>` | Parentheses *run* the method |

## 9. Real-world example: username and email generator (3 min)

Demo section 8 (mock answer `"  bilal RAZA "`):

```python
full_name = input("Full name: ")
display_name = full_name.strip().title()
username = full_name.strip().lower().replace(" ", ".")
email = f"{username}@student.example.com"
print(f"Welcome, {display_name}!")       # Welcome, Bilal Raza!
print(f"Username: {username}")           # Username: bilal.raza
print(f"Email: {email}")                 # Email: bilal.raza@student.example.com
```

Ask: "What would happen if we did `.replace` **before** `.strip`?" (*The outer spaces become dots:
`..bilal.raza.`.*) Order matters in a chain.

## 10. Practice (20 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict, then check | operators and methods on strings | recall |
| 2 Clean up messy input | `.strip()` `.title()` `.lower()` `.replace()`, `len()` | application |
| 3 Fix the broken code | quotes, `TypeError`, immutability, missing `f`, `len()` | modification |
| 4 Review inspector | `.count()` `.find()` `.endswith()` `.replace()` on cleaned text | application |
| 5 Username and email generator | chaining methods, f-strings | problem solving |
| 6 Name badge (challenge) | `*` with `len()`, `\n` | challenge |

Walk around and look for:
- cleaned values that are printed but never stored (then `len()` gives the old length);
- `"_" + birth_year` → `TypeError` in Exercise 5;
- quote clashes inside f-strings, e.g. `f"{text.count("great")}"`. Python 3.12+ accepts it, but suggest single
  quotes inside or a separate variable: it is easier to read and works in every version;
- `"*" * len(name) + 4` → `TypeError` in Exercise 6 (precedence, Day 03).

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

## 11. Recap and exit ticket (4 min)

Recap (ask students to supply each line):
1. Quotes: pick `'` or `"` to avoid clashes; `\n` new line, `\t` tab.
2. `+` joins, `*` repeats, `len()` counts characters (spaces too).
3. Methods return a **new** string; keep it with `x = x.method()`.
4. f-strings: `f"... {value} ..."`, and anything inside braces is evaluated.

**Exit ticket:** What does this print?

```python
city = "  dubai "
city.upper()
city = city.strip().title()
print(f"{city} has {len(city)} letters")
```

Answer: `Dubai has 5 letters`. Line 2 changes nothing because its result is not kept.

## Homework (20 min)

1. Finish Exercises 5 and 6.
2. Write a "message of the day" in a new notebook cell: store your name, a city and a number of hours studied in
   variables, then print **three** lines with one f-string each, using at least two methods and one calculation.

## Next class

Day 05: **indexing and slicing** (`name[0]` for an initial, `email[-4:]` for an ending, `word[::-1]` to reverse)
and **f-string formats** (`{price:.2f}`, alignment) to print a neat receipt. `.find()` returning `8` today is a
preview: tomorrow we learn what positions are. Day 05 also has mixed practice and **Checkpoint 1** on Days 01–05.

## Instructor notes

- **Do not introduce** indexing, slicing or `.split()` today, even though they would make the username generator
  "better" (initials, middle names). Indexing is tomorrow; `.split()` comes with lists on Day 07.
- **Escape sequences:** `\n`, `\t`, `\'` are enough. Windows paths like `"C:\new"` (where `\n` is a newline)
  only matter for files in Week 5.
- **`.title()` quirks:** `"o'neil".title()` gives `O'Neil` and `"mcdonald".title()` gives `Mcdonald`. Mention only
  if someone finds it: real names are messy, and no single method handles all of them.
- **f-string details:** format specs (`:.2f`) are tomorrow. Avoid nested quotes in demos.
- `.find()` vs `.index()`: only `.find()` today (it returns `-1` instead of crashing).
- Fast students: Exercise 6, then make Exercise 5 work for `"zara  ahmed"` (two spaces in the middle) using a
  second `.replace()`. Slow students: Exercises 2 and 3 matter most; Exercise 5 can be homework.
