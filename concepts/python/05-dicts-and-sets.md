# Dictionaries and Sets

**What it is:** a dict maps **keys** to **values** (`{"name": "Asha"}`); a set is an unordered collection with no duplicates.
**Why it exists:** look things up by a meaningful name instead of a position number, and remove duplicates instantly.

**Taught on:** [Day 08](../../weeks/week-02/day-08-dicts-sets/lesson.md) · looping over dicts and counting with a
dict on [Day 12](../../weeks/week-03/day-12-iterating-collections/lesson.md)

## Syntax at a glance

| You want to… | Write | Note |
|--------------|-------|------|
| Create a dict | `stock = {"apples": 12, "pears": 0}` | keys are usually strings, must be unique |
| Read a value | `stock["apples"]` | `KeyError` if the key is missing |
| Read safely | `stock.get("plums")`, `stock.get("plums", 0)` | `None` or your default, never an error |
| Add or update | `stock["plums"] = 5` | same syntax for both |
| Delete | `del stock["pears"]` | |
| Does the key exist? | `"apples" in stock` | checks **keys**, not values |
| All keys / values / pairs | `stock.keys()`, `stock.values()`, `stock.items()` | `.items()` gives `(key, value)` tuples |
| Size | `len(stock)` | number of keys |
| Create a set | `tags = {"red", "blue"}`, `set(a_list)` | empty set is `set()`, **not** `{}` |
| Add to a set | `tags.add("green")` | adding a duplicate does nothing |
| Both / either / only first | `a & b`, `a \| b`, `a - b` | or `a.intersection(b)`, `a.union(b)`, `a.difference(b)` |

## Examples

### 1. A dict as a record

```python
student = {"name": "Fatima", "age": 20, "course": "Python"}
print(student["name"])        # Fatima
student["age"] = 21           # update
student["city"] = "Quetta"    # add a new key
del student["course"]         # remove a key
print(student)                # {'name': 'Fatima', 'age': 21, 'city': 'Quetta'}
```

### 2. Safe lookups with `.get()` and `in`

```python
stock = {"apples": 12, "pears": 0}
print(stock.get("plums"))      # None
print(stock.get("plums", 0))   # 0
print("pears" in stock)        # True
print(12 in stock)             # False   (12 is a value, not a key)
```

### 3. Keys, values and items

```python
prices = {"tea": 1.5, "coffee": 2.25, "juice": 3.0}
print(prices.keys())         # dict_keys(['tea', 'coffee', 'juice'])
print(sum(prices.values()))  # 6.75
print(max(prices.values()))  # 3.0
```

### 4. A list of dicts (a small table)

```python
team = [
    {"name": "Omar", "score": 82},
    {"name": "Zara", "score": 91},
]
print(team[1]["name"], team[1]["score"])   # Zara 91
team.append({"name": "Ken", "score": 77})
print(len(team))                           # 3
```

### 5. Looping over a dict (Day 12)

```python
attendance = {"Asha": 18, "Ken": 15, "Diego": 20}
for name, days in attendance.items():
    print(f"{name}: {days} days")
# Asha: 18 days
# Ken: 15 days
# Diego: 20 days
```

### 6. Counting with a dict (Day 12)

```python
votes = ["tea", "coffee", "tea", "juice", "tea"]
counts = {}
for drink in votes:
    counts[drink] = counts.get(drink, 0) + 1
print(counts)   # {'tea': 3, 'coffee': 1, 'juice': 1}
```

### 7. Sets: de-duplicate and compare groups

```python
sign_ups = ["Asha", "Bilal", "Asha", "Mei", "Bilal"]
unique = set(sign_ups)
print(len(sign_ups), len(unique))   # 5 3

python_club = {"Asha", "Bilal", "Mei"}
ai_club = {"Mei", "Omar", "Asha"}
print(sorted(python_club & ai_club))   # ['Asha', 'Mei']                    in both
print(sorted(python_club | ai_club))   # ['Asha', 'Bilal', 'Mei', 'Omar']   in either
print(sorted(python_club - ai_club))   # ['Bilal']                          only Python club
```

Sets have no fixed order, so we print `sorted(…)` to get a predictable list.

### 8. Missing key

```python
# (shows an error)
stock = {"apples": 12}
print(stock["bananas"])   # KeyError: 'bananas'
```

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| Reading a key that is not there | `KeyError: 'bananas'` | `.get("bananas", 0)` or check `if "bananas" in stock:` |
| `empty = {}` to make a set | it is an empty **dict** | `empty = set()` |
| `tags[0]` on a set | `TypeError: 'set' object is not subscriptable` | Sets have no positions; use `sorted(tags)[0]` or a list |
| A list as a key: `{["a", "b"]: 1}` | `TypeError: unhashable type: 'list'` | Use a string or a tuple as the key |
| Same key twice in one literal | the last value silently wins | Keys must be unique; use a list of dicts for several records |
| `for x in my_dict:` expecting pairs | you only get the keys | `for key, value in my_dict.items():` |
| `"Fatima" in student` to find a value | `False` (it searches keys) | `"Fatima" in student.values()` |
| Printing a set and expecting the same order each time | order looks random | `sorted(my_set)` |

## See also

- [04 Lists and tuples](04-lists-and-tuples.md)
- [07 Loops](07-loops.md): looping over `.items()`
- [09 Built-ins and comprehensions](09-built-ins-and-comprehensions.md): dict comprehensions, sorting dicts by a value
- [14 CSV and JSON](14-csv-and-json.md): rows of a CSV file become dicts; JSON objects become dicts
