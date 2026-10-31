# Checkpoint 10: Week 10 (Days 46–49)

**Given in the first 20 minutes of Day 50 · 10 points · individual, on paper, closed notes, no running code**

Name: ______________________ Date: ____________

Write your answers under each question. If you are not sure, write your best guess **and one sentence of
reasoning**: partial answers earn partial points. In all questions `pandas` is imported as `pd`, and these
imports have already run:

```python
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
```

`df` is `students.csv` (298 rows, target `passed`: 1 = pass, 0 = fail) and `apts` is `apartments.csv`.

## Part A: Predict the output

Write **exactly** what each program prints.

**1.**
```python
X = df[["study_hours", "previous_score"]]
y = df["passed"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape, X_test.shape, y_test.shape)
```

**2.**
```python
y_train = pd.Series([1, 1, 0, 1, 0, 1])
y_test = pd.Series([0, 1, 1, 0])
baseline = DummyClassifier(strategy="most_frequent")
baseline.fit(pd.DataFrame({"hours": [1, 2, 3, 4, 5, 6]}), y_train)
predictions = baseline.predict(pd.DataFrame({"hours": [7, 8, 9, 10]}))
print(predictions)
print((predictions == y_test).mean())
```

**3.**
```python
print(mean_absolute_error([60, 45, 80, 52], [55, 50, 72, 52]))
print(confusion_matrix([0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0]))
```
Then answer in words: in the confusion matrix, how many real 0s were predicted as 1?

## Part B: Find and fix

**4.** This cell crashes. Explain why in one sentence, then write a corrected version that also evaluates the model
**fairly**.

```python
model = LinearRegression()
model.fit(apts["area_sqm"], apts["price_k"])
```

**5.** This cell runs without an error and prints `accuracy: 1.0`. Name **two** problems and write a fixed version.

```python
features = ["study_hours", "attendance_pct", "final_score"]
X_train, X_test, y_train, y_test = train_test_split(df[features], df["passed"], test_size=0.2, random_state=42)
tree = DecisionTreeClassifier(max_depth=2, random_state=42)
tree.fit(X_train, y_train)
print("accuracy:", tree.score(X_train, y_train))
```

## Part C: Write code

**6.** Using `apts`, predict `price_k` from `area_sqm` and `distance_km`: split 80/20 with `random_state=42`, train a
`LinearRegression`, and print the **test** MAE and the **baseline** MAE (always guessing the training mean; you may
use `DummyRegressor` or compute it yourself).

**7.** `model` is a classifier already trained with `FEATURES = ["study_hours", "previous_score"]` (1 = pass).
Write `predict_one(example)` that takes a dict such as `{"study_hours": 9, "previous_score": 70}`, raises a
`ValueError` if a feature is missing, and otherwise returns the word `"pass"` or `"fail"`.

## Part D: Explain in words

**8.** A tree-depth experiment on student data gave:

| max_depth | train accuracy | test accuracy |
|-----------|----------------|---------------|
| 1 | 0.73 | 0.65 |
| 3 | 0.85 | 0.77 |
| 8 | 0.98 | 0.70 |

(a) Which depth underfits and which overfits? How can you tell from the numbers?
(b) Bilal picks depth 3 *because* it has the best test accuracy and reports "my model is 77% accurate".
What is the problem, and what should he have done?

## Part E: Retrieval (earlier weeks)

**9.** (Week 9) What does this print?
```python
students = pd.DataFrame({
    "name": ["Asha", "Omar", "Mei", "Ken"],
    "hours": [12, 4, 9, 6],
    "passed": [1, 0, 1, 0],
})
print(students[students["hours"] > 5]["passed"].mean())
print(students.groupby("passed")["hours"].mean())
```

**10.** (Weeks 4–5) What does this print?
```python
def grade(score):
    if score >= 50:
        return "pass"
    return "fail"


scores = {"Sara": 72, "Bilal": 48, "Zara": 50}
results = [grade(s) for s in scores.values()]
print(results)
print(results.count("pass"))
```

---

_Answer key (instructor only, not published): `assessments/answer-keys/week-10-checkpoint.md`_
