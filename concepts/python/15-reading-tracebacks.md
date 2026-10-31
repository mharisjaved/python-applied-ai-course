# Reading Tracebacks and Debugging

**What it is:** a traceback is Python's report of *what* went wrong and *where*; debugging is finding the cause systematically.
**Why it exists:** errors are normal. Reading the message carefully is faster than guessing and changing random lines.

**Taught on:** [Day 28](../../weeks/week-06/day-28-debugging/lesson.md) · first error messages on
[Day 02](../../weeks/week-01/day-02-variables/lesson.md) and [Day 03](../../weeks/week-01/day-03-numbers-input/lesson.md) ·
catching errors on [Day 25](../../weeks/week-05/day-25-exceptions/lesson.md)

## Read it bottom-up

```text
Traceback (most recent call last):
  File "report.py", line 10, in <module>         <- 3. where it started: your top-level call
    report("Omar", [])
    ~~~~~~^^^^^^^^^^^^
  File "report.py", line 6, in report            <- 2. which function called which
    print(f"{name}: {average(marks):.1f}")
                     ~~~~~~~^^^^^^^
  File "report.py", line 2, in average           <- 1b. the exact line that failed
    return sum(marks) / len(marks)
           ~~~~~~~~~~~^~~~~~~~~~~~
ZeroDivisionError: division by zero              <- 1a. START HERE: error type + message
```

1. **Last line:** the error type and message. 2. **Line just above:** the file, line number and code that failed.
3. **Walk upwards** through the calls until you reach a line *you* wrote and can change. Here the real cause is
line 10: `report` was given an empty list. The `~~~^^^` marks point at the part of the line that failed.

## Error types at a glance

| Error | Typical example | Message (Python 3.13) | Usual fix |
|-------|-----------------|-----------------------|-----------|
| `SyntaxError` | `print("hi"` | `'(' was never closed` | Python could not read the code; check brackets, quotes, colons (often on the line *before*) |
| `SyntaxError` | `if x > 3` | `expected ':'` | add the colon |
| `IndentationError` | body of `if` not indented | `expected an indented block after 'if' statement on line 1` | indent 4 spaces |
| `NameError` | `prnt("hi")` | `name 'prnt' is not defined. Did you mean: 'print'?` | typo, or the defining cell was not run |
| `TypeError` | `"Age: " + 5` | `can only concatenate str (not "int") to str` | convert types |
| `TypeError` | `len(5)` | `object of type 'int' has no len()` | check what the variable really holds |
| `TypeError` | `None + 1` | `unsupported operand type(s) for +: 'NoneType' and 'int'` | a function forgot to `return` |
| `ValueError` | `int("ten")` | `invalid literal for int() with base 10: 'ten'` | validate input / `try` |
| `IndexError` | `[1, 2][5]` | `list index out of range` | check `len()`; last item is `[-1]` |
| `KeyError` | `{"a": 1}["b"]` | `'b'` | `.get()` or check with `in` |
| `AttributeError` | `[].appendd(1)` | `'list' object has no attribute 'appendd'. Did you mean: 'append'?` | typo, or the object is not the type you think |
| `AttributeError` | `x.upper()` with `x = None` | `'NoneType' object has no attribute 'upper'` | something returned `None` earlier |
| `ZeroDivisionError` | `10 / 0` | `division by zero` | check for empty lists / zero before dividing |
| `FileNotFoundError` | `open("nope.txt")` | `[Errno 2] No such file or directory: 'nope.txt'` | check the path and the folder you run from |
| `ModuleNotFoundError` | `import pandaz` | `No module named 'pandaz'` | typo, or `uv add` the package |

## Examples

### 1. The program behind the traceback above

```python
# (shows an error)
def average(marks):
    return sum(marks) / len(marks)


def report(name, marks):
    print(f"{name}: {average(marks):.1f}")


report("Asha", [80, 90])   # Asha: 85.0
report("Omar", [])         # ZeroDivisionError: division by zero
```

### 2. Print debugging: look at the values, not at the code

```python
prices = ["4.50", "3.20", "10.00"]
total = 0
for p in prices:
    print("DEBUG p =", p, type(p))   # temporary line, delete when fixed
    total += float(p)
print(total)
# DEBUG p = 4.50 <class 'str'>
# DEBUG p = 3.20 <class 'str'>
# DEBUG p = 10.00 <class 'str'>
# 17.7
```

### 3. The error is reported far from the real mistake

```python
# (shows an error)
def get_discount(code):
    if code == "SAVE10":
        return 0.1
    # forgot: return 0 for other codes, so Python returns None


price = 50
discount = get_discount("HELLO")
print(price - price * discount)   # TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
```

The crash is on the last line, but the bug is the missing `return` inside `get_discount`.

## Debugging routine

1. Read the **last line**; look up the error type above. 2. Go to the **line number**; read the code there.
3. **Check the values**: `print("DEBUG", x, type(x))`, or a VS Code breakpoint (click left of the line number,
then *Run → Start Debugging* / F5; **F10** step over, **F11** step into, hover or use the *Variables* panel; in
notebooks use *Debug Cell*). 4. Change **one thing**, re-run, check. 5. Remove the debug prints.

## Common mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Reading only the first line ("Traceback…") | no idea what happened | Start from the last line |
| Fixing the line in the message when the cause is earlier | the error moves somewhere else | Ask "where did this value come from?" and walk back |
| Ignoring "Did you mean: …?" | time lost on a typo | Python is usually right about typos |
| `SyntaxError` pointing at a line that looks fine | you change correct code | Look at the line *before* (unclosed bracket or quote) |
| Changing several things at once | you don't know which change helped | One change, then re-run |
| Leaving `DEBUG` prints in the final code | noisy output | Delete them before you submit |

## See also

- [11 Exceptions](11-exceptions.md): catching errors you expect
- [12 Modules, uv and testing](12-modules-uv-and-testing.md): tests find bugs before users do
- [08 Functions](08-functions.md): the missing-`return` → `None` bug
