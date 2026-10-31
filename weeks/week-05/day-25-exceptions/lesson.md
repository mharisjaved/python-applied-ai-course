# Day 25: Exceptions and Defensive Input

**Week 5 · Session 25 of 60 · Planned 75 min** · Previous: [Day 24](../day-24-writing-files-pathlib/lesson.md) · Next: [Day 26](../../week-06/day-26-modules-imports/lesson.md)

## Objectives

By the end of this lesson students can:

1. Wrap risky code in `try`/`except` and explain which lines run when an exception happens.
2. Catch **specific** exceptions (`ValueError`, `ZeroDivisionError`, `KeyError`, `FileNotFoundError`) with a
   helpful message for each, and show Python's message with `except ValueError as error:`.
3. Use `else` (runs only on success) and `finally` (always runs) correctly.
4. Write a retry loop that keeps asking until the input is valid.
5. `raise ValueError("clear message")` inside their own function, and explain why a bare `except:` is dangerous.

**Prior knowledge:** errors from bad conversion (Day 03), `KeyError` and `.get()` (Day 08), `while` loops and
`.isdigit()` validation (Day 13), `while True`/`break`/`continue` (Day 14), functions and `return` (Days 16–17),
print-checks (Day 19), reading files and `FileNotFoundError` (Day 23), `pathlib.Path` (Day 24).

**Files:** `demo.ipynb` · `practice.ipynb` · `solutions.ipynb` · `data/marks.txt` (demo section 8) ·
`data/step_counts.txt` (Exercise 5) · [Week 5 checkpoint](../../../assessments/weekly/week-05-checkpoint.md)
(print one copy per student).

## Timing

Today ends with the **Week 5 checkpoint**, so the concept part is brisk and practice continues as homework.

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:03 | Warm-up: errors we already know | core |
| 0:03–0:10 | `try`/`except` and the flow of control | core |
| 0:10–0:16 | Specific exceptions, `as error` | core |
| 0:16–0:20 | `else` and `finally` | core |
| 0:20–0:27 | Retry loops for input | core |
| 0:27–0:33 | `raise` in your own functions | core |
| 0:33–0:37 | Why bare `except:` is bad | core |
| 0:37–0:40 | Real-world example: safe file loader (demo section 8) | optional (skip for 60 min) |
| 0:40–0:57 | Practice exercises 1–3 (4–5 if time) | core |
| 0:57–0:72 | **Week 5 checkpoint** (15 min, individual, no notes) | core |
| 0:72–0:75 | Collect papers, preview Week 6 | core |
| +15 min | Exercises 4–5 in class, then go through two checkpoint questions together after collecting | optional (90-min session) |

**For 60 min:** skip demo sections 4 and 8 (students meet `else` in Exercise 6 and the loader in Exercise 5), give 12
minutes of practice (Exercises 1–3) and run the checkpoint for 15 minutes.

## 1. Warm-up (3 min)

Show the table in demo section 1 and ask students to supply the error name for each line from memory. Then run the
tagged cell `int("twelve")` and read the last line: **type** + **message**.

Key sentence: "These are called **exceptions**. A crash is just an exception that **nobody handled**. Today we
handle them."

## 2. `try` / `except` (7 min)

**Analogy:** a safety net under a trapeze. The artist (the `try` block) attempts the trick. If they fall
(an exception), the net (`except`) catches them and the show goes on. No fall → the net is never used.

```python
text = "twelve"
try:
    number = int(text)
    print("You typed", number)          # skipped when int() fails
except ValueError:
    print(f"'{text}' is not a whole number")
print("The program keeps running")
```

Trace the flow on the board with arrows: line 1 of `try` raises → **jump** to `except ValueError` → continue after.
The `print("You typed", ...)` line is skipped, **not** run later.

**Prediction question:** with `text = "12"`: *`You typed 12` and `The program keeps running`; the `except`
block is skipped entirely.*

## 3. Specific exceptions and `as error` (6 min)

Demo section 3, `split_bill(total_text, people_text)`, has two `except` blocks:

**Prediction question:** what does each call print?

```python
split_bill("90", "4")      # Each person pays 22.50
split_bill("90", "four")   # Please type numbers only.
split_bill("90", "0")      # There must be at least one person.
```

