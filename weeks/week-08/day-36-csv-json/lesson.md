# Day 36: CSV and JSON

**Week 8 · Session 36 of 60 · Planned 75 min** · Previous: [Day 35](../../week-07/day-35-project-inventory/lesson.md) · Next: [Day 37](../day-37-data-pipelines/lesson.md)

## Objectives

By the end of this lesson students can:

1. Explain why `line.split(",")` breaks on real CSV files, and read a CSV with `csv.reader` and `csv.DictReader`.
2. Load a CSV into a list of dicts, convert its text values to numbers and summarise them.
3. Write a table with `csv.writer` / `csv.DictWriter`, always opening the file with `newline=""` and `encoding="utf-8"`.
4. Save and load Python data with `json.dump` / `json.load` (`indent=2`), use `json.dumps` / `json.loads` with
   strings, and predict what changes in a round trip (`True` → `true`, `None` → `null`, tuples → lists, keys → strings).
5. Choose CSV or JSON for a given kind of data and justify the choice in one sentence.

**Prior knowledge:** list of dicts and `.get()` (Day 08), counting with a dict (Day 12), functions (Days 16–19),
`max(key=)` (Day 21), `open`/`with` and reading lines (Day 23), `Path`, writing files, `.mkdir()` (Day 24),
`try/except` (Day 25). **New today:** the `csv` and `json` modules and the `json.JSONDecodeError` exception.

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only) ·
`data/purchases.csv` (provided, 5 rows with commas inside quoted fields) · `../../../datasets/expenses.csv`
(course dataset, 148 rows). The notebooks write everything into an `output/` folder they create themselves;
it is safe to delete.

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: reading files and lists of dicts | core |
| 0:05–0:12 | Why the `csv` module: the quoted-comma trap | core |
| 0:12–0:22 | Reading: `csv.reader`, `csv.DictReader` | core |
| 0:22–0:29 | Writing: `csv.writer`, `csv.DictWriter` | core |
| 0:29–0:39 | JSON: `dump`/`load`, `dumps`/`loads`, CSV or JSON? | core |
| 0:39–0:45 | Common mistakes + safe loading | core |
| 0:45–0:50 | Real-world: expenses CSV → JSON summary | core |
| 0:50–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (nested monthly JSON) and the "why not CSV?" discussion | optional (90-min session) |
| +5 min | Students open `output/expenses_summary.json` and a CSV in VS Code / a spreadsheet and compare | optional (90-min session) |

**For 60 min:** skip demo section 8 (Exercise 5 covers the same skill) and do only the first prediction in demo
section 5. Practice: Exercises 1–4.

## 1. Warm-up (5 min)

Retrieval questions (cold-call, answers on the board):
- "Write the three lines that read a file line by line." (*`with open(path, encoding="utf-8") as f:` /
  `for line in f:` / `print(line.strip())`, Day 23.*)
- "The line is `Asha,82,present`. How do you get `82` as a number?" (*`int(line.split(",")[1])`.*)
- "Now the name is written `Khan, Asha`. What happens?" Leave it open. It is today's first demo.

## 2. Why the `csv` module? (7 min)

**Intuition:** a CSV file is a spreadsheet saved as plain text: one line per row, commas between columns. But
data often *contains* commas: addresses, descriptions, "Chen, Mei". The CSV format solves this by putting such
fields in double quotes. A plain `split(",")` knows nothing about quotes.

Live code (demo section 1): print the raw file, then split every line.

```
3 ['date', 'description', 'amount']
4 ['2026-11-02', '"notebooks', ' pens and folders"', '12.40']
3 ['2026-11-03', 'bus pass', '25.00']
```

**Prediction question** before running: "How many pieces will each line split into?" Then run the total
calculation, which fails with `ValueError: could not convert string to float: ' pens and folders"'`.

Key point: **never split CSV lines by hand.** The `csv` module knows the rules (quotes, commas inside quotes, even
quotes inside quotes and line breaks inside a field).

## 3. Reading CSV files (10 min)

Live code (demo section 2):

```python
import csv

with open(purchases_path, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)        # ['2026-11-02', 'notebooks, pens and folders', '12.40'] ...
```

Teaching points:
- Each row is a **list of strings**. The quotes are gone and the comma stays in the description.
- **`newline=""`**: the `csv` module wants to handle line endings itself. Without it, CSV files *written* on Windows
  get a blank line between rows. Rule for students: *every* `open` used with `csv` gets `newline=""`.
