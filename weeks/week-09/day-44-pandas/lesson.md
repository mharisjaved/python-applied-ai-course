# Day 44: pandas DataFrames

**Week 9 · Session 44 of 60 · Planned 75 min** · Previous: [Day 43](../day-43-numpy/lesson.md) · Next: [Day 45](../day-45-cleaning-visualization/lesson.md)

## Objectives

By the end of this lesson students can:

1. Load a CSV into a DataFrame with `pd.read_csv` and inspect it with `head`, `shape`, `info` and `describe`.
2. Select one column (a Series) or several columns (a DataFrame), and explain the double brackets.
3. Filter rows with one or more conditions using `&`, `|` and parentheses.
4. Sort rows with `sort_values`, add a new column, and count categories with `value_counts`.
5. Summarise a value per group with `groupby(...)[...].sum()` / `.mean()`.
6. Turn a question in plain words ("where did the money go?") into a short pandas expression and answer it in words.

**Prior knowledge:** dicts and lists (Days 06–08), string slicing (Day 05), `pathlib.Path` (Day 24),
`csv` (Day 36), NumPy arrays, masks, `&`/`|` with brackets, `mean`/`median` (Day 43), the pass rate
as the mean of 0/1 values (Day 43).

**Files:** `demo.ipynb` · `practice.ipynb` · `solutions.ipynb` · datasets `expenses.csv` (main) and
`students.csv` (demo section 9).

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: masks retrieval + "what would you ask this data?" | core |
| 0:05–0:12 | DataFrame and Series; `read_csv`, `head`, `shape`, `info`, `describe` (demo sections 1–2) | core |
| 0:12–0:17 | Selecting columns (demo section 3) | core |
| 0:17–0:27 | Filtering rows (demo section 4) | core |
| 0:27–0:32 | Sorting and new columns (demo sections 5–6) | core |
| 0:32–0:42 | `value_counts` and `groupby` (demo sections 7–8) | core |
| 0:42–0:45 | Same tools on `students.csv` (demo section 9) | core |
| 0:45–0:70 | Practice exercises 1–5 (Q1–Q5) | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (monthly spending) together; discuss count vs total vs average | optional (90-min session) |

**60-minute version:** show only the first cell of demo section 9 and let Exercise 5 become homework.

## 1. Warm-up (5 min)

- Day 43 retrieval on the board: "`scores = np.array([45, 70, 82, 51])`. Write the mask for scores from 50 to 80
  inclusive." (*`(scores >= 50) & (scores <= 80)`, brackets required.*)
- Homework check (Day 42): "Which columns of `expenses.csv` are numeric? What question did you write?" Collect 3–4
  questions on the board. Most of them will be answered by the end of today.

## 2. DataFrame, Series, loading (7 min)

**Why pandas?** NumPy arrays hold one type and have no names; `final[program == "science"]` needed three separate
arrays. A **DataFrame** is a table: named columns, each with its own type, plus a row label (the **index**).

**Analogy:** a DataFrame is a spreadsheet you control with code. A **Series** is one column of it.

Demo section 1 builds a 4-row `shopping` DataFrame from a dict (key = column name). `shopping["price"]` is a Series
with `.mean()` and `.max()`, just like an array.

Demo section 2: `pd.read_csv(DATA_DIR / "expenses.csv")`, then the inspection routine students should run on
**every** new dataset:

| Method | Answers |
|--------|---------|
| `.head()` | what do the rows look like? |
| `.shape` | how many rows and columns? → `(148, 5)` |
| `.info()` | which columns, which types, any missing values? |
| `.describe()` | summary statistics of the numeric columns |

**Prediction question:** "The file has 149 lines. What is `.shape`?" (*`(148, 5)`: the header is not a row.*)

