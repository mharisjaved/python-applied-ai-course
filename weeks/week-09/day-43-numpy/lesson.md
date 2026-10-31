# Day 43: NumPy Essentials

**Week 9 · Session 43 of 60 · Planned 75 min** · Previous: [Day 42](../day-42-datasets/lesson.md) · Next: [Day 44](../day-44-pandas/lesson.md)

## Objectives

By the end of this lesson students can:

1. Create a NumPy array from a list and read its `shape` and `dtype`.
2. Apply arithmetic to a whole array at once (vectorised) and predict how it differs from the same operator on a list.
3. Compute `mean`, `median`, `std`, `min`, `max` of an array and explain in words what the standard deviation says.
4. Filter an array with a boolean mask, combine masks with `&` / `|`, and count with `mask.sum()`.
5. Index a 2-D array (rows = students, columns = features) with `[row, col]` and `[:, col]`, and average along an axis.
6. Generate repeatable random numbers with `np.random.default_rng(seed)`.

**Prior knowledge:** lists, `sum/min/max` (Day 06), list indexing (Days 05–06), comprehensions (Day 22),
`import … as …` (Day 26), loading `students.csv` with `csv.DictReader` (Days 36, 41), Day 42's "averaging a column
with a loop" pain.

**Files:** `demo.ipynb` · `practice.ipynb` · `solutions.ipynb` · dataset `students.csv` (demo section 8, Exercise 6).

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: average a column the long way | core |
| 0:05–0:15 | Arrays, `shape`, `dtype`, vectorised arithmetic (demo sections 1–3) | core |
| 0:15–0:25 | Summary statistics, mean vs median, std intuition (demo section 4) | core |
| 0:25–0:35 | Boolean masks and the `&` pitfalls (demo section 5) | core |
| 0:35–0:43 | 2-D arrays and axes (demo section 6) | core |
| 0:43–0:47 | Random numbers with a seed (demo section 7) | core |
| 0:47–0:50 | Real data: grade statistics in 5 lines (demo section 8, first two cells) | core |
| 0:50–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +4 min | Speed comparison loop vs NumPy (end of demo section 3) | optional |
| +8 min | Rest of demo section 8 (groups, text masks, feature table) or Exercise 6 together | optional (90-min session) |

**60-minute version:** skip the speed test, show section 7 in one cell, and set Exercise 5 as homework.

## 1. Warm-up (5 min)

On the board: "Compute the average of `[72, 85, 58, 91, 64, 77]`, in Python, without `sum()`." Students write the
accumulator loop (Day 11). Then: "Yesterday we did this for 304 rows and ten columns, with blank values and
conversions. How many lines was that?" Lots. **Today the average of a column is one line.**

Retrieval (Day 42): "What is a feature? What is the target?" and "Which problems did the audit find?"

## 2. Arrays, `shape`, `dtype` (5 min)

**Analogy:** a list is a shopping bag (anything goes in, mixed types). An array is an egg carton: every slot holds
the same kind of thing, and that is what makes it fast and lets one operation work on every slot.

Demo sections 1–2:

```python
import numpy as np
quiz = np.array([72, 85, 58, 91, 64, 77])
print(quiz.shape)   # (6,)
print(quiz.dtype)   # int64
```

**Prediction question:** `np.array([1.62, 1.75, 2, 1.80]).dtype`? (*`float64`: one float makes every item a float.*)

Do not go into memory layout. "64" = "stored in 64 bits"; that is enough.

## 3. Vectorised arithmetic (5 min)

Demo section 3: `quiz + 5`, `quiz / 100 * 20`. "Vectorised" = the operation is applied to every item; no loop
written by us.

**Prediction question:** `[1, 2, 3] * 2` vs `np.array([1, 2, 3]) * 2`. (*`[1, 2, 3, 1, 2, 3]` vs `[2 4 6]`.*)
This is the single most important "list vs array" difference; most students get it wrong.

