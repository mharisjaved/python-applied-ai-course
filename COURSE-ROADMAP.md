# Course Roadmap: Python + Applied AI (12 weeks, 60 sessions)

This is the **single source of truth** for what is taught on which day. Week READMEs, lessons and
`PROGRESS.md` refer back here. If you change the order, change it here first.

## Schedule settings (edit these to fit your timetable)

| Setting | Value | Notes |
|---------|-------|-------|
| Start date | Monday 2026-10-12 (Day 01) | |
| Sessions per week | 5 (Mon–Fri) | Content is numbered by **Day**, not date. Fewer sessions per week simply stretches the calendar |
| Session length | 75 min (planned) | Every `lesson.md` has a timing table with **core** segments and **optional** ones. For 60 min skip the optional rows, for 90 min use them all |
| Total | 60 sessions: 40 Python (Weeks 1–8) + 20 AI (Weeks 9–12) | |
| Homework load | 20–40 min per session, more on project weeks | |

Planned week start dates (5 sessions/week): W1 Oct 12 · W2 Oct 19 · W3 Oct 26 · W4 Nov 2 · W5 Nov 9 · W6 Nov 16 ·
W7 Nov 23 · W8 Nov 30 · W9 Dec 7 · W10 Dec 14 · W11 Dec 21 · W12 Dec 28.
⚠️ Dec 25 (Day 55) and Jan 1 (Day 60) are likely holidays, so expect the last week to shift into January. Record
actual dates in `PROGRESS.md`.

## How the course is built

- **Phase 1, Python Foundations (Weeks 1–8):** syntax → data structures → decisions → loops → functions →
  files & errors → modules & testing → basic OOP → CSV/JSON → Python capstone.
- **Phase 2, Applied AI (Weeks 9–12):** what AI is → data with NumPy/pandas → scikit-learn ML →
  LLM applications (offline mock first, real API optional) → AI capstone.
- **Every week ends with something students build or are assessed on.** Weekly checkpoints live in
  `assessments/weekly/`. Milestone projects live in `projects/`.

### Milestone projects (each student builds these independently → their portfolio)

| # | Project | Day(s) | Proves they can… | Folder |
|---|---------|--------|------------------|--------|
| 01 | Quiz Game | D15 | combine input, conditionals, loops, lists and dicts into a working program | [projects/01-quiz-game](projects/01-quiz-game/) |
| 02 | Hangman | D20 | decompose a program into small functions | [projects/02-hangman](projects/02-hangman/) |
| 03 | Expense Tracker | D30 | build a multi-file program with files, error handling and tests | [projects/03-expense-tracker](projects/03-expense-tracker/) |
| 04 | Inventory Manager | D35 | model a problem with classes and composition | [projects/04-inventory-manager](projects/04-inventory-manager/) |
| 05 | **Python Capstone** (own choice) | D38–D40 | plan and ship a complete Python application | [projects/05-python-capstone](projects/05-python-capstone/) |
| 06 | Data Analysis Report | D45 (+homework) | clean, analyse and visualise a dataset with pandas | [projects/06-data-analysis-report](projects/06-data-analysis-report/) |
| 07 | ML Predictor | D50 | train, evaluate and use a scikit-learn model end to end | [projects/07-ml-predictor](projects/07-ml-predictor/) |
| 08 | AI Text Assistant | D55 | build an LLM-powered tool with validation and an offline mock | [projects/08-ai-text-assistant](projects/08-ai-text-assistant/) |
| 09 | **AI Capstone** (own choice) | D56–D60 | scope, build, test and present an AI application | [projects/09-ai-capstone](projects/09-ai-capstone/) |

## Daily outline

Column guide: **New concepts** = what is introduced that day (nothing else may be assumed) ·
**Students can…** = observable outcomes · **Builds on** = prerequisite days · **Output** = what students produce.
Every day folder contains `lesson.md` (instructor notes), `demo.ipynb` (live teaching), `practice.ipynb`
(student exercises) and `solutions.ipynb` (instructor answers).

