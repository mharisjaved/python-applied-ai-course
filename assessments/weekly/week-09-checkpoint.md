# Checkpoint 9: Week 9 (Days 41–45)

**Given in the first 15–20 minutes of Day 46 · 10 points · individual, on paper, closed notes, no running code**

(Week 9 ends with the Project 06 launch on Day 45, so the checkpoint moves to the start of the next session.)

Name: ______________________ Date: ____________

Write your answers under each question. If you are not sure, write your best guess **and one sentence of
reasoning**: partial answers earn partial points. In all questions, `numpy` is imported as `np` and `pandas` as `pd`.

## Part A: Predict the output

Write **exactly** what each program prints (for pandas output, the values and their labels are enough).

**1.**
```python
marks = np.array([40, 70, 60, 80, 55])
passed = marks >= 60
print(passed.sum(), marks[passed].mean())
print(marks + 5)
```

**2.**
```python
orders = pd.DataFrame({
    "customer": ["Asha", "Omar", "Asha", "Mei", "Omar"],
    "amount": [20, 35, 10, 50, 15],
})
print(orders.shape)
print(orders.groupby("customer")["amount"].sum())
print(len(orders[orders["amount"] > 15]))
```

**3.**
```python
answers = pd.Series([" Yes", "no", "YES", "No ", "yes"])
print(answers.str.strip().str.lower().value_counts())
```

## Part B: Find and fix

**4.** This line should keep the food purchases above 30 in `expenses`, but it crashes with
`ValueError: The truth value of a Series is ambiguous`. Explain why and rewrite it.

```python
big_food = expenses[expenses["category"] == "food" and expenses["amount"] > 30]
```

**5.** `raw` has 300 rows: 2 have impossible values and 8 have a **missing** `study_hours`. This filter should
remove only the 2 impossible rows (298 left), but the result has 290 rows. (a) Explain what went wrong. (b) Fix it.

```python
clean = raw[(raw["attendance_pct"] <= 100) & (raw["study_hours"] >= 0)]
```

## Part C: Write code

**6.** `students` is a clean DataFrame with columns including `passed` (0/1) and `sleep_hours`. Write **one line** of
pandas that shows the average `sleep_hours` of students who failed (0) and of students who passed (1).

**7.** Write matplotlib code for a chart that answers *"Do students who attend more classes get higher final
scores?"* using the columns `attendance_pct` and `final_score` of `students`. Include a title and axis labels.
Then write one sentence: what can this chart **not** tell you?

## Part D: Explain in words

**8.** A gym wants to predict whether a member will **cancel** their membership next month (`cancelled`: yes/no).
It has two years of records with the columns `member_id`, `age`, `visits_last_month`, `plan` (basic/premium) and
`cancelled`.

(a) Name the target and two features. Which column should **not** be used as a feature, and why?
(b) Is this a job for hand-written rules, machine learning or generative AI? One sentence why.
(c) Give one reason the predictions could be worse (or unfair) for some members.

## Part E: Looking back (Weeks 3 and 7)

**9.** What does this print? Then name the pandas method that does the same counting in one step.

```python
drinks = ["tea", "coffee", "tea", "juice", "tea"]
counts = {}
for drink in drinks:
    counts[drink] = counts.get(drink, 0) + 1
print(counts)
```

**10.** What does this program print? What happens on the last two lines?

```python
class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def pay(self, amount):
        if amount > self.balance:
            raise ValueError("Not enough money")
        self.balance -= amount


wallet = Wallet("Sara", 50)
wallet.pay(20)
print(wallet.balance)
wallet.pay(40)
print(wallet.balance)
```

---

_Answer key (instructor only, not published): `assessments/answer-keys/week-09-checkpoint.md`_