Two arrays of the same length combine item by item (`exam * 0.7 + coursework * 0.3` → `[63. 72. 59. 88.6]`).
Different lengths → `ValueError: operands could not be broadcast together` (tagged cell). Say "broadcast" means
"pairing up items"; do not teach broadcasting rules.

Optional speed test (1 million numbers): loop vs `array * 2`. Two small new things appear in that cell:
`time.perf_counter()` from the standard `time` module (a stopwatch in seconds) and the literal `1_000_000` (the
underscores only make the number readable). Exact timings vary by machine; NumPy is typically around 10× faster or
more. Make the point and move on.

## 4. Summary statistics (10 min)

Demo section 4: `.mean()` `np.median()` `.min()` `.max()` `.std()`, plus `.argmax()` (the **position** of the
largest value, new today) to find *who* scored highest (`3 Omar 91`).

**Mean vs median, prediction question:** "Ken was absent and got 0. Which moves more?" Expected: mean 74.5 → 63.9,
median 74.5 → 72.0. Rule of thumb: when a few values are extreme (rent in an expenses list, a 0 for an absence),
report the median too.

**Standard deviation without formulas.** Say: "std is the *typical distance* of a value from the average." Show
two classes with the same mean 70: class A std 1.4 (everyone close to 70), class B std 19.2 (spread out).
**Prediction question first:** "Which class has the bigger std?" Then: "Which class would you rather teach? Why does
the mean alone not tell you?"

Do **not** write the std formula. If a strong student asks: "it is roughly an average of the distances from the
mean; NumPy does the exact calculation."

## 5. Boolean masks (10 min)

**Analogy:** a mask is a stencil with holes. Put it over the array and only the values under the holes show.

Demo section 5:

```python
passed = quiz >= 65        # [ True  True False  True False  True]
quiz[passed]               # [72 85 91 77]
passed.sum()               # 4    (True counts as 1)
passed.mean()              # 0.666...  (share of True)
```

**Prediction question:** "How many scores are between 60 and 80?" Then show `(quiz >= 60) & (quiz <= 80)` → 3.

Run both tagged cells and read the error: `and` on arrays and missing parentheses both give
`ValueError: The truth value of an array with more than one element is ambiguous`. Rule to write on the board:
**`&` instead of `and`, `|` instead of `or`, and brackets around every condition.** The same rule applies to pandas
tomorrow, so this is worth the time.

Mask assignment: `curved[curved > 100] = 100` caps values. Practice Exercise 4 uses it.

## 6. 2-D arrays and axes (8 min)

Demo section 6: a gradebook, 4 students × 3 tests, `shape (4, 3)` = (rows, columns).

| Code | Means | Result |
|------|-------|--------|
| `grades[0]` | row 0 (Asha) | `[70 82 64]` |
| `grades[2, 1]` | row 2, column 1 | `88` |
| `grades[:, 0]` | all rows, column 0 | `[70 55 90 62]` |
| `grades.mean(axis=0)` | collapse the rows → one value per **column** (per test) | `[69.25 69. 71.75]` |
| `grades.mean(axis=1)` | collapse the columns → one value per **row** (per student) | `[72. 62. 91. 55.]` |

**Axis trick:** "the axis you name is the one that disappears." `axis=0` squashes the 4 rows into 1, leaving 3
numbers. Check by counting: 4 students → a per-student result has 4 numbers.

Connect to ML: next week the feature table `X` is exactly this: rows = students, columns = features.

## 7. Random numbers with a seed (4 min)

Demo section 7: `rng = np.random.default_rng(42)`, `rng.integers(0, 101, size=5)` → `[ 9 78 66 44 43]`,
`rng.normal(70, 10, size=5)` → values "around 70, typically 10 away". Re-create with the same seed → same numbers.

Why it matters: everyone in the room gets identical results, and next week's train/test split uses the same idea
(`random_state`). Compare with `random.seed()` from Day 14.

## 8. Real data (3 min core + optional)

