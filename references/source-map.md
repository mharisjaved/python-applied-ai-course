# Reference Source Map

How the instructor's personal learning repository (`learn-python`) relates to this course.
`learn-python` is **read-only reference material**. Nothing from it is copied into this course. All lessons,
examples, exercises, datasets and project implementations here are original.

Reference location: `/home/harry/Desktop/prcx_01/xx_github/learn-python` (inspected 2026-10-13).

## 1. What the reference folder contains

| Area | Contents | Useful for this course? |
|------|----------|-------------------------|
| `notebooks/02-…` to `13-…` | 47 notebooks of course notes and exercises (functions, OOP, errors, modules, decorators, generators, images, email, advanced data structures) | Yes. Topic order and prerequisite chain |
| `notebooks/06-…/01-unittest/` | Small `unittest` example (`capitalize_module.py`, `test.py`) and a `pylint` demo script | Yes. Week 6 testing idea (re-taught with `assert` + pytest) |
| `data-structures-algorithms/` | 9 notebooks: interview patterns (frequency counting, two pointers, stack, binary search, sliding window…) | Mostly too advanced. A few patterns become optional challenges |
| `leetcode/` | 4 LeetCode solutions (two sum, add two numbers, longest substring, median of arrays) | No. Beyond beginner level |
| `pyproject.toml`, `uv.lock` | uv project, Python 3.13, deps: fastapi, pillow, pylint, uvicorn | Confirms uv + Python 3.13 workflow |
| `.env` | Environment secrets | **Not opened.** Never copy |

### Important gaps and inconsistencies

1. **Udemy Module 01 ("Python Object and Data Structure Basics") has no notebooks.** Variables, numbers,
   strings, lists, dictionaries, tuples, sets, booleans and basic file I/O (course Days 2 to 10) have no local
   reference material, so those lessons are written from scratch. `13-advanced-python-objects…` only covers extra
   *methods* of numbers, strings, sets and dicts.
2. **Module 02 ("Python Statements") only has a test notebook** (`statements_test.ipynb`: `for` + `split` + `if`,
   `range`, comprehensions, FizzBuzz). There are no teaching notes for `if`, `for` or `while`.
3. **Folder numbers do not match the README's module table.** E.g. folder `06` is *Errors* but the README lists
   06 = *Modules and Packages*; folder `07` is *Milestone II* but README 07 = *Errors*. Modules 13 *Web Scraping*,
   15 *PDFs & Spreadsheets* and 17 *Final Capstone* have no folders at all.
   → **The mapping to official Udemy section numbers is UNVERIFIED.** The table below uses local folder paths only.
4. **No AI, data science or machine learning material exists.** Weeks 9 to 12 are entirely original.
5. Several reference notebooks contain Udemy exercise sets verbatim (e.g. the "function practice" problems).
   Those exercise texts and solutions are **not reused**; only the idea of "warm-up → level 1 → level 2 → challenge"
   progression is kept.

## 2. Topic mapping

Adaptation key: **Reuse idea** = same concept, new original examples · **Simplify** = beginner subset only ·
**Defer** = optional/extension only · **Exclude** = not taught · **New** = no reference material.

