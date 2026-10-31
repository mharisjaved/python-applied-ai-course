# Day 45: Cleaning, EDA and Visualisation

**Week 9 · Session 45 of 60 · Planned 75 min** · Previous: [Day 44](../day-44-pandas/lesson.md) · Next: [Day 46](../../week-10/day-46-ml-workflow/lesson.md)

## Objectives

By the end of this lesson students can:

1. Find missing values, duplicates, inconsistent categories and impossible values with pandas
   (`isna().sum()`, `duplicated().sum()`, `value_counts()`, filters).
2. Apply a written cleaning recipe in order: `drop_duplicates()`, `.str.strip().str.lower()`, filtering bad rows,
   `fillna(median)`, and explain the choice between `dropna()` and `fillna()`.
3. Verify a cleaning result against a trusted reference (same shape, same column means).
4. Draw a histogram, a bar chart and a scatter plot with matplotlib, each with a title and axis labels.
5. Choose the right chart type for a question and state why a scatter plot does not prove cause and effect.

**Prior knowledge:** Day 42 audit of `students_raw.csv` (the same four problems), Day 43 mean vs median and masks,
Day 44 pandas (`read_csv`, filtering with `&`/`|`, `groupby`, `.str[:7]`, new columns), functions (Day 17).

**New today:** `isna`, `duplicated`, `drop_duplicates`, `dropna`, `fillna`, `.str.strip()` / `.str.lower()`,
`.median()` on a column, `mean(numeric_only=True)`, a Series' `.index` / `.values`, and matplotlib
(`plt.hist` `plt.bar` `plt.scatter` `plt.title` `plt.xlabel` `plt.ylabel` `plt.show`).

**Files:** `demo.ipynb` · `practice.ipynb` · `solutions.ipynb` · datasets `students_raw.csv`, `students.csv`,
`expenses.csv` · project brief [Project 06](../../../projects/06-data-analysis-report/README.md).

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: "what did the Day 42 audit find?" | core |
| 0:05–0:10 | Finding the problems with pandas (demo section 1) | core |
| 0:10–0:25 | The 4-step cleaning recipe, including the missing-value trap (demo section 2) | core |
| 0:25–0:28 | Check against `students.csv` (demo section 3) | core |
| 0:28–0:30 | EDA: look at the numbers first (demo section 4) | core |
| 0:30–0:42 | Three charts + chart mistakes (demo section 5) | core |
| 0:42–0:45 | How to choose a chart (demo section 6) | core |
| 0:45–0:65 | Practice exercises 1–3 (4 if time) | core |
| 0:65–0:72 | Project 06 launch | core |
| 0:72–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 4 in class; students present one chart each | optional (90-min session) |
| +5 min | The `clean_students()` function in demo section 3, written live | optional (90-min session) |

**60-minute version:** skip demo section 4, show only the histogram and the scatter live (the bar chart is in
Exercise 3b), and cut practice to Exercises 1–2.

**Checkpoint 9 is given in the first 15 minutes of Day 46**, not today. Reasons: this session is already full
(cleaning + a new library + project launch), and students do better on the cleaning/chart questions after one
evening of project work with them. Week 9 is a project week, so this matches the course rule for checkpoints.

## 1. Warm-up (5 min)

Ask the class to rebuild the Day 42 audit from memory on the board: *8 missing study hours, 6 missing sleep hours,
messy `program`/`has_job` spellings, 4 duplicates, attendance 150 %, study −3 hours.* Then: "On Day 42 we only
**decided** what to do. Today we **do** it, in about ten lines."

Retrieval (Day 44): "Write the pandas line for the average `final_score` per `program`."
(*`students.groupby("program")["final_score"].mean()`*)

## 2. Finding the problems with pandas (5 min)

Demo section 1:

```python
raw = pd.read_csv(DATA_DIR / "students_raw.csv")   # (304, 10)
raw.isna().sum()                                   # study_hours 8, sleep_hours 6
raw.duplicated().sum()                             # 4
raw[(raw["attendance_pct"] > 100) | (raw["study_hours"] < 0)]   # S018 and S204
```

Explain `NaN`: pandas' marker for "missing" (blank cells become `NaN` when loading). `isna()` is True/False per
cell, so `.sum()` counts per column (the mask trick again).