Then two short ones: `KeyError` for a menu lookup (`Sorry, we do not sell juice.`) and `FileNotFoundError` for a
missing file (`No marks file for 2025 yet.`). Mention that for dictionaries `.get()` (Day 08) is often simpler:
**check first** when it is easy, **try** when checking is hard (is this text a valid number?).

`except ValueError as error:` gives the exception a name; `print(error)` shows Python's message:
`Problem: invalid literal for int() with base 10: '4.5'`. We will use `error` (not `e`) as the name all course.

## 4. `else` and `finally` (4 min)

- `else:` runs only when the `try` block raised **nothing**.
- `finally:` runs **always**: success, handled error, even an unhandled one.

`show_first_line(path)` (demo section 4) prints `data/marks.txt: Asha,78` then `Finished checking data/marks.txt`,
and for a missing file `data/marks_2025.txt: not found` then `Finished checking ...`.

Why `else` at all? To keep the `try` block **small**, containing only the line that can fail. Otherwise a bug in
the "success" code could be mistaken for the error we meant to catch. Do not oversell `finally`: `with` already
closes files. Use it for "always do this" steps (a log line, a counter).

## 5. Retry loops for input (7 min)

Connect to Day 13: `.isdigit()` validation rejects `"12.5"` and `"-3"`. With `try` we accept whatever `float()`
accepts.

```python
def get_number(prompt):
    """Ask until the user types a valid number, then return it as a float."""
    while True:
        text = input(prompt)
        try:
            return float(text)
        except ValueError:
            print(f"'{text}' is not a number. Please try again.")
```

**Prediction question:** inputs `twelve`, (empty), `12.5`: how many error messages? (*Two; then
`Price with tax: 13.75`.*) Point out that `return` leaves the function **and** the loop, so no `break` is needed.

`get_int_in_range(prompt, low, high)` adds a range check after the conversion, using `continue` to go back to the
top of the loop after a conversion error. Mock run: `five` → `Please type a whole number.`, `9` →
`Please choose a number from 1 to 5.`, `4` → `Thanks for rating 4`.

## 6. `raise` in your own functions (6 min)

**Why:** a function that receives a bad value has three options: crash with a confusing error, return nonsense,
or **raise a clear error**. Show `percentage(part, whole)`:

```python
if whole <= 0:
    raise ValueError(f"whole must be greater than 0, got {whole}")
```

`percentage(5, 0)` (tagged cell) → `ValueError: whole must be greater than 0, got 0`. Compare with Python's
`ZeroDivisionError: division by zero`: ours says which value and what was expected. And without the check,
`percentage(5, -10)` would silently return `-50.0`.

Then show the caller deciding: `except ValueError as error: print("Could not calculate:", error)`.

Key message: **the function reports the problem, the caller decides what to do** (show a message, ask again, skip a
line). That is why we `raise` instead of `print` inside the function. Week 7 classes use exactly this pattern.

## 7. Why a bare `except:` is bad (4 min)

**Prediction question:** input `"42"` is valid. What prints? (*`Please type a number.`, which is wrong!*) The real
problem is the typo `numbr`, a `NameError` that the bare `except:` swallowed. With `except ValueError:` the
`NameError` appears (tagged cell) and we can fix it in seconds.

Rules for the board:
1. Always name the exception.
2. Keep the `try` block small.
3. Handle errors usefully; never hide them.

## 8. Real-world example: safe file loader (3 min, optional)

Demo section 8: `parse_mark_line(line)` validates **one** line and raises `ValueError` with a clear message;
`load_marks(path)` returns `{}` with a warning for a missing file, and for each bad line prints its number and
reason, then carries on:

```
Skipping line 2: invalid literal for int() with base 10: 'ninety'
Skipping line 5: invalid literal for int() with base 10: ''
Skipping line 7: expected 'name,mark' but got 'Diego 67'
Skipping line 8: mark must be 0-100, got 105
{'Asha': 78, 'Sara': 85, 'Mei': 91, 'Ken': 64}
```

Point out the `try` is **inside** the loop: one bad line must not stop the others. Project 03 (Day 30) needs this.

## 9. Common mistakes

