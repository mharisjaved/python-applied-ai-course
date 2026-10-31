# Day 26: Modules and Imports

**Week 6 · Session 26 of 60 · Planned 75 min** · Previous: [Day 25](../../week-05/day-25-exceptions/lesson.md) · Next: [Day 27](../day-27-packages-uv/lesson.md)

## Objectives

By the end of this lesson students can:

1. Import a module in three ways (`import m`, `from m import name`, `import m as nick`) and say when each is useful.
2. Use four standard-library tools: `math.ceil`, `random.sample`, `datetime.date` (today, from text, subtracting
   dates) and `collections.Counter` (`most_common`).
3. Move functions into their own `.py` file in the same folder and import them from a notebook.
4. Explain what `if __name__ == "__main__":` does by running a module with `uv run` and by importing it.
5. Fix `NameError`, `ImportError` and `ModuleNotFoundError` caused by imports, and restart the kernel after
   editing a module.

**Prior knowledge:** functions with parameters, `return` and defaults (Days 16–18), print-checks
`print(f(x) == expected)` (Day 19), `help()` and `sorted(key=)` (Day 21), comprehensions (Day 22),
`try/except` (Day 25). `import random` was used on Day 14 without explanation. Today we explain it properly.

**Files:** `demo.ipynb` (you) · `practice.ipynb` (students) · `solutions.ipynb` (you) · `textutils.py` (example
module) · `name_demo.py` (shows `__name__`) · `solution_gradetools.py` (reference for practice Exercise 5)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: retrieval questions on functions and exceptions | core |
| 0:05–0:12 | Why modules + `import math` (demo 1–2) | core |
| 0:12–0:18 | `from … import`, `as` (demo 3) | core |
| 0:18–0:30 | Standard-library tour: `random`, `datetime`, `Counter` (demo 4) | core |
| 0:30–0:43 | Your own module + `__name__` + terminal (demo 5–6) | core |
| 0:43–0:48 | Common mistakes + real-world example (demo 7–8) | core |
| 0:48–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (challenge) together, or students convert their Day 19 text-statistics functions into a module | optional (90-min session) |

For a 60-minute session: skip `help()` and `statistics` in demo 3, shorten demo 8 to one run, and set Exercise 5 as homework.

## 1. Warm-up (5 min)

Write on the board and ask for answers without running anything:

```python
def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return 0

print(safe_int("12") + safe_int("twelve"))
```

Answer: `12`. Follow-up: "Functions like this one from Day 25 are useful in every program. How would you reuse it without
copy-pasting it?" Collect ideas; the answer is today's topic.

## 2. Why modules + `import math` (7 min)

**Problem first:** a 600-line file is hard to navigate, and copy-pasted functions drift apart (you fix a bug in
one copy and forget the other four). A **module** is just a `.py` file. `import` lets one file use another's
functions. Python comes with hundreds of modules (the *standard library*, "batteries included").

> **Analogy:** a module is a toolbox in the cupboard. `import math` brings the whole box to your desk. To use a
> tool you name the box and the tool: `math.sqrt`.

Live code (demo section 2):

```python
import math
print(math.sqrt(81))          # 9.0
print(math.ceil(4.2))         # 5
print(math.floor(4.8))        # 4
print(math.ceil(47 / 12))     # 4 buses for 47 students, 12 seats each
```

**Prediction question:** before running, ask "does `ceil` round 4.2 up or to the nearest?" Then show `help(math.ceil)`.
Point out that `help` works on module contents because they are ordinary functions with docstrings.

## 3. `from … import` and `as` (6 min)

```python
from math import ceil, sqrt     # copy these names in: ceil(9.01) -> 10
import statistics as stats      # nickname: stats.mean([72, 85, 64, 90, 85]) -> 79.2
```

Use the table in demo section 3. Recommendation for beginners: **default to `import module`**, because the
`module.` prefix tells a reader where each name comes from. Use `from` for one or two names used often, and `as`
for conventions they will meet in Week 9 (`np`, `pd`, `plt`). Say "don't use `from x import *`" and move on.

## 4. Standard-library tour (12 min)

Keep each tool to 2–3 minutes. The goal is recognition plus one useful call, not completeness.

| Module | Use today | Example | Output |
|--------|-----------|---------|--------|
| `random` | repeatable picks | `random.seed(3)` then `random.sample(names, 2)` | `['Bilal', 'Mei']` |
| `datetime` | dates | `date(2026, 12, 18) - date(2026, 11, 16)` | `32 days, 0:00:00` (`.days` → `32`) |
| `datetime` | dates from text | `date.fromisoformat("2026-10-12")` | `2026-10-12` |
| `collections` | counting | `Counter(votes).most_common(1)` | `[('museum', 3)]` |

Key teaching points:
- `from datetime import date`: the **module** is `datetime`, the **type** inside it is `date`. Students will
  mix these up all week; say it twice.
- `date.today()` changes every day, so use fixed dates whenever a result is discussed or checked.
- `date.fromisoformat("2026-02-30")` raises `ValueError`, so it doubles as a free date validator. The
  Expense Tracker on Day 30 uses exactly this.
- `Counter` is a dict that counts. Show the Day 12 loop next to it so students see it replaces code they already
  understand. A missing key gives `0`, not `KeyError`.

**Prediction question (demo 4b):** "What do you get when you subtract two dates?" Most will guess a number.
It is a time difference whose `.days` is the number.

## 5. Your own module and `__name__` (13 min)

Open `textutils.py` in VS Code next to the notebook. Walk through it top to bottom: docstring, one import,
a constant, four functions, then the `if __name__ == "__main__":` block at the bottom.

Live code (demo section 5):