Demo section 8: build `final`, `hours`, `program` arrays from `students.csv` with list comprehensions. Expected:
mean 56.0, median 56.2, std 10.8, lowest 19.9, highest 92.7, pass rate 71.1 % (matches Day 41's baseline!).

Optional cells: 10+ hours of study → mean 61.8 vs 52.4; masks on text (`program == "science"`); `~` to flip a mask;
a `(298, 3)` feature table with `mean(axis=0)`.

## 9. Common mistakes

| Mistake | Error / symptom | How to explain it |
|---------|-----------------|-------------------|
| `(a > 1) and (a < 5)` | `ValueError: The truth value of an array … is ambiguous` | `and` wants one True/False; use `&` |
| `a > 1 & a < 5` | same `ValueError` | `&` binds tighter than `>`; add brackets |
| `scores.median()` | `AttributeError: 'numpy.ndarray' object has no attribute 'median'` | it is `np.median(scores)` |
| expecting `[1, 2] * 2` to double | `[1, 2, 1, 2]` | lists repeat, arrays multiply |
| arrays of different lengths | `ValueError: operands could not be broadcast together` | items are paired by position |
| swapping `axis=0` and `axis=1` | wrong number of results | count: per-student result has one value per student |
| `>`/`<` when the task says "inclusive" | silently misses boundary values | no error at all, so check the boundaries yourself |

## 10. Practice (20 min)

Rule for Exercises 2–5: **no `for` loops**. It forces students to think in arrays.

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict, then run | list vs array, dtype, masks | recall/predict |
| 2 Quiz statistics | `mean` `median` `std` `min` `max`, mask counting | application |
| 3 Fix the masks | `&`, parentheses, inclusive boundaries | modification |
| 4 Curve the scores | vectorised `+`, mask assignment | application |
| 5 A 2-D gradebook | `[r, c]`, `[:, c]`, axes, `argmax` | problem solving |
| 6 Real students, real questions (challenge) | arrays from CSV, group comparison, seeded simulation | challenge |

Circulate and look for: `np.median` written as a method; off-by-one column numbers in Exercise 5 ("quiz 3" =
column 2); Exercise 3c accepted as "works" because it runs. Ask "is 80 in your output?"

Expected outcome: everyone completes 1–3, most 4–5, fast students 6.

## 11. Recap and exit ticket (5 min)

Recap (students supply it): arrays hold one type; arithmetic is vectorised; masks filter and count; 2-D arrays
are tables indexed `[row, col]`; a seed makes randomness repeatable.

**Exit ticket:** what does this print?

```python
import numpy as np
temps = np.array([18, 25, 31, 22, 29])
hot = temps >= 25
print(temps[hot], hot.sum(), temps.mean())
```

Answer: `[25 31 29] 3 25.0`

## Homework (20 min)

Finish Exercise 5. Then write, in a markdown cell, one sentence each: what `std` tells you that `mean` does not, and
why `(a > 1) and (a < 5)` fails on arrays.

## Next class

Day 44: **pandas**. Arrays have no column names and hold one type; real tables have names and mix text with
numbers. pandas DataFrames are "NumPy with column names", and the mask rule (`&`, `|`, brackets) comes straight back
for filtering rows. We will answer questions about `expenses.csv`.

## Instructor notes

- Keep NumPy to what pandas and scikit-learn need next. Do **not** teach reshape, broadcasting rules, `np.where`,
  `np.concatenate`, linear algebra or the std formula.
- In NumPy 2, a bare `quiz.mean()` as the last line of a cell displays `np.float64(74.5)`. That is why the demo uses
  `print()`. If a student sees `np.float64(...)`, say "it is just a number with a NumPy label; `print` hides it."
- `np.random.default_rng` is the modern API. Older tutorials use `np.random.seed`; tell students both exist and we
  use the new one.
- Fast students: Exercise 6, then ask them to find the student with the highest final score using `argmax` on
  the real data. Slow students: pair them on Exercise 3 and let them skip Exercise 5 step 5.
