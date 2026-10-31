# Day 47: Regression: Predicting a Number

**Week 10 · Session 47 of 60 · Planned 75 min** · Previous: [Day 46](../day-46-ml-workflow/lesson.md) · Next: [Day 48](../day-48-classification/lesson.md)

## Objectives

By the end of this lesson students can:

1. Decide whether a question is **classification** (a category) or **regression** (a number).
2. Train a `LinearRegression` model and explain `coef_` and `intercept_` in plain words ("each extra study hour adds about 1.5 points, holding the others fixed").
3. Compute the **MAE** by hand and with `mean_absolute_error`, state it in the target's units, and compare it with the baseline MAE.
4. Convert a yes/no text column into 0/1 so a model can use it.
5. Draw and read a predicted-vs-actual scatter plot.

**Prior knowledge:** Day 46 workflow, `train_test_split`, `DummyRegressor`, "average miss" with `.abs().mean()`,
`pd.DataFrame([...])`; matplotlib `scatter` with labels (Day 45); `zip` (Day 21); format specs `:.2f` (Day 05).

**New today:** `LinearRegression`, `coef_`, `intercept_`, `mean_absolute_error`, R² via `model.score` (optional),
`.astype(int)`, `pd.DataFrame({...})` from a dict of columns, `plt.plot` for a line, `plt.legend` with `label=`.

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students, uses `apartments.csv`) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: Day 46 workflow + Project 06 hand-in | core |
| 0:05–0:08 | Classification vs regression (demo section 1) | core |
| 0:08–0:20 | One feature: a line through the points, slope and intercept (section 2) | core |
| 0:20–0:28 | MAE by hand and with sklearn, vs the baseline (section 3) | core |
| 0:28–0:40 | Six features: text → 0/1, coefficients in plain words (section 4) | core |
| 0:40–0:45 | Predicted-vs-actual plot, predicting for Asha (sections 6–7) | core |
| 0:45–0:48 | Common mistakes (section 8) | core |
| 0:48–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +5 min | R² as "share of differences explained" (section 5) | optional |
| +10 min | Exercise 6 together | optional (90-min session) |

**For 60 min:** skip section 5 (R²) and the training-vs-test MAE cell, and set Exercise 5 as homework.

## 1. Warm-up (5 min)

Collect Project 06 (data analysis report). Then retrieval questions:
- "Name the steps of yesterday's workflow." (*question → data → X/y → split → baseline → fit → evaluate → predict*)
- "Yesterday's regression baseline missed by 8.8 points. What did it predict for every student?" (*The training mean, about 56.5.*)
- "Why `df[["study_hours"]]` and not `df["study_hours"]` for `X`?" (*X must be a table.*)

## 2. Classification vs regression (3 min)

Show the table in demo section 1. Quick test, hands up: price of a used phone? (*regression*) Will a parcel
arrive late, yes/no? (*classification*) Number of visitors tomorrow? (*regression*). The rule: if "close" makes sense
(98 vs 100), it is regression.

## 3. A line through the points (12 min)

**Intuition:** show the scatter (demo section 2). "If I gave you a ruler and said: draw *one* straight line that
stays as close to as many points as possible, you could do it by eye. `LinearRegression` does the same, but
measures 'close' exactly." No formulas: a line needs only a **starting height** and a **slope**.

```python
line_model = LinearRegression()
line_model.fit(X_train, y_train)        # X = df[["study_hours"]], y = df["final_score"]
line_model.coef_                        # [1.48756108]  ← slope
line_model.intercept_                   # 43.15...      ← start (0 hours)
```

Say it in words and write it on the board: **predicted score = 43.2 + 1.49 × study hours**. "Each extra study hour
adds about 1.5 points." The intercept is the predicted score at 0 hours.

**Prediction question:** "What does the line predict for 10 hours?" Students compute 43.15 + 14.9 ≈ **58.0**, then
run `predict` (58.03). This shows the model is nothing magic: two numbers and a multiplication.

Draw the line (`plt.plot` with the predictions at 0 and 22 hours). Point out that many points are far from the
line: study hours are not the whole story.

## 4. How wrong are we? MAE (8 min)

Build the comparison table (demo section 3): `actual`, `predicted`, `miss = |actual − predicted|`. Read two rows:
student 264 was predicted perfectly (55.4); student 254 was off by 13.7.

```python
mean_absolute_error(y_test, predictions)      # 7.30
```

**MAE = mean absolute error = the average miss, in the target's units (points).** Yesterday's "average miss" was
MAE all along. **Prediction question:** "Will the line beat the baseline's 8.8?" (*Yes: 7.3. Better, but still large.*)