| Mistake | What happens | How to explain it |
|---------|--------------|-------------------|
| bare `except:` | hides typos and other bugs (wrong message shown) | Name the exception you expect |
| huge `try` block around a whole loop | first bad line stops everything | Put the `try` around **one item's** work |
| `print` instead of `raise` in a function | the function returns nonsense or `None`, and the caller crashes later | `raise ValueError("…")` with a message |
| `return ValueError("…")` | no error at all; an error object is returned like a value | `raise`, not `return` |
| catching the wrong type (`except TypeError` for `int("abc")`) | the crash still happens | Run it once, read the type on the last line, catch that |
| retry loop without a way out | infinite loop with no valid input | `return` (or `break`) on success; interrupt the kernel if stuck (Day 13) |

## 10. Practice (17 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Name that exception | recognising the six common exception types | recall |
| 2 Make it safe | two specific `except` blocks, returning `None` | application |
| 3 Ask until it is valid | retry loop with conversion + range check | application |
| 4 Raise a clear error | `raise ValueError(f"…")` in own function | modification / application |
| 5 Safe file loader | `FileNotFoundError` + per-line `try` + own `raise` | problem solving |
| 6 Cash machine (challenge) | one `except` for Python's and own errors, `else`, `finally` | challenge |

Expected outcome in class: everyone completes 1–3; Exercises 4–5 are homework; 6 for fast students.

Exercise 3 uses `input()`. In VS Code, an input box appears at the top of the window; students sometimes miss it and
think the notebook froze. Show it once.

While circulating, look for:
- `except:` without a type (correct it every time today);
- `return` missing in the retry loop, which makes it loop forever even on valid input. Show how to interrupt the kernel;
- the range check placed inside `try` so a `150` is reported as "not a whole number".

## 11. Recap, checkpoint and exit ticket

Recap (2 min, before the checkpoint):
1. `try` the risky line; `except SpecificError:` handles it; the program continues.
2. `else` = success only; `finally` = always.
3. Retry loop: `while True` + `try: return ...` + `except ValueError: print(...)`.
4. `raise ValueError("clear message")` in your own functions; never use a bare `except:`.

**Checkpoint (15 min):** hand out the [Week 5 checkpoint](../../../assessments/weekly/week-05-checkpoint.md)
(individual, no notes, no computer). It replaces today's exit ticket. Collect it and mark with the answer key before
Day 26.

**Exit ticket (only if the checkpoint is moved to another day):** what does this print?

```python
for text in ["8", "x", "0"]:
    try:
        print(16 / int(text))
    except ValueError:
        print("not a number")
    except ZeroDivisionError:
        print("cannot divide by zero")
```

Answer: `2.0`, `not a number`, `cannot divide by zero`.

## Homework (30 min)

Finish Exercises 4 and 5. Then make your Day 24 `daily_log.py` (or the Hangman letter input from Day 20) robust:
use a retry loop so that bad input never crashes it, and handle a missing log file with `FileNotFoundError`.

## Next class

Week 6 starts with **modules and imports** (Day 26): `from pathlib import Path` will finally be explained, and
students will move functions like `get_number` and `load_marks` into their own `.py` module. Day 28 (debugging)
reads full tracebacks, and Day 29 replaces our print-checks with `assert` and pytest, including tests that check a
function **raises** the right error.

## Instructor notes

- Out of scope: custom exception classes, `raise ... from ...`, exception hierarchies, `except Exception`,
  re-raising with a bare `raise`, `pass`, and `traceback`. If a student asks about `except Exception:`, say "it is a
  slightly safer catch-all used at the very top of big programs. We always name the specific error in this course."
- Do not read full tracebacks today. Only the **last line** (type + message). Day 28 teaches reading the rest.
- `int(" 12 ")` works (spaces are ignored) but `int("12.0")` does not. Students are often surprised; `float()` first
  if decimals are allowed.
- The validator answers `input()` from the notebook metadata. In class the instructor types the inputs live:
  demo needs `twelve`, (Enter), `12.5`, then `five`, `9`, `4`.
- Slow students: let them copy the structure of `get_number` from the demo for Exercise 3 and only add the range check.
- Fast students: Exercise 6, then ask them to make `load_marks` also reject duplicate names with a raised
  `ValueError("duplicate name: ...")`.
