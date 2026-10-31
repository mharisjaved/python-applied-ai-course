# Modules, uv Projects and Testing

**What it is:** a module is a `.py` file you can `import`; uv manages a project's Python and packages; pytest runs your tests.
**Why it exists:** real programs are split into files, use other people's code, and need proof that they still work after every change.

**Taught on:** [Day 26](../../weeks/week-06/day-26-modules-imports/lesson.md) (imports, own modules, `__name__`) ·
[Day 27](../../weeks/week-06/day-27-packages-uv/lesson.md) (uv projects) ·
[Day 29](../../weeks/week-06/day-29-testing/lesson.md) (`assert`, pytest) · used in
[Day 30](../../weeks/week-06/day-30-project-expense-tracker/lesson.md)

## Syntax at a glance

| You want to… | Write | Then use |
|--------------|-------|----------|
| Import a whole module | `import math` | `math.sqrt(16)` |
| Import one name | `from math import sqrt` | `sqrt(16)` |
| Short alias | `import datetime as dt` | `dt.date.today()` |
| Your own module | `import pricing` (file `pricing.py` in the same folder) | `pricing.apply_discount(…)` |
| Code that runs only when the file is run directly | `if __name__ == "__main__":` | not when imported |
| Check something | `assert total == 60, "total should be 60"` | silent if True, `AssertionError` if False |

| uv command (terminal) | What it does |
|-----------------------|--------------|
| `uv init my_app` | new project folder with `pyproject.toml` |
| `uv add requests` | install a package into the project, record it in `pyproject.toml` and `uv.lock` |
| `uv run main.py` | run a file with the project's own Python and packages (`.venv`) |
| `uv run pytest -q` | run every `test_*.py` file |

`pyproject.toml` = what the project needs (you can read/edit it) · `uv.lock` = exact versions (do not edit) ·
`.venv/` = the installed packages (never commit it). A **package** is a folder of modules.

## Examples

### 1. Standard library modules

```python
import math
from collections import Counter
from datetime import date

print(math.sqrt(49), math.ceil(4.1))   # 7.0 5
words = "the cat and the hat and the bat".split()
print(Counter(words).most_common(2))   # [('the', 3), ('and', 2)]
print((date(2026, 12, 18) - date(2026, 10, 12)).days)   # 67
```

### 2. Your own module

```python
# file: pricing.py
"""Price helpers for the shop."""


def apply_discount(price, percent):
    """Return the price after a percent discount, rounded to cents."""
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (100 - percent) / 100, 2)


if __name__ == "__main__":
    # Runs with `uv run pricing.py`, but NOT when another file imports pricing
    print(apply_discount(80, 25))
```

### 3. Importing it from another file in the same folder

```python
# file: main.py
import pricing
from pricing import apply_discount as discount

print(pricing.apply_discount(50, 10))   # 45.0
print(discount(19.99, 0))               # 19.99
print(pricing.__name__, __name__)       # pricing __main__
```

### 4. `assert` in plain Python

```python
marks = [10, 20, 30]
assert sum(marks) == 60, "sum should be 60"
assert len(marks) == 3
print("all checks passed")   # all checks passed
```

### 5. A pytest file: normal, edge and error cases

```python
# file: test_pricing.py
import pytest

from pricing import apply_discount


def test_normal_case():
    assert apply_discount(80, 25) == 60.0


def test_edge_cases():
    assert apply_discount(80, 0) == 80
    assert apply_discount(80, 100) == 0


def test_bad_percent_raises():
    with pytest.raises(ValueError):
        apply_discount(80, 150)
```

Run it from the project folder:

```text
$ uv run pytest -q
...                                                                      [100%]
3 passed in 0.01s
```

A failing test prints the line, the values involved (`assert 59.0 == 60.0`) and `1 failed, 2 passed`.

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| Naming your file `random.py` or `math.py` | `AttributeError: module 'random' has no attribute 'randint'` | Rename your file (and delete `__pycache__`) |
| `import pricing.py` | `ModuleNotFoundError: No module named 'pricing.py'; 'pricing' is not a package` | `import pricing` (no `.py`) |
| Running from a different folder | `ModuleNotFoundError: No module named 'pricing'` | `cd` into the folder that contains the file |
| No `__name__` guard around the demo code | demo prints/asks for input when imported (and during tests) | Put it under `if __name__ == "__main__":` |
| Test function not starting with `test_` (or file not `test_*.py`) | `no tests ran` | Name both `test_…` |
| `assert(total == 60, "msg")` with brackets | always passes (`SyntaxWarning: assertion is always true`) | `assert total == 60, "msg"` |
| `pip install pandas` inside a uv project | package missing when you `uv run` | `uv add pandas` |
| Comparing floats exactly: `assert 0.1 + 0.2 == 0.3` | `AssertionError` | `assert round(0.1 + 0.2, 2) == 0.3` (or `pytest.approx`) |

## See also

- [08 Functions](08-functions.md): what you put in modules and test
- [11 Exceptions](11-exceptions.md): the errors your tests check for
- [15 Reading tracebacks](15-reading-tracebacks.md): reading pytest failure output