### Week 1: Getting Started with Python · [weeks/week-01](weeks/week-01/)

| Day | Topic · New concepts | Students can… | Builds on | Output |
|-----|----------------------|---------------|-----------|--------|
| [01](weeks/week-01/day-01-environment/) ✅ | **Environment & Hello World.** Python interpreter, VS Code, uv, `.py` file, `print()`, running `uv run hello.py` | run a Python file from VS Code and the terminal; explain what the interpreter does | none | `hello.py` |
| [02](weeks/week-01/day-02-variables/) | **Variables & basic data types.** Jupyter notebooks in VS Code (cells, kernel, Shift+Enter), comments, assignment, naming rules, `int` `float` `str` `bool`, `type()`, reassignment, `print` with several values, `NameError` | create variables of four types and confirm them with `type()`; predict a variable's value after reassignment; fix a `NameError` | 01 | "profile card" printed from variables |
| [03](weeks/week-01/day-03-numbers-input/) | **Numbers, operators & input.** `+ - * / // % **`, precedence, `+=`, `input()`, `int()` `float()` `str()` conversion, `round()`, `TypeError`/`ValueError` from bad conversion | predict `/` vs `//` vs `%`; read a number from the user and calculate with it; explain why `input()` returns text | 02 | bill-splitter calculator |
| [04](weeks/week-01/day-04-strings/) | **Strings & string operations.** quotes, `\n` `\t`, `+` and `*` on strings, `len()`, `.upper() .lower() .title() .strip() .replace() .count() .find() .startswith() .endswith()`, immutability, basic f-strings | clean and transform text with string methods; build messages with f-strings; explain why `s.upper()` does not change `s` | 03 | username generator |
| [05](weeks/week-01/day-05-slicing-formatting/) | **Indexing, slicing & formatting + weekly practice.** positive/negative index, `[start:stop:step]`, `[::-1]`, `IndexError`, f-string formats `:.2f` `:>8` `:,` | extract parts of text by index/slice; format money and tables neatly; pass Checkpoint 1 | 02–04 | formatted receipt · Checkpoint 1 |

### Week 2: Data Structures & Decisions · [weeks/week-02](weeks/week-02/)

| Day | Topic · New concepts | Students can… | Builds on | Output |
|-----|----------------------|---------------|-----------|--------|
| [06](weeks/week-02/day-06-lists/) | **Lists & indexing.** list literals, index/slice on lists, `len` `sum` `min` `max`, changing an item, `in`, lists of strings/numbers, nested list preview | store related values in a list, read and change items by index, compute simple statistics | 05 | class-marks list |
| [07](weeks/week-02/day-07-list-methods-tuples/) | **List methods, tuples & mutability.** `.append .insert .remove .pop .sort .reverse .index .count`, `sorted()`, `.split()` → list, `" ".join()`, tuples, unpacking, aliasing vs `.copy()` | choose the right list method; explain mutable vs immutable; unpack a tuple into variables | 06 | shopping-list operations |
| [08](weeks/week-02/day-08-dicts-sets/) | **Dictionaries & sets.** key→value, lookup, `KeyError`, `.get()`, add/update/`del`, `.keys() .values() .items()`, list of dicts, sets, `.add`, union/intersection/difference, de-duplicating with `set()` | model a record with a dict; look values up safely; remove duplicates with a set | 06–07 | contact book / student record |
| [09](weeks/week-02/day-09-conditionals/) | **Booleans, comparisons & conditionals.** `== != < > <= >=`, `and or not`, `if/elif/else`, indentation blocks, nested `if`, truthiness of empty values | write a multi-branch decision; combine conditions correctly; trace which branch runs | 02–08 | grade calculator |
| [10](weeks/week-02/day-10-decisions-practice/) | **Decision problems + weekly review.** No new syntax: combining input, dicts and conditionals; testing every branch | solve a small decision problem from a written spec and test all branches; pass Checkpoint 2 | 06–09 | ticket-price calculator · Checkpoint 2 |

### Week 3: Control Flow · [weeks/week-03](weeks/week-03/)