Key points: always compare with the baseline MAE · MAE is easy to explain to anyone ("about 7 points off on
average") · a lower MAE is better.

## 5. Six features and plain-words coefficients (12 min)

Text must become numbers. Demo section 4:

```python
df["has_job_num"] = (df["has_job"] == "yes").astype(int)   # "yes" → 1, "no" → 0
```

Explain in two steps: `==` gives True/False (Day 43/44), `.astype(int)` turns True → 1, False → 0.

With six features the MAE drops to **5.04**. **Prediction question:** "Which coefficient will be negative?"
(*`has_job_num`, −4.54.*) Print with `zip(features, model.coef_)`:

```
study_hours: 1.63      attendance_pct: 0.24     sleep_hours: 1.59
previous_score: 0.36   assignments_done: 1.13   has_job_num: -4.54
```

Teach the sentence template: **"One more [unit] of [feature] changes the predicted score by [coef] points, if all
other features stay the same."** Have two students say it for `sleep_hours` and `has_job_num`.

Three warnings to say out loud:
1. **Units:** 0.24 per *percent* vs 1.63 per *hour*. Bigger number ≠ more important feature.
2. **Not a cause:** "having a job is linked to 4.5 lower points in this data", not "a job lowers your score".
3. The intercept (−19) means nothing alone here: no student has 0% attendance and a previous score of 0.

Optional (section 5): `model.score(X_test, y_test)` gives **R² ≈ 0.67**: "these six features explain about two
thirds of the differences between students' scores". One feature: 0.28. No formula.

## 6. Predicted vs actual, and using the model (5 min)

Demo section 6: scatter of `y_test` (x) vs `predictions` (y) with a red diagonal `plt.plot([20, 100], [20, 100])`.
"Points on the line = perfect. Vertical distance = the miss." Ask: "Where does the model struggle?" (*Look for
points far from the line. With 60 points the picture is rough; that is fine.*)

Demo section 7: predict Asha's score with a one-row DataFrame → **69.8**. Model the honest phrasing: "about 70,
give or take 5 points" (the MAE).

## 7. Common mistakes (3 min)

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| A text column in `X` (`has_job`) | `ValueError: could not convert string to float: 'no'` | Models do maths; convert yes/no to 1/0 first |
| New example missing some features | `ValueError: The feature names should match ...` (lists the missing ones) | Give every training column, same spelling |
| `mean_absolute_error(y_train, test_predictions)` | `ValueError: Found input variables with inconsistent numbers of samples` | Compare test answers with test predictions |
| Reporting training MAE (4.91) instead of test MAE (5.04) | **no error** | The model has seen the training rows; report test |
| "Bigger coefficient = more important" | **no error**, wrong conclusion | Coefficients depend on units (practice Exercise 6) |

## 8. Practice (22 min)

Students use `apartments.csv` (`price_k` = price in thousands). Circulate and watch for:
- `apts["area_sqm"]` as `X` (1-D error again; point at yesterday's fix);
- computing the by-hand price without the intercept;
- reading `has_parking` +11.6 as "parking costs 11.6": it is "apartments with parking are predicted 11.6 thousand
  higher, other things equal";
- plots without axis labels: insist on labels with units ("price (thousands)").

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Classification or regression? | choosing the task and baseline | recall |
| 2 Baseline for apartment prices | `DummyRegressor`, MAE | application |
| 3 A line for price vs area | coef/intercept in words, by-hand prediction | application |
| 4 Fix the broken code | train on test, wrong MAE inputs, missing feature | modification |
| 5 All the features | coefficients, plot, new prediction | problem solving |
| 6 Which single feature is most useful? (challenge) | loop + results, coefficient ≠ usefulness | challenge |

Expected numbers (same split for everyone): baseline 54.2 · area only 29.7 (coef 2.29, intercept 18.2) · six
features 12.2 · Zara's apartment 225.4.

## 9. Recap and exit ticket (5 min)

Ask students to supply:
1. Regression predicts a number; `LinearRegression` learns one slope per feature plus a start value.
2. A coefficient = change in prediction for one more unit of that feature, others fixed. A pattern, not a cause.
3. MAE = average miss in the target's units; it must beat the baseline MAE.

**Exit ticket:** A model predicts apartment prices with `coef_` for `distance_km` = −3.0 and test MAE = 12.
Write two sentences a home buyer would understand.

Answer: *"Each extra kilometre from the centre lowers the predicted price by about 3 thousand, if everything else
is the same. On average the prediction is about 12 thousand away from the real price."*

## Homework (25 min)

Finish Exercise 5. Then, on `students.csv`, train a `LinearRegression` that predicts `final_score` **without**
`previous_score` and compare its MAE with today's 5.04. One sentence: what does the difference tell you?

## Next class

Day 48: **classification**: predicting `passed` (yes/no) with `LogisticRegression` and a deeper decision tree,
measuring with accuracy, and the **confusion matrix**, which shows *which kind* of mistakes a model makes. Tease:
"Two models can both be 80% accurate and still make completely different mistakes."

## Instructor notes

- Stay intuitive: no least squares, no gradient descent, no "minimising the sum of squared errors". "Closest
  line by an exact measure of closeness" is enough. If a strong student asks, say it minimises the squared misses
  and that this is for a later course.
- R² is optional. If you show it, say "share of the differences explained", never the formula. Do not let R² replace
  MAE: beginners can explain MAE to anyone.
- `final_score` is a fine regression target, but do not use `passed` as a feature for it (it is computed *from*
  `final_score`). Day 49 is the full leakage lesson; mention it only if a student tries.
- Students may ask about the `program` column (3 categories). Turning it into numbers needs one column per
  category; leave it out this week. Fast students can look up `pd.get_dummies` as an extension.
- The test set has 60 students: MAE numbers move a little with a different `random_state`. Keep 42 for the class.
- Fast students: Exercise 6, then try to beat MAE 12.2 on apartments by removing features (it gets worse; ask why).
- Slow students: pair them and give them the sentence template for coefficients on a card.
