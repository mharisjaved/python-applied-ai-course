# pandas DataFrames and Cleaning

**What it is:** pandas loads tables (CSV files) into a `DataFrame`: rows and named columns, with tools to filter, summarise and clean them.
**Why it exists:** what took 20 lines with `csv.DictReader` and loops (Day 36) is one line in pandas, and every ML dataset starts as a table.

**Taught on:** [Day 44](../../weeks/week-09/day-44-pandas/lesson.md) (DataFrames) ·
[Day 45](../../weeks/week-09/day-45-cleaning-visualization/lesson.md) (cleaning) · used through
[Day 46](../../weeks/week-10/day-46-ml-workflow/lesson.md)–[Day 50](../../weeks/week-10/day-50-project-ml-predictor/lesson.md)

## Syntax at a glance

| You want to… | Write |
|--------------|-------|
| Import / load | `import pandas as pd` · `df = pd.read_csv(DATA_DIR / "students.csv")` |
| First look | `df.head()`, `df.shape`, `df.info()` (types, missing), `df.describe()` (statistics) |
| One column (a `Series`) | `df["final_score"]` |
| Several columns | `df[["name", "final_score"]]` (double brackets) |
| Filter rows | `df[df["final_score"] >= 70]` |
| Two conditions | `df[(df["program"] == "arts") & (df["study_hours"] > 5)]` (`&` and, `\|` or) |
| Sort | `df.sort_values("final_score", ascending=False)` |
| New column | `df["passed"] = df["final_score"] >= 50` |
| Count each category | `df["program"].value_counts()` |
| Statistic per group | `df.groupby("program")["final_score"].mean()` |
| Missing values | `df.isna().sum()`, `df.dropna()`, `df["col"].fillna(df["col"].median())` |
| Duplicates | `df.drop_duplicates()` |
| Fix messy text | `df["program"].str.strip().str.lower()` |

Most methods return a **new** DataFrame: write `df = df.dropna()` to keep the result.

## Examples

### 1. Build a small DataFrame and look at it

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Bilal", "Sara", "Omar", "Mei"],
    "program": ["science", "arts", "science", "commerce", "arts"],
    "study_hours": [12.0, 4.5, 9.0, 6.5, 11.0],
    "final_score": [81, 52, 74, 60, 88],
})
print(df.shape)                   # (5, 4)
print(df["final_score"].mean())   # 71.0
print(df.head(2))
#     name  program  study_hours  final_score
# 0   Asha  science         12.0           81
# 1  Bilal     arts          4.5           52
```

### 2. Filter and sort

```python
# (continues from example 1)
high = df[df["final_score"] >= 70]
print(high["name"].tolist())                     # ['Asha', 'Sara', 'Mei']
busy_arts = df[(df["program"] == "arts") & (df["study_hours"] > 5)]
print(busy_arts["name"].tolist())                # ['Mei']
top = df.sort_values("final_score", ascending=False).head(3)
print(top[["name", "final_score"]])
#    name  final_score
# 4   Mei           88
# 0  Asha           81
# 2  Sara           74
```

### 3. New columns, `value_counts`, `groupby`

```python
# (continues from example 2)
df["passed"] = df["final_score"] >= 60
df["points_per_hour"] = (df["final_score"] / df["study_hours"]).round(1)
print(df[["name", "passed", "points_per_hour"]].head(2))
#     name  passed  points_per_hour
# 0   Asha    True              6.8
# 1  Bilal   False             11.6
print(df["program"].value_counts())
# program
# science     2
# arts        2
# commerce    1
# Name: count, dtype: int64
print(df.groupby("program")["final_score"].mean())
# program
# arts        70.0
# commerce    60.0
# science     77.5
# Name: final_score, dtype: float64
```

### 4. Cleaning a messy table (the Day 45 recipe in miniature)

```python
import pandas as pd

raw = pd.DataFrame({
    "program": ["Science", " arts", "ARTS", "science", "Science"],
    "study_hours": [10.0, None, 6.0, -2.0, 10.0],
})
print(raw.isna().sum()["study_hours"])          # 1
df = raw.drop_duplicates()                      # row 4 repeats row 0
df["program"] = df["program"].str.strip().str.lower()
df = df[~(df["study_hours"] < 0)]               # drop negatives; "~" means "not" for a mask
df["study_hours"] = df["study_hours"].fillna(df["study_hours"].median())
print(df)
#    program  study_hours
# 0  science         10.0
# 1     arts          8.0
# 2     arts          6.0
```

### 5. Loading a course dataset from a lesson notebook

```python
# (needs a file)
from pathlib import Path

import pandas as pd

DATA_DIR = Path("../../../datasets")
df = pd.read_csv(DATA_DIR / "students.csv")
print(df.shape)   # (298, 10)
df.info()         # column types and non-null counts
```

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| `df["name", "final_score"]` | `KeyError: ('name', 'final_score')` | Double brackets: `df[["name", "final_score"]]` |
| Column name typo | `KeyError: 'final_scor'` | Check `df.columns` |
| `and` / `or` in a filter | `ValueError: The truth value of a Series is ambiguous…` | `&` / `\|` with brackets around each condition |
| `df.dropna()` on its own line | nothing changes | `df = df.dropna()` |
| `df[df["study_hours"] >= 0]` to drop negatives | rows with missing hours disappear too (NaN comparisons are False) | `df[~(df["study_hours"] < 0)]`, or fill missing values first |
| Messy categories (`"Arts"`, `" arts"`) | `value_counts`/`groupby` show extra groups | `.str.strip().str.lower()` |
| Maths on a column that pandas read as text (a stray `"n/a"` in a number column) | `TypeError`, or numbers glued together | Check the column type in `df.info()`; clean the bad values first |
| Filling missing values with the mean of a column that has outliers | strange filled values | Use the median, as in the course recipe |

## See also

- [02 NumPy](02-numpy.md): masks work the same way
- [04 matplotlib](04-matplotlib.md): plotting DataFrame columns
- [14 CSV and JSON](../python/14-csv-and-json.md): what `read_csv` saves you from writing
- [01 AI vocabulary](01-ai-vocabulary.md): features, target, data quality words
