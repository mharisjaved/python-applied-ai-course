# CSV and JSON Files

**What it is:** CSV stores a table (rows and columns) as text; JSON stores nested data (dicts and lists) as text.
**Why it exists:** spreadsheets export CSV, web APIs and LLMs speak JSON, and both can be opened by other programs.

**Taught on:** [Day 36](../../weeks/week-08/day-36-csv-json/lesson.md) · used in the pipeline on
[Day 37](../../weeks/week-08/day-37-data-pipelines/lesson.md) · `json.loads` for LLM replies on
[Day 54](../../weeks/week-11/day-54-parsing-validation/lesson.md)

## Syntax at a glance

| You want to… | Write | You get |
|--------------|-------|---------|
| Read CSV rows as lists | `csv.reader(f)` | `['2026-10-01', 'food', '12.50']` per row (header included) |
| Read CSV rows as dicts | `csv.DictReader(f)` | `{'date': '2026-10-01', 'category': 'food', …}` per row |
| Write CSV from dicts | `w = csv.DictWriter(f, fieldnames=[…])` · `w.writeheader()` · `w.writerow(d)` / `w.writerows(rows)` | |
| Open a CSV file | `open(path, newline="", encoding="utf-8")` | `newline=""` avoids blank rows on Windows |
| Save Python data as JSON | `json.dump(data, f, indent=2)` | pretty, readable file |
| Load a JSON file | `data = json.load(f)` | dicts / lists |
| JSON **text** ↔ Python | `json.dumps(data)`, `json.loads(text)` | the `s` means "string" |

| JSON | Python |
|------|--------|
| `{"key": …}` object | `dict` |
| `[1, 2]` array | `list` |
| `"text"` (double quotes only) | `str` |
| `3`, `2.5` | `int`, `float` |
| `true` / `false` / `null` | `True` / `False` / `None` |

**Every CSV value is text.** Convert with `float(row["amount"])` before doing maths.

## Examples

Run example 1 first: it creates `expenses_oct.csv` for examples 2–3.

### 1. Write a CSV with `DictWriter`

```python
import csv

rows = [
    {"date": "2026-10-01", "category": "food", "amount": 12.5},
    {"date": "2026-10-01", "category": "transport", "amount": 3.2},
    {"date": "2026-10-02", "category": "food", "amount": 8.05},
]
with open("expenses_oct.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["date", "category", "amount"])
    writer.writeheader()
    writer.writerows(rows)
print("saved", len(rows), "rows")   # saved 3 rows
```

### 2. Read rows as lists with `csv.reader`

```python
import csv

with open("expenses_oct.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))
print(rows[0])        # ['date', 'category', 'amount']
print(rows[1])        # ['2026-10-01', 'food', '12.5']
print(len(rows[1:]))  # 3
```

### 3. Read rows as dicts and total by category

```python
import csv

totals = {}
with open("expenses_oct.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        amount = float(row["amount"])   # text -> number
        totals[row["category"]] = totals.get(row["category"], 0) + amount
print(totals)   # {'food': 20.55, 'transport': 3.2}
```

### 4. Save and load JSON (and `json.loads` for text)

```python
import json
from pathlib import Path

summary = {"month": "2026-10", "total": 23.75, "categories": ["food", "transport"], "closed": False}
with open("summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)
print(Path("summary.json").read_text(encoding="utf-8"))
# {
#   "month": "2026-10",
#   "total": 23.75,
#   "categories": [
#     "food",
#     "transport"
#   ],
#   "closed": false
# }

with open("summary.json", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded["categories"][0], loaded["closed"])   # food False
print(json.loads('{"late": null, "scores": [7, 9]}'))   # {'late': None, 'scores': [7, 9]}   (text → dict, Day 54)
```

### 5. Load → clean → analyse → report (Day 37 pipeline shape)

In a real program `load()` would read a CSV file; here it returns two rows so the example runs anywhere.

```python
def load():
    return [{"name": " asha ", "mark": "81"}, {"name": "KEN", "mark": "67"}]


def clean(rows):
    return [{"name": r["name"].strip().title(), "mark": int(r["mark"])} for r in rows]


def analyse(rows):
    marks = [r["mark"] for r in rows]
    return {"count": len(marks), "average": sum(marks) / len(marks)}


def main():
    rows = clean(load())
    print(rows[0])           # {'name': 'Asha', 'mark': 81}
    print(analyse(rows))     # {'count': 2, 'average': 74.0}


if __name__ == "__main__":
    main()
```

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| Maths on CSV values: `row["amount"] + 1` | `TypeError: can only concatenate str (not "int") to str` | `float(row["amount"]) + 1` |
| Sorting/comparing CSV numbers as text | `"100" < "20"` is `True` | Convert to numbers first |
| No `newline=""` when writing CSV | empty line between rows (Windows) | `open(…, "w", newline="", encoding="utf-8")` |
| A dict key missing from `fieldnames` | `ValueError: dict contains fields not in fieldnames: 'note'` | Add it to `fieldnames` |
| Arguments swapped: `json.dump(f, data)` | `TypeError: Object of type TextIOWrapper is not JSON serializable` | `json.dump(data, f)`: data first |
| Saving a set to JSON | `TypeError: Object of type set is not JSON serializable` | `sorted(my_set)` (a list) first |
| Single quotes in a JSON file | `JSONDecodeError: Expecting property name enclosed in double quotes` | JSON uses double quotes only |
| `json.load(text)` on a string | `AttributeError: 'str' object has no attribute 'read'` | `json.loads(text)` for strings, `json.load(f)` for files |

## See also

- [05 Dicts and sets](05-dicts-and-sets.md) · [10 Files and paths](10-files-and-paths.md)
- [03 pandas](../ai/03-pandas.md): `pd.read_csv` does all of this for tables in one line
- [06 LLM apps](../ai/06-llm-apps.md): validating JSON that a model returns
