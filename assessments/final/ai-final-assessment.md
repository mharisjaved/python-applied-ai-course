# Final Assessment: Python + Applied AI (Weeks 9–12)

**Given on Day 60 · 45 minutes (full) or 30 minutes (short) · 50 points**

- On paper, or in a fresh notebook with **no internet and no AI assistants**. Course notes are not allowed.
- Short (30-minute) version: skip **Section A** (it revisits Weeks 1–9) and mark out of **38**.
- Write code as you would type it. Small typos do not cost points if the idea is clear.
- All data and model replies in this paper are invented for the questions.

---

## Section A: Python and data (12 points)

**Q1. Predict the output (3 points)**

```python
def count_long(words, min_length=5):
    count = 0
    for word in words:
        if len(word) >= min_length:
            count += 1
    return count


stock = {"pens": 12, "notebooks": 0, "lamps": 3}
print(count_long(["model", "data", "pandas", "AI"]))
print(count_long(["model", "data"], 4))
print([item for item, quantity in stock.items() if quantity > 0])
```

**Q2. Find and fix (3 points).** This program should print the average of the numbers in `scores.txt` (one
number per line). Find **two** problems and write a fix for **one** of them.

```python
def load_scores(path):
    scores = []
    with open(path) as file:
        for line in file:
            scores.append(int(line))
    return scores


try:
    scores = load_scores("scores.txt")
except FileNotFoundError:
    print("File not found")
print(sum(scores) / len(scores))
```

**Q3. Predict the output (3 points)**

```python
import pandas as pd

sales = pd.DataFrame({
    "shop": ["north", "south", "north", "east", "south"],
    "units": [5, 2, 7, 4, 6],
    "price": [2.0, 3.5, 2.0, 5.0, 3.5],
})
sales["revenue"] = sales["units"] * sales["price"]
print(sales["revenue"].sum())
print(list(sales[sales["units"] >= 5]["shop"]))
print(sales.groupby("shop")["units"].sum()["south"])
```

**Q4. Find and fix (3 points).** The goal is to show the final scores of the **three best** students in
`students.csv`. Find both bugs and fix them.

```python
students = pd.read_csv("students.csv")
top = students.sort_values("final_score").head(3)
print(top["Final_score"])
```

## Section B: Machine learning (12 points)

**Q5. Overfitting (3 points).** A decision tree was trained with three settings:

| `max_depth` | train accuracy | test accuracy |
|-------------|----------------|---------------|
| 1 | 0.71 | 0.70 |
| 3 | 0.86 | 0.83 |
| 12 | 1.00 | 0.72 |

a) Which depth would you choose, and why? b) In plain words, what is happening at depth 12?
c) Why do we compare settings on test data and not on training data?

**Q6. Leakage (3 points).** A gym wants to predict whether a member will **cancel next month**. The features are:
`age`, `visits_last_month`, `months_as_member`, `cancellation_fee_paid`, `has_personal_trainer`.

a) Which feature leaks, and why? b) What would you expect the test accuracy to look like with that feature, and
what would happen when the model is used for real?

**Q7. Write code (4 points).** `students` is loaded and:

```python
X = students[["study_hours", "attendance_pct", "previous_score"]]
y = students["passed"]
```

Write the code to: split into 80 % training and 20 % test data (`random_state=42`); train a
`DecisionTreeClassifier(max_depth=3, random_state=0)`; print the **test** accuracy; print the **baseline**
accuracy (always predicting the most common class of the test set). Include the imports.

**Q8. Confusion matrix (2 points).** A camera checks products for defects (positive = *defective*). On 200
products: 30 true positives, 10 false negatives, 5 false positives, 155 true negatives.

a) Calculate the recall. b) A missed defect can hurt a customer. Is recall or precision more important here? Why?

## Section C: LLM applications (12 points)

**Q9. Predict the output (3 points)**

```python
import json


def parse_label(reply):
    try:
        data = json.loads(reply)
    except json.JSONDecodeError:
        return None
    if not isinstance(data, dict) or data.get("label") not in ["positive", "negative", "neutral"]:
        return None
    return data["label"]


print(parse_label('{"label": "negative"}'))
print(parse_label('{"label": "Negative"}'))
print(parse_label('The label is "negative".'))
```

**Q10. Find the problems (3 points).** Name **three** different problems in this code (`prompt` is defined
earlier) and say briefly how to fix each.

```python
import json

import anthropic

client = anthropic.Anthropic(api_key="my-real-key-123")
response = client.messages.create(model="claude-opus-5-5", max_tokens=1000,
                                  messages=[{"role": "user", "content": prompt}])
data = json.loads(response.content[0].text)
print(data["summary"])
```

**Q11. Write code (4 points).** Using `parse_label` from Q9, write `classify_review(text, ask)`:
- build a prompt that contains the review text and asks for JSON like `{"label": "positive"}`;
- call `ask(prompt)`;
- return the label, or `"unknown"` if the reply is `"[The model declined this request.]"` or cannot be parsed.

Then write a **fake** `ask` function that makes `classify_review` return `"unknown"`.

**Q12. Explain (2 points).** Every LLM app in this course has an offline mock. Give **two** reasons.

## Section D: AI capstone and responsible AI (14 points)

**Q13. One function boundary (4 points).**
a) What does "the AI part sits behind one function" mean? b) Give two benefits.
c) How can a pytest test check the fallback path **without** the internet and without an API key?

**Q14. Hallucination (5 points).** A campus FAQ assistant replies: *"The library is open on Sundays from 10:00
to 14:00."* The FAQ says the library is **closed** on Sundays and public holidays.
a) What is this problem called? b) Name two things in the **prompt** that make it less likely.
c) Describe one **check in code** that would catch it, and what the app should show instead.

**Q15. Privacy and bias (5 points).** Omar's capstone sends each student's **full record** (name, e-mail, student
ID, grades, `has_job`, a free-text comment) to an LLM to write personal study advice.
a) Name two privacy problems and how to fix each.
b) Name one bias risk and describe a simple test (probe) for it.
c) Write one sentence for his README under *When not to trust it*.

---

_Answer key (instructor only, not published): `assessments/answer-keys/ai-final-assessment.md`_
