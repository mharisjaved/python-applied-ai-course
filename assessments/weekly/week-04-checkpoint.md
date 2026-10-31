# Checkpoint 4: Functions

**Week 4 · Day 20 (first 18 minutes) · Individual · No notes, no computer · 10 points**

Write your answers on paper (or in the form). For "predict" questions, write **exactly** what is printed, one
line per output line. You may write "error" and the name of the error if you think the code crashes.

**Q1. Predict the output.**

```python
def show_line():
    """Print a line of stars."""
    print("*****")

def show_title():
    """Print the title."""
    print("REPORT")

print("A")
show_line()
show_line()
print("B")
```

**Q2. Predict the output.**

```python
def add_bonus(score):
    print(score + 5)

def add_bonus_return(score):
    return score + 5

x = add_bonus(10)
y = add_bonus_return(10)
print(x, y)
```

**Q3. Predict the output.**

```python
total = 100

def checkout(price, delivery=5):
    total = price + delivery
    return total

print(checkout(20))
print(checkout(20, delivery=0))
print(total)
```

**Q4. Find and fix.** This code crashes on the last line. Name the error, explain the cause in one sentence, and
write the corrected line(s).

```python
def average(numbers):
    """Return the average of numbers."""
    total = 0
    for n in numbers:
        total += n
    print(total / len(numbers))

result = average([4, 8, 6])
print("Average doubled:", result * 2)
```

**Q5. Find and fix.** This code crashes with an `UnboundLocalError`. Rewrite it **without** the `global` keyword so
that it prints `2`.

```python
lives = 3

def lose_life():
    lives = lives - 1

lose_life()
print(lives)
```

**Q6. Write code.** Write a function `price_with_discount(price, percent=10)` that **returns** the price after a
`percent` discount, with a docstring. Then write two calls that print the result: one for a price of 80 using the
default discount, and one for a price of 80 with a 25% discount. What do the two calls print?

**Q7. Write code and checks.** Write a function `count_letter(text, letter)` that returns how many times `letter`
appears in `text`, ignoring capital letters (`count_letter("Banana", "a")` is `3`). Then write **two checks** in
the style `print(f(x) == expected)`: one normal case and one edge case.

**Q8. Explain in words.** A classmate says: *"My function prints the right answer, so it doesn't need a
`return`."* In 2–3 sentences, explain why this is a problem. Use the word `None` in your answer.

**Q9. Retrieval (Week 2). Predict the output.**

```python
stock = {"pens": 12, "pads": 0}
stock["pens"] -= 2
stock["clips"] = 5
print(stock.get("pads"), stock.get("tape", "none"), len(stock))
```

**Q10. Retrieval (Week 3). Predict the output.**

```python
n = 0
while True:
    n += 1
    if n % 2 == 0:
        continue
    if n > 5:
        break
    print(n)
```

---

_Answer key (instructor only, not published): `assessments/answer-keys/week-04-checkpoint.md`_