| Day | Topic · New concepts | Students can… | Builds on | Output |
|-----|----------------------|---------------|-----------|--------|
| [11](weeks/week-03/day-11-for-loops/) | **`for` loops & `range`.** loop variable, body indentation, `range(stop)` `range(start, stop, step)`, accumulator pattern (total/count) | repeat an action a set number of times; total and count values with a loop | 06–09 | multiplication table, marks total |
| [12](weeks/week-03/day-12-iterating-collections/) | **Iterating strings, lists & dicts.** looping over characters/items/`.items()`, `enumerate()`, building a new list with `.append` in a loop, counting with a dict, finding a max manually | transform and summarise a collection with a loop; count occurrences with a dict | 11 | letter/word counter, attendance report |
| [13](weeks/week-03/day-13-while-loops/) | **`while` loops.** condition-controlled repetition, counters, sentinel values, infinite loops (and how to stop the kernel), validation loop with `.isdigit()` | choose `while` vs `for`; write a loop that keeps asking until input is valid | 11–12 | PIN retry / input validator |
| [14](weeks/week-03/day-14-break-continue-nested/) | **`break`, `continue`, nested loops & `random`.** `while True` + `break`, `continue`, nested loops, `import random`, `randint` `choice` `shuffle` | exit or skip loop iterations deliberately; build a guessing game with a random secret | 11–13 | number-guessing game |
| [15](weeks/week-03/day-15-project-quiz-game/) | **🏗 Project 01: Quiz Game.** project workflow: read brief → plan → build smallest version → test → extend | build a complete quiz program independently from a brief | 02–14 | Quiz Game · Checkpoint 3 |

### Week 4: Functions · [weeks/week-04](weeks/week-04/)

| Day | Topic · New concepts | Students can… | Builds on | Output |
|-----|----------------------|---------------|-----------|--------|
| [16](weeks/week-04/day-16-functions-intro/) | **Why functions; define & call.** duplication problem, `def`, calling, body, docstring, calling many times | turn repeated code into a function and call it | 11–15 | banner/menu printer |
| [17](weeks/week-04/day-17-parameters-return/) | **Parameters, arguments & return values.** parameters vs arguments, positional & keyword arguments, `return`, return vs print, `None`, returning a tuple | write a function that takes inputs and returns a result; explain print vs return | 16 | grade & discount functions |
| [18](weeks/week-04/day-18-scope-defaults/) | **Scope, defaults & composition.** local vs global, default parameter values, functions calling functions, why to avoid `global` (`*args` named only) | predict which variable a function sees; build a result from small functions | 17 | price calculator built from small functions |
| [19](weeks/week-04/day-19-decomposition/) | **Problem decomposition.** top-down design, pseudocode, one-job functions, checking functions with `print(f(x) == expected)`, `.isalpha()` for validating letters | break a problem into functions before coding; plan Hangman | 16–18 | text-statistics tool · Hangman plan |
| [20](weeks/week-04/day-20-project-hangman/) | **🏗 Project 02: Hangman.** building a program function by function | build Hangman from a function plan | 11–19 | Hangman · Checkpoint 4 |

### Week 5: Practical Python Skills · [weeks/week-05](weeks/week-05/)

