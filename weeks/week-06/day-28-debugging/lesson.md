# Day 28: Debugging and Tracebacks

**Week 6 · Session 28 of 60 · Planned 75 min** · Previous: [Day 27](../day-27-packages-uv/lesson.md) · Next: [Day 29](../day-29-testing/lesson.md)

## Objectives

By the end of this lesson students can:

1. Read a multi-level traceback bottom-up and name the error type, the failing line and the chain of calls.
2. Recognise the ten most common error types and give a typical cause for each.
3. Find a logic bug (wrong output, no error) with temporary `print(f"{name=}")` debug lines.
4. Use the VS Code debugger: set a breakpoint, Step Over / Step Into, read the Variables and Call Stack panels,
   and evaluate an expression in the Debug Console.
5. Follow a systematic process (reproduce → read → locate → hypothesise → check → fix → re-run) to fix five bugs.

**Prior knowledge:** functions and return values (Days 16–18), print-checks (Day 19), `try/except`, `raise`,
`except ValueError as error` (Day 25), modules and `if __name__ == "__main__":` (Day 26), `uv run` (Days 01, 27).
Students have *seen* plenty of tracebacks since Day 02 but have only read the last line.

**Files:** `demo.ipynb` (you) · `practice.ipynb` (students) · `solutions.ipynb` (you) · `buggy_grades.py` (debugger
walkthrough; contains 3 bugs on purpose, so do not fix the provided copy before class)

**Before class:** open `buggy_grades.py` in VS Code and press F5 once. The **Python Debugger** extension
(installed with the Python extension) must be present, and the interpreter (bottom-right of the status bar) must
be the course `.venv`.

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: "what does the last line of an error tell you?" | core |
| 0:05–0:15 | Anatomy of a traceback (demo 1–2) | core |
| 0:15–0:20 | Common error types (demo 3) | core |
| 0:20–0:28 | Print debugging + the debugging process (demo 4–5) | core |
| 0:28–0:48 | VS Code debugger walkthrough on `buggy_grades.py` (demo 6), students follow along | core |
| 0:48–0:70 | Practice exercises 1–4 (five bugs) | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Demo 7–8 (bad habits, discount bug) and Exercise 5 with **Debug Cell** | optional (90-min session) |

For a 60-minute session: shorten demo 3 to the table only, do bugs 1 and 2 of the walkthrough, and set
Exercise 4 as homework.

## 1. Warm-up (5 min)

Write on the board: `ValueError: invalid literal for int() with base 10: 'ten'`. Ask: "What happened, and what
was the input?" (*`int("ten")`: the right type, a string, but an impossible value.*) Then: "Since Day 02 we have
read only the last line of an error. Today we read the rest, because it tells us *where* and *how*."

## 2. Anatomy of a traceback (10 min)

**Intuition:** a traceback is a **trail of breadcrumbs**: Python records every function call that led to the
crash. The newest call is at the bottom ("most recent call last").

Live code (demo section 1): `print_receipt` → `total_price` → `parse_price`, called with `["2.50", "1,20", "3.00"]`.

Read it together, bottom-up, and write the three questions on the board:

| Question | Where to look | Answer here |
|----------|---------------|-------------|
| **What** went wrong? | last line | `ValueError: could not convert string to float: '1,20'` |
| **Where** did it happen? | the block just above | `parse_price`, line `return float(text)` |
| **How** did we get there? | further up | cell → `print_receipt` → `total_price` → `parse_price` |

Key point: the line that crashed (`float(text)`) is not wrong; the **data** was wrong. The cause can be anywhere
up the chain.

**Prediction question (demo section 2):** show the `stock` dict and `needs_restock("Bread")`. Ask for the error
type and the function *before* running. (*`KeyError: 'Bread'` in `quantity_of`, called from `needs_restock`.*)

In `.py` files, tracebacks show `File "…/buggy_grades.py", line 34, in average`, and Python 3.13 underlines the
failing part with `~~~^^^`. In notebooks the same blocks show `Cell In[5], line 2`.

## 3. Common error types (5 min)

