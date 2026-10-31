# Lists and Tuples

**What it is:** a list `[ ]` is an ordered, changeable collection; a tuple `( )` is an ordered collection that cannot change.
**Why it exists:** instead of 30 variables `mark1`, `mark2`…, keep all the marks in one list and work on them together.

**Taught on:** [Day 06](../../weeks/week-02/day-06-lists/lesson.md) (lists, indexing, `in`, `sum/min/max`) ·
[Day 07](../../weeks/week-02/day-07-list-methods-tuples/lesson.md) (methods, `sorted`, `split/join`, tuples, copying)

## Syntax at a glance

| You want to… | Write | Result (with `nums = [4, 1, 3]`) |
|--------------|-------|-----------------------------------|
| Create | `nums = [4, 1, 3]`, `empty = []` | |
| Read / change an item | `nums[0]`, `nums[-1]`, `nums[1] = 9` | `4`, `3`, list becomes `[4, 9, 3]` |
| Slice | `nums[0:2]` | `[4, 1]` (new list) |
| Size and stats | `len(nums)` `sum(nums)` `min(nums)` `max(nums)` | `3` `8` `1` `4` |
| Is it there? | `3 in nums` | `True` |
| Add to the end / at a position | `nums.append(7)`, `nums.insert(0, 7)` | |
| Remove by value / by position | `nums.remove(1)`, `nums.pop()`, `nums.pop(0)` | `pop` also *returns* the item |
| Sort / reverse in place | `nums.sort()`, `nums.reverse()` | change `nums`, return `None` |
| Sorted copy | `sorted(nums)` | `[1, 3, 4]`, `nums` unchanged |
| Position / how many | `nums.index(3)`, `nums.count(3)` | `2`, `1` |
| Text → list → text | `"a b c".split()`, `"-".join(["a", "b"])` | `['a', 'b', 'c']`, `"a-b"` |
| Tuple and unpacking | `point = (3, 5)`, `x, y = point` | `x` is 3, `y` is 5 |
| Independent copy | `backup = nums.copy()` | |

## Examples

### 1. Simple statistics

```python
marks = [72, 85, 64, 90, 58]
print(len(marks), sum(marks), min(marks), max(marks))   # 5 369 58 90
print(sum(marks) / len(marks))                          # 73.8
print(90 in marks, 100 in marks)                        # True False
```

### 2. Reading and changing items

```python
shopping = ["milk", "eggs", "bread"]
print(shopping[0], shopping[-1])   # milk bread
shopping[1] = "rice"
print(shopping)                    # ['milk', 'rice', 'bread']
print(shopping[1:])                # ['rice', 'bread']
```

### 3. Adding and removing

```python
queue = ["Sara", "Omar"]
queue.append("Mei")         # add to the end
queue.insert(0, "Diego")    # add at position 0
print(queue)                # ['Diego', 'Sara', 'Omar', 'Mei']
served = queue.pop(0)       # remove AND return the first item
queue.remove("Omar")        # remove by value
print(served, queue)        # Diego ['Sara', 'Mei']
```

### 4. `sort()` changes the list, `sorted()` makes a new one

```python
prices = [4.5, 1.2, 3.0]
cheap_first = sorted(prices)
print(cheap_first, prices)   # [1.2, 3.0, 4.5] [4.5, 1.2, 3.0]
prices.sort()
prices.reverse()
print(prices)                # [4.5, 3.0, 1.2]
```

### 5. `split()` and `join()`

```python
line = "apples,pears,plums"
fruits = line.split(",")
print(fruits)                          # ['apples', 'pears', 'plums']
print(" | ".join(fruits))              # apples | pears | plums
print(len("the quick brown fox".split()))   # 4
```

### 6. Tuples and unpacking

```python
location = (31.5, 74.3)    # (latitude, longitude): a fixed pair
lat, lon = location
print(lat, lon)            # 31.5 74.3
name, score = "Ken", 88    # a tuple without brackets
print(f"{name}: {score}")  # Ken: 88
```

### 7. Two names for one list vs a real copy

```python
original = ["pen", "ruler"]
alias = original            # same list, second name
backup = original.copy()    # separate list
alias.append("eraser")
print(original)             # ['pen', 'ruler', 'eraser']
print(backup)               # ['pen', 'ruler']
```

### 8. Nested lists (a preview)

```python
seating = [["Asha", "Bilal"], ["Sara", "Omar"]]   # row 0, row 1
print(seating[1])      # ['Sara', 'Omar']
print(seating[1][0])   # Sara
```

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| `marks = marks.sort()` | `marks` becomes `None` | `marks.sort()` alone, or `marks = sorted(marks)` |
| `nums[len(nums)]` | `IndexError: list index out of range` | Last item is `nums[-1]` |
| `nums.remove(99)` when 99 is not there | `ValueError: list.remove(x): x not in list` | Check `if 99 in nums:` first |
| `nums.append(5, 6)` | `TypeError: list.append() takes exactly one argument (2 given)` | Append one at a time |
| Changing `alias` and being surprised `original` changed | both names show the change | Use `.copy()` when you need a separate list |
| `sum(["3", "4"])` | `TypeError: unsupported operand type(s) for +: 'int' and 'str'` | Convert to numbers first |
| `point[0] = 5` on a tuple | `TypeError: 'tuple' object does not support item assignment` | Tuples are fixed; use a list if it must change |
| `x, y = (1, 2, 3)` | `ValueError: too many values to unpack` | Number of names must match number of items |

## See also

- [03 Strings](03-strings.md): indexing and slicing work the same way on text
- [05 Dicts and sets](05-dicts-and-sets.md): look things up by name instead of position
- [07 Loops](07-loops.md): do something with every item
- [09 Built-ins and comprehensions](09-built-ins-and-comprehensions.md): `sorted(key=…)`, `zip`, list comprehensions
