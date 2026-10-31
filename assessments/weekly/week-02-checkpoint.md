# Checkpoint 2: Week 2 (Days 06–10)

**Given at the end of Day 10 · 20 minutes · 10 points · individual, on paper, closed notes, no running code**

Name: ______________________ Date: ____________

Write your answers under each question. If you are not sure, write your best guess **and one sentence of
reasoning**: partial answers earn partial points.

## Part A: Predict the output

Write **exactly** what each program prints.

**1.**
```python
queue = ["Ken", "Mei", "Omar"]
queue.append("Zara")
first = queue.pop(0)
queue.insert(1, "Asha")
print(first, queue, len(queue))
```

**2.**
```python
stock = {"pens": 12, "pads": 0}
stock["pens"] -= 2
stock["clips"] = 40
print(stock["pens"], stock.get("pads", "none"), stock.get("tape", "none"), len(stock))
print(sorted({"a", "b", "c"} - {"b", "d"}), len({"x", "y", "x"}))
```

**3.** (a) What does this print? (b) What does it print if the first two lines are `temp = 18` and `raining = True`?
```python
temp = 25
raining = False
if temp > 30 or raining:
    print("Stay inside")
elif temp >= 25 and not raining:
    print("Go to the park")
else:
    print("Take a jacket")
print("Done")
```

## Part B: Find and fix

**4.** This program should print `Lowest: 55`. Instead it crashes.
(a) Explain what goes wrong. (b) Fix it.

```python
marks = [55, 80, 67]
marks = marks.sort()
print("Lowest:", marks[0])
```

**5.** This program should print `Child ticket` when the user types `15`. It has **two** mistakes.
Rewrite it so it works.

```python
age = input("Age: ")
if age < 18
    print("Child ticket")
else:
    print("Adult ticket")
```

## Part C: Write code

**6.** Start from this menu:

```python
menu = {"tea": 2.5, "cake": 3.75, "juice": 3.0}
```

Write code that (a) adds `"water"` costing `1.0`, (b) changes the price of tea to `2.75`, (c) prints the number of
items and the highest price, (d) prints the price of `"coffee"`, or `not on the menu` **without crashing**.

Expected output:
```
Items: 4 | Highest: 3.75
coffee: not on the menu
```

**7.** A courier charges by weight: **up to and including 1 kg**: 2.00 · **above 1 kg up to and including 5 kg**:
4.50 · **above 5 kg**: 9.00. A weight of 0 or less prints `Invalid weight`.

(a) Write the code. It should print, for example, `Fee: 4.50`. Start from `weight_kg = 3.2`.
(b) Write **four** test values for `weight_kg` with the expected output for each. At least one must be a boundary.

| weight_kg | Expected output |
|-----------|-----------------|
| | |
| | |
| | |
| | |

## Part D: Explain in words

**8.** After this code runs, `monday` also contains `"dentist"`. Using the **name tag** idea, explain why in
2–3 sentences, and write the one change that keeps `monday` as `["gym", "laundry"]`.

```python
monday = ["gym", "laundry"]
tuesday = monday
tuesday.append("dentist")
```

## Part E: Looking back (Days 03–05)

**9.**
```python
title = "  data science basics "
clean = title.strip().title()
print(clean, len(clean), clean[:4], clean[-6:])
```

**10.**
```python
points = 10
points += 5 * 2
points = points // 4
print(points, 2 ** 3, 7 / 2)
```

---

_Answer key (instructor only, not published): `assessments/answer-keys/week-02-checkpoint.md`_
