# Day 03: Numbers, Operators and Input

**Week 1 · Session 3 of 60 · Planned 75 min** · Previous: [Day 02](../day-02-variables/lesson.md) · Next: [Day 04](../day-04-strings/lesson.md)

## Objectives

By the end of this lesson students can:

1. Calculate with `+ - * / // % **` and predict the difference between `17 / 5`, `17 // 5` and `17 % 5`.
2. Use parentheses to control the order of operations (e.g. the average of three marks).
3. Update a running total with `+=`.
4. Read a value with `input()`, explain why it is always a `str`, and convert it with `int()` or `float()` (and a number back to text with `str()`).
5. Tidy a result with `round()`, and read and fix a `TypeError` (`"5" + 5`) and a `ValueError` (`int("abc")`).

**Prior knowledge (Days 01–02):** running a `.py` file with `uv run`; notebooks (Shift+Enter, last line shown
automatically); variables and `=` read right to left; `int` `float` `str` `bool`; `type()`; reassignment
(`score = score + 5`); `print` with several values separated by commas; `NameError`.

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: Day 02 retrieval | core |
| 0:05–0:12 | Arithmetic operators `+ - * / **` | core |
| 0:12–0:20 | `//` and `%`: sharing, minutes → hours, even/odd | core |
| 0:20–0:25 | Order of operations and parentheses | core |
| 0:25–0:28 | Updating with `+=` | core |
| 0:28–0:40 | `input()` and converting types | core |
| 0:40–0:43 | `round()` | core |
| 0:43–0:47 | Common errors (live debugging) | core |
| 0:47–0:50 | Real-world example: bill splitter | core |
| 0:50–0:71 | Practice exercises 1–5 | core |
| 0:71–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (challenge) together on the board | optional (90-min session) |
| +5 min | Students run their bill splitter as a `.py` file in the terminal (see Homework) | optional (90-min session) |

**60-min session:** warm-up 2 min, show `+=` with one cell only, skip demo section 9 (the bill splitter is
Exercise 5 anyway), and give 14 min of practice (Exercises 1–4; Exercise 5 becomes homework).

## 1. Warm-up (5 min)

Write on the board and ask students to answer on paper first:

```python
price = "3.5"
qty = 4
qty = qty + 2
```

- "What is the type of `price`? Of `qty`?" (*`str`, because of the quotes; `int`.*)
- "What is the value of `qty` now?" (*6. Right side first: 4 + 2.*)
- "What happens with `print(prise)`?" (*`NameError`: typo, Python only knows names we created.*)
- Hook: "Could we calculate `price * qty`?" Do not answer yet. (*It runs, but repeats the text `"3.5"` six
  times. By the end of section 6 everyone should be able to explain why and fix it with `float(price)`.*)

## 2. Arithmetic operators (7 min)

**Why:** almost every program calculates something: a total, an average, a time, a discount. Python is a
calculator that can *remember* results in variables.

Live code (demo section 1):

```python
notebook_price = 2.5
quantity = 4
print("Cost:", notebook_price * quantity)   # Cost: 10.0
```

**Prediction question:** "Does `10 / 2` give `5` or `5.0`?" (*`5.0`.*)

Key points:
- `/` **always** returns a `float`, even for a whole answer. Show `type(10 / 2)`.
- `int` and `float` mixed → `float` (`3 + 2.0` → `5.0`).
- `**` is power: `side_m ** 2` is the area of a square room, `2 ** 10` is `1024`.

## 3. Floor division and remainder (8 min)

**Intuition:** 17 sweets, 5 children. `/` says 3.4 each, but you cannot hand out 0.4 of a sweet. Real life asks
two questions: *how many whole times?* (`//`) and *how many left over?* (`%`).

Live code (demo section 2):

```python
print(17 / 5)    # 3.4
print(17 // 5)   # 3   each child gets 3
print(17 % 5)    # 2   2 sweets left over
```

Draw five groups of three circles with two left outside: with that picture students rarely mix up `//` and `%`.

**Prediction question:** "A bus journey takes 200 minutes. How many whole hours and how many minutes left over?"
Let students work it out on paper, then run: `200 minutes = 3 hours and 20 minutes`.

**Even or odd:** `number % 2` is `0` for even numbers and `1` for odd ones. We cannot *decide* anything with it
yet (that needs `if`, Day 09); today it is enough to read the remainder.

