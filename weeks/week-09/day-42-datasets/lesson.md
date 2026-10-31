# Day 42: Datasets, Features, Labels and Data Quality

**Week 9 · Session 42 of 60 · Planned 75 min** · Previous: [Day 41](../day-41-what-is-ai/lesson.md) · Next: [Day 43](../day-43-numpy/lesson.md)

## Objectives

By the end of this lesson students can:

1. Describe a dataset in terms of rows (examples) and columns, and say how many of each a file has.
2. Identify the **features**, the **target** (label) and any **identifier** column for a given prediction task.
3. Classify a column as **numeric** or **categorical**, including numbers that are really categories (`0/1`).
4. Audit a raw CSV with plain Python: count missing values per column, find inconsistent categories, exact
   duplicates and out-of-range values.
5. Produce a one-screen **data-quality audit table** and propose a fix for each problem (without applying it yet).

**Prior knowledge:** `csv.DictReader` (Day 36), counting with a dict and `.get()` (Days 08, 12), sets and tuples
(Days 07–08), comprehensions (Day 22), `try/except ValueError` (Day 25), functions (Days 16–18), Day 41's vocabulary
(training, prediction, accuracy). **New today (small):** `value is not None`, the standard way to test for `None`.

**Files:** `demo.ipynb` · `practice.ipynb` · `solutions.ipynb` · datasets `students_raw.csv` (audit),
`apartments.csv` and `expenses.csv` (practice).

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: retrieval from Day 41 and Day 36 | core |
| 0:05–0:15 | Rows, columns, features vs target (demo sections 1–2) | core |
| 0:15–0:20 | Numeric vs categorical (demo section 3) | core |
| 0:20–0:40 | The four quality problems, live (demo sections 4–7) | core |
| 0:40–0:47 | The audit table + "what would we do?" (demo section 8) | core |
| 0:47–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (reusable audit) on the board, discuss outliers vs errors | optional (90-min session) |
| +5 min | "Where does real data come from and who checks it?" discussion | optional (90-min session) |

**60-minute version:** show section 6 (duplicates) quickly from the finished cell and skip Exercise 5 in class.

## 1. Warm-up (5 min)

- Day 41 retrieval: "What did *training* mean in our threshold example?" (*Trying many thresholds on students with
  known results and keeping the most accurate.*) "What is the baseline we had to beat?" (*Always predict pass: 71 %.*)
- Day 36 retrieval: "`csv.DictReader` gives each row as a … ?" (*dict*) "…and every value is a … ?" (*str*).
- Bridge: "Yesterday's file was clean. Somebody cleaned it. Today we look at what it looked like **before**."

## 2. Rows, columns, features and target (10 min)

**Why:** a model only sees columns. Before training anything we must decide which columns are inputs and which one is
the answer we want to predict.

Live code (demo section 1): load `students_raw.csv` with `csv.DictReader`. Expected: `304 rows, 10 columns`.
Show `rows[0]` and read one row aloud as a sentence: "student S001, arts, studies 14 hours a week…".

Vocabulary table (demo section 1): **row** = example/record · **column** = attribute · **feature** = input column ·
**target** = label = the column we predict.

Demo section 2 table, then the key distinctions:
- `student_id` is an **identifier**, not a feature. Analogy: a name tag tells you *who* someone is, not *how they
  will do*. A model given IDs can memorise answers instead of learning patterns.
- Two possible targets: `final_score` (a number → *regression*, Day 47) and `passed` (a category → *classification*,
  Day 48). Just name the words today.
- **Prediction question:** "To predict `passed`, may we use `final_score` as a feature?" (*No: `passed` is computed
  from `final_score`. It would be like predicting the answer by reading the answer sheet. Day 49 calls this
  leakage.*)

## 3. Numeric vs categorical (5 min)

| Kind | Test | Examples |
|------|------|----------|
| numeric | "does an average make sense?" yes | `study_hours`, `attendance_pct`, `final_score` |
| categorical | a label from a small set; average is meaningless | `program`, `has_job`, `passed` (0/1) |

Demo section 3 counts distinct values per column with `set([... for row in rows])`. Expected: `program` 10,
`has_job` 8, `passed` 2.

**Prediction question:** "`program` should have 3 values. Why 10?" Leave it open until section 5.

