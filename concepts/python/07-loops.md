# Loops: `for`, `while`, `break`, `continue`

**What it is:** a loop repeats a block of code: `for` once per item (or number), `while` as long as a condition is True.
**Why it exists:** totalling 300 expenses or re-asking until the input is valid would be impossible to write by hand.

**Taught on:** [Day 11](../../weeks/week-03/day-11-for-loops/lesson.md) (`for`, `range`, accumulators) ·
[Day 12](../../weeks/week-03/day-12-iterating-collections/lesson.md) (strings, lists, dicts, `enumerate`) ·
[Day 13](../../weeks/week-03/day-13-while-loops/lesson.md) (`while`, validation) ·
[Day 14](../../weeks/week-03/day-14-break-continue-nested/lesson.md) (`break`, `continue`, nested, `random`)

## Syntax at a glance

| You want to… | Write | Note |
|--------------|-------|------|
| Repeat n times | `for i in range(5):` | `i` is 0, 1, 2, 3, 4 (stop is excluded) |
| Count from a to b | `range(1, 11)` | 1 … 10 |
| Count in steps | `range(0, 20, 5)`, `range(10, 0, -1)` | 0, 5, 10, 15 · 10 … 1 |
| Each item of a list / string | `for mark in marks:`, `for ch in word:` | |
| Item **and** its position | `for i, name in enumerate(names, start=1):` | |
| Each key and value | `for key, value in my_dict.items():` | |
| Repeat while a condition holds | `while balance > 0:` | something inside must change the condition |
| Loop "forever" until told to stop | `while True:` … `break` | |
| Leave the loop now / skip to the next round | `break` / `continue` | `break` leaves only the innermost loop |
| Random numbers (Day 14) | `import random` · `random.randint(1, 6)` · `random.choice(items)` · `random.shuffle(items)` | `random.seed(1)` makes results repeatable |

**Accumulator pattern:** create the result *before* the loop (`total = 0`, `found = []`), update it *inside*, use it *after*.

## Examples

### 1. `range` with a step

```python
for n in range(10, 0, -3):
    print(n)
# 10
# 7
# 4
# 1
```

### 2. Accumulators: total and count

```python
expenses = [12.5, 40.0, 7.25, 3.0]
total = 0
big_ones = 0
for amount in expenses:
    total += amount
    if amount > 10:
        big_ones += 1
print(total, big_ones)   # 62.75 2
```

### 3. `enumerate` for numbered lists

```python
names = ["Asha", "Bilal", "Sara"]
for position, name in enumerate(names, start=1):
    print(f"{position}. {name}")
# 1. Asha
# 2. Bilal
# 3. Sara
```

### 4. Build a new list and find the maximum by hand

```python
temps_c = [21, 25, 19, 30]
temps_f = []
hottest = temps_c[0]
for t in temps_c:
    temps_f.append(round(t * 9 / 5 + 32, 1))
    if t > hottest:
        hottest = t
print(temps_f)   # [69.8, 77.0, 66.2, 86.0]
print(hottest)   # 30
```

### 5. `while`: repeat until a goal is reached

```python
savings = 0
weeks = 0
while savings < 100:
    savings += 30
    weeks += 1
print(weeks, savings)   # 4 120
```

### 6. Validation loop: keep asking until the input is valid

```python
pin = input("Enter a 4-digit PIN: ")       # you type: 12a4
while not (pin.isdigit() and len(pin) == 4):
    print("Digits only, exactly 4.")
    pin = input("Enter a 4-digit PIN: ")   # you type: 1234
print("PIN accepted")
# Digits only, exactly 4.
# PIN accepted
```

### 7. `continue` skips, `break` stops

```python
orders = ["tea", "", "cake", "STOP", "juice"]
for item in orders:
    if item == "":
        continue        # skip blank entries
    if item == "STOP":
        break           # leave the loop completely
    print("Serving", item)
# Serving tea
# Serving cake
```

### 8. Nested loops and `random`

```python
import random

for row in range(1, 4):
    line = ""
    for col in range(1, 4):
        line += f"{row * col:>4}"
    print(line)
#    1   2   3
#    2   4   6
#    3   6   9

random.seed(3)                 # same "random" results every run
print(random.randint(1, 6))    # 2
```

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| `while` condition never becomes False (e.g. re-asking but not storing the new answer) | cell runs forever (`[*]`), no output | Interrupt the kernel (■ button / Ctrl+C), then make sure the loop changes its variable |
| `range(1, 10)` expecting 10 | last number is 9 | Stop is excluded: `range(1, 11)` |
| `total = 0` *inside* the loop | total is reset each round, wrong answer | Create accumulators before the loop |
| `print(total)` indented inside the loop | prints every round instead of once | Dedent it to run after the loop |
| A float in `range`: `range(5.0)`, `range(total / 2)` | `TypeError: 'float' object cannot be interpreted as an integer` | Use whole numbers: `range(int(n))` |
| Removing items from the list you are looping over | items get skipped | Build a new list instead |
| `break` in an inner loop expecting both to stop | outer loop keeps going | `break` only leaves the innermost loop |

## See also

- [04 Lists and tuples](04-lists-and-tuples.md) · [05 Dicts and sets](05-dicts-and-sets.md) · [06 Conditionals](06-conditionals.md)
- [09 Built-ins and comprehensions](09-built-ins-and-comprehensions.md): shorter ways to build lists and find maxima
- [11 Exceptions](11-exceptions.md): retry loops with `try/except`
