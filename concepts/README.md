# Concept Cheatsheets

One page per concept: what it is and why it exists, a syntax table, short runnable examples with their output, the
common mistakes (with the exact error message) and links to related pages. Use them to revise before class or a
checkpoint, or keep one open while you code. The day links go to the lesson where the concept is taught.

**Reading the examples**
- `# 42` after a line shows what it prints. Comment lines under a loop show its output, in order.
- `# you type: Asha` shows what to type when `input()` asks.
- `# (continues from example 1)`: run the earlier example first (same notebook).
- `# (shows an error)`: the example fails on purpose, to show the error message.
- `# (needs a file)`: only works from a lesson folder, where the course `datasets/` folder is `../../../datasets`.

## Python (Weeks 1–8)

| Cheatsheet | Covers | Taught on |
|------------|--------|-----------|
| [01 Variables and types](python/01-variables-and-types.md) | variables, `int` `float` `str` `bool`, `type()`, naming rules, `NameError` | [Day 02](../weeks/week-01/day-02-variables/lesson.md) |
| [02 Numbers and input](python/02-numbers-and-input.md) | `+ - * / // % **`, precedence, `+=`, `input()`, `int()` `float()` `str()`, `round()` | [Day 03](../weeks/week-01/day-03-numbers-input/lesson.md) |
| [03 Strings](python/03-strings.md) | string methods, `len`, f-strings, indexing, slicing, `:.2f` `:>8` `:,` | [Day 04](../weeks/week-01/day-04-strings/lesson.md), [Day 05](../weeks/week-01/day-05-slicing-formatting/lesson.md) |
| [04 Lists and tuples](python/04-lists-and-tuples.md) | lists, `in`, `sum/min/max`, list methods, `sorted`, `split/join`, tuples, unpacking, `.copy()` | [Day 06](../weeks/week-02/day-06-lists/lesson.md), [Day 07](../weeks/week-02/day-07-list-methods-tuples/lesson.md) |
| [05 Dicts and sets](python/05-dicts-and-sets.md) | dicts, `.get`, `.items()`, list of dicts, counting, sets and set operations | [Day 08](../weeks/week-02/day-08-dicts-sets/lesson.md), [Day 12](../weeks/week-03/day-12-iterating-collections/lesson.md) |
| [06 Conditionals](python/06-conditionals.md) | comparisons, `and/or/not`, `if/elif/else`, nesting, truthiness | [Day 09](../weeks/week-02/day-09-conditionals/lesson.md), [Day 10](../weeks/week-02/day-10-decisions-practice/lesson.md) |
| [07 Loops](python/07-loops.md) | `for`, `range`, accumulators, `enumerate`, `while`, validation loops, `break/continue`, nested loops, `random` | [Day 11](../weeks/week-03/day-11-for-loops/lesson.md)–[Day 14](../weeks/week-03/day-14-break-continue-nested/lesson.md) |
| [08 Functions](python/08-functions.md) | `def`, docstrings, parameters, `return`, `None`, defaults, keyword args, scope, decomposition | [Day 16](../weeks/week-04/day-16-functions-intro/lesson.md)–[Day 19](../weeks/week-04/day-19-decomposition/lesson.md) |
| [09 Built-ins and comprehensions](python/09-built-ins-and-comprehensions.md) | `sorted(key=, reverse=)`, `zip`, `any/all`, `abs`, `.isdigit/.isalpha`, list and dict comprehensions | [Day 21](../weeks/week-05/day-21-built-in-functions/lesson.md), [Day 22](../weeks/week-05/day-22-comprehensions/lesson.md) |
| [10 Files and paths](python/10-files-and-paths.md) | `open`, `with`, reading lines, modes `"w"`/`"a"`, `pathlib.Path`, `FileNotFoundError` | [Day 23](../weeks/week-05/day-23-reading-files/lesson.md), [Day 24](../weeks/week-05/day-24-writing-files-pathlib/lesson.md) |
| [11 Exceptions](python/11-exceptions.md) | `try/except/else/finally`, specific exceptions, retry loops, `raise ValueError` | [Day 25](../weeks/week-05/day-25-exceptions/lesson.md) |
| [12 Modules, uv and testing](python/12-modules-uv-and-testing.md) | `import`, stdlib modules, own modules, `__name__`, uv commands, `assert`, pytest | [Day 26](../weeks/week-06/day-26-modules-imports/lesson.md), [Day 27](../weeks/week-06/day-27-packages-uv/lesson.md), [Day 29](../weeks/week-06/day-29-testing/lesson.md) |
| [13 Classes](python/13-classes.md) | `class`, `__init__`, `self`, attributes, methods, `__str__`, validation, composition | [Day 31](../weeks/week-07/day-31-objects/lesson.md)–[Day 34](../weeks/week-07/day-34-composition/lesson.md) |
| [14 CSV and JSON](python/14-csv-and-json.md) | `csv.reader`, `DictReader`, `DictWriter`, `json.load/dump/loads`, pipeline of functions | [Day 36](../weeks/week-08/day-36-csv-json/lesson.md), [Day 37](../weeks/week-08/day-37-data-pipelines/lesson.md) |
| [15 Reading tracebacks](python/15-reading-tracebacks.md) | reading a traceback bottom-up, error types and messages, print debugging, VS Code debugger | [Day 28](../weeks/week-06/day-28-debugging/lesson.md) |