| Day | Topic · New concepts | Students can… | Builds on | Output |
|-----|----------------------|---------------|-----------|--------|
| [21](weeks/week-05/day-21-built-in-functions/) | **Built-in functions & useful methods.** `sorted(key=, reverse=)`, `abs` `round` `zip` `any` `all`, `.isdigit`/`.isalpha` recap, `.split/.join` recap, `help()` | replace hand-written loops with the right built-in; sort by a key | 12, 17 | leaderboard report |
| [22](weeks/week-05/day-22-comprehensions/) | **Comprehensions.** list comprehension, with `if`, dict comprehension, when a loop is clearer | rewrite a build-a-list loop as a comprehension and judge readability | 12, 21 | data clean-up one-liners |
| [23](weeks/week-05/day-23-reading-files/) | **Reading text files.** `open()`, `with`, `.read()`, looping over lines, `.strip()`, `encoding="utf-8"`, relative paths, `FileNotFoundError` | read a text file and compute statistics from its lines | 12, 21 | word counter for a text file |
| [24](weeks/week-05/day-24-writing-files-pathlib/) | **Writing files & `pathlib`.** modes `"w"` `"a"`, `.write()`, `Path`, `/` for paths, `.exists()` `.mkdir()` `.read_text()` `.write_text()` | save program results to a file and append new entries | 23 | notes/journal saver |
| [25](weeks/week-05/day-25-exceptions/) | **Exceptions & defensive input.** `try/except`, specific exceptions, `else` `finally`, retry loop, `raise ValueError` in your own function | prevent crashes from bad input and missing files; raise a clear error from a function | 13, 17, 23 | robust number input & safe file loader · Checkpoint 5 |

### Week 6: Working Like a Python Developer · [weeks/week-06](weeks/week-06/)

| Day | Topic · New concepts | Students can… | Builds on | Output |
|-----|----------------------|---------------|-----------|--------|
| [26](weeks/week-06/day-26-modules-imports/) | **Modules & imports.** `import`, `from … import`, `as`, stdlib tour (`math` `random` `datetime` `collections.Counter`), your own `.py` module, `if __name__ == "__main__":` | split code into a module and import it | 16–25 | `textutils.py` module |
| [27](weeks/week-06/day-27-packages-uv/) | **Packages, uv & project environments.** virtual environments, `uv init` `uv add` `uv run`, `pyproject.toml`, `uv.lock`, packages (folders of modules) | create a uv project, add a dependency and run a script in it | 26 | own uv project |
| [28](weeks/week-06/day-28-debugging/) | **Debugging & tracebacks.** reading a traceback bottom-up, common error types, VS Code breakpoints/step/variables, print debugging | locate and fix bugs systematically instead of guessing | 25–27 | five bugs fixed |
| [29](weeks/week-06/day-29-testing/) | **Testing with assertions.** `assert`, normal/edge/error cases, `test_*.py`, `uv run pytest`, reading failures | write tests for their own functions and use failures to fix code | 17, 25–28 | tests for earlier functions |
| [30](weeks/week-06/day-30-project-expense-tracker/) | **🏗 Project 03: Expense Tracker.** multi-file layout (`storage.py`, `reports.py`, `main.py`, tests) | build and test a multi-file program that saves data | 21–29 | Expense Tracker · Checkpoint 6 |

### Week 7: Introductory OOP · [weeks/week-07](weeks/week-07/)

| Day | Topic · New concepts | Students can… | Builds on | Output |
|-----|----------------------|---------------|-----------|--------|
| [31](weeks/week-07/day-31-objects/) | **Objects, state & behaviour.** "everything is an object", methods as behaviour, `type()`, modelling with dict + functions and where it gets messy | identify state and behaviour in a real-world thing | 16–30 | dict-based account → pain points |
| [32](weeks/week-07/day-32-classes/) | **Classes, instances & constructors.** `class`, `__init__`, `self`, attributes, many instances | write a class and create several independent instances | 31 | `Student` class |
| [33](weeks/week-07/day-33-methods/) | **Attributes & methods.** methods that read/change state, returning from methods, validation with `raise`, `__str__` | add behaviour to a class that keeps its data valid | 32 | `BankAccount` / `Product` class |
| [34](weeks/week-07/day-34-composition/) | **Class design & composition.** objects containing lists of objects, nouns→classes / verbs→methods, has-a; inheritance preview (optional) | design two cooperating classes from a description | 33 | `Playlist` of `Song`s |
| [35](weeks/week-07/day-35-project-inventory/) | **🏗 Project 04: Inventory Manager.** OOP design applied end to end | build a class-based app from a brief | 31–34 | Inventory Manager · Checkpoint 7 |

### Week 8: Consolidation & Python Capstone · [weeks/week-08](weeks/week-08/)