Say it explicitly: **`%` is not percent.** A 10% tip is `bill * 10 / 100`. Students who used spreadsheets will
try `bill * 10%`.

## 4. Order of operations (5 min)

Live code (demo section 3). **Prediction question first:** "Asha scored 78, 85 and 92. Is `78 + 85 + 92 / 3` her
average?" Most students say yes.

```python
78 + 85 + 92 / 3          # 193.66666666666666  only 92 was divided
(78 + 85 + 92) / 3        # 85.0
```

Order: `( )` first, then `**`, then `* / // %`, then `+ -`. Same level → left to right, so `10 - 4 - 3` is `3`,
not `9`. Rule for the course: **when in doubt, add parentheses.** They cost nothing and show what you meant.

## 5. Updating a variable with `+=` (3 min)

Connect to Day 02: `score = score + 5` (right side first). A running total is so common that Python has a
shortcut. Live code (demo section 4):

```python
cart_total = 0
cart_total += 4.5          # same as cart_total = cart_total + 4.5
cart_total += 12.0
cart_total += 3.25
print("Cart total:", cart_total)   # Cart total: 19.75
```

`-=`, `*=`, `/=`, `//=` and `%=` work the same way. Show the typo `count =+ 1` (demo section 8) later: no error,
but it sets `count` to `1`.

## 6. `input()` and converting types (12 min)

**Why:** so far every value was typed into the code. A real program asks its *user*: the same bill splitter
should work for any bill without editing the code.

Live code (demo section 5). Mock answers in the demo: `Asha`, `20`, `35`, then `72.40`, `3`, `10`.

```python
name = input("What is your name? ")
print("Hello,", name)
age_text = input("How old are you? ")
type(age_text)        # str
age_text * 2          # '2020'
```

In a notebook VS Code opens a **box at the top of the window**; the cell shows `[*]` until you press Enter.
If a cell "hangs", look for that box.

**Prediction questions:** "What type is `age_text`?" and "What does `age_text * 2` show?" `'2020'` is the key
moment of the lesson: **`input()` always returns a `str`** (the keyboard sends *characters*; text × 2 repeats it).

Now convert (demo section 6):

| Call | Result | Note |
|------|--------|------|
| `int("42")` | `42` | text → whole number |
| `float("4.75")` | `4.75` | text → decimal number |
| `str(2026)` | `'2026'` | number → text (useful when gluing text together, Day 04) |
| `int(9.99)` | `9` | cuts off decimals, does **not** round |
| `int("3.5")` | `ValueError` | `int()` cannot read a decimal point in text, so use `float()` |

Then the one-line pattern, read **inside out** (`input` runs first, `int` converts its answer):

```python
pages = int(input("How many pages did you read today? "))
print("At this pace you read", pages * 7, "pages a week")    # 245 for an answer of 35
```

Naming tip: when a variable still holds raw text, name it `age_text`; after converting, `age`. It makes the type
visible in the name. Go back to the warm-up hook: `price * qty` repeated the text; `float(price) * qty` gives `21.0`.

## 7. `round()` (3 min)

Live code (demo section 7). **Prediction question:** "What is `0.1 + 0.2`?" (*`0.30000000000000004`.*)
One sentence of explanation: computers store most decimals approximately, like 1/3 = 0.333… on paper.

```python
round(0.1 + 0.2, 2)   # 0.3
round(85.6666, 1)     # 85.7
round(7.8)            # 8   (no digits → a whole number)
```

Key point: **round at the end**, when you show the result, not in the middle of the calculation.

## 8. Common mistakes (live debugging, 4 min)

Run the cells in demo section 8 and read the **last line** of each error together.

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `"5" + 5` | `TypeError: can only concatenate str (not "int") to str` | `+` cannot mix text and a number. Maths → `int("5") + 5`; text → `"5" + str(5)` |
| `int("abc")` | `ValueError: invalid literal for int() with base 10: 'abc'` | The type is right (`str`) but the value is not a number |
| `int("3.5")` | `ValueError` | Use `float("3.5")` for decimals |
| `age_text * 2` after `input()` | none: gives `'2020'` | Forgot to convert. Check with `type()` |
| `78 + 85 + 92 / 3` | none: wrong answer | Missing parentheses |
| `count =+ 1` | none: `count` becomes `1` | The shortcut is `+=` |
| `2 ^ 3` | none: gives `1` | Power is `**` in Python |