Point out in `.describe()`: mean 39.94 vs median 26.16. Ask why (*three 650 rent payments pull the mean up:
yesterday's mean vs median lesson*).

## 3. Selecting columns (5 min)

```python
expenses["amount"]                          # one column → Series
expenses[["date", "description", "amount"]] # a LIST of names → DataFrame
```

Explain the double brackets as "the outer brackets select, the inner brackets are a Python list". Then run the
tagged cell `expenses["Amount"]` → `KeyError: 'Amount'`. Reading a `KeyError` is the same as on Day 08 (dicts).

## 4. Filtering rows (10 min)

**Intuition:** identical to NumPy masks. A comparison makes a True/False Series; the DataFrame keeps the `True` rows.

```python
big = expenses["amount"] > 50
expenses[big]                       # 14 rows
food_cash = expenses[(expenses["category"] == "food") & (expenses["payment_method"] == "cash")]
# 18 purchases, total 470.02
```

**Prediction question before the `food_cash` cell:** "About how many food purchases were paid in cash?"

Then `|` (entertainment *or* shopping) and the tagged `and` cell:
`ValueError: The truth value of a Series is ambiguous`. Same rule as yesterday: **`&` `|` and brackets**.

Key point: filtering returns a **new** DataFrame; `expenses` itself is unchanged.

## 5. Sorting and new columns (5 min)

Demo section 5: `sort_values("amount", ascending=False).head(5)` shows the three rents at the top.
**Prediction question:** "Without `ascending=False`?" (*Smallest first.*) Then combine: filter out rent, then sort.

Demo section 6: `expenses["is_big"] = expenses["amount"] >= 50` (a calculation on every row) and
`expenses["month"] = expenses["date"].str[:7]`. **New today:** `.str` applies string methods/slicing to every value in
a text column. Day 45 uses `.str.strip()` and `.str.lower()`.

## 6. `value_counts` and `groupby` (10 min)

`expenses["category"].value_counts()`: food 67, transport 38, … **Prediction question first:** "Which category
appears most often?"

**`groupby` analogy:** sort the receipts into piles by category, then add up each pile. Write the pattern on the
board and leave it there during practice:

```python
df.groupby("pile column")["value column"].sum()     # or .mean()
```

```python
expenses.groupby("category")["amount"].sum().sort_values(ascending=False)
# rent 1950.00, food 1748.95, transport 632.41, ...
```

**Prediction question:** "Food has the most transactions. Does it have the biggest total?" (*No: rent, from only 3
payments. Counting and summing answer different questions.*)

## 7. Same tools, another dataset (3 min)

Demo section 9: `students.groupby("program")["final_score"].mean()` and
`students.groupby("has_job")["passed"].mean()` → no 0.799, yes 0.506. Remind them: on Day 41 that took a function
and a loop. The mean of a 0/1 column is a share, same as `mask.mean()` yesterday.

## 8. Common mistakes

| Mistake | Error / symptom | How to explain it |
|---------|-----------------|-------------------|
| `df["Amount"]` | `KeyError: 'Amount'` | names are case-sensitive; check `df.columns` or `.head()` |
| `df["date", "amount"]` | `KeyError: ('date', 'amount')` | several columns need a list: `df[["date", "amount"]]` |
| `df[a == 1 & b > 2]` | `TypeError` (or `ValueError`) | brackets around each condition |
| `(cond1) and (cond2)` | `ValueError: The truth value of a Series is ambiguous` | use `&` / `|` |
| `sort_values("amount").head(3)` for "most expensive" | cheapest rows, no error | add `ascending=False`; always sanity-check results |
| `!= "rent" \| != "utilities"` | nothing gets removed | "not A or not B" is always true; use `&` |
| creating a filtered copy, then adding a column to the original | `KeyError` on the copy | add columns first, then filter (Exercise 6) |
| writing `df.sort_values(...)` and expecting `df` to change | `df` unchanged | most pandas methods return a **new** table; assign it |

## 9. Practice (25 min)

The practice notebook frames five questions (Q1–Q5) about a friend's spending. Insist on **an answer in words**
under each question: data analysis is not finished when the code runs.

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Load and inspect | `shape`, `head`, `info`, `describe` | recall/predict |
| 2 Fix the broken selections | brackets, case, sort order | modification |
| 3 Totals and counts (Q1, Q2) | `sum`, `mean`, `value_counts` | application |
| 4 Filter and sort (Q3, Q4) | `&`, `!=`, `sort_values`, column selection | application |
| 5 Group and compare (Q5) | `groupby().sum()`, percentage of total | problem solving |
| 6 Monthly everyday spending (challenge) | `.str[:7]`, filter + groupby, total vs average | challenge |

Circulate and look for: `|` instead of `&` in Q3 (rent and utilities still in the result); Exercise 2d marked
"correct" because it runs; answers with code but no sentence.

Expected answers: Q1 5910.39 total, 39.94 average · Q2 card 97, cash 45, transfer 6 · Q3 pharmacy 78.00, shoes 71.81,
gym 69.82, gym 66.29, headphones 58.85 · Q4 18 purchases, 470.02 · Q5 rent 1950.00 = 33.0 % of spending.

## 10. Recap and exit ticket (5 min)

Recap: point at the summary table at the end of the demo and have students read each row as a sentence.

**Exit ticket:** write the pandas line that answers "what is the average `final_score` of students with and without
a part-time job?" (`students` is already loaded.)

Answer: `students.groupby("has_job")["final_score"].mean()` (no ≈ 57.9, yes ≈ 51.4).

## Homework (25 min)

Finish Exercises 4–5 and write the five answers in words. Optional: Exercise 6.

## Next class

Day 45: back to the messy `students_raw.csv` from Day 42. Today's tools plus `isna`, `fillna`, `drop_duplicates` and
`.str.strip().str.lower()` will clean it in a few lines, then **matplotlib** turns the clean data into charts.
Project 06 (a data analysis report) starts at the end of the session.

## Instructor notes

- pandas 3 is installed: text columns show as `str` in `.info()` (older tutorials show `object`). Both mean "text".
- Do not teach `.loc`/`.iloc`, `merge`, `pivot_table`, `apply` or dates (`pd.to_datetime`) today. Everything in the
  practice works with the seven tools in the recap table. If a strong student asks for `.isin()`, show it once.
- A bare number as the last line of a cell may display as `np.float64(5910.39)`. Use `print()` or an f-string.
- Make students say the result **in words** every time ("rent is a third of all spending"). This habit is graded
  in Project 06.
- Fast students: Exercise 6, then "which description is bought most often in cash?" Slow students: give the
  `groupby` pattern on paper and let them complete Exercises 1, 3 and 4 only.
