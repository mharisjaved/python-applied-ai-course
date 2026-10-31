# Functions

**What it is:** a named, reusable block of code that can take inputs (parameters) and give back a result (`return`).
**Why it exists:** stop copy-pasting the same code, and split a big problem into small pieces you can test one by one.

**Taught on:** [Day 16](../../weeks/week-04/day-16-functions-intro/lesson.md) (`def`, calling, docstrings) ·
[Day 17](../../weeks/week-04/day-17-parameters-return/lesson.md) (parameters, `return`, `None`) ·
[Day 18](../../weeks/week-04/day-18-scope-defaults/lesson.md) (scope, defaults, composition) ·
[Day 19](../../weeks/week-04/day-19-decomposition/lesson.md) (decomposition, `print(f(x) == expected)` checks)

## Syntax at a glance

| You want to… | Write | Note |
|--------------|-------|------|
| Define | `def greet(name):` + indented body | defining does **not** run it |
| Describe it | `"""Return a greeting for name."""` as the first line of the body | docstring, shown by `help(greet)` |
| Call | `greet("Mei")` | the brackets make it run |
| Give back a result | `return value` | the function stops here |
| Several results | `return low, high` → `low, high = f(...)` | returns a tuple |
| Default value | `def price(amount, tax=0.1):` | defaults go **after** normal parameters |
| Keyword argument | `price(amount=50, tax=0.2)` | order no longer matters |
| No `return` | the result is `None` | |
| Quick check | `print(average([2, 4]) == 3)` | `True` means the check passed |

**Words:** *parameter* = the name in the `def` line; *argument* = the value you pass in the call.
**Scope:** variables created inside a function are *local*: they disappear when it returns. A function can read a
global variable, but pass values in as parameters instead (avoid `global`).

## Examples

### 1. Define once, call many times

```python
def show_menu():
    """Print the café menu."""
    print("1. Tea")
    print("2. Coffee")


show_menu()   # call it as often as you like
# 1. Tea
# 2. Coffee
```

### 2. Parameters and `return`

```python
def average(marks):
    """Return the mean of a list of marks."""
    return sum(marks) / len(marks)


result = average([70, 80, 90])
print(result)                     # 80.0
print(average([50, 60]) + 5)      # 60.0
```

### 3. `print` vs `return`

```python
def shout_print(text):
    print(text.upper())


def shout(text):
    return text.upper()


a = shout_print("hi")   # HI   (printed inside; nothing is returned)
b = shout("hi")
print(a, b)             # None HI
```

### 4. Defaults and keyword arguments

```python
def discounted(price, percent=10):
    """Return price after a percent discount."""
    return price - price * percent / 100


print(discounted(200))                    # 180.0
print(discounted(200, 25))                # 150.0
print(discounted(percent=50, price=80))   # 40.0
```

### 5. Returning two values

```python
def min_max(values):
    return min(values), max(values)


low, high = min_max([7, 3, 9, 4])
print(low, high)   # 3 9
```

### 6. Scope: local variables stay inside

```python
def final_score(raw, bonus):
    total = raw + bonus   # total is local
    return total


print(final_score(80, 5))   # 85
# print(total) here would give NameError: name 'total' is not defined
```

### 7. Small functions working together, checked with `== expected`

```python
def subtotal(prices):
    return sum(prices)


def apply_coupon(amount, coupon):
    if coupon == "SAVE5":
        return amount - 5
    return amount


def checkout(prices, coupon=""):
    return apply_coupon(subtotal(prices), coupon)


print(checkout([10, 20]) == 30)            # True
print(checkout([10, 20], "SAVE5") == 25)   # True
```

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| Calling without brackets: `show_menu` | nothing happens (notebook shows `<function show_menu at 0x…>`) | `show_menu()` |
| Printing inside instead of returning | caller gets `None`; `None + 1` → `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'` | `return` the value; print outside |
| Code after `return` | never runs | Put `return` last |
| Wrong number of arguments | `TypeError: … missing 1 required positional argument` / `takes 1 positional argument but 2 were given` | Match the `def` line |
| Using a local variable outside | `NameError: name 'total' is not defined` | Return it and store the result |
| Default before a normal parameter: `def f(a=1, b):` | `SyntaxError: parameter without a default follows parameter with a default` | Defaults go last |
| Calling before the `def` has run | `NameError` | Run the cell with the `def` first |
| One giant function | hard to test and read | One job per function (Day 19) |

## See also

- [09 Built-ins and comprehensions](09-built-ins-and-comprehensions.md): passing your function as `key=`
- [11 Exceptions](11-exceptions.md): `raise ValueError` from your own function
- [12 Modules, uv and testing](12-modules-uv-and-testing.md): put functions in a module and test them with pytest
- [15 Reading tracebacks](15-reading-tracebacks.md): following an error through several function calls
