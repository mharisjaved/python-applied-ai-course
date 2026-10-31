# Checkpoint 1: Week 1 (Days 01–05)

**Given on Day 05 · 15 minutes · 10 points · individual, on paper, closed notes, no running code**

Name: ______________________ Date: ____________

Write your answers under each question. If you are not sure, write your best guess **and one sentence of
reasoning**: partial answers earn partial points.

## Part A: Predict the output

Write **exactly** what each program prints.

**1.**
```python
x = 17
print(x // 5, x % 5, x / 4)
```

**2.**
```python
word = "notebook"
print(word[0], word[-1], word[2:5], len(word))
```

**3.**
```python
price = 4.5
qty = "3"
total = price * int(qty)
print(f"{qty} x {price} = {total:.2f}")
```

## Part B: Find and fix

**4.** This program should print `In 5 years you will be 25` when the user types `20`. Instead it crashes.
(a) Name the error. (b) Rewrite the line(s) so it works.

```python
age = input("How old are you? ")
print("In 5 years you will be", age + 5)
```

**5.** This program should print `Initial: A`. It does not crash, but the output is wrong.
(a) Explain what goes wrong. (b) Fix it.

```python
name = "  asha khan "
name.strip()
print(f"Initial: {name[0].upper()}")
```

## Part C: Write code

**6.** A video is `500` seconds long. Using `//` and `%`, write code that prints:

```
500 seconds = 8 min 20 s
```

Start from:
```python
total_seconds = 500
```

**7.** Write code that cleans the email below (no spaces at the ends, all lowercase) and then prints the part
**before** the `@`, using `.find()` and slicing. Your code must still work for a different email.

```python
email = "  Bilal.Raza@Example.com "
```

Expected output:
```
Clean: bilal.raza@example.com
User: bilal.raza
```

## Part D: Explain in words

**8.** A program asks `age = input("Your age? ")`, the user types `20`, and `print(age * 2)` shows `2020`
instead of `40`. Explain in 2–3 sentences **why** this happens and **how** to fix it.

## Part E: Looking back (Days 01–02)

**9.** What command runs the file `hello.py` in our uv project? In one sentence, what does the Python
interpreter do with that file?

**10.** (a) Write the type of each value: `"42"` · `42` · `4.2` · `False`
(b) Which of these variable names are **valid** in Python? `2nd_place` · `total_price` · `my city` · `score`

---

_Answer key (instructor only, not published): `assessments/answer-keys/week-01-checkpoint.md`_
