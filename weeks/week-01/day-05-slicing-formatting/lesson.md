# Day 05: Indexing, Slicing and Formatting + Week 1 Review

**Week 1 · Session 5 of 60 · Planned 75 min** · Previous: [Day 04](../day-04-strings/lesson.md) · Next: [Day 06](../../week-02/day-06-lists/lesson.md)

## Objectives

By the end of this lesson students can:

1. Get a single character with a positive or negative index (`name[0]`, `code[-1]`) and explain an `IndexError`.
2. Extract part of a string with `[start:stop]`, knowing that `stop` is **not** included, and reverse it with `[::-1]`.
3. Format numbers in f-strings with `:.2f`, `:,`, `:<10` and `:>8` to print an aligned receipt.
4. Combine Week 1 skills (conversion, operators, string methods, slicing, f-strings) in small programs.
5. Complete Checkpoint 1.

**Prior knowledge (Days 01–04):** variables and types; operators, `input()` and conversion; `round()`; string
methods, `len()`, immutability; basic f-strings; `.find()` returns a position counted from 0.

**Files:** `demo.ipynb` · `practice.ipynb` (today = mixed Week 1 review) · `solutions.ipynb` ·
[Checkpoint 1](../../../assessments/weekly/week-01-checkpoint.md) (print one copy per student, or share it as a file)

## Timing

New content is deliberately short today (~35 min) to leave room for review and the checkpoint.

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:03 | Warm-up: one Day 04 retrieval question | core |
| 0:03–0:13 | Indexing: positive, negative, `IndexError` | core |
| 0:13–0:23 | Slicing, step and `[::-1]` | core |
| 0:23–0:35 | f-string format specs + formatted receipt | core |
| 0:35–0:55 | Mixed Week 1 practice (Exercises 1–4) | core |
| 0:55–0:58 | Checkpoint instructions | core |
| 0:58–0:73 | **Checkpoint 1** (15 min) | core |
| 0:73–0:75 | Close the week, preview Week 2 | core |
| +10 min | Go through the checkpoint answers together (after collecting papers) | optional (90-min session) |
| +5 min | Exercise 6 (challenge) on the board | optional (90-min session) |

**60-min session:** skip the warm-up, show the step only as `[::-1]`, show the receipt (demo section 7) without
live-typing it, and give 13 min of practice (Exercises 1, 2 and 4). Keep the full 15 min for the checkpoint.

## 1. Warm-up (3 min)

```python
email = "  Omar@Example.com "
email = email.strip().lower()
print(email.find("@"), len(email))
```

Answer: `4 16`. Use it as the bridge: "`.find()` told us the `@` is at **position 4**. Today we use positions to
*take out* parts of a string, like the name before the `@`."

## 2. Indexing (10 min)

**Intuition:** a string is a row of numbered boxes, one character per box, and the numbering starts at **0**.
Draw this on the board and leave it up all lesson:

```
 P    Y    T    H    O    N
 0    1    2    3    4    5
-6   -5   -4   -3   -2   -1
```

> **Analogy:** floors in a building where the ground floor is 0. "Index 0" is "no steps from the start".
> Negative indexes count from the end: `-1` is the last character, whatever the length.

Live code (demo section 1):

```python
word = "PYTHON"
word[0]           # 'P'
word[3]           # 'H'
word[-1]          # 'N'
f"Initials: {first_name[0]}.{last_name[0]}."    # Initials: F.K.
```

**Prediction questions:** "What is `word[-1]`?" and "What happens with `word[6]`?" (*`IndexError: string index
out of range`. The last index is `len(word) - 1`.*)

Mixed retrieval in the ticket example: `ticket[-1]` is `'3'`, still a `str`, so `int(ticket[-1]) % 2` tells us
the last digit is odd (Day 03).

## 3. Slicing (10 min)

**Rule:** `text[start:stop]` takes characters from `start` up to **but not including** `stop`. The slice has
`stop - start` characters.

> **Analogy:** `stop` is a fence. You walk up to it but do not climb over. This is also why `[0:4]` gives exactly
> 4 characters.

Live code (demo sections 2–3):

```python
word[0:3]          # 'PYT'
word[:2]           # 'PY'     start left out = from the beginning
word[2:]           # 'THON'   stop left out = to the end
date_text = "2026-10-16"
date_text[:4]      # '2026'   then [5:7] → '10' and [8:] → '16'
"sales_report.csv"[-3:]                         # 'csv'
"sales_report.csv"[:-4]                         # 'sales_report'
word[::2]          # 'PTO'    every 2nd character
word[::-1]         # 'NOHTYP' reversed
```

**Prediction questions:** "`word[2:5]`?" (*`'THO'`*) · "`word[0:100]`, error or not?" (*No error: slices stop at
the end, only single indexes raise.*) · "`"stressed"[::-1]`?" (*`'desserts'`*)

Tie back to Day 04 (demo section 4): `word[0] = "J"` raises `TypeError: 'str' object does not support item
assignment`. Strings are immutable, so build a new one: `"J" + word[1:]`.

## 4. Formatting numbers (12 min)

**Why:** on Day 03 the bill splitter printed `Bill: 135.8` and we used `round()`. Money should always show two
decimals, and columns of numbers should line up.

Live code (demo section 5). After the value, a colon starts the **format spec**:

```python
price = 1234.5
f"{price:.2f}"       # '1234.50'    2 decimal places
f"{price:,}"         # '1,234.5'    thousands separator
f"{price:,.2f}"      # '1,234.50'
f"{share:.2f}"       # '26.55'      share = 26.546666666666667, unchanged
f"[{'Tea':<10}]"     # '[Tea       ]'  left-aligned in 10 characters
f"[{4.5:>8.2f}]"     # '[    4.50]'    right-aligned in 8
```

Key points:
- `:.2f` rounds **for display only**: the variable keeps all its decimals. `round()` gives a number; a format
  spec gives text.
- Text usually goes left (`<`), numbers right (`>`). Same width + same decimals → the decimal points line up.
- A literal text inside the braces needs the *other* kind of quotes: `f"{'Tea':<10}"`.

Then show the common mistakes (demo section 6) and the receipt (demo section 7): three items, line totals,
subtotal, 8% tax and total, aligned to 32 characters. Point out "16 + 4 + 12 = 32" and that nine variables for
three items is painful: **lists next week** fix that.

## 5. Common mistakes

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `word[6]` on a 6-letter word | `IndexError: string index out of range` | Last index is `len(word) - 1` |
| `date_text[0:3]` for the year | none: gives `'202'` | `stop` is not included: `[0:4]` |
| `city[1]` for the first letter | none: second letter | Counting starts at 0 |
| `word[0] = "J"` | `TypeError: 'str' object does not support item assignment` | Strings are immutable: `"J" + word[1:]` |
| `f"{price_text:.2f}"` on a `str` | `ValueError: Unknown format code 'f' for object of type 'str'` | Still text from `input()`: `float()` first |
| `f"{price:.2}"` | none: `1.2e+03` | The `f` in `.2f` means "fixed decimals" |

## 6. Mixed Week 1 practice (20 min)

Today's practice notebook is the **weekly review**: every exercise mixes Day 05 with earlier days.

| Exercise | Skills | Days | Level |
|----------|--------|------|-------|
| 1 Predict, then check | indexing, slicing, `IndexError` | 05 | recall |
| 2 Extract the parts | slicing fixed layouts, `int()` | 03, 05 | application |
| 3 Week 1 bug hunt | `NameError`, `ValueError`, `TypeError`, immutability, slice stop, format spec | 02–05 | modification |
| 4 Café receipt | conversion, arithmetic, `.strip().title()`, alignment, `:.2f` | 03–05 | application |
| 5 Student name card | `.find()` + indexing, slicing, methods, arithmetic | 03–05 | problem solving |
| 6 Hide and shorten (challenge) | `*` + `len()`, slicing, `:,` | 04–05 | challenge |

Walk around and look for:
- off-by-one: `[4:7]` instead of `[4:8]` for a 4-digit year;
- quantities still text in Exercise 4 (`TypeError: can't multiply sequence by non-int of type 'float'`);
- `name[space]` instead of `name[space + 1]` in Exercise 5;
- students who skip writing down the error name in Exercise 3: reading errors is part of the checkpoint.

Expected outcome: everyone completes 1–3; most complete 4. Exercises 5–6 are weekend homework for anyone who
does not finish.

## 7. Checkpoint 1 (3 + 15 min)

Use [assessments/weekly/week-01-checkpoint.md](../../../assessments/weekly/week-01-checkpoint.md): print the
part above the `---` line only (the answer key is below it).

Instructions to read out:
- 15 minutes, individual, on paper (or in a fresh notebook with **no running of code**: the skill being
  checked is *predicting*).
- Closed notes. If unsure, write your best guess and one sentence of reasoning: partial credit exists.
- Questions 9–10 revisit Days 01–02.

Collect papers. Mark with the 10-point guide in the answer key. Students scoring **below 6** need a short catch-up
before Day 06 (lists build directly on indexing and slicing). Note the most-missed question for Monday's warm-up.

## 8. Close the week (2 min)

Week 1 in one sentence each: run Python (Day 01), store values (Day 02), calculate with input (Day 03), work with
text (Day 04), pick out parts and format output (Day 05). Next week: **lists, dictionaries and decisions**. The
bill splitter and the receipt will finally be able to *decide* things (`if`) and hold many items (lists).

## Homework (30 min, over the weekend)

1. Finish practice Exercises 4–5 (and 6 if you like a challenge).
2. Make your receipt from Exercise 4 a program: save it as `receipt.py` in your `python-class` folder, ask for
   the three quantities with `input()`, and run it with `uv run receipt.py`.

## Next class

[Day 06](../../week-02/day-06-lists/lesson.md): **lists**. Everything from today carries over: `marks[0]`,
`marks[-1]`, `marks[1:3]` and `len(marks)` work on lists exactly as on strings. Start Monday with the
checkpoint's most-missed question as the warm-up.

## Instructor notes

- **Keep new content to 35 minutes.** If indexing takes longer, show slicing with step only as `[::-1]` and keep
  the receipt as a demo. Do not cut practice below 13 minutes or the checkpoint below 15.
- **Do not introduce** lists, `.split()`, `in`, `if` or loops, even though Exercise 6 "wants" an `if`. Name
  the need ("we'll be able to decide that on Day 09") and move on.
- **Format specs:** stay with `.2f`, `,`, `<`, `>` and a width. Centring (`^`), padding with zeros and
  percentages exist; mention them only if asked.
- Slicing with negative steps other than `-1` (e.g. `[5:1:-1]`) confuses beginners. Skip it.
- During the checkpoint, walk around but do not hint. Note common errors for the answer review.
- Fast students during practice: Exercise 6, then the `.find(".")` version of the file type (in the solutions).
  Slow students: make sure Exercises 1 and 3 are done before the checkpoint: they are the best preparation.