Go through the table in demo section 3 quickly; run the three live examples (`TypeError`, `IndexError`,
`AttributeError`). Ask students which ones they have met already. Most have met all of them.
Point out `SyntaxError` is different: Python refuses to *start*, so no code runs at all.

## 4. Print debugging and the process (8 min)

**Problem:** logic bugs produce wrong answers *without* an error, so there is no traceback to read.

Live code (demo section 4): `average_of_last([55, 70, 80, 90], 3)` returns `75.0` instead of `80.0`.

**New today:** `print(f"DEBUG {scores=} {n=} {recent=}")`. Inside an f-string, `{name=}` prints `name=value`,
and strings appear with quotes. Output: `DEBUG scores=[55, 70, 80, 90] n=3 recent=[70, 80]`, so the last score is
missing; `[-n:-1]` should be `[-n:]`. Remove debug prints after fixing.

Then show the six-step process (demo section 5) and leave it on the board for the rest of the lesson. Stress
**"change one thing at a time"** and **"re-run all your checks"**.

## 5. The VS Code debugger: walkthrough on `buggy_grades.py` (20 min)

Students open `buggy_grades.py` in VS Code and follow each step on their own machine. Its docstring shows the
correct output. Line numbers below are for the **unedited** file.

**Step 1: reproduce.** In the terminal:

```
cd weeks/week-06/day-28-debugging
uv run buggy_grades.py
```

Output: `Class report`, then a traceback ending in `ZeroDivisionError: division by zero`. Read it bottom-up:
`average` line 34 (`return total / len(marks)`) ← `build_report` line 47 ← `main` line 59 ← line 66.
Demo section 6 shows the same traceback from the notebook. **Question:** "Which student caused it?"
The traceback doesn't say, so we need to see the values.

**Step 2: let the debugger stop at the crash.** Press **F5** and choose **Python Debugger: Current File**
(VS Code may ask once). With no breakpoints, the debugger **pauses on the uncaught exception**: line 34 is
highlighted. Show the panels:
- **Variables:** `marks = []`, `total = 0`.
- **Call Stack:** `average` / `build_report` / `main` / `<module>`, the traceback as a clickable list. Click
  `build_report`: its Variables show `name = 'Omar'`.

Bug 1 found: Omar has no marks and the docstring promises 0 for an empty list. Press **Shift+F5** (stop), then add
at the start of `average`:

```python
    if len(marks) == 0:
        return 0
```

**Step 3: a wrong answer.** `uv run buggy_grades.py` again. No crash, but `Asha 30.7 FAIL` (expected `85.0 pass`).
Click left of the line `total = 0` in `average` to set a **breakpoint** (red dot). Press **F5**: the program pauses
there during Asha's turn. Press **F10 (Step Over)** repeatedly and watch Variables:

| After line | `mark` | `total` |
|------------|--------|---------|
| `total = 0` | – | 0 |
| `total = mark` (1st) | 78 | 78 |
| `total = mark` (2nd) | 85 | **85**, but it should be 163 |

Bug 2: `total = mark` replaces instead of adding. Stop, change it to `total += mark`, remove the breakpoint
(click the red dot).

**Step 4: Step Into and the Debug Console.** Run again: everything is right except `Mei 50.0 FAIL`. Set a breakpoint
on the line `if has_passed(avg):` in `build_report` (line 50 now; line 48 before the first fix). To skip the first three students, right-click the red dot →
**Edit Breakpoint → Expression** → `name == "Mei"` (a *conditional breakpoint*). Press F5. Then **F11 (Step Into)**
goes *inside* `has_passed`: Variables shows `avg = 50.0`. In the **Debug Console** type `avg > PASS_MARK` (→ `False`)
and `avg >= PASS_MARK` (→ `True`). The docstring says "exactly 50 passes". Bug 3: change `>` to `>=`. Show
**Shift+F11 (Step Out)** to return to `build_report`, then stop.

**Step 5: re-run everything.** `uv run buggy_grades.py` now matches the expected output in the docstring:
`Passed: 4 of 5`.

