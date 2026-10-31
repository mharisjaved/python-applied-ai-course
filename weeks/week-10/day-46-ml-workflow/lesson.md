# Day 46: The Machine-Learning Workflow and the Train/Test Split

**Week 10 · Session 46 of 60 · Planned 75 min** · Previous: [Day 45](../../week-09/day-45-cleaning-visualization/lesson.md) · Next: [Day 47](../day-47-regression/lesson.md)

## Objectives

By the end of this lesson students can:

1. List the steps of the supervised-learning workflow (question → data → `X`/`y` → split → baseline → train → evaluate → predict).
2. Build a feature table `X` (double brackets) and a target `y` (single brackets) from a DataFrame.
3. Split data with `train_test_split(..., test_size=0.2, random_state=42)` and explain, with the exam analogy, why the test set stays hidden.
4. Compute a baseline (most common class, or the training mean) by hand and with `DummyClassifier` / `DummyRegressor`.
5. Use the scikit-learn pattern create → `fit` → `predict`/`score` and say whether a model beats the baseline.

**Prior knowledge:** rules vs learning and the hand-searched study-hours threshold (Day 41), features vs target
(Day 42), boolean masks and `mean` (Day 43), `read_csv`, column selection, `value_counts` (Day 44), cleaning
`students_raw.csv` into `students.csv` (Day 45). `from … import …` (Day 26), lists of dicts (Day 08).

**New today:** scikit-learn (`sklearn`), `train_test_split`, `DummyClassifier`, `DummyRegressor`,
`DecisionTreeClassifier` as a "threshold finder" (properly on Day 48), `export_text`, `.fit` `.predict` `.score`,
`pd.DataFrame([...])` from a list of dicts, `Series.abs()`.

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only) ·
Checkpoint 9: [assessments/weekly/week-09-checkpoint.md](../../../assessments/weekly/week-09-checkpoint.md)

## Timing

Checkpoint 9 (Week 9) is given at the start of today because Day 45 was full. To make room, the warm-up is
folded into the checkpoint and the regression baseline (demo section 8) is shown quickly.

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:15 | Checkpoint 9 (Week 9 quiz, on paper) | core |
| 0:15–0:19 | The workflow, bridge from Day 41 (demo section 1) | core |
| 0:19–0:29 | `X`/`y` and the train/test split (demo sections 2–3) | core |
| 0:29–0:37 | Baseline by hand, then `DummyClassifier`: create → fit → predict (sections 4–5) | core |
| 0:37–0:44 | First real model, predict a new student (sections 6–7) | core |
| 0:44–0:47 | Regression baseline: "average miss" (section 8) | core |
| 0:47–0:50 | Common mistakes (section 9) | core |
| 0:50–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 together (how much the split matters) | optional (90-min session) |

**For 60 min:** keep the checkpoint, skip demo section 8 (students meet it in Exercise 4b) and mistake 4,
and set Exercises 4–5 as homework.

## 1. Checkpoint 9 (15 min)

Hand out [week-09-checkpoint.md](../../../assessments/weekly/week-09-checkpoint.md). Collect it, then use one
question from it about features vs target as the bridge into today: "Which column was the *target* in
`students.csv`?" (*`final_score` for numbers, `passed` for yes/no.*)

## 2. The workflow (4 min)

**Why a workflow?** On Day 41 students tried thresholds ("pass if study hours ≥ 8") and kept the one that was
right most often, *on the same students they used to choose it*. Two questions they could not answer then:
*Would the rule work for next year's students? Is it better than not thinking at all?* Today's workflow answers
both. Show the seven steps in demo section 1 and keep them on the board all week:

```
question → data → X / y → split → baseline → train (fit) → evaluate (test set) → use (predict)
```

*Supervised* = every training row comes with the right answer.

## 3. `X`, `y` and the train/test split (10 min)

Live code (demo section 2):

```python
features = ["study_hours", "previous_score"]
X = df[features]      # double brackets → a table   (298, 2)
y = df["passed"]      # single brackets → one column (298,)
```

Make the bracket rule explicit: a **list** of column names inside the brackets gives a table. scikit-learn always
wants `X` as a table, even with one feature: `df[["study_hours"]]`.