**Prediction question:** "Why does `value_counts()` show two lines that both read `arts`?" (*One is `"arts "` with a
space; pandas does not show quotes. That is why we printed quotes on Day 42.*)

## 3. The cleaning recipe (15 min)

**Why a recipe?** Cleaning involves choices. Writing them down in a fixed order makes the result repeatable and
lets someone else check it. The order matters (step 4's median depends on which rows are left).

| Step | Code | Rows |
|------|------|------|
| 1 duplicates | `df = raw.drop_duplicates()` | 304 → 300 |
| 2 categories | `df["program"] = df["program"].str.strip().str.lower()` (same for `has_job`) | 300 |
| 3 impossible values | `keep = (df["attendance_pct"] <= 100) & ((df["study_hours"] >= 0) \| df["study_hours"].isna())` | 300 → 298 |
| 4 missing values | `df[col] = df[col].fillna(df[col].median())` for `study_hours`, `sleep_hours` | 298 |

**Step 2:** chaining reads left to right: strip spaces, *then* lower-case. Result: 3 programs, 2 `has_job` values.

**Step 3, the key teaching moment.** First run the "obvious" filter `df["study_hours"] >= 0`.
**Prediction question:** "How many rows remain?" Most say 298. It is **290**. A missing value compared with anything
gives `False`, so the filter silently deleted the 8 students with missing study hours. Write on the board:
**"say exactly what you mean: not negative *or* missing."** Silent errors are the dangerous ones.

**Step 4, drop or fill?** Show `df.dropna().shape` → `(284, 10)`: 14 students lost because one number is missing.
`fillna(median)` keeps them but **invents** a value (8.9 hours for 8 students). Neither is "right"; the point is to
choose deliberately and write the choice down. Median rather than mean because it is not pulled by extreme values.

## 4. Check against the official file (3 min)

Demo section 3: compare `df.shape` with `students.csv` and put both `mean(numeric_only=True)` Series side by side in
a small DataFrame (`numeric_only=True` skips the text columns). `all(comparison["mine"] == comparison["official"])`
→ `True`. Message: **always check cleaning against something you trust**, even if it is just "shape and means look
right".

The same recipe as a function `clean_students(raw)` closes the section. Students can reuse it in Project 06.

## 5. EDA and three charts (2 + 12 min)

**EDA** (exploratory data analysis) = look at `describe()` and group means **before** plotting, so you know what to
expect. Demo section 4.

matplotlib: `import matplotlib.pyplot as plt`. Every chart is the same four moves: **draw → title → axis labels →
`plt.show()`**. Demo section 5:

| Chart | Code | Message to draw out |
|-------|------|---------------------|
| histogram | `plt.hist(students["final_score"], bins=20)` | most scores 45–65; some below the pass mark |
| bar | `plt.bar(pass_rate.index, pass_rate.values)` | 79.9 % pass without a job vs 50.6 % with one |
| scatter | `plt.scatter(students["study_hours"], students["final_score"], alpha=0.5)` | upward drift, lots of spread |

Explain `.index` (the group names → bar labels) and `.values` (the numbers → bar heights) of a `groupby` result.
`bins` = how many bars the histogram has; `alpha` = transparency so overlapping dots show.

**Prediction/discussion on the scatter:** "Does this prove studying more *causes* higher scores?" (*No.
Students who study more may also attend more, sleep more, or be more motivated. **Correlation ≠ causation.***)
Second question: "Would a scholarship rule based on this chart be fair?" (link to Day 41's bias discussion).

Then the two mistake cells: an unlabeled histogram ("what is on the x-axis?") and `plt.bar(means)` →
`TypeError: bar() missing 1 required positional argument: 'height'`.

## 6. How to choose a chart (3 min)

| Question | Chart |
|----------|-------|
| How are the values of one number spread out? | histogram |
| How does a number compare across groups? | bar chart |
| Do two numbers move together? | scatter plot |
| How does something change over time? | line chart (`plt.plot`, mention only) |

Checklist: title says what it shows · axis labels with units · bars start at zero · one message per chart.
Avoid pie charts with many slices and 3-D effects. Students will be graded on this checklist in Project 06.

## 7. Common mistakes

| Mistake | Error / symptom | How to explain it |
|---------|-----------------|-------------------|
| filter `study_hours >= 0` | 290 rows instead of 298, no error | missing values fail every comparison; add `\| df["study_hours"].isna()` |
| `.str.lower()` without `.str.strip()` | `"arts "` still separate | strip spaces *and* lower-case |
| `df["program"].str.strip().str.lower()` not assigned back | nothing changes | methods return a new column; assign it: `df["program"] = ...` |
| filling before removing bad rows/duplicates | means differ slightly from `students.csv` | the median depends on which rows are left: follow the order |
| `raw.isna().sum` (no brackets) | prints a method description | call it: `.sum()` |
| `plt.bar(means)` | `TypeError: bar() missing 1 required positional argument: 'height'` | bars need labels **and** heights |
| no title/labels | (not an error) | a chart nobody can read is a wrong chart |
| scatter of IDs or categories | meaningless dots | match the chart to the question (section 6) |

## 8. Practice (20 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Spot the problems | `isna`, `duplicated`, `value_counts`, filters | recall |
| 2 Apply the cleaning recipe | the 4 steps + built-in checks against `students.csv` | application |
| 3 Fix the charts | labels, `plt.bar` arguments, choosing the chart | modification |
| 4 Three questions, three charts | hist / bar / scatter + one-sentence answers | problem solving |
| 5 Choose the chart (`expenses.csv`) | chart choice + a sorted bar chart | problem solving |
| 6 What did filling do? (challenge) | side effects of `fillna`, `bins=40` spike, dropna vs fillna | challenge |

Exercise 2 has two checks that print `False` until the recipe is right. Students who get `(290, 10)` fell into the
step-3 trap; ask them "where did the 8 students go?" rather than telling them.

Expected outcome: everyone completes 1–2, most 3, Exercises 4–5 become homework and feed directly into Project 06.

## 9. Project 06 launch (7 min)

Open [the brief](../../../projects/06-data-analysis-report/README.md) and walk through it:

- Deliverable: one notebook, `report.ipynb`, starting from `starter/report.ipynb`. Due **Day 47**.
- Default dataset: `students_raw.csv` (today's cleaning is step 2 of the report). Alternatives: `expenses.csv`
  or `apartments.csv`.
- Must: load + inspect, documented cleaning, ≥ 5 questions answered with pandas, ≥ 3 labelled charts, Findings
  (3–5 bullets) and Limitations.
- Show the rubric, especially "clarity of charts" and "quality of written conclusions".
- Tonight: steps 1–2 of the build plan (load, inspect, clean) + write the 5 questions.

## 10. Recap and exit ticket (3 min)

Recap (students supply it): find → clean in a written order → check → explore → chart → write what it means.

**Exit ticket:** match each question to a chart: (a) "Do older apartments cost less?" (b) "How old are the
apartments?" (c) "Which has a higher average price: apartments with or without parking?"

Answer: (a) scatter (`age_years` vs `price_k`) · (b) histogram of `age_years` · (c) bar chart of mean `price_k` by
`has_parking`.

## Homework (30 min)

Finish Exercises 3–4. Start Project 06: complete sections 1–2 of `starter/report.ipynb` (load, inspect, clean) and
write your five questions in the Questions section.

## Next class

Day 46 starts with **Checkpoint 9** (15 min, [assessments/weekly/week-09-checkpoint.md](../../../assessments/weekly/week-09-checkpoint.md)),
then begins machine learning with scikit-learn on exactly today's clean `students.csv`: features `X`, target `y`,
train/test split, and a baseline (the 71 % "always pass" from Day 41 returns).

## Instructor notes

- The recipe must be applied **exactly** as written (order and median) to reproduce `students.csv`; that file is
  used by Days 46–50 and Project 07. If students invent other cleaning, that is fine in their project, but not in
  Exercise 2.
- pandas 3 uses copy-on-write, so `df[col] = ...` after a filter does not raise `SettingWithCopyWarning`. If a
  student on an old pandas sees that warning, `df = df[keep].copy()` silences it. Do not go deeper.
- Keep matplotlib to the `plt.` functions. Do not introduce `fig, ax = plt.subplots()`, seaborn, colours/styles
  or saving figures; `plt.xticks(rotation=45)` is the only optional polish.
- `numeric_only=True` is needed because `mean()` on text columns raises a `TypeError` in pandas 3.
- Fast students: Exercise 6 (side effects of filling), then a line chart of total spending per month from
  `expenses.csv`. Slow students: let them use `clean_students()` from the demo for Exercise 2 and focus on charts.
