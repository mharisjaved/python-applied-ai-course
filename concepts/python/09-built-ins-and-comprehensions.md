# Built-in Functions and Comprehensions

**What it is:** ready-made functions (`sorted`, `zip`, `any`, `all`…) plus a one-line way to build lists and dicts.
**Why it exists:** many loops you write by hand already exist as a tested built-in, and short code is easier to read.

**Taught on:** [Day 21](../../weeks/week-05/day-21-built-in-functions/lesson.md) (built-ins) ·
[Day 22](../../weeks/week-05/day-22-comprehensions/lesson.md) (comprehensions)

## Syntax at a glance

| Built-in | What it does | Example | Result |
|----------|--------------|---------|--------|
| `sorted(items, reverse=True)` | new sorted list, biggest first | `sorted([3, 9, 1], reverse=True)` | `[9, 3, 1]` |
| `sorted(items, key=f)` | sort by `f(item)` | `sorted(["kiwi", "fig"], key=len)` | `['fig', 'kiwi']` |
| `zip(a, b)` | pairs items up | `zip(["Asha", "Ken"], [88, 72])` | `("Asha", 88)`, `("Ken", 72)` |
| `any(bools)` / `all(bools)` | at least one / every one True | `all([True, False])` | `False` |
| `abs(x)` | distance from 0 | `abs(-12.5)` | `12.5` |
| `round(x, n)` | round | `round(3.14159, 2)` | `3.14` |
| `"…".isdigit()` / `.isalpha()` | only digits / only letters | `"2026".isdigit()` | `True` |
| `help(sorted)` | show the documentation | | press `q` to leave in a terminal |

| Comprehension | Means |
|---------------|-------|
| `[expr for x in items]` | new list with `expr` for every `x` |
| `[expr for x in items if condition]` | … only for the `x` that pass the condition (the `if` goes at the end) |
| `{key: value for x in items}` | new dict |

**Rule of thumb:** use a comprehension when it fits comfortably on one line and only *builds* something.
Use a normal loop when you need several steps, `print`, or `break`.

## Examples

### 1. Sorting with `key=` and `reverse=`

```python
names = ["mei", "Bilal", "asha", "Omar"]
print(sorted(names))                         # ['Bilal', 'Omar', 'asha', 'mei']   (capitals first!)
print(sorted(names, key=str.lower))          # ['asha', 'Bilal', 'mei', 'Omar']
print(sorted(names, key=len, reverse=True))  # ['Bilal', 'asha', 'Omar', 'mei']
```

### 2. A leaderboard: sort dicts with your own key function

```python
players = [
    {"name": "Diego", "points": 120},
    {"name": "Zara", "points": 150},
    {"name": "Ken", "points": 95},
]


def get_points(player):
    return player["points"]


for player in sorted(players, key=get_points, reverse=True):
    print(f"{player['name']:<6}{player['points']:>4}")
# Zara   150
# Diego  120
# Ken     95
```

Pass the function **name** (`key=get_points`), not a call (`key=get_points()`).

### 3. `zip` pairs two lists

```python
students = ["Asha", "Omar", "Mei"]
marks = [88, 72, 95]
for name, mark in zip(students, marks):
    print(name, mark)
# Asha 88
# Omar 72
# Mei 95
print(dict(zip(students, marks)))   # {'Asha': 88, 'Omar': 72, 'Mei': 95}
```

### 4. `any`, `all`, `abs`, `isdigit`

```python
homework_done = [True, True, False]
print(all(homework_done), any(homework_done))      # False True
budget, spent = 300, 345.5
print(abs(budget - spent))                         # 45.5
print("2026".isdigit(), "20.5".isdigit(), "-3".isdigit())   # True False False
print("Fatima".isalpha(), "Mei Ling".isalpha())    # True False
```

### 5. Loop vs list comprehension: same result

```python
words = ["  tea ", "Coffee", " JUICE"]

clean = []
for w in words:
    clean.append(w.strip().lower())
print(clean)                                   # ['tea', 'coffee', 'juice']

print([w.strip().lower() for w in words])      # ['tea', 'coffee', 'juice']
```

### 6. Filtering with `if`

```python
marks = [88, 42, 95, 49, 70]
failed = [m for m in marks if m < 50]
print(failed)                          # [42, 49]
print(any([m < 50 for m in marks]))    # True
print([m + 5 for m in marks if m >= 50])   # [93, 100, 75]   (bonus for passing marks only)
```

### 7. Dict comprehension

```python
prices = {"tea": 1.5, "cake": 3.0, "juice": 2.25}
with_tax = {item: round(price * 1.2, 2) for item, price in prices.items()}
print(with_tax)                                       # {'tea': 1.8, 'cake': 3.6, 'juice': 2.7}
cheap = {item: price for item, price in prices.items() if price < 2.5}
print(cheap)                                          # {'tea': 1.5, 'juice': 2.25}
```

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| `sorted(players)` on a list of dicts | `TypeError: '<' not supported between instances of 'dict' and 'dict'` | `sorted(players, key=get_points)` |
| `key=get_points()` with brackets | `TypeError: get_points() missing 1 required positional argument: 'player'` | `key=get_points` (no brackets) |
| `zip` with lists of different lengths | extra items silently dropped | Check `len(a) == len(b)` first |
| `"3.5".isdigit()` expecting `True` | `False` (`.` and `-` are not digits) | Use `try: float(text)` (Day 25) |
| `else` in a filtering comprehension: `[m for m in marks if m > 50 else 0]` | `SyntaxError` | Keep just the `if` at the end, or use a normal loop |
| A comprehension with three conditions | works but nobody can read it | Write a normal loop |
| `[print(m) for m in marks]` | prints, and also builds a useless list of `None` | Use a `for` loop for actions |
| Expecting `sorted()` to change the list | original unchanged | `items = sorted(items)` or `items.sort()` |

## See also

- [04 Lists and tuples](04-lists-and-tuples.md) · [05 Dicts and sets](05-dicts-and-sets.md)
- [07 Loops](07-loops.md): the long form of every comprehension
- [08 Functions](08-functions.md): writing the key function