- **Prediction question** (`print(row[2], type(row[2]))`): `18.30 <class 'str'>`. CSV only stores text, so
  converting with `float()` / `int()` is our job.

Then `csv.DictReader` (demo section 3). Ask "what is column 2?" to show why indexes are fragile. `DictReader`
uses the header line as keys:

```python
with open(purchases_path, newline="", encoding="utf-8") as f:
    purchases = list(csv.DictReader(f))     # list of dicts, read while the file is open
print(purchases[0])
# {'date': '2026-11-02', 'description': 'notebooks, pens and folders', 'amount': '12.40'}
```

**Prediction question:** "The file has 6 lines. How many rows does `DictReader` give?" (*5. The header becomes
the keys.*)

`list(...)` inside the `with` block is the pattern to remember: read everything while the file is open, then work
with an ordinary list of dicts (exactly the structure from Day 08).

## 4. Writing CSV files (7 min)

Live code (demo section 4): `csv.writer` with `writerows` for a list of lists that includes `"Chen, Mei"`.
**Prediction question:** "What will that line look like inside the file?" (*`"Chen, Mei",20,0`: the writer
adds the quotes for us.*)

Then `csv.DictWriter`, the usual choice when data is already a list of dicts:

```python
with open(results_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score", "passed"])
    writer.writeheader()          # without this line the file has no header!
    writer.writerows(results)
```

**Prediction question:** read Omar's row back: what is `type(row["score"])` and is `row["passed"] == False`?
(*`str`, and `False`: the text `"False"` is not the bool `False`.*) Message: **CSV forgets types.** This is the
cue for JSON.

## 5. JSON (10 min)

**Intuition:** JSON is a text format that looks almost exactly like Python dicts and lists, keeps numbers as
numbers, has `true`/`false`/`null`, and can **nest** (lists inside dicts inside lists). Nearly every web service
answers in JSON, including the AI models students will call in Week 11.

Live code (demo section 5):

```python
text = json.dumps(profile, indent=2)    # dict -> str
with open(profile_path, "w", encoding="utf-8") as f:
    json.dump(profile, f, indent=2)     # dict -> file (data first, file second)
with open(profile_path, encoding="utf-8") as f:
    loaded_profile = json.load(f)       # file -> dict
print(loaded_profile == profile)        # True
```

Put this table on the board. The memory trick is "**the `s` means string**":

| | with a file | with a string |
|-|-------------|---------------|
| Python → JSON | `json.dump(data, f)` | `json.dumps(data)` |
| JSON → Python | `json.load(f)` | `json.loads(text)` |

Prediction questions:
- "How are `True` and `None` written in JSON?" (*`true`, `null`.*)
- `json.loads(json.dumps({1: (90, 85)}))` → `{'1': [90, 85]}`. JSON keys are always strings and there are no
  tuples. Advice: use string keys and lists in anything you plan to save.

**CSV or JSON?** (demo section 6) Discuss with the table in the demo. Short version: *one flat table, or people open
it in a spreadsheet → CSV; nested data, settings or saved app state → JSON.* Ask: "A recipe with a list of
ingredients?" (JSON) "A log of daily temperatures?" (CSV)

## 6. Common mistakes (6 min)

Run the tagged cells in demo section 7 and read the last line of each error together.

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `total += row["amount"]` without converting | `TypeError: unsupported operand type(s) for +=: 'int' and 'str'` | CSV values are always text. Convert with `float()` |
| `row["Amount"]` | `KeyError: 'Amount'` | Keys are the header text, exactly, including case |
| Looping over the reader *after* the `with` block | `ValueError: I/O operation on closed file` | Read rows into a list inside the `with` block |
| `json.dump(f, data)` | `TypeError: Object of type TextIOWrapper is not JSON serializable` | Data first, file second |
| Saving a set | `TypeError: Object of type set is not JSON serializable` | Convert with `sorted(...)` or `list(...)` first |
| `json.loads("{'name': 'Ken'}")` | `json.JSONDecodeError: Expecting property name enclosed in double quotes` | JSON requires double quotes |
| Forgetting `writeheader()` | none; the first data row becomes the header when read back | Always check a written file by reading it back |

