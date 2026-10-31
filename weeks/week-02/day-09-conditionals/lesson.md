# Day 09: Booleans, Comparisons and Conditionals

**Week 2 · Session 9 of 60 · Planned 75 min** · Previous: [Day 08](../day-08-dicts-sets/lesson.md) · Next: [Day 10](../day-10-decisions-practice/lesson.md)

## Objectives

By the end of this lesson students can:

1. Write comparisons with `== != < > <= >=`, and explain the difference between `=` and `==`.
2. Write `if`, `if/else` and `if/elif/else` blocks with correct colons and indentation.
3. Trace which branch runs for a given value, and explain why the order of `elif` branches matters.
4. Combine conditions with `and`, `or`, `not`, and avoid the `day == "Sat" or "Sun"` trap.
5. Use a nested `if` and the truthiness of empty values (`""`, `[]`, `{}`, `0`).
6. Build a grade calculator that validates its input.

**Prior knowledge (Days 02–08):** `bool` (Day 02), `%` and `input()` + `int()/float()` (Day 03), `.strip()` and
`.lower()` (Day 04), `in` on lists (Day 06) and dicts (Day 08), `.get()` and `KeyError` (Day 08).

**New today besides the roadmap list:** `bool(...)` as a conversion (to show truthiness) and chained comparisons
such as `0 <= score <= 100`.

**Files:** `demo.ipynb` (you, projected; the last cell calls `input()`) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: booleans we already have | core |
| 0:05–0:13 | Comparison operators; `=` vs `==`; text vs numbers | core |
| 0:13–0:20 | `if` and indentation; `if/else` | core |
| 0:20–0:30 | `if/elif/else`; order matters | core |
| 0:30–0:38 | `and`, `or`, `not`; the `or "Sun"` trap | core |
| 0:38–0:42 | Nested `if` | core |
| 0:42–0:46 | Truthiness | core (cut first for 60 min) |
| 0:46–0:50 | Common mistakes + grade calculator with `input()` | core |
| 0:50–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (challenge) traced together | optional (90-min session) |
| +5 min | Students swap grade calculators and try to break each other's with test values | optional (90-min session) |

**For 60 min:** skip truthiness (demo section 7; Exercise 6 is the only exercise that needs it) and the nested
`if` example, and set Exercises 1–4 in class.

## 1. Warm-up (5 min)

Demo section 0: `"Sara" in class_list`, `"rulers" in stock`, `type(True)`. Students have been producing `True` /
`False` since Day 06 but could only print it. Ask: "Yesterday we kept saying *check with `in` first*. What would
we want the program to do with the answer?" (*Look the value up only if it is there, otherwise print a message.*)
That is today.

## 2. Comparisons (8 min)

Live code (demo section 1) and put the operator table on the board.

```python
score = 72
score >= 50     # True
score == 100    # False
score != 100    # True
```

Key teaching points:
- **`=` attaches a name, `==` asks a question.** Read `==` aloud as "is equal to?" with a rising voice.
- Text comparison is exact: `"Asha" == "asha"` is `False`. Clean user text first: `answer.strip().lower() == "yes"`.
- `input()` gives text: `"18" >= 16` → `TypeError: '>=' not supported between instances of 'str' and 'int'`.
  Convert first: `int(age_text) >= 16`. (`"5" == 5` does not error; it is just `False`, which is sneakier.)

**Prediction question:** `print(10 > 9, 3 <= 3, "Asha" == "asha")` → `True True False`.

## 3. `if` and `if/else` (7 min)

**Analogy:** a gate. The condition is the guard's question; the indented block is the path behind the gate. Code
back at the left edge is the road after the gate, which everyone walks on.

```python
temperature = 37
if temperature > 35:
    print("Heat warning: drink water!")
print("Forecast done.")
```

Point at the three parts: the `if` line, the **colon**, the **indented block** (4 spaces; VS Code indents for you
after the colon). **Prediction question:** run again with `temperature = 30` (demo section 2). Only
`Forecast done.` prints.

`if/else` (demo section 3): exactly one of the two blocks runs. Then even/odd with `% 2 == 0` as a Day 03 callback.

## 4. `if/elif/else` and order (10 min)

Write the grade boundaries on the board: A ≥ 85 · B ≥ 70 · C ≥ 55 · D ≥ 40 · otherwise F. Live code demo section 4.

Trace `score = 78` out loud: "Is 78 >= 85? No. Is 78 >= 70? Yes → B. **Stop.** The rest are skipped."

**Prediction question:** the reversed-order version (demo section 4, second cell). Most students say B. It prints
**D**, because `78 >= 40` is the first true condition. No error message, just a wrong answer.

Rule for the board: **with `>=` chains, put the highest boundary first.** And: each `elif` may assume every
condition above it was false. That is why `elif score >= 70` does not need `and score < 85`.

## 5. `and`, `or`, `not` (8 min)

Table from demo section 5. Everyday wording helps: `and` = "both", `or` = "at least one", `not` = "the opposite".

```python
age < 18 or is_student            # True for a 20-year-old student
order_total >= 50 and city == "Lahore"
0 <= score <= 100                 # chained form of score >= 0 and score <= 100
```