Point out: `passed` is stored as numbers but is categorical. Phone numbers, postcodes and IDs are the same story
(callback to Day 02's student ID that had to be a string).

## 4. The four quality problems (20 min)

**Intuition:** "garbage in, garbage out". A model cannot tell a typo from a fact. Every problem we miss becomes
something the model learns.

| Problem | What it looks like in a CSV | Demo section |
|---------|-----------------------------|--------------|
| missing values | empty string `""` | 4 |
| inconsistent categories | `"Arts"`, `"ARTS"`, `"arts "` | 5 |
| duplicates | the same row twice | 6 |
| out-of-range values | attendance 150 %, study −3 hours | 7 |

**Section 4, missing:** first run the tagged cell that sums `float(row["study_hours"])`: it crashes with
`ValueError: could not convert string to float: ''`. That is *why* we look for blanks. Then count blanks per
column with `.strip() == ""`. Expected: `study_hours` 8, `sleep_hours` 6, everything else 0.

**Section 5, inconsistent categories:** count raw `program` values with a dict. Print with quotes
(`f"'{value}'"`) so trailing spaces become visible: `'arts '`. Normalise with `.strip().lower()` → 3 categories
(`arts` 106, `commerce` 93, `science` 105, still including duplicates).

**Section 6, duplicates:** a dict cannot go into a set, but `tuple(row.values())` can. Expected: 4 exact
duplicates (S006, S043, S100, S251). **Discuss:** "Why do duplicates hurt a model?" (*They count one student
several times. With many copies, the model over-learns that student.*)

**Section 7, out of range:** introduce `to_number()` (from Day 25 `try/except`) that returns `None` for blanks.
Explain `value is not None`: "this is how Python asks *is there a value at all?*". Using a dict of allowed ranges,
expected output: `S204 study_hours -3.0` and `S018 attendance_pct 150.0`.

**Prediction question before running section 7:** "Will the missing `study_hours` be reported as out of range?"
(*No: we skip `None`. Missing and impossible are different problems and need different fixes.*)

## 5. The audit table (7 min)

Demo section 8 combines everything into one table (the day's output):

```text
column            missing out of range distinct
student_id              0            -      300
program                 0            -       10
study_hours             8            1      133
attendance_pct          0            1       43
sleep_hours             6            0       47
...
Exact duplicate rows: 4
```

Then discuss the "what should we do?" table at the end of the demo. Make the class vote on one row, e.g.
"8 missing study hours: drop those students or fill in a typical value?" There is no single right answer: dropping
loses information, filling invents it. **We apply the fixes on Day 45** with pandas.

The golden rule to repeat: **never edit the raw file by hand.** Cleaning is code, so anyone can see and repeat it.

## 6. Common mistakes

| Mistake | Error / symptom | How to explain it |
|---------|-----------------|-------------------|
| `if row["sleep_hours"] == None` | count is 0 | CSV blanks are `""`, never `None` |
| `float(row["study_hours"])` on every row | `ValueError: could not convert string to float: ''` | Skip blanks first, or use `to_number()` |
| `value < low` when `value` is `None` | `TypeError: '<' not supported between instances of 'NoneType' and 'int'` | Check `value is not None` **before** comparing |
| dividing by `len(rows)` after skipping blanks | average slightly too small | Divide by how many values you actually added |
| `set(rows)` to find duplicates | `TypeError: unhashable type: 'dict'` | Convert each row to `tuple(row.values())` |
| printing values without quotes | `'yes'` and `'yes '` look identical | Wrap in quotes in the f-string |

## 7. Practice (23 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Features, target or ID? (`apartments.csv`) | vocabulary, numeric vs categorical | recall |
| 2 Count missing values | function + loop over columns | application |
| 3 Fix the broken audit | `""` vs `None`, skipping blanks, correct divisor | modification |
| 4 How messy is `has_job`? | counting categories, normalising | application |
| 5 Find the impossible values | ranges, `to_number`, judgement | problem solving |
| 6 A reusable audit (challenge) | generalising into one function, outliers vs errors | challenge |

Circulate and look for:
- students who print raw values without quotes and conclude "there are duplicates of `yes`";
- Exercise 3: fixing the crash but keeping `len(rows)` (6.87 instead of 7.0);
- Exercise 5: answers that "fix" 150 to 100 without saying how they know. Ask "how do you know it wasn't 50?"

Expected outcome: everyone completes 1–3, most complete 4–5, fast students attempt 6.

## 8. Recap and exit ticket (5 min)

Recap (students supply it):
1. Rows are examples; features are inputs; the target (label) is what we predict; IDs are neither.
2. Numeric = averages make sense; categorical = labels, even when stored as 0/1.
3. Audit for four problems before analysing: missing, inconsistent, duplicate, out of range. Never edit raw data by hand.

**Exit ticket:** a file of exam results has these columns: `exam_id`, `room` (`"A1"`, `"a1"`, `"B2"`),
`minutes_late` (one value is `-5`), `score` (two are blank). We want to predict `score`. Name the target, one
feature, one column that is not a feature, and two quality problems.

Answer: target `score`; features `room`, `minutes_late`; `exam_id` is an identifier; problems: inconsistent
categories in `room`, an impossible negative `minutes_late`, two missing `score` values (missing *targets*: those
rows cannot be used for training).

## Homework (20 min)

Finish Exercise 5. Then open `datasets/expenses.csv` in VS Code and write three sentences in your notebook: which
columns are numeric, which are categorical, and one question you would like to answer with this data. We use it
on Day 44.

## Next class

Day 43 introduces **NumPy**: doing maths on a whole column at once (no loops), plus averages, spread, and
filtering with True/False masks. Today's loops over `rows` are exactly what NumPy will shorten. Teaser: "tomorrow
the average of 298 numbers is one line."

## Instructor notes

- This is the last day of "data with plain Python". Let students feel that the loops are long and repetitive: it
  motivates NumPy and pandas. But do not show pandas yet; the point is to understand what the tools will automate.
- Do not fix the data today. Students will want to. Keep "decide" (today) and "apply" (Day 45) separate.
- Range limits are **judgement calls** made with domain knowledge (0–80 study hours per week is generous). Say so.
  If a student argues for different limits, that is a good sign.
- "Outlier" vs "error": a 650 rent payment is unusual but real. Never delete values only because they are large.
- Fast students: Exercise 6, then ask them to also report the most common value of each categorical column.
  Slow students: give them the Exercise 2 function header and let them focus on calling it in a loop.