| Reference topic | Source location (in `learn-python/`) | Target week/day | Adaptation | Notes |
|-----------------|--------------------------------------|-----------------|------------|-------|
| Environment, uv, running Python | `README.md`, `pyproject.toml` | W1 D01 | Reuse idea | Taught 2026-10-12 |
| Variables, data types, numbers | *(none, Module 01 missing)* | W1 D02–D03 | New | |
| Advanced numbers (`abs`, `round`, `pow`, `hex`, `bin`) | `notebooks/13-…/00_advanced_numbers.ipynb` | W1 D03, W5 D21 | Simplify | `hex`/`bin` excluded |
| Strings and string methods | `notebooks/13-…/01_advanced_strings.ipynb` | W1 D04–D05 | Simplify | Keep `upper/lower/strip/replace/count/find/split`; skip `expandtabs`, `partition` |
| Lists, tuples | *(none)* | W2 D06–D07 | New | |
| Dictionaries, sets | `notebooks/13-…/02_advanced_set.ipynb`, `03_advanced_dictionary.ipynb` | W2 D08 | Simplify | Set update methods excluded; dict comprehensions moved to W5 D22 |
| Booleans, `if/elif/else` | *(none)* | W2 D09–D10 | New | |
| `for`, `range`, `split` + `if` | `notebooks/02-python-statements/statements_test.ipynb` | W3 D11–D12 | Reuse idea | |
| `while`, `break`, `continue` | *(none)* | W3 D13–D14 | New | |
| FizzBuzz-style loop problems | `statements_test.ipynb` | W3 D14 practice | Reuse idea | Original variants used |
| Functions, return values, scope | `notebooks/03-methods-functions/00_python_functions.ipynb`, `02_lambda_map_filter.ipynb` (scope part) | W4 D16–D18 | Reuse idea | |
| `*args` / `**kwargs` | `00_python_functions.ipynb` | W4 D18 (optional box) | Defer | Mentioned only so students recognise the syntax |
| Function practice problem sets | `01_function_practice_excersice.ipynb`, `03_functions_methods_assignment.ipynb` | W4 D17–D19 practice | Reuse idea | Progression kept, all problems original |
| Lambda, `map`, `filter` | `02_lambda_map_filter.ipynb` | W5 D22 | Defer | Comprehensions taught instead; lambda only as `sorted(key=...)` aside |
| Milestone 1: Tic-Tac-Toe | `notebooks/04-milestone/00_milestone_project.ipynb` | W4 D20 (Project 02) | Reuse idea | Course uses **Hangman** (simpler); Tic-Tac-Toe offered as an extension |
| Classes, `__init__`, attributes, methods | `notebooks/05-…/00_attributes_and_class_keywords.ipynb` | W7 D32–D33 | Simplify | |
| `__str__` and dunder methods | `notebooks/05-…/08_special_magic_dunder_methods.ipynb` | W7 D33 | Simplify | `__str__` only (`__len__`, `__del__` excluded) |
| Composition / aggregation | `notebooks/05-…/04_aggregation_composition.ipynb` | W7 D34 | Reuse idea | |
| Inheritance, polymorphism | `notebooks/05-…/02_inheritance_and_polymorphism.ipynb` | W7 D34 (optional) | Defer | Brief preview only |
| Encapsulation, `@property`, private attrs | `notebooks/05-…/01_encapsulation.ipynb` | – | Exclude | Too much for an 8-week beginner track |
| Abstract classes (`abc`), duck typing | `notebooks/05-…/03_abstraction.ipynb`, `04_…` | – | Exclude | |
| `@classmethod`, `@staticmethod` | `notebooks/05-…/05_method_types.ipynb` | – | Exclude | |
| OOP homework / bank-account challenge | `notebooks/05-…/06_oop_homework.ipynb`, `07_oop_challenge.ipynb` | W7 D33–D35 | Reuse idea | Course uses an original inventory domain |
| Errors, `try/except/finally`, input-retry loop | `notebooks/06-errors-exception-handling/00_introduction.ipynb` | W5 D25 | Reuse idea | |
| `unittest` example | `notebooks/06-…/01-unittest/` | W6 D29 | Simplify | Taught with plain `assert` + pytest |
| `pylint` | `notebooks/06-…/index.py` | W6 D28 (aside) | Defer | |
| Milestone 2: card games (War, Blackjack) | `notebooks/07-milestone-II/*.ipynb` | W7 D35 | Reuse idea | Project 04 is an Inventory Manager; card game listed as an alternative |
| Decorators | `notebooks/08-decorators/` | – | Exclude | Advanced |
| Generators, `iter`/`next` | `notebooks/09-generators/` | – | Exclude | Advanced |
| `collections.Counter`, `defaultdict` | `notebooks/10-…/00_python_collections_module.ipynb` | W6 D26 (Counter only) | Simplify | `namedtuple` excluded |
| Files and folders (`open`, `os`, `shutil`) | `notebooks/10-…/01_opening_reading_files_folders.ipynb` | W5 D23–D24 | Reuse idea | `pathlib` replaces `os`/`shutil` |
| `datetime` | `notebooks/10-…/02_python_datetime_module.ipynb` | W6 D26 | Simplify | |
| `math`, `random` | `notebooks/10-…/03_math_random_modules.ipynb` | W3 D14, W6 D26 | Simplify | |
| Debugger (`pdb`) | `notebooks/10-…/04_python_debugger.ipynb` | W6 D28 | Simplify | VS Code debugger instead of `pdb` |
| Timing code (`time`, `timeit`) | `notebooks/10-…/05_timing_python_code.ipynb` | – | Exclude | |
| Images with Pillow | `notebooks/11-working-with-images/` | – | Exclude | |
| Email (`smtplib`, `imaplib`) | `notebooks/12-emails-with-python/` | – | Exclude | Also involves real credentials |
| Data-structures & algorithms patterns | `data-structures-algorithms/preparation-common-patterns/` | W3, W5 optional challenges | Defer | Only frequency counting and palindrome ideas |
| LeetCode solutions | `leetcode/` | – | Exclude | |
| CSV and JSON | *(none)* | W8 D36 | New | |
| NumPy, pandas, matplotlib | *(none)* | W9 D43–D45 | New | |
| scikit-learn, ML workflow | *(none)* | W10 D46–D50 | New | |
| LLMs, prompting, API calls, mocks | *(none)* | W11 D51–D55 | New | |
| Final AI capstone | *(none)* | W12 D56–D60 | New | |

## 3. Prerequisite chain observed in the reference

data types → statements (`if`, `for`, `while`) → functions → **milestone project** → OOP → errors/modules →
**milestone project** → advanced topics.

The course keeps this spine, adds a milestone project after loops (Week 3) and after modules (Week 6), moves
errors and files earlier (Week 5) because every later project needs them, and replaces advanced topics with
CSV/JSON plus the AI phase.
