# Day 48: Classification: Predicting a Category

**Week 10 · Session 48 of 60 · Planned 75 min** · Previous: [Day 47](../day-47-regression/lesson.md) · Next: [Day 49](../day-49-evaluation-overfitting/lesson.md)

## Objectives

By the end of this lesson students can:

1. Train a `LogisticRegression` and a `DecisionTreeClassifier` (small `max_depth`) to predict `passed`, and compare both with the baseline.
2. Compute and explain **accuracy** as "fraction of test students classified correctly".
3. Read a **confusion matrix** cell by cell in plain words (caught, missed, false alarm, correctly cleared).
4. Use `predict_proba` to say how confident a model is about one student, and explain that confident ≠ correct.
5. Follow a small decision tree by hand for a new student.
6. Explain in one sentence why `final_score` must not be a feature when predicting `passed`.

**Prior knowledge:** Day 46 (split, baseline 0.65, fit/predict, the tree as a threshold finder), Day 47
(`LinearRegression`, `has_job_num` with `.astype(int)`, a table from a dict of columns), 2-D indexing `[:, 1]` (Day 43).

**New today:** `LogisticRegression` (`max_iter`), `accuracy_score`, `predict_proba`, `plot_tree`,
`confusion_matrix`, `ConfusionMatrixDisplay.from_predictions`, a results table from a list of dicts; optional:
`DecisionTreeRegressor`, `load_iris`.

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: regression retrieval | core |
| 0:05–0:10 | Classes, baseline, the `final_score` leak (demo section 1) | core |
| 0:10–0:20 | Logistic regression + `predict_proba` (sections 2–3) | core |
| 0:20–0:28 | Decision tree: read it, follow it for Fatima (section 4) | core |
| 0:28–0:40 | Confusion matrix, cell by cell; compare models (sections 5–6) | core |
| 0:40–0:45 | Common mistakes (section 9) | core |
| 0:45–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +5 min | Trees for numbers: `DecisionTreeRegressor` (section 7) | optional |
| +5 min | Three classes: iris (section 8) | optional (90-min session) |

**For 60 min:** skip `plot_tree` (use `export_text` from Day 46 instead), sections 7–8, and set Exercise 5 as homework.

## 1. Warm-up (5 min)

- "Yesterday's model said: each extra study hour adds 1.6 points. What does 'holding others fixed' mean?"
  (*Comparing two students who are identical except for study hours.*)
- "MAE was 5.04. Explain it to a parent." (*On average the predicted score is about 5 points from the real one.*)
- "Today the target is `passed`. Regression or classification? What is the baseline?" (*Classification; always
  predict pass; 0.65 on our test set.*)

## 2. Classes and the forbidden column (5 min)

`df["passed"].value_counts()` → 212 pass, 86 fail. Two classes, 0 and 1.

**Leakage, briefly** (demo section 1): `passed` is *computed* from `final_score` (≥ 50). If we give the model
`final_score`, it learns "score ≥ 50" and looks perfect, but when you know the final score the exam is over,
so there is nothing to predict. **Rule: only use features you would know at the moment you need the prediction.**
Promise the full story (and a "too good to be true" demo) for tomorrow. Features today: the six
"before the exam" columns, including `has_job_num`.

## 3. Logistic regression and confidence (10 min)

**Intuition:** like yesterday's line, it adds up the features into one "pass score", then squeezes that score into
a probability between 0 and 1 (an S-shaped squeeze; draw a flat-S on the board if you like, no formula).
Above 0.5 → pass. The name says "regression" for historical reasons; it is a classifier.

```python
log_model = LogisticRegression(max_iter=1000)   # more attempts to settle; avoids a ConvergenceWarning
log_model.fit(X_train, y_train)
accuracy_score(y_test, log_model.predict(X_test))  # 0.85 (baseline 0.65)
```

0.85 = 51 of 60 correct vs 39 for the baseline.

`predict_proba` (demo section 3): two columns, P(fail) and P(pass). The table of the first five test students
shows student 264: actually passed, predicted fail with P(pass) = 0.23. **Prediction question:** "Which of the
five did the model get wrong?" Then: "Was the model *sure*?" Explain: 0.23 means "about 1 in 4 students like this
pass", so being wrong sometimes is expected. Near 0.5 = unsure. Near 0 or 1 = confident, **not** guaranteed right.

## 4. The decision tree, properly (8 min)

Recall Day 46: the tree is the automated threshold search. Now with `max_depth=3` and a picture
(`plot_tree`, demo section 4). Teach how to read one box:

- first line: the question (`previous_score <= 64.5`); **left arrow = yes (True), right = no (False)**;
- `samples` = training students reaching this box; `value = [fails, passes]`; `class` = the majority.

**Prediction question:** "Follow the tree for Fatima (previous 60, study 9 h, attendance 85%, no job)." Students
trace: 60 ≤ 64.5 yes → 9 ≤ 7.65 no → 85 ≤ 78 no → leaf `[3, 44]` → **pass**. `predict_proba` gives 0.94 = 44/47:
a tree's probability is just the share of passers in that leaf.

Tree accuracy: **0.767**, lower than logistic regression here. Small `max_depth` keeps it readable; tomorrow we
see what happens without the limit.

## 5. The confusion matrix (12 min)