Finish with the safe loader `load_json(path, default)` from demo section 7: `FileNotFoundError` → default;
`json.JSONDecodeError` → warning + default. Students will reuse this pattern in the capstone (the requirement "never
crashes on a missing file").

## 7. Real-world example (5 min)

Demo section 8: `expenses.csv` → `output/expenses_summary.json` with total, count and average per category.
Point out that the code is already split into `load_expenses(path)` and `summarise_by_category(expenses)`:
tomorrow's lesson is entirely about that structure.

**Prediction question:** "Which category has the highest total?" Most students say food. It is **rent**
(1950.00 vs 1748.95): three big payments beat 67 small ones.

## 8. Practice (20 min)

Students open `practice.ipynb` and run the setup cell first.

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the output | types after CSV/JSON round trips | recall |
| 2 Read the purchases file | `DictReader`, converting, max | application |
| 3 Fix the broken code | `split` trap, `writeheader`, `dump` order, JSON quotes | modification |
| 4 Write a reading list | `DictWriter` + reading back | application |
| 5 Spending by payment method → JSON | full CSV → JSON task with functions | problem solving |
| 6 Monthly report as nested JSON (challenge) | nested dicts, choosing a format | challenge |

While circulating, look for:
- `open(...)` for `csv` without `newline=""` (no visible bug on Linux/macOS, so they think it does not matter);
- comparing amounts as strings in Exercise 2 (`"6.75" > "25.00"` is `True`);
- `json.dump(summary)` without the file argument, or `json.dumps(summary, f)`;
- in Exercise 5, rounding inside the loop instead of once at the end.

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

## 9. Recap and exit ticket (5 min)

Ask students to supply the three sentences:
1. Read CSV with the `csv` module (`DictReader` → list of dicts), never with `split(",")`; every value is text.
2. Write CSV with `DictWriter` + `writeheader()`; always `newline=""` and `encoding="utf-8"`.
3. JSON keeps types and nesting: `json.dump(data, f, indent=2)` to save, `json.load(f)` to load.

**Exit ticket:** what does this print?

```python
import json
data = {"name": "Omar", "scores": (70, 82), "active": True}
text = json.dumps(data)
back = json.loads(text)
print(text)
print(back["scores"], back == data)
```

Answer: `{"name": "Omar", "scores": [70, 82], "active": true}` then `[70, 82] False` (the tuple came back as a
list, so the dicts are no longer equal).

## Homework (20 min)

1. Finish Exercise 5 (and 6 if you like).
2. Look at your Project 03 Expense Tracker's storage file. In 2–3 sentences: would CSV or JSON have been a better
   format than your text format, and why?
3. Read the six options in the [Python Capstone brief](../../../projects/05-python-capstone/README.md) and pick
   your favourite two. We plan the capstone on Day 38.

## Next class

Day 37 builds a **data pipeline**: load → clean → analyse → report, each step a small function with a clear input
and output, plus a `main()` that connects them. Today's `load_expenses` and `summarise_by_category` are already
two stages of such a pipeline. Tomorrow the input file is messy (blank scores, wrong capitalisation, impossible
values), and cleaning becomes its own stage.

## Instructor notes

- **Out of scope today:** CSV dialects and `quoting` options, `json` custom encoders (`default=`), `sort_keys`,
  pandas. If asked about pandas: "Yes, `pd.read_csv` exists and we use it on Day 44. Today we learn what it does
  for us."
- **Excel exports.** Some locales save "CSV" with semicolons; `csv.reader(f, delimiter=";")` handles it. Excel
  can also add an invisible marker at the start, so the first key shows up as `'﻿date'`. Fix: open with
  `encoding="utf-8-sig"`. Mention only if a student hits it with their own file.
- **`list(csv.DictReader(f))`** is enough for files of this size. Do not explain iterators or why a reader can only
  be looped over once. If a student loops twice and gets nothing the second time, say "a reader is used up after
  one pass; load it into a list".
- **`json` vs `.txt`:** some students will ask why not just `str(my_dict)` into a text file. Show that reading it
  back gives a string, not a dict, and `json.loads` cannot parse Python's single quotes.
- **Fast students:** Exercise 6, then convert their Project 03 storage to CSV with `DictWriter`/`DictReader`.
- **Slow students:** write the 4-line `DictReader` pattern on the board and keep it there. Make sure they finish
  Exercises 2 and 4; the capstone needs exactly these skills.