> **Exam analogy:** if you grade students with the exact questions they practised, someone who memorised the answer
> sheet scores 100% and understands nothing. A fair exam uses *new* questions. The **test set** is the new exam: the
> model never sees it while learning.

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# training rows: 238   test rows: 60
```

Key points:
- Order of results: **X before y, train before test**. Swapping them gives no error, just nonsense (Exercise 3).
- `test_size=0.2` → 20% (rounded up: 59.6 → 60 rows).
- The split shuffles. `random_state=42` fixes the shuffle so the whole room, and next week's you, get the same rows.

**Prediction question** (demo section 3): "Same `random_state` again: same first test students? And with 7?"
(*Same: 159, 264, 254. With 7: different students.*)

## 4. Baseline and the fit/predict pattern (8 min)

**Intuition:** before praising a model, ask what a no-brain guess scores. A weather app that always says "no rain"
is right most days in a dry city. That does not make it a good forecaster.

Demo section 4: `y_train.value_counts()` → 173 pass, 65 fail. Rule: always say 1.

```python
correct = (y_test == 1)
correct.mean()        # 0.65
```

Explain the mean of True/False = fraction of True (Day 43 masks). **Prediction question:** "Roughly what accuracy
will 'always pass' get?" Many say 71% (the overall pass rate). The test set happens to have 65% passers, which is
itself a lesson: the baseline depends on the split.

Demo section 5 introduces the pattern every model follows:

```python
baseline = DummyClassifier(strategy="most_frequent")   # create
baseline.fit(X_train, y_train)                          # learn from training data ONLY
baseline.predict(X_test)                                # [1 1 1 1 ...]
baseline.score(X_test, y_test)                          # 0.65 (accuracy)
```

## 5. A first real model (7 min)

Present the decision tree as **"the Day 41 threshold search, automated"**: it tries many thresholds on every
feature and keeps the question that best separates pass from fail. `max_depth` = how many questions in a row.
(Day 48 covers trees properly; today it is just our first real model.)

**Prediction question** (demo section 6): "A tree allowed one question. Will it beat 0.65?" Let students vote.
Answer: no, exactly 0.65. `export_text` shows why: it splits on `previous_score <= 64.5` but both groups are
mostly passers, so both leaves say "pass". *A model can learn something and still be useless; only the baseline
reveals this.*

With `max_depth=2`: accuracy **0.733**. Read a rule aloud: "previous score ≤ 64.5 **and** study hours ≤ 7.65 →
fail." 0.733 vs 0.65 on 60 students ≈ 5 more students classified correctly.

Demo section 7: predict for new students. The input must be a table with the **same columns**:

```python
new_students = pd.DataFrame([
    {"study_hours": 12, "previous_score": 70},   # Asha
    {"study_hours": 4, "previous_score": 50},    # Omar
])
model.predict(new_students)     # array([1, 0])
```

`pd.DataFrame([...])` is new: a list of dicts → one row per dict, keys become columns.

## 6. Regression baseline (3 min)

Demo section 8: for a number target the no-brain guess is the **training mean** (56.45 for everyone).
Accuracy makes no sense for numbers, so ask "how far off, on average?":

```python
misses = (yr_test - mean_predictions).abs()
misses.mean()      # 8.8 points
```

Tomorrow this number gets its name (MAE) and a real model that beats it.

## 7. Common mistakes (3 min)

Run the tagged cells in demo section 9 and read the last line of each error together.

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `tree.fit(df["study_hours"], y)` | `ValueError: Expected a 2-dimensional container but got <class 'pandas.Series'>` | `X` must be a table: `df[["study_hours"]]` |
| `predict` before `fit` | `NotFittedError: ... is not fitted yet` | A new model knows nothing until `.fit` |
| New data with other column names (`"hours"`) | `ValueError: The feature names should match those that were passed during fit` | Same columns, same spelling, as `X_train` |
| Scoring on the training data | **no error**: 0.99 on training vs 0.68 on test | Grading with practised questions. Always report the test score |
| Unpacking the split in the wrong order | **no error**: "train" has 60 rows | X before y, train before test. Print `len(X_train)` |

## 8. Practice (20 min)

Students open `practice.ipynb`. Circulate and watch for:
- `df["a", "b"]` (single brackets with two names → `KeyError`);
- forgetting `random_state`, then "my numbers don't match the expected output";
- computing the baseline with `df["passed"]` (all rows) instead of `y_train`/`y_test`;
- in Exercise 5, students who "fix" the tree that fails to beat the baseline by changing `random_state` until it
  wins. Stop that publicly: choosing the split by its result is cheating the exam (Day 49 calls it leakage).

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the split sizes | `test_size`, rounding | recall/predict |
| 2 Features and target for a new question | building `X`, `y`, split | application |
| 3 Fix the broken code | brackets, unpacking order, `random_state` | modification |
| 4 Two baselines | baseline by hand + `DummyClassifier`/`DummyRegressor` | application |
| 5 Does the tree beat the baseline? | fit/score/predict, interpreting a "no" | problem solving |
| 6 How much does the split matter? (challenge) | loop over `random_state` | challenge |

Expected outcome: everyone finishes 1–4, most finish 5 (its first model **does not** beat the baseline, and
that is the point), fast students do 6.

## 9. Recap and exit ticket (5 min)

Ask students to supply:
1. The workflow: question → data → `X`/`y` → split → baseline → fit → evaluate on test → predict.
2. The test set is the hidden exam; we never train on it.
3. A model is only "good" if it beats the baseline on the same test set.

**Exit ticket:** A classmate says: "My model is 70% accurate on the test set, so it is good." Ask two questions
that would tell you whether that is true.

Answer (any two): *What does the baseline score on the same test set? (If 72% of test students passed,
"always pass" beats it.) Was the 70% measured on the test set, not the training set? Was `random_state`
fixed so the result can be reproduced?*

## Homework (20 min)

Finish Exercises 4–5. In a markdown cell, explain in 3–4 sentences to a friend who missed class why we split the
data before training, using your own analogy (not the exam one). Project 06 (data analysis report) is due
next class.

## Next class

Day 47: **regression**. A `LinearRegression` model draws the best straight line through the points, its numbers
read as "each extra study hour adds about 1.5 points", and today's "average miss" becomes **MAE**. Tease: "Today
guessing the average missed by 8.8 points. Can a line do better?"

## Instructor notes

- The 60-student test set is small: one student = 1.7 percentage points. Do not over-interpret 0.733 vs 0.75.
- Students may ask why the test set's pass rate (65%) differs from the dataset's (71%). Answer: randomness of the
  split; that is exactly why we compare with a baseline computed on the same split.
- Do not explain *how* the tree picks its questions (impurity, Gini). "It tries thresholds and keeps the one that
  separates pass from fail best" is enough. Same for `strategy` options of the dummies beyond the two used.
- `X` capital and `y` lowercase is a maths convention (a table vs a single column). Mention it once; do not
  enforce it as a Python rule.
- Fast students: Exercise 6, then ask them to find a pair of features whose depth-2 tree beats 0.75.
- Slow students: pair them; the copy-able pattern is the four lines create → fit → predict → score.
- Every later day this week reuses `test_size=0.2, random_state=42` on `students.csv`, so the same 60 test
  students appear all week. The baseline to beat for `passed` is always **0.65**.
