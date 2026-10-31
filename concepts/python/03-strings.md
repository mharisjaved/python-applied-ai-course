# Strings: Methods, Slicing and Formatting

**What it is:** a string (`str`) is a sequence of characters, with methods to clean, search and change text.
**Why it exists:** names, messages, file contents, user input and LLM replies are all text.

**Taught on:** [Day 04](../../weeks/week-01/day-04-strings/lesson.md) (methods, f-strings) ·
[Day 05](../../weeks/week-01/day-05-slicing-formatting/lesson.md) (indexing, slicing, format specs) · later:
`.isdigit()` on [Day 13](../../weeks/week-03/day-13-while-loops/lesson.md), `.isalpha()` on
[Day 21](../../weeks/week-05/day-21-built-in-functions/lesson.md)

## Syntax at a glance

| You want to… | Write | Result (with `s = " Hello World "`) |
|--------------|-------|--------------------------------------|
| Length | `len(s)` | `13` (spaces count) |
| Remove spaces at both ends | `s.strip()` | `"Hello World"` |
| Change case | `s.upper()` `s.lower()` `s.title()` | `" HELLO WORLD "` … |
| Replace | `s.replace("World", "Mei")` | `" Hello Mei "` |
| Count | `s.count("l")` | `3` |
| Find position | `s.find("World")` | `7` (`-1` if not found) |
| Check the start | `s.strip().startswith("He")` | `True` |
| Join / repeat | `"ab" + "cd"`, `"-" * 5` | `"abcd"`, `"-----"` |
| New line, tab | `"a\nb"`, `"a\tb"` | line break, tab |
| Insert values | `f"{name} is {age}"` | f-string (note the `f`) |
| One character | `s[1]`, `s[-1]` | first real letter `"H"`, last `" "` |
| Slice `[start:stop:step]` | `s[1:6]`, `s[::-1]` | `"Hello"`, reversed text (stop is **not** included) |
| Only digits? only letters? | `"2026".isdigit()`, `"Mei".isalpha()` | `True`, `True` |

**Format specs** (inside `{}` after a colon): `:.2f` two decimals · `:>8` right-align in 8 spaces ·
`:<8` left-align · `:,` thousands separator · combine them: `:>10,.2f`.

## Examples

### 1. Cleaning user text

```python
raw = "   asha KHAN  "
clean = raw.strip().title()
print(clean)                  # Asha Khan
print(len(raw), len(clean))   # 14 9
```

### 2. Strings never change: methods return a *new* string

```python
city = "lahore"
city.upper()          # result is thrown away
print(city)           # lahore
city = city.upper()   # keep the result
print(city)           # LAHORE
```

### 3. Searching text

```python
note = "Pay rent, pay water bill, pay phone"
print(note.count("pay"))            # 2   (case-sensitive)
print(note.lower().count("pay"))    # 3
print(note.find("water"))           # 14
print(note.find("gas"))             # -1
print(note.startswith("Pay"))       # True
print(note.replace("pay", "paid"))  # Pay rent, paid water bill, paid phone
```

### 4. f-strings

```python
name = "Bilal"
items = 3
total = 7.5
print(f"{name} bought {items} items for {total} dollars")   # Bilal bought 3 items for 7.5 dollars
print(f"Next year {name} will buy {items * 2} items")      # Next year Bilal will buy 6 items
```

### 5. Indexing and slicing

```python
code = "PK-2026-0417"
print(code[0], code[-1])   # P 7
print(code[3:7])           # 2026
print(code[-4:])           # 0417
print(code[:2])            # PK
print(code[::-1])          # 7140-6202-KP
```

### 6. Formatting a receipt line

```python
item = "Notebook"
qty = 12
price = 3.5
print(f"{item:<10}{qty:>4}{price * qty:>8.2f}")   # Notebook    12   42.00
print(f"{1234567.891:,.2f}")                      # 1,234,567.89
```

### 7. Changing one character is not allowed

```python
# (shows an error)
word = "data"
word[0] = "D"   # TypeError: 'str' object does not support item assignment
```

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| `"Age: " + 19` | `TypeError: can only concatenate str (not "int") to str` | `f"Age: {19}"` or `"Age: " + str(19)` |
| `name.upper()` without saving it | text unchanged | `name = name.upper()` |
| Forgot the `f`: `"Hi {name}"` | prints `Hi {name}` literally | `f"Hi {name}"` |
| `s[len(s)]` | `IndexError: string index out of range` | Last character is `s[len(s) - 1]` or `s[-1]` |
| Expecting `s[0:3]` to include index 3 | one character short | The stop index is excluded |
| `.find()` and expecting an error when missing | returns `-1` quietly | Check `if pos == -1` (Day 09) or use `in` |
| `s.upper` without `()` | `<built-in method upper of str object at 0x…>` | Call it: `s.upper()` |
| `"Yes" == "yes"` | `False` | Compare cleaned text: `answer.strip().lower() == "yes"` |

## See also

- [02 Numbers and input](02-numbers-and-input.md): `str()` / `int()` conversion
- [04 Lists and tuples](04-lists-and-tuples.md): `.split()` and `.join()` turn text into lists and back
- [09 Built-ins and comprehensions](09-built-ins-and-comprehensions.md): `.isdigit()`, `.isalpha()`, sorting text