**Why:** "Two models with the same accuracy can make completely different mistakes. If the school wants to help
students at risk, which mistake is worse: missing a struggling student, or worrying about one who is fine?"

```python
confusion_matrix(y_test, log_predictions)     # actual first, then predicted
# [[15  6]
#  [ 3 36]]
```

Draw the 2 × 2 grid on the board and fill it together. **Rows = what really happened, columns = what the model
said.**

| | said fail | said pass |
|-|-----------|-----------|
| **really failed (21)** | 15 caught | 6 **missed** |
| **really passed (39)** | 3 **false alarms** | 36 correctly cleared |

Read it as a story: "21 students failed; the model caught 15 and missed 6. Of 39 who passed, it wrongly worried about
3." Accuracy is the diagonal: (15 + 36) / 60 = 0.85. Then show the `ConfusionMatrixDisplay` picture (sklearn labels the
axes "True label" / "Predicted label"; point at them).

**Prediction question:** "The tree is less accurate (0.77). Will it miss more or fewer failing students?" Tree:
`[[12 9] [5 34]]` → misses **9**. Finish with the results table (demo section 6): baseline 0.65, logistic 0.85,
tree 0.767. The project requires exactly this kind of table.

## 6. Common mistakes (5 min)

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `final_score` (a number) as `y` for a classifier | `ValueError: Unknown label type: continuous` | Classifiers need classes. Use `passed`, or a regression model |
| `final_score` as a feature for `passed` | **no error**, accuracy near 100% | Leakage: known only after the event. Tomorrow's topic |
| `confusion_matrix(predictions, y_test)` | **no error**, the 6 and 3 swap | Actual first, like `accuracy_score(y_test, ...)` |
| Using column 0 of `predict_proba` as "chance of passing" | **no error** | Column order follows the classes: 0 = fail, 1 = pass |
| Reporting accuracy without the baseline | **no error** | Always put the baseline row in the results table |

## 7. Practice (25 min)

Circulate and watch for:
- reading the confusion matrix by columns ("15 + 3 failed"): ask "which side is reality?";
- in Exercise 3, students who run the model before tracing by hand: cover the screen, trace on paper first;
- in Exercise 4, students who fix only the crash and celebrate ~100% accuracy: ask "would you know
  `final_score` before the exam?";
- in Exercise 5, sorting by `P(pass)` instead of by distance from 0.5.

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Read a confusion matrix | reading cells in words, accuracy by hand | recall/reasoning |
| 2 Logistic regression with three features | fit, accuracy, confusion matrix | application |
| 3 Follow the tree by hand | `export_text`, tracing, predict | application |
| 4 Fix the broken code | continuous target, leakage, argument order | modification |
| 5 Who is the model unsure about? | `predict_proba`, sorting, counting mistakes | problem solving |
| 6 Three classes of wine (challenge) | 3-class baseline + confusion matrix | challenge |

Expected numbers: Ex 1 accuracy 0.783 · Ex 2 accuracy 0.80, `[[14 7] [5 34]]` · Ex 3 Ken → fail, tree 0.733 ·
Ex 5: 6 mistakes among the 15 least-sure students, 3 among the other 45 · Ex 6 baseline 0.40, tree 0.867.

## 8. Recap and exit ticket (5 min)

Ask students to supply:
1. Accuracy = fraction correct; compare with the baseline (0.65).
2. Confusion matrix: rows = actual, columns = predicted; the off-diagonal cells are the two kinds of mistakes.
3. `predict_proba` says how sure the model is, not whether it is right.

**Exit ticket:** `confusion_matrix(y_test, predictions)` gives `[[18 3] [9 30]]` (0 = fail, 1 = pass).
How many failing students were missed? How many false alarms? Accuracy?

Answer: *3 missed (failed, predicted pass); 9 false alarms (passed, predicted fail); accuracy (18 + 30) / 60 = 0.80.*

## Homework (20 min)

Finish Exercise 5. Then write 3–4 sentences: a school will use your pass/fail model to decide who gets a
free tutoring place. Which cell of the confusion matrix matters most to the school, and which to the students?

## Next class

Day 49: **evaluation, overfitting and leakage**. Why a tree with no depth limit scores 99% on training students and
68% on new ones; **precision and recall**, which give names to today's "missed" and "false alarm" cells; and the
"too good to be true" model that uses `final_score`.

## Instructor notes

- Do not show the logistic (sigmoid) formula or talk about log-odds. "Adds up the features, then squeezes into
  0–1" is the right level. Do not mention regularisation (`C`) either.
- If someone asks why `max_iter`: the model improves its line step by step; 1000 allows enough steps. Without it,
  unscaled features sometimes trigger a `ConvergenceWarning`. A warning is not an error, but we keep notebooks clean.
- "Accuracy" vs `.score`: for classifiers they are the same number. Show both once; then use `accuracy_score` for
  clarity.
- Trees: avoid Gini/entropy. "It picks the question that best separates pass from fail" is enough.
- The confusion-matrix vocabulary (true/false positive/negative) comes tomorrow, attached to a story. Today use plain
  words only: caught, missed, false alarm, correctly cleared.
- Fast students: Exercise 6, then section 8 of the demo (iris), then compare `max_depth` 2, 3, 4 on wine.
- Slow students: give them the 2 × 2 grid template on paper with "really failed / really passed" pre-written as
  row labels.