Summary of controls (also in demo section 6): breakpoint · F5 start/continue · F10 Step Over · F11 Step Into ·
Shift+F11 Step Out · Shift+F5 stop.

## 6. Common mistakes (covered while circulating)

| Mistake | Symptom | How to explain it |
|---------|---------|-------------------|
| Reading only the top of the traceback | "the error is in the `print` line" | the top is where the chain *started*; read bottom-up |
| Fixing the line that crashed when the data is wrong | code becomes weird, bug remains | ask "is this line wrong, or the value it received?" |
| `try/except: pass` to silence an error | error gone, wrong results | hiding is not fixing; catch only errors you expect |
| Changing several things at once | "it works now, but I don't know why" | one change, then re-run |
| Debugger never stops | breakpoint on a line that never runs, or file run with `uv run` instead of F5 | breakpoints only work in a debug session |
| Kernel uses the old module after a fix | notebook still shows the bug | restart the kernel (Day 26) |

## 7. Practice (22 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Read the traceback | three questions: what / where / how | recall |
| 2 Fix the crashes (bugs 1–2) | `TypeError`, off-by-one `IndexError` | modification |
| 3 Fix the wrong answers (bugs 3–4) | reset inside a loop, `or` vs `and` | reasoning |
| 4 Print debugging (bug 5) | `f"{name=}"` reveals strings vs numbers | problem solving |
| 5 Two bugs, one function (challenge) | precedence + missing validation, **Debug Cell** | challenge |

While circulating, look for:
- "fixes" that stop the crash but give the wrong output (`str(price)` gives `3.5`, not `3.50`);
- students guessing instead of adding a debug print; ask "what is the value of `count` after each mark?";
- in Exercise 4, students who add `int()` but keep `best_score = "0"`. The new `TypeError` is progress, so say so.

Expected outcome: everyone fixes bugs 1–4, most fix bug 5, fast students do Exercise 5.

## 8. Recap and exit ticket (5 min)

1. Read tracebacks bottom-up: **what** (last line) → **where** (block above) → **how** (further up).
2. No error but wrong output? Print values with `f"{name=}"` or pause with a breakpoint.
3. Debugger: breakpoint, F5, F10 over, F11 into, Variables, Call Stack, Debug Console.

**Exit ticket:** a traceback has these blocks, top to bottom: `<module>` line 40 → `main` line 31 →
`load_scores` line 12 → `ValueError: invalid literal for int() with base 10: 'abc'`. Which function contains the
failing line, and which function called it?

Answer: `load_scores` (line 12) failed; it was called by `main` (line 31).

## Homework (20 min)

Finish Exercise 4 (and 5 if you like). Then take one program you wrote earlier (Hangman or the Day 25 safe
loader), set a breakpoint inside a loop and step through one full iteration, writing down how two variables change.

## Next class

Day 29 turns today's `print(f(x) == expected)` checks into **automatic tests**: `assert`, choosing normal/edge/error
cases, `test_*.py` files and `uv run pytest`. Teaser: "Each bug you fixed today could come back next month. A test
makes sure it can't come back unnoticed."

## Instructor notes

- Do **not** go into `pdb`, logging, `launch.json` configuration, watch expressions or exception chaining today.
  The debugger needs no configuration for a single file.
- If F5 runs without stopping at the `ZeroDivisionError`, check the **Breakpoints** panel: "Uncaught Exceptions"
  should be ticked (it is by default).
- `f"{name=}"` is the one piece of new syntax today. It works only inside f-strings and needs Python 3.8+.
- Logic bugs are harder than crashes. That is the message of Exercise 3: a crash is a gift because it tells you
  where to look.
- Students will want to fix `buggy_grades.py` in place. Fine for class, but the provided file should stay buggy
  for next year: tell them to work on a copy (`buggy_grades_mine.py`) or restore it afterwards.
- Fast students: Exercise 5 with **Debug Cell**, then ask them to write the bug report for bug 5 as "expected /
  actual / cause / fix" in four lines.
- Slow students: Exercises 1–3 are the core. Sit with them for one debugger session; seeing `total` change line by
  line is the moment it clicks.
