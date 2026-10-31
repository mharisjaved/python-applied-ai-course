# Variables and Basic Types

**What it is:** a variable is a name attached to a value, and every value has a type (`int`, `float`, `str`, `bool`).
**Why it exists:** programs need to remember things (a name, a price, a score) and use them again later.

**Taught on:** [Day 02](../../weeks/week-01/day-02-variables/lesson.md)

## Syntax at a glance

| You want to… | Write | Result / note |
|--------------|-------|---------------|
| Create a variable | `city = "Lahore"` | `=` means "attach this name to this value", not "is equal to" |
| Whole number | `age = 19` | `int` |
| Decimal number | `price = 4.99` | `float` |
| Text | `name = "Asha"` or `'Asha'` | `str` (quotes required) |
| Yes / no value | `is_member = True` | `bool`: only `True` or `False` (capital letter) |
| Check a type | `type(price)` | `<class 'float'>` |
| Print several values | `print("Age:", age)` | values are separated by one space |
| Comment | `# this is ignored by Python` | notes for humans |
| Change a value | `score = score + 5` | right side is worked out first, then the name moves |

**Naming rules:** letters, digits and `_` only · cannot start with a digit · no spaces · case-sensitive
(`Score` and `score` are different) · not a Python keyword (`if`, `for`, `class`…). Style: `snake_case`,
descriptive (`total_price`, not `tp`).

**Notebooks:** the *last line* of a cell is displayed automatically. In a `.py` file nothing appears unless you
`print()` it.

## Examples

### 1. Four basic types

```python
student_name = "Asha"
age = 19
height_m = 1.62
is_enrolled = True
print(student_name, age, height_m, is_enrolled)   # Asha 19 1.62 True
print(type(age), type(height_m))                  # <class 'int'> <class 'float'>
print(type(student_name), type(is_enrolled))      # <class 'str'> <class 'bool'>
```

### 2. Reassignment: the newest value wins

```python
balance = 100
balance = balance - 30   # 100 - 30, so balance is now 70
balance = balance + 5    # 70 + 5, so balance is now 75
print(balance)           # 75
```

### 3. `7` and `"7"` look the same but are different types

```python
a = 7
b = "7"
print(a, b)              # 7 7
print(type(a), type(b))  # <class 'int'> <class 'str'>
```

### 4. A variable can change type (Python allows it, but it is confusing)

```python
value = 7
print(type(value))   # <class 'int'>
value = "seven"
print(type(value))   # <class 'str'>
```

### 5. A "profile card" from variables

```python
name = "Bilal"
city = "Karachi"
courses = 3
print("Name:", name)        # Name: Bilal
print("City:", city)        # City: Karachi
print("Courses:", courses)  # Courses: 3
```

### 6. `NameError`: Python does not know that name

```python
# (shows an error)
total_score = 90
print(total_scor)   # NameError: name 'total_scor' is not defined. Did you mean: 'total_score'?
```

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| Typo in a name: `print(scor)` | `NameError: name 'scor' is not defined` | Copy the exact name; read the "Did you mean" hint |
| Using a name before creating it | `NameError` | Run the cell that creates it first (notebooks run in the order *you* click) |
| Forgot quotes: `name = Asha` | `NameError: name 'Asha' is not defined` | Text needs quotes: `"Asha"` |
| Name starts with a digit: `1st_place = "Mei"` | `SyntaxError: invalid decimal literal` | `first_place = "Mei"` |
| Space in a name: `first name = "Sara"` | `SyntaxError: invalid syntax` | `first_name = "Sara"` |
| Lower-case boolean: `done = true` | `NameError: name 'true' is not defined. Did you mean: 'True'?` | `True` / `False` |
| Using a built-in as a name: `print = 5` | later `TypeError: 'int' object is not callable` | Pick another name; restart the kernel to undo it |
| Expecting every line of a cell to show | only the last value appears | Use `print()` for each value you want to see |

## See also

- [02 Numbers and input](02-numbers-and-input.md): calculating with variables, converting types
- [03 Strings](03-strings.md): working with text values
- [15 Reading tracebacks](15-reading-tracebacks.md): understanding error messages