| Day | Topic · New concepts | Students can… | Builds on | Output |
|-----|----------------------|---------------|-----------|--------|
| [36](weeks/week-08/day-36-csv-json/) | **CSV & JSON.** `csv.reader` `DictReader` `DictWriter` (`newline=""`), `json.load` `json.dump` (`indent`) | load and save structured data in both formats | 08, 23–25 | expenses CSV → JSON summary |
| [37](weeks/week-08/day-37-data-pipelines/) | **Combining functions, files & data.** load → clean → analyse → report pipeline, `main()` | structure a data-processing program as a pipeline of functions | 36 | grade-report generator |
| [38](weeks/week-08/day-38-capstone-planning/) | **🎓 Python Capstone: plan & structure.** requirements, user stories, MVP, module layout | write a project plan and skeleton | 01–37 | approved plan + skeleton |
| [39](weeks/week-08/day-39-capstone-build/) | **🎓 Capstone: build, debug & test.** incremental builds, review checklist | deliver a working MVP with tests | 38 | working MVP |
| [40](weeks/week-08/day-40-capstone-demo/) | **🎓 Capstone presentations & readiness assessment.** | demo and explain their code; pass the Python readiness assessment | 38–39 | Capstone demo · readiness assessment. ⚠️ Does not fit 75 min for most class sizes: see the lesson's Plan A/B, or add an extra presentation slot |

### Week 9: Introduction to AI & Data · [weeks/week-09](weeks/week-09/)

| Day | Topic · New concepts | Students can… | Builds on | Output |
|-----|----------------------|---------------|-----------|--------|
| [41](weeks/week-09/day-41-what-is-ai/) | **What AI, ML, DL & GenAI are.** rules vs learning from examples, training vs prediction, use cases, limitations, bias | classify a use case as rules/ML/GenAI and name a limitation | 01–40 | hand-coded rule vs threshold "learned" from data |
| [42](weeks/week-09/day-42-datasets/) | **Datasets, features, labels & quality.** rows/columns, features vs target, numeric vs categorical, missing/duplicate/out-of-range/inconsistent values | identify features and target; audit a raw dataset with plain Python | 36–37, 41 | data-quality audit |
| [43](weeks/week-09/day-43-numpy/) | **NumPy essentials.** arrays, `shape` `dtype`, vectorised maths, `mean` `std` `min` `max`, boolean masks, 2-D indexing basics | compute statistics on arrays without loops | 42 | vectorised grade statistics |
| [44](weeks/week-09/day-44-pandas/) | **pandas DataFrames.** `read_csv`, `head` `info` `describe`, column selection, filtering, `sort_values`, new columns, `value_counts`, `groupby` | answer questions about a dataset with pandas | 43 | expenses analysis |
| [45](weeks/week-09/day-45-cleaning-visualization/) | **Cleaning, EDA & visualisation.** `isna` `dropna` `fillna`, `drop_duplicates`, fixing categories, filtering bad values, matplotlib `hist` `bar` `scatter` with labels | clean a messy dataset and explain it with 3 charts | 44 | cleaned dataset · Project 06 launched |

### Week 10: Introductory Machine Learning · [weeks/week-10](weeks/week-10/)

| Day | Topic · New concepts | Students can… | Builds on | Output |
|-----|----------------------|---------------|-----------|--------|
| [46](weeks/week-10/day-46-ml-workflow/) | **ML workflow & train/test split.** supervised learning steps, `X`/`y`, `train_test_split`, `random_state`, baseline, `fit`/`predict` | split data correctly and beat (or fail to beat) a baseline | 42–45 | baseline + split · Checkpoint 9 (first 15 min) |
| [47](weeks/week-10/day-47-regression/) | **Regression.** `LinearRegression`, coefficients in plain words, MAE, predicted-vs-actual plot | train a regression model and explain its error in the target's units | 46 | final-score predictor |
| [48](weeks/week-10/day-48-classification/) | **Classification.** classes, `LogisticRegression`, `DecisionTreeClassifier`, accuracy, confusion matrix | train a classifier and read its confusion matrix | 46–47 | pass/fail predictor |
| [49](weeks/week-10/day-49-evaluation-overfitting/) | **Evaluation, overfitting & leakage.** train vs test score, tree depth experiment, precision/recall intuition, data leakage | detect overfitting and leakage in a given experiment | 46–48 | leakage hunt + depth experiment |
| [50](weeks/week-10/day-50-project-ml-predictor/) | **🏗 Project 07: ML Predictor.** end-to-end workflow on a chosen dataset | independently train, evaluate and use a model | 41–49 | ML Predictor · Checkpoint 10 |