## Applied AI (Weeks 9–12)

| Cheatsheet | Covers | Taught on |
|------------|--------|-----------|
| [01 AI vocabulary](ai/01-ai-vocabulary.md) | AI/ML/DL/GenAI, features, target, training, inference, baseline, overfitting, leakage, tokens, hallucination… | [Day 41](../weeks/week-09/day-41-what-is-ai/lesson.md), [Day 42](../weeks/week-09/day-42-datasets/lesson.md), [Day 46](../weeks/week-10/day-46-ml-workflow/lesson.md), [Day 49](../weeks/week-10/day-49-evaluation-overfitting/lesson.md), [Day 51](../weeks/week-11/day-51-how-llms-work/lesson.md) |
| [02 NumPy](ai/02-numpy.md) | arrays, `shape` `dtype`, vectorised maths, statistics, boolean masks, 2-D indexing | [Day 43](../weeks/week-09/day-43-numpy/lesson.md) |
| [03 pandas](ai/03-pandas.md) | `read_csv`, `head/info/describe`, selecting, filtering, sorting, `value_counts`, `groupby`, cleaning | [Day 44](../weeks/week-09/day-44-pandas/lesson.md), [Day 45](../weeks/week-09/day-45-cleaning-visualization/lesson.md) |
| [04 matplotlib](ai/04-matplotlib.md) | `hist`, `bar`, `scatter`, labels, predicted-vs-actual plot, choosing a chart | [Day 45](../weeks/week-09/day-45-cleaning-visualization/lesson.md), [Day 47](../weeks/week-10/day-47-regression/lesson.md) |
| [05 scikit-learn workflow](ai/05-scikit-learn-workflow.md) | `X`/`y`, `train_test_split`, baseline, `fit/predict`, regression, classification, metric cheat table, overfitting, leakage | [Day 46](../weeks/week-10/day-46-ml-workflow/lesson.md)–[Day 49](../weeks/week-10/day-49-evaluation-overfitting/lesson.md) |
| [06 LLM apps](ai/06-llm-apps.md) | LLM app pipeline, prompt checklist, `ask_llm()` helper, mock model, JSON validation, retries, `MockLLM`, safety and privacy | [Day 51](../weeks/week-11/day-51-how-llms-work/lesson.md)–[Day 54](../weeks/week-11/day-54-parsing-validation/lesson.md) |