Two lessons: **`TypeError` = wrong types combined; `ValueError` = right type, impossible value.** And the
mistakes without an error are the dangerous ones, so check one result by hand.

## 9. Real-world example: bill splitter (3 min)

Demo section 9 puts everything together (mock answers `72.40`, `3`, `10`):

```python
bill = float(input("Total bill: "))
people = int(input("Number of people: "))
tip_percent = float(input("Tip percent: "))
tip = bill * tip_percent / 100
total = bill + tip
share = total / people
print("Tip:", round(tip, 2))                 # Tip: 7.24
print("Total with tip:", round(total, 2))    # Total with tip: 79.64
print("Each person pays:", round(share, 2))  # Each person pays: 26.55
```

Ask: "Why `float` for the bill but `int` for people?" and "Why `/ 100`?" Then add `print(share)` to show
`26.546666666666667` and why we round.

## 10. Practice (21 min)

Students open `practice.ipynb`. "User input" is given as text variables marked `# pretend the user typed this`,
so cells run without waiting; Exercise 5 Step 2 switches to real `input()` calls.

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict, then check | operators, precedence, conversion | recall |
| 2 Hours, pairs and leftovers | `//` and `%` | application |
| 3 Fix the broken code | `TypeError`, `ValueError`, silent wrong answers | modification |
| 4 Temperature converter | `float()`, parentheses, `round()` | application |
| 5 Bill splitter | full program with conversion and `input()` | problem solving |
| 6 Screen-time report (challenge) | chaining `//` and `%` | challenge |

Walk around and look for:
- `hours = film_minutes / 60` → `2.25` in Exercise 2. Ask "how many **whole** hours?";
- `int(bill_text)` on `"135.80"` → `ValueError`. Ask "does the text have a decimal point?";
- `tip = bill * 15%` → `SyntaxError`;
- students who round in the middle of the calculation, or never round at all;
- an `input()` box left waiting at the top of VS Code while the student wonders why nothing runs.

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

## 11. Recap and exit ticket (4 min)

Recap (ask students to supply each line):
1. `/` gives a `float`; `//` = whole times; `%` = left over.
2. `**` first, then `* / // %`, then `+ -`; parentheses when in doubt.
3. `input()` always returns a `str`; convert with `int()` or `float()` before doing maths.
4. `TypeError` = wrong types combined; `ValueError` = text that cannot be converted.

**Exit ticket:** What does this print? Why do we need `int()`?

```python
answer = "7"            # what input() gave us
total = int(answer) * 2 + 1
print(total, 17 // 5, 17 % 5)
```

Answer: `15 3 2`. `input()` gives text; without `int()`, `answer * 2` would be `"77"` and `+ 1` would raise a
`TypeError`.

## Homework (20 min)

1. Finish Exercises 5 and 6.
2. In the Day 01 project folder (`python-class`), create `bill_splitter.py`, paste the Step 2 version of
   Exercise 5 and run `uv run bill_splitter.py`. The questions now appear in the terminal, like a real program.
3. Run it three times: a normal bill, 1 person, and `four` people typed in letters. Write down the error name
   for the last run.

## Next class

Day 04 is about **text**: joining and repeating strings (`+` and `*`, which explains today's `'2020'`), `len()`,
methods like `.upper()` `.strip()` `.replace()`, and **f-strings**, which will replace today's comma-separated
`print` calls with tidy messages such as `f"Each person pays {share}"`.

## Instructor notes

- **Floats:** one sentence ("computers store most decimals approximately") is enough. Do not explain binary.
- **`round()` and halves:** Python rounds an exact half to the even neighbour (`round(2.5)` is `2`). Examples
  avoid halves; if a student finds one, confirm it is intentional ("banker's rounding") and move on.
- **Do not teach** negative `//` and `%` (`-7 // 2` is `-4`), `divmod`, `math`, or `int()` with other bases.
- Students will ask "how do I stop the crash when someone types `four`?" Answer: "with `if` (Day 09) and
  `try/except` (Day 25). Today, learn to read the error." Do not show `try` now.
- Fast students: Exercise 6, then extend the bill splitter so it also prints how much each person pays
  *without* the tip. Slow students: make sure Exercises 2 and 3 are solid. Exercise 5 can wait for homework.
- `print` with commas is still our only output tool. f-strings found online? Praise, and say "tomorrow".
