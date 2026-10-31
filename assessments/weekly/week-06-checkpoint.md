# Checkpoint 6: Working Like a Python Developer

**Week 6 · given at the end of Day 30 (or the start of Day 31) · 15–20 minutes · paper, closed notes, no computer**

Name: ______________________  Date: ____________

Covers Days 26–29 (modules, uv, debugging, testing) plus two questions from earlier weeks.

---

### Question 1 (predict the output)

```python
import math
from collections import Counter

votes = ["tea", "coffee", "tea", "juice", "tea"]
print(math.ceil(len(votes) / 2))
print(Counter(votes).most_common(1))
```

### Question 2 (predict the output)

`helpers.py` contains:

```python
print("A", __name__)

def double(n):
    return n * 2

if __name__ == "__main__":
    print("B", double(4))
```

a) What does `uv run helpers.py` print?
b) `main.py` (same folder) contains only `import helpers`. What does `uv run main.py` print?

### Question 3 (predict the output)

```python
def average(marks):
    return sum(marks) / len(marks)

def report(name, marks):
    return f"{name}: {average(marks):.1f}"

print(report("Asha", [70, 85]))
print(report("Omar", []))
```

What is printed before the crash? What is the **last line** of the traceback, and in **which function** did the
error happen?

### Question 4 (find and fix)

This code has **two** import mistakes. Write the corrected code.

```python
from datetime import date
import textutils

exam = datetime.date(2026, 12, 18)
print(word_count("Good luck everyone"))
```

### Question 5 (find and fix)

`total_spent([12.5, 3.0, 4.5])` should return `20.0` but returns `12.5`. Find the bug, fix it, and write **one**
`assert` that would have caught it.

```python
def total_spent(amounts):
    total = 0
    for amount in amounts:
        total = total + amount
        return total
```

### Question 6 (write code)

`checkout.py` contains `apply_discount(price, percent)`, which returns the price after the discount and raises
`ValueError` when `percent` is below 0 or above 100. Write a file `test_checkout.py` with **three** pytest tests:
one normal case, one edge case and one error case.

### Question 7 (write code)

Write a module `convert.py` with a function `km_to_miles(km)` (1 km = 0.621371 miles, round to 2 decimals) and a
self-check that runs **only** when the file is run directly. Then write the line(s) that `main.py` (same folder)
needs to print `km_to_miles(10)`.

### Question 8 (explain in words)

Your classmate Mei asks: "Why do I need both `pyproject.toml` and `uv.lock`? And why shouldn't I send you my `.venv`
folder?" Answer her in 2–4 sentences.

### Question 9 (retrieval, Week 4)

What does this print?

```python
total = 10

def add_tax(price, rate=0.2):
    total = price + price * rate
    return round(total, 2)

print(add_tax(50))
print(add_tax(50, rate=0.1))
print(total)
```

### Question 10 (retrieval, Week 5)

What does this print if the file `scores.txt` does **not** exist?

```python
try:
    with open("scores.txt", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("No scores yet")
finally:
    print("Done")
```

---

_Answer key (instructor only, not published): `assessments/answer-keys/week-06-checkpoint.md`_
