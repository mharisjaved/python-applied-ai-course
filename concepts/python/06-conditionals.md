# Conditionals: `if`, `elif`, `else`

**What it is:** comparisons produce `True`/`False`, and `if` runs a block of code only when a condition is `True`.
**Why it exists:** programs must make decisions: pass or fail, free or paid ticket, valid or invalid input.

**Taught on:** [Day 09](../../weeks/week-02/day-09-conditionals/lesson.md) ·
practised on [Day 10](../../weeks/week-02/day-10-decisions-practice/lesson.md)

## Syntax at a glance

| Comparison | Meaning | Example (`x = 7`) | Result |
|------------|---------|-------------------|--------|
| `==` / `!=` | equal / not equal | `x == 7` | `True` |
| `<` `>` `<=` `>=` | less / greater (or equal) | `x >= 10` | `False` |
| `a <= x <= b` | between (both ends included) | `0 <= x <= 10` | `True` |
| `in` / `not in` | is it in a list / string / dict keys? | `x in [1, 7]` | `True` |
| `and` | both must be True | `x > 0 and x < 5` | `False` |
| `or` | at least one is True | `x < 0 or x == 7` | `True` |
| `not` | flips True/False | `not x == 7` | `False` |

```text
if condition:            <- colon
    runs when True       <- indented 4 spaces
elif other_condition:    <- optional, any number; checked top to bottom
    runs when this one is the first True
else:                    <- optional, no condition
    runs when nothing above was True
```

**Truthiness:** `0`, `0.0`, `""`, `[]`, `{}`, `None` count as `False`; everything else counts as `True`.

## Examples

### 1. Two branches

```python
temperature = 31
if temperature > 30:
    print("Hot day: drink water")
else:
    print("Normal day")
# Hot day: drink water
```

### 2. Grade calculator with `elif`

```python
score = 74
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "F"
print(grade)   # C
```

### 3. `and`, `or`, `not`

```python
age = 16
has_ticket = True
print(age >= 18 and has_ticket)   # False
print(age >= 18 or has_ticket)    # True
print(not has_ticket)             # False
```

### 4. Checking against several values with `in`

```python
day = "sat"
if day in ["sat", "sun"]:
    print("Weekend: shop opens at 10")
else:
    print("Weekday: shop opens at 8")
# Weekend: shop opens at 10
```

### 5. Nested `if` and a dict lookup

```python
ticket_prices = {"child": 5, "adult": 12, "senior": 7}
category = "adult"
is_member = True
if category in ticket_prices:
    price = ticket_prices[category]
    if is_member:
        price = price - 2
    print("Price:", price)
else:
    print("Unknown category")
# Price: 10
```

### 6. Truthiness of empty values

```python
cart = []
name = ""
if not cart:
    print("Your cart is empty")   # Your cart is empty
if name:
    print("Hello", name)
else:
    print("No name given")        # No name given
```

### 7. Order matters: the first True branch wins

```python
score = 95
if score >= 50:
    print("C")    # this runs, so the next branch is never checked
elif score >= 90:
    print("A")
# C
```

Put the strictest condition (`>= 90`) first.

### 8. Cleaning input before comparing

```python
answer = "  Yes "              # pretend the user typed this
if answer.strip().lower() == "yes":
    print("Booking confirmed")   # Booking confirmed
```

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| `if day == "sat" or "sun":` | always True (a non-empty string is truthy) | `day == "sat" or day == "sun"`, or `day in ["sat", "sun"]` |
| `if score = 90:` | `SyntaxError: invalid syntax. Maybe you meant '==' …` | `==` compares, `=` assigns |
| Missing colon: `if score > 50` | `SyntaxError: expected ':'` | `if score > 50:` |
| Body not indented | `IndentationError: expected an indented block after 'if' statement on line 1` | Indent 4 spaces |
| Comparing raw input with a number: `input("Age? ") >= 18` | `TypeError: '>=' not supported between instances of 'str' and 'int'` | `int(input("Age? ")) >= 18` |
| Loosest `elif` first | wrong branch runs, no error | Order from most specific to least specific |
| `"Yes" == "yes"` | `False` | Normalise with `.strip().lower()` |
| `0.1 + 0.2 == 0.3` | `False` | Compare rounded values: `round(0.1 + 0.2, 2) == 0.3` |

## See also

- [05 Dicts and sets](05-dicts-and-sets.md): `in` on dict keys
- [07 Loops](07-loops.md): conditions inside loops, `while` conditions
- [11 Exceptions](11-exceptions.md): when `if` checks are not enough for bad input