### Week 11: Generative AI & Python Applications · [weeks/week-11](weeks/week-11/)

| Day | Topic · New concepts | Students can… | Builds on | Output |
|-----|----------------------|---------------|-----------|--------|
| [51](weeks/week-11/day-51-how-llms-work/) | **How LLM apps work.** next-token prediction, tokens, system/user messages, context window, temperature, app pipeline (input → prompt → model → parse → output), mock model | explain an LLM app pipeline and build a prompt template | 17, 33, 41 | prompt template + mock model |
| [52](weeks/week-11/day-52-prompt-design/) | **Prompt design & reliability.** clear instructions, context, examples (few-shot), output format, delimiters, hallucination, testing prompts on several inputs | improve a prompt and evaluate it on a test set | 51 | prompt comparison table |
| [53](weeks/week-11/day-53-llm-api/) | **Calling an LLM API.** API keys, environment variables, `.env` + `.gitignore`, SDK client, messages, cost & rate limits, mock fallback | call a real or mock LLM from a function without exposing a key | 25, 26, 52 | `ask_llm()` helper |
| [54](weeks/week-11/day-54-parsing-validation/) | **Parsing, validation & mocks.** JSON output, `json.loads`, validating fields, handling API/parse errors, retries, a `MockLLM` class, testing with mocks | turn free-form model output into validated data | 25, 29, 33, 36, 53 | robust review analyser |
| [55](weeks/week-11/day-55-project-ai-assistant/) | **🏗 Project 08: AI Text Assistant.** | build a small LLM-powered tool that works offline | 51–54 | AI Text Assistant · Checkpoint 11 |

### Week 12: Final AI Capstone · [weeks/week-12](weeks/week-12/)

| Day | Topic · New concepts | Students can… | Builds on | Output |
|-----|----------------------|---------------|-----------|--------|
| [56](weeks/week-12/day-56-capstone-scoping/) | **🎓 AI Capstone: select & scope.** options, success criteria, data & privacy check | write a scoped capstone plan with measurable success criteria | 41–55 | approved plan |
| [57](weeks/week-12/day-57-capstone-core/) | **🎓 Implement the core.** data loading, logic, model or text pipeline without the LLM | build the non-AI core and test it | 56 | working core |
| [58](weeks/week-12/day-58-capstone-ai-integration/) | **🎓 Integrate AI & test.** connect ML model or LLM (mock first), tests with mocks | integrate the AI part behind a function and test it offline | 57 | integrated app |
| [59](weeks/week-12/day-59-capstone-reliability/) | **🎓 Reliability & demo prep.** failure cases, hallucination/privacy/bias review, README, demo script | harden the app and prepare a 5-minute demo | 58 | README + demo script |
| [60](weeks/week-12/day-60-final-presentations/) | **🎓 Final presentations, assessment & feedback.** | present, explain decisions and limitations; complete the final assessment | 56–59 | AI Capstone · final assessment. ⚠️ Fits one session only with ≤ 6 students; otherwise split into 60a (presentations) and 60b (assessment), see lesson |

## Explicitly out of scope (beginner track)

Decorators, generators/iterators, metaclasses, `*args/**kwargs` in depth, lambda-heavy functional style,
properties/private attributes, abstract classes, inheritance hierarchies, concurrency/async, web scraping,
GUIs, web frameworks, images, email, databases, deep-learning training, GPUs and cloud deployment. Strong
students can take these as extensions after the capstones.
