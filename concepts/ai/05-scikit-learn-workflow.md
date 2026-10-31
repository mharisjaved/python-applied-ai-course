# The scikit-learn Workflow

**What it is:** scikit-learn (`sklearn`) trains models with the same few steps every time: split → `fit` → `predict` → evaluate.
**Why it exists:** it lets you try regression and classification models in a few lines, and measure honestly how good they are on data they have never seen.

**Taught on:** [Day 46](../../weeks/week-10/day-46-ml-workflow/lesson.md) (workflow, split, baseline) ·
[Day 47](../../weeks/week-10/day-47-regression/lesson.md) (regression, MAE) ·
[Day 48](../../weeks/week-10/day-48-classification/lesson.md) (classification, confusion matrix) ·
[Day 49](../../weeks/week-10/day-49-evaluation-overfitting/lesson.md) (overfitting, precision/recall, leakage)

## The workflow

1. **Question:** what do we predict (the *target*), from what (the *features*)? Number → regression; category → classification.
2. **`X` and `y`:** `X = df[[feature columns]]` (a table, capital X) · `y = df["target"]` (one column).
3. **Split:** `train_test_split(X, y, test_size=0.2, random_state=42)` (same split every run). Lock the test set away.
4. **Baseline:** the score of a "dumb" guess (the average; the most common class). A model must beat it.
5. **Train:** `model.fit(X_train, y_train)`. Only training data!
6. **Predict and evaluate:** `model.predict(X_test)` → compare with `y_test` using a metric.
7. **Improve and check for problems:** overfitting (train ≫ test score), leakage (too good to be true).

**Models:** `LinearRegression()` (a number) and `LogisticRegression()` (a class) from `sklearn.linear_model`;
`DecisionTreeClassifier(max_depth=3, random_state=42)` (a class, via yes/no questions) from `sklearn.tree`.

## Metric cheat table

| Metric | Task | In plain words | Good when… | Code (`from sklearn.metrics import …`) |
|--------|------|----------------|------------|-----------------------------------------|
| **MAE** (mean absolute error) | regression | average size of the mistake, in the target's units: "off by 4.8 points on average" | lower than the baseline's MAE | `mean_absolute_error(y_test, pred)` |
| **Accuracy** | classification | share of predictions that were right | higher than "always guess the most common class" | `accuracy_score(y_test, pred)` |
| **Confusion matrix** | classification | table: rows = actual class, columns = predicted class (below: 0 = fail, 1 = pass) | big numbers on the diagonal | `confusion_matrix(y_test, pred)` |
| **Precision** | classification | of all the students we *predicted* "pass", how many really passed? TP / (TP + FP) | false alarms are costly | `precision_score(y_test, pred)` |
| **Recall** | classification | of all the students who *really* passed, how many did we find? TP / (TP + FN) | missing one is costly (e.g. illness) | `recall_score(y_test, pred)` |

```text
                 predicted 0     predicted 1
actual 0         TN (right)      FP (false alarm)
actual 1         FN (missed)     TP (right)
```

## Examples

### 1. Data, `X`/`y` and the split

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Made-up data so this runs anywhere (in class we use datasets/students.csv)
rng = np.random.default_rng(0)
df = pd.DataFrame({
    "study_hours": rng.uniform(0, 15, 200).round(1),
    "attendance_pct": rng.integers(40, 101, 200),
})
noise = rng.normal(0, 6, 200)
df["final_score"] = (5 + 3 * df["study_hours"] + 0.4 * df["attendance_pct"] + noise).round(1)
df["passed"] = (df["final_score"] >= 50).astype(int)

X = df[["study_hours", "attendance_pct"]]   # features (a table)
y = df["final_score"]                       # target (one column)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape, X_test.shape)          # (160, 2) (40, 2)
```

### 2. Regression: baseline vs `LinearRegression`

```python
# (continues from example 1)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

baseline = [y_train.mean()] * len(y_test)   # guess the average score for everyone
print(round(mean_absolute_error(y_test, baseline), 1))      # 14.3

model = LinearRegression()
model.fit(X_train, y_train)
pred = model.predict(X_test)
print(round(mean_absolute_error(y_test, pred), 1))          # 4.8
print(model.coef_.round(2))   # [2.92 0.37]   (+2.92 points per study hour, +0.37 per attendance %)

new_student = pd.DataFrame({"study_hours": [8.0], "attendance_pct": [90]})
print(model.predict(new_student).round(1))                  # [64.2]
```

### 3. Classification: accuracy, confusion matrix, precision, recall

```python
# (continues from example 2)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score

y = df["passed"]   # new target: 1 = passed, 0 = failed
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
print(accuracy_score(y_test, [1] * len(y_test)))   # 0.64   (baseline: always guess "pass")

clf = LogisticRegression()
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
print(accuracy_score(y_test, pred))                # 0.86
print(confusion_matrix(y_test, pred))
# [[17  1]
#  [ 6 26]]
print(round(precision_score(y_test, pred), 2), round(recall_score(y_test, pred), 2))   # 0.96 0.81
```

### 4. Overfitting: the tree-depth experiment

```python
# (continues from example 3)
from sklearn.tree import DecisionTreeClassifier

for depth in [1, 3, None]:   # None = no limit
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree.fit(X_train, y_train)
    print(depth, round(tree.score(X_train, y_train), 2), round(tree.score(X_test, y_test), 2))
# 1 0.87 0.82
# 3 0.91 0.86
# None 1.0 0.84   <- memorised the training set, worse on new data: OVERFITTING
```

`model.score(X, y)` is accuracy for classifiers (for regressors it is R², which this course does not use).

### 5. Leakage: a score that is too good to be true

```python
# (continues from example 4)
leaky_X = df[["study_hours", "attendance_pct", "final_score"]]   # final_score DEFINES passed
Xl_train, Xl_test, yl_train, yl_test = train_test_split(leaky_X, y, test_size=0.25, random_state=42)
leaky_tree = DecisionTreeClassifier(random_state=42)
leaky_tree.fit(Xl_train, yl_train)
print(leaky_tree.score(Xl_test, yl_test))   # 1.0   (perfect and useless: final_score is unknown when you predict)
```

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| `X = df["study_hours"]` (one column, single brackets) | `ValueError: Expected a 2-dimensional container but got <class 'pandas.Series'> instead…` | `X = df[["study_hours"]]` |
| Text columns in `X` (`"arts"`) | `ValueError: could not convert string to float: 'arts'` | Use numeric columns (or turn yes/no into 1/0 first) |
| `predict` before `fit` | `NotFittedError: This LinearRegression instance is not fitted yet…` | Call `model.fit(X_train, y_train)` first |
| Fitting on all the data, then testing on part of it | scores look great, model fails on new data | Split first; fit only on the training set |
| Wrong order: `X_train, y_train, X_test, y_test = train_test_split(…)` | shapes look odd, nonsense scores | Order is `X_train, X_test, y_train, y_test` |
| Accuracy without a baseline on unbalanced data | 64% "sounds good" but guessing "pass" already gets 64% | Always print the baseline |
| A feature that contains the answer (leakage) | ~100% test score | Ask: "would I know this value *before* the prediction?" |

## See also

- [01 AI vocabulary](01-ai-vocabulary.md): features, target, overfitting, leakage in plain words
- [03 pandas](03-pandas.md): preparing `X` and `y`
- [04 matplotlib](04-matplotlib.md): predicted-vs-actual plot