**Prediction question (the trap):** `day = "Mon"`, `if day == "Sat" or "Sun":` → prints `Weekend!`. Explain:
Python reads `(day == "Sat") or ("Sun")`, and the text `"Sun"` on its own counts as true (section 7 shows why).
Fix: a full comparison on **each** side of `or`, or `day in ["Sat", "Sun"]`.

When mixing `and` and `or`, tell students to **always add brackets** (Exercise 5 needs it).

## 6. Nested `if` (4 min)

Demo section 6: a library loan using a dict.

```python
if title in catalogue:
    if catalogue[title] > 0:
        ...borrow...
    else:
        ...on loan...
else:
    ...not stocked...
```

Two points: indentation shows which `else` belongs to which `if`, and the outer check makes the inner
`catalogue[title]` safe from `KeyError`. This is the automatic version of Day 08's "check with `in` first".

## 7. Truthiness (4 min)

Demo section 7: `bool(0)`, `bool("")`, `bool([])`, `bool({})` are all `False`; `bool(" ")` and `bool("0")` are
`True`. **Prediction question:** those last two; most students get them wrong.

Rule: **zero and empty are `False`; everything else is `True`.** Practical uses:

```python
if name.strip():      # "did the user type anything other than spaces?"
if cart:              # "is there anything in the cart?"
```

Keep it practical; students should recognise `if cart:` and know `if len(cart) > 0:` means the same.

## 8. Common mistakes and the grade calculator (4 min)

Run demo section 8:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `if pin = "4321":` | `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?` | `=` assigns; comparisons need `==` (Python even suggests it) |
| missing colon | `SyntaxError: expected ':'` | every `if`, `elif`, `else` line ends with `:` |
| block not indented | `IndentationError: expected an indented block after 'if' statement on line 2` | the block must be indented under its `if` |
| extra spaces before a normal line | `IndentationError: unexpected indent` | only lines inside a block are indented |
| `else score < 50:` | `SyntaxError: expected ':'` | `else` never has a condition; use `elif` |
| `"18" >= 16` | `TypeError: '>=' not supported between instances of 'str' and 'int'` | convert `input()` text with `int()` / `float()` |
| `elif` chain in the wrong order | **no error**, wrong branch | strictest condition first |
| `day == "Sat" or "Sun"` | **no error**, always true | full comparison on each side |

Then run demo section 9: the grade calculator with `input()` and validation (outer `if 0 <= score <= 100`, inner
`elif` chain). End by asking the 🤔 question: "Which inputs prove every branch works?" (*One per grade, an invalid
one each side, and boundaries like 85 / 84.9.*) Do not answer fully; it is tomorrow's topic.

## 9. Practice (20 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict, then check | comparisons, logic, tracing an `elif` chain | recall |
| 2 Two paths with `if/else` | even/odd, balance check with `:.2f` | application |
| 3 Fix the broken code | three syntax errors + two silent logic bugs | modification |
| 4 Grade calculator | `if/elif/else` with validation, tested on a table | application |
| 5 Scholarship check | `and/or/not` with brackets; reasons via `elif` | problem solving |
| 6 Library help desk (challenge) | truthiness, `in`, dict update, string cleaning | challenge |

While circulating, look for:
- missing colons and mixed indentation (tabs vs spaces): VS Code shows a red squiggle; teach them to look for it;
- `score > 85` instead of `>=` (the 85 test row catches it: point at the table, not at the code);
- students who only run the first test value. Insist on filling in the "Actual" row in Exercise 4;
- Exercise 5: `not has_unpaid_fees and average >= 95 or ...` without brackets.

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

## 10. Recap and exit ticket (5 min)

Recap (students supply):
1. Comparisons give booleans; `==` compares, `=` assigns.
2. `if` / `elif` / `else` with colons and indented blocks; only the first true branch runs.
3. `and` both, `or` at least one, `not` flips; a full comparison on each side.
4. Empty and zero values count as `False`.

**Exit ticket:** what does this print for `points = 70`? And for `points = 40`?

```python
if points >= 80:
    print("Gold")
elif points >= 50:
    print("Silver")
else:
    print("Keep going")
print("Thanks!")
```

Answer: `Silver` then `Thanks!`; for 40: `Keep going` then `Thanks!`.

## Homework (20 min)

1. Finish Exercise 5 (and 6 if you like a challenge).
2. Write a "what to wear" advisor: given `temperature` and `is_raining`, print one piece of advice with at least
   four branches. Write a test table with one row per branch and run every row.

## Next class

Day 10 is about **solving decision problems from a written specification** and proving the code works by
**testing every branch**, including boundary values. Today's Exercise 4 table is the model. We finish with
**Checkpoint 2** (lists, dicts, sets and conditionals), so ask students to review Days 06–09.

## Instructor notes

- No loops yet: testing is done by changing a value at the top of a cell and re-running. That is deliberate. On
  Day 11 students will appreciate loops, and on Day 19 testing with functions.
- Do not introduce `is`, `match/case` or the ternary `x if c else y`. If a student uses `is` for comparison,
  replace it with `==`.
- Do not go into operator precedence tables; "add brackets when mixing `and` and `or`" is the rule.
- String ordering (`"apple" < "banana"`) works alphabetically, capitals first. Mention only if asked.
- Fast students: ask them to rewrite Exercise 5 Part 2 with nested `if`s and compare readability.
  Slow students: have them draw the branches as boxes on paper and trace one value with a finger before coding.
