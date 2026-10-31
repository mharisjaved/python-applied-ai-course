# Numbers, Operators and Input

**What it is:** arithmetic operators, `input()` to read what the user types, and conversion functions between types.
**Why it exists:** most programs calculate something (a bill, an average) from numbers the user gives them.

**Taught on:** [Day 03](../../weeks/week-01/day-03-numbers-input/lesson.md)

## Syntax at a glance

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` `-` `*` | add, subtract, multiply | `7 * 2` | `14` |
| `/` | divide (always gives a `float`) | `8 / 2` | `4.0` |
| `//` | floor division (whole part) | `7 // 2` | `3` |
| `%` | remainder (modulo) | `7 % 2` | `1` |
| `**` | power | `2 ** 3` | `8` |
| `+=` `-=` `*=` | update in place | `steps += 100` | same as `steps = steps + 100` |

**Precedence (who goes first):** `( )` → `**` → `* / // %` → `+ -`. When unsure, add parentheses.

| Function | What it does | Example | Result |
|----------|--------------|---------|--------|
| `input("prompt")` | shows the prompt, waits, returns what was typed **as text** | `input("Age? ")` | `"17"` (a `str`) |
| `int(x)` | to whole number | `int("17")` | `17` |
| `float(x)` | to decimal | `float("2.5")` | `2.5` |
| `str(x)` | to text | `str(42)` | `"42"` |
| `round(x, n)` | round to `n` decimals | `round(3.14159, 2)` | `3.14` |

## Examples

### 1. Splitting a bill

```python
bill = 47.5
people = 4
share = bill / people
print(share)             # 11.875
print(round(share, 2))   # 11.88
```

### 2. `//` and `%` together: minutes to hours

```python
minutes = 135
hours = minutes // 60
left_over = minutes % 60
print(hours, "h", left_over, "min")   # 2 h 15 min
print(10 % 2, 11 % 2)                 # 0 1   (remainder 0 means "even")
```

### 3. Precedence

```python
print(2 + 3 * 4)      # 14
print((2 + 3) * 4)    # 20
print(10 - 4 / 2)     # 8.0
```

### 4. Updating a running total with `+=`

```python
steps = 0
steps += 2500    # morning walk
steps += 4000    # evening walk
print(steps)     # 6500
```

### 5. `input()` always gives text, so convert it

```python
age_text = input("How old are you? ")   # you type: 17
age = int(age_text)
print(age + 1)                          # 18
print(type(age_text), type(age))        # <class 'str'> <class 'int'>
```

### 6. Converting in one line

```python
price = float(input("Price: "))   # you type: 12.5
quantity = int(input("How many? "))  # you type: 3
print("Total:", price * quantity)    # Total: 37.5
```

### 7. Joining a number to text with `str()`

```python
count = 3
print("You have " + str(count) + " new messages")   # You have 3 new messages
```

### 8. Text + number does not work

```python
# (shows an error)
age_text = "17"
print(age_text + 1)   # TypeError: can only concatenate str (not "int") to str
```

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| Calculating with `input()` directly: `input("Age? ") + 1` | `TypeError: can only concatenate str (not "int") to str` | `int(input("Age? ")) + 1` |
| `"3" * 2` when you meant maths | `"33"` (no error!) | Convert first: `int("3") * 2` gives `6` |
| `int("3.5")` | `ValueError: invalid literal for int() with base 10: '3.5'` | `float("3.5")`, or `int(float("3.5"))` to drop the decimals |
| User just presses Enter: `int("")` | `ValueError: invalid literal for int() with base 10: ''` | Validate the input (loops on Day 13, `try` on Day 25) |
| Expecting `8 / 2` to be `4` | prints `4.0` | `/` always gives a float; use `//` for a whole number |
| `0.1 + 0.2 == 0.3` | `False` (result is `0.30000000000000004`) | Computers store decimals approximately; use `round(…, 2)` before showing money |
| `round(2.5)` | `2`, not `3` | Python rounds exact halves to the even number; fine for everyday use |
| Forgetting brackets: `total / count * 100` vs `total / (count * 100)` | wrong answer, no error | Add parentheses to say what you mean |

## See also

- [01 Variables and types](01-variables-and-types.md)
- [03 Strings](03-strings.md): f-strings and `:.2f` formatting for nicer output
- [11 Exceptions](11-exceptions.md): stop bad input from crashing the program
