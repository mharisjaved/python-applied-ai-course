# NumPy Essentials

**What it is:** NumPy gives Python fast arrays: grids of numbers where one line of maths applies to every value at once.
**Why it exists:** loops over 100 000 numbers are slow and long to write. pandas and scikit-learn are built on NumPy arrays.

**Taught on:** [Day 43](../../weeks/week-09/day-43-numpy/lesson.md)

## Syntax at a glance

| You want to… | Write | Result / note |
|--------------|-------|---------------|
| Import | `import numpy as np` | `np` is the standard nickname |
| Array from a list | `a = np.array([72, 85, 64])` | all values get one type |
| Size and type | `a.shape`, `a.dtype` | `(3,)`, `int64` |
| Maths on every value | `a + 5`, `a * 2`, `a / 100` | new array, no loop |
| Two arrays, value by value | `a - b` | shapes must match |
| Statistics | `a.mean()` `a.std()` `a.min()` `a.max()` `a.sum()` | |
| Round | `a.round(1)`, `round(a.mean(), 1)` | |
| True/False for each value | `a >= 70` | a **boolean mask** |
| Keep only matching values | `a[a >= 70]` | |
| Combine conditions | `a[(a > 60) & (a < 80)]`, `\|` for "or" | brackets around each condition |
| How many match | `(a >= 70).sum()` | `True` counts as 1 |
| 2-D array | `m = np.array([[1, 2], [3, 4]])` | rows × columns |
| One cell / row / column | `m[1, 0]`, `m[0]`, `m[:, 1]` | `3`, `[1 2]`, `[2 4]` |
| Per column / per row | `m.mean(axis=0)`, `m.mean(axis=1)` | axis 0 goes down, axis 1 goes across |
| Repeatable random numbers | `rng = np.random.default_rng(42)` · `rng.integers(1, 7, size=5)` | same seed, same numbers |

## Examples

### 1. Vectorised maths and statistics

```python
import numpy as np

marks = np.array([72, 85, 64, 90, 58])
print(marks + 5)                            # [77 90 69 95 63]
print(marks.mean(), marks.max(), marks.min())   # 73.8 90 58
print(round(marks.std(), 1))                # 12.1
print(marks.shape, marks.dtype)             # (5,) int64
```

### 2. Lists vs arrays: `*` means different things

```python
import numpy as np

prices = [1.5, 2.0]
print(prices * 2)             # [1.5, 2.0, 1.5, 2.0]   (list: repeated)
print(np.array(prices) * 2)   # [3. 4.]               (array: maths; "3." means 3.0)
```

### 3. Boolean masks: filter without a loop

```python
import numpy as np

hours = np.array([2, 9, 5, 12, 7])
mask = hours >= 7
print(mask)                                 # [False  True False  True  True]
print(hours[mask])                          # [ 9 12  7]
print(mask.sum())                           # 3
print(hours[(hours > 3) & (hours < 10)])    # [9 5 7]
```

### 4. Two arrays together

```python
import numpy as np

this_term = np.array([72, 85])
last_term = np.array([70, 80])
print(this_term - last_term)   # [2 5]
```

### 5. 2-D arrays: rows are students, columns are tests

```python
import numpy as np

scores = np.array([[70, 80, 90],
                   [60, 75, 85]])
print(scores.shape)              # (2, 3)
print(scores[1, 2])              # 85
print(scores[0])                 # [70 80 90]
print(scores[:, 0])              # [70 60]
print(scores.mean(axis=0))       # [65.  77.5 87.5]
print(scores.mean(axis=1).round(1))   # [80.  73.3]
```

### 6. Repeatable random data

```python
import numpy as np

rng = np.random.default_rng(42)
print(rng.integers(1, 7, size=5))   # [1 5 4 3 3]
```

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| `and` / `or` with arrays: `hours > 3 and hours < 10` | `ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()` | `(hours > 3) & (hours < 10)` |
| `&` without brackets: `hours > 3 & hours < 10` | same `ValueError` | Brackets around each condition |
| Arrays of different lengths: `[1, 2, 3] + [1, 2]` as arrays | `ValueError: operands could not be broadcast together with shapes (3,) (2,)` | Make sure the shapes match |
| `np.array(1, 2, 3)` | `TypeError: array() takes from 1 to 2 positional arguments but 3 were given` | Pass one list: `np.array([1, 2, 3])` |
| Numbers stored as text: `np.array(["1", "2"]) + 1` | `UFuncTypeError: ufunc 'add' did not contain a loop …` | Convert first: `np.array([1, 2])` |
| Putting a decimal into an `int64` array: `marks[0] = 72.9` | silently stored as `72` | Create the array with floats (`72.0`) |
| Expecting `print` to show commas | `[77 90 69]` | That is how arrays print; `.tolist()` gives a normal list |

## See also

- [03 pandas](03-pandas.md): tables built on NumPy columns
- [05 scikit-learn workflow](05-scikit-learn-workflow.md): models take and return arrays
- [04 Lists and tuples](../python/04-lists-and-tuples.md): the plain-Python version