```python
import textutils
review = "Great coffee, great music. The coffee was hot and the staff were great!"
print(textutils.word_count(review))   # 13
print(textutils.top_words(review))    # [('great', 3), ('coffee', 2), ('the', 2)]
```

Rule: the notebook and the module must be in the **same folder**; import by file name without `.py`.

**`__name__` (demo section 6):** every module has a variable `__name__`. In the file you *run* it is
`"__main__"`, and in an *imported* file it is the module's name. Show it both ways:

1. In the notebook: `import name_demo` prints `Its __name__ is: name_demo` and `-> I was imported by another file.`
2. In the VS Code terminal:

   ```
   cd weeks/week-06/day-26-modules-imports
   uv run name_demo.py
   ```

   Output: `Its __name__ is: __main__` and `-> I was run directly.`
3. Then `uv run textutils.py`: four `True` self-checks. In the notebook, `import textutils` printed nothing.

> **Analogy:** a module is a recipe card. When you *cook from it* (run it), you also do the "taste test" at the
> bottom. When someone *photocopies it into their cookbook* (imports it), they want the recipes, not your taste test.

**Prediction question:** "What happens if I run `import name_demo` again?" Nothing: modules run only on the
first import. Consequence: **after editing a `.py` file, restart the kernel.** Demonstrate this live: add a
`print` to `textutils.py`, re-import (nothing changes), restart, import (it appears). Then remove the `print`.

## 6. Common mistakes (3 min)

Run the tagged cells in demo section 7 and read the last line of each error:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `from math import ceil` then `floor(7.9)` | `NameError: name 'floor' is not defined` | `from` brings in only the names you list |
| `import statistics as stats` then `statistics.median(...)` | `NameError: name 'statistics' is not defined` | after `as`, only the nickname exists |
| `import textutil` | `ModuleNotFoundError: No module named 'textutil'` | typo, or the file is in another folder |
| `from collections import counter` | `ImportError: cannot import name 'counter'` | names are case-sensitive |
| Own file named `random.py` | strange `AttributeError`s from the real `random` | your file shadows the standard module, so rename it |
| Edited the module, notebook ignores it | no error, old behaviour | restart the kernel |

Then run demo section 8 (club trip) as a quick "everything together" example: `Counter` finds people who
signed up twice, date subtraction counts days, `random.shuffle` with a seed makes a seating order.

## 7. Practice (22 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Three ways to import | predicting import styles, `floor` of negatives | recall |
| 2 Standard library errands | `math.ceil`, dates, `Counter`, `random.sample` | application |
| 3 Use the `textutils` module | calling functions from your own module | application |
| 4 Fix the imports | `NameError` / `ImportError` / `ModuleNotFoundError` | modification |
| 5 Write your own module | creating `gradetools.py`, `__name__`, `uv run` | problem solving |
| 6 Birthday calculator (challenge) | date comparison, edge cases | challenge |

While circulating, look for:
- `gradetools.py` saved in the wrong folder, or as `gradetools.py.txt` on Windows;
- "my fix doesn't work" after editing the module: they need to **restart the kernel**;
- self-checks written outside the `if __name__` block, so they appear in the notebook;
- `datetime.date(...)` after `from datetime import date`.

Expected outcome: everyone completes 1–4, most complete 5, fast students try 6.

## 8. Recap and exit ticket (5 min)

Recap (ask students to supply each line):
1. A module is a `.py` file; `import` runs it once and gives you its names.
2. `import m` → `m.name`; `from m import name` → `name`; `import m as x` → `x.name`.
3. `if __name__ == "__main__":` code runs only when the file is run directly, not when imported.

**Exit ticket:** `helpers.py` contains:

```python
print("loading helpers")

def double(n):
    return n * 2

if __name__ == "__main__":
    print(double(21))
```

What does `uv run helpers.py` print? What does `import helpers` (in another file) print?

Answer: run → `loading helpers` then `42`; import → only `loading helpers`.

## Homework (20 min)

Finish Exercise 5. Then move two functions you wrote earlier (for example from Day 19's text-statistics tool or
Day 25's safe input) into a module of your own, add self-checks under `if __name__ == "__main__":`, and import
them from a fresh notebook.

## Next class

Day 27 moves from modules *you* write to packages *other people* write: why every project gets its own virtual
environment, `uv init` / `uv add` / `uv run`, what `pyproject.toml` and `uv.lock` are, and how a folder of modules
becomes a **package**. Teaser: "Today every import came from Python itself or from our folder. Tomorrow we install
something from the internet without breaking anything else."

## Instructor notes

- The kernel's working folder is the notebook's folder, which is why `import textutils` works. If a student
  opens the notebook from a different place and gets `ModuleNotFoundError`, check where the `.py` file is.
- Do **not** explain `sys.path`, the import system, `importlib.reload` or relative imports today. "Restart the
  kernel" is the only fix students need. `sys.path` gets a short look on Day 27.
- `from datetime import date` vs `import datetime` confuses everyone. Use only `from datetime import date` in
  examples and in the project.
- If asked about `timedelta` (adding days to a date): `date(2026, 11, 16) + timedelta(days=14)` after
  `from datetime import timedelta`. Fine to show to fast students; it is not needed this week.
- `random.seed` was used on Day 14. Remind students it makes randomness repeatable, which matters again in
  Week 10 (`random_state=`).
- Fast students: ask them to write `textutils.longest_word(text)` with a self-check, re-run `uv run textutils.py`,
  then restart the kernel and use it. Remind them to undo the change afterwards (or work in a copy) so the
  provided file stays as it was.
- Slow students: concentrate on Exercises 1, 3 and 4. Importing and calling is the core skill; writing a module
  can wait until homework.
