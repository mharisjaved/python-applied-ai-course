# Checkpoint 3: Control Flow (Week 3)

**Given at the start of Day 15 · 15–20 minutes · individual · no notes, no computer** (or a blank notebook with no
access to earlier files). Covers Days 11–14, plus two retrieval questions from Weeks 1–2.

Name: ____________________ Date: __________

---

### Part A: Predict the output (1 point each)

**Q1.** What is printed?

```python
total = 0
for n in range(2, 12, 3):
    total += n
print(total)
```

**Q2.** What is printed?

```python
stock = {"pens": 4, "rulers": 0, "books": 7}
low = []
for item, qty in stock.items():
    if qty < 5:
        low.append(item)
print(low, len(stock))
```

**Q3.** What is printed? (`end=" "` keeps the output on one line.)

```python
n = 0
while True:
    n += 1
    if n % 2 == 0:
        continue
    if n > 6:
        break
    print(n, end=" ")
```

### Part B: Find and fix (1 point each)

**Q4.** This code should print `3`, the number of words with more than 3 letters. It prints something else.
Find the **two** bugs and write the corrected code.

```python
sentence = "the quick brown fox jumps"
for word in sentence:
    count = 0
    if len(word) > 3:
        count += 1
print(count)
```

**Q5.** This code should keep asking until the user types a whole number. Find the **two** bugs and write the
corrected code.

```python
qty = input("Quantity: ")
while qty.isdigit():
    print("Numbers only!")
qty = int(qty)
```

### Part C: Explain in words (1 point)

**Q6.** In one or two sentences each:
(a) What is the difference between `break` and `continue`?
(b) Give an everyday example where a `while` loop is a better choice than a `for` loop, and say why.

### Part D: Write code (1.5 points each)

**Q7.** Given `temps = [18, 22, 25, 19, 30, 27]`, write a `for` loop (do **not** use `sum()`) that works out the
average temperature and counts the days above 24. Print both, like this:

```
Average: 23.5
Days above 24: 3
```

**Q8.** Write a loop that asks `Rate today's class (1-5): ` and keeps asking until the user types a whole number
from 1 to 5. Then print `Thanks for rating N!`. The program must not crash on input such as `great` or `-2`.

### Part E: Retrieval from Weeks 1–2 (0.5 points each)

**Q9.** What is printed?

```python
word = "notebook"
price = 3.5
print(word[:4].upper(), word[-4:])
print(f"Total: {price * 3:.2f}")
```

**Q10.** What is printed?

```python
scores = [40, 75, 90]
scores.append(60)
scores.sort()
best = scores[-1]
if best >= 80:
    print("A", scores)
elif best >= 60:
    print("B", scores)
grades = {"A": 80, "B": 60}
print(grades.get("C", "none"))
```

---

_Answer key (instructor only, not published): `assessments/answer-keys/week-03-checkpoint.md`_
