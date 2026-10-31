# Exceptions: `try`, `except`, `raise`

**What it is:** an exception is Python's way of saying "something went wrong"; `try/except` lets you catch it and react.
**Why it exists:** users type letters into number fields and files go missing. A good program explains the problem instead of crashing.

**Taught on:** [Day 25](../../weeks/week-05/day-25-exceptions/lesson.md)

## Syntax at a glance

```text
try:
    code that might fail
except ValueError:              <- only this kind of error
    what to do instead
except (TypeError, KeyError):   <- several kinds, in brackets
    ...
else:                           <- optional: runs only if NO error happened
    ...
finally:                        <- optional: ALWAYS runs (cleanup, "done" message)
    ...
```

| You want to… | Write |
|--------------|-------|
| See the error message | `except ValueError as error:` then `print(error)` |
| Signal a problem from your own function | `raise ValueError("percent must be 0-100")` |
| Retry until the input is valid | `while True:` + `try:` … `break` + `except ValueError:` |

**Types you will catch most:** `ValueError` (right type, wrong value: `int("abc")`) · `TypeError` (`"5" + 3`) ·
`ZeroDivisionError` · `KeyError` / `IndexError` · `FileNotFoundError` (full list in [15](15-reading-tracebacks.md)).

## Examples

### 1. Catch bad number input

```python
text = "12a"   # pretend the user typed this
try:
    quantity = int(text)
    print("Quantity:", quantity)
except ValueError:
    print("That is not a whole number")
# That is not a whole number
```

### 2. Different errors, different messages

```python
for value in ["10", "x", "0"]:
    try:
        print(100 / int(value))
    except ValueError:
        print(f"'{value}' is not a number")
    except ZeroDivisionError:
        print("Cannot divide by zero")
# 10.0
# 'x' is not a number
# Cannot divide by zero
```

### 3. `else` and `finally`

```python
try:
    price = float("4.75")
except ValueError:
    print("Bad price")
else:
    print("Price OK:", price)   # runs only when there was no error
finally:
    print("Done checking")      # always runs
# Price OK: 4.75
# Done checking
```

### 4. Retry loop for user input

```python
while True:
    answer = input("How many tickets? ")
    try:
        tickets = int(answer)
        break
    except ValueError:
        print("Please type a whole number, e.g. 3")
print("Booking", tickets, "tickets")
# How many tickets? two        ← you type: two
# Please type a whole number, e.g. 3
# How many tickets? 3          ← you type: 3
# Booking 3 tickets
```

### 5. Raise a clear error from your own function

```python
def set_age(age):
    if age < 0 or age > 120:
        raise ValueError(f"age must be 0-120, got {age}")
    return age


try:
    set_age(150)
except ValueError as error:
    print("Problem:", error)
# Problem: age must be 0-120, got 150
```

### 6. A safe file loader

```python
def load_lines(filename):
    """Return the stripped lines of a file, or [] if it does not exist."""
    try:
        with open(filename, encoding="utf-8") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        print(f"{filename} not found, starting with an empty list")
        return []


print(load_lines("todo.txt"))
# todo.txt not found, starting with an empty list
# []
```

If nobody catches an exception, the program stops and prints a traceback ending in
`ValueError: age must be 0-120, got -5`; see [15 Reading tracebacks](15-reading-tracebacks.md).

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| Bare `except:` | hides *every* error, including your typos (`NameError`) | Catch the specific exception you expect |
| Catching the wrong type (`except ValueError` around `x / 0`) | program still crashes with `ZeroDivisionError` | Read the traceback's last line; catch that type |
| A huge `try` block around everything | you cannot tell which line failed | Keep only the risky line(s) inside `try` |
| Using a variable that the failed `try` never created | `NameError` after the `except` | Give it a default before `try`, or use `else:` |
| `except ValueError, TypeError:` | `SyntaxError: multiple exception types must be parenthesized` | `except (ValueError, TypeError):` |
| `raise "bad value"` | `TypeError: exceptions must derive from BaseException` | `raise ValueError("bad value")` |
| Returning `"error"` strings instead of raising | callers forget to check, bugs travel further | `raise` and let the caller decide |
| Retry loop with no `break` | asks forever even after valid input | `break` right after the line that can fail |

## See also

- [02 Numbers and input](02-numbers-and-input.md): where `ValueError` usually comes from
- [07 Loops](07-loops.md): `while True` + `break`
- [10 Files and paths](10-files-and-paths.md): `FileNotFoundError`
- [15 Reading tracebacks](15-reading-tracebacks.md): reading the error before catching it
- [12 Modules, uv and testing](12-modules-uv-and-testing.md): testing that a function raises with `pytest.raises`
