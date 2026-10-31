# Checkpoint 5: Week 5 (Days 21–25)

**Given at the end of Day 25 · 15 minutes · 10 points · individual, on paper, closed notes, no running code**

Name: ______________________ Date: ____________

Write your answers under each question. If you are not sure, write your best guess **and one sentence of
reasoning**: partial answers earn partial points.

## Part A: Predict the output

Write **exactly** what each program prints.

**1.**
```python
names = ["mei", "Omar", "fatima"]
print(sorted(names))
print(sorted(names, key=str.lower))
print(max(names, key=len))
```

**2.**
```python
marks = [45, 82, 67, 30]
print([m + 5 for m in marks if m < 50])
print({m: m >= 50 for m in marks[:2]})
```

**3.** The file `log.txt` does not exist before this program runs.
```python
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("A\n")
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("B")
    f.write("C\n")
with open("log.txt", encoding="utf-8") as f:
    print(f.read())
```
What would it print if the **second** `open` used `"w"` instead of `"a"`?

## Part B: Find and fix

**4.** `prices.txt` holds one price per line (e.g. `2.50`). This code should print the total, but it has
**two** mistakes. Name each problem and write the corrected code.

```python
total = 0
with open("prices.txt", encoding="utf-8") as price_file:
    print("Reading prices...")
for line in price_file:
    total = total + line
print(total)
```

**5.** This function should keep asking until the user types a whole number, then **give that number back** to the
caller. It has **two** problems. Name them and write the corrected function.

```python
def get_quantity():
    while True:
        text = input("Quantity: ")
        try:
            quantity = int(text)
        except:
            print("Please type a whole number.")
```

## Part C: Write code

**6.** Write **one** list comprehension that turns `words` into `['data', 'ai', 'python']` (no spaces, lowercase,
no empty entries).

```python
words = ["  Data ", "", "AI", " python", "  "]
```

**7.** Write a function `average(numbers)` that returns the average of a list of numbers. If the list is empty, it
must **raise** a `ValueError` with the message `cannot average an empty list`. Use built-in functions.

## Part D: Explain in words

**8.** A classmate puts `try:` around their whole program and ends it with `except:` (no error type) "so it never
crashes". Explain in 2–3 sentences why this is a bad idea and what they should do instead.

## Part E: Looking back (Weeks 2–4)

**9.** What does this print?
```python
stock = {"pens": 12, "rulers": 0}
stock["glue"] = 5
stock["pens"] = stock["pens"] - 2
print(stock.get("tape", 0), len(stock), stock["pens"])
```

**10.** What does this print?
```python
def count_long(words, min_length=4):
    count = 0
    for word in words:
        if len(word) >= min_length:
            count += 1
    return count

print(count_long(["sun", "cloud", "rain"]))
print(count_long(["sun", "cloud", "rain"], 5))
```

---

_Answer key (instructor only, not published): `assessments/answer-keys/week-05-checkpoint.md`_
