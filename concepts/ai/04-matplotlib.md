# matplotlib Charts

**What it is:** `matplotlib.pyplot` draws charts from lists, arrays or DataFrame columns.
**Why it exists:** a chart shows a distribution, a comparison or a relationship in seconds; a table of 300 numbers does not.

**Taught on:** [Day 45](../../weeks/week-09/day-45-cleaning-visualization/lesson.md) (`hist`, `bar`, `scatter`, labels) ·
predicted-vs-actual plot on [Day 47](../../weeks/week-10/day-47-regression/lesson.md)

## Which chart?

| Question you want to answer | Chart | Code |
|-----------------------------|-------|------|
| How are the values of **one** number column spread out? | histogram | `plt.hist(values, bins=10)` |
| How do **categories** compare (totals, counts, averages)? | bar chart | `plt.bar(labels, heights)` |
| Do **two** number columns move together? | scatter plot | `plt.scatter(x, y)` |
| How good are my regression predictions? | predicted vs actual (scatter + diagonal) | `plt.scatter(y_test, pred)` + `plt.plot([lo, hi], [lo, hi])` |

## Syntax at a glance

| You want to… | Write |
|--------------|-------|
| Import | `import matplotlib.pyplot as plt` |
| Title and axis labels | `plt.title("…")`, `plt.xlabel("…")`, `plt.ylabel("…")` |
| Show the chart | `plt.show()` (last line of the cell) |
| Bigger figure | `plt.figure(figsize=(8, 4))` (first line, before plotting) |
| Readable long labels | `plt.xticks(rotation=45)` |
| Bar outlines / transparency | `edgecolor="black"`, `alpha=0.6` |
| Save to a file (only when needed, e.g. a report) | `plt.savefig("chart.png", dpi=150)` **before** `plt.show()` |

**Every chart needs:** a title that says what it shows, axis labels **with units**, and one sentence in your
notebook saying what you learned from it.

## Examples

### 1. Histogram: distribution of one column

```python
import matplotlib.pyplot as plt

study_hours = [2, 4, 4, 5, 6, 6, 6, 7, 8, 9, 10, 12, 14]
plt.hist(study_hours, bins=5, edgecolor="black")
plt.title("Weekly study hours")
plt.xlabel("Hours per week")
plt.ylabel("Number of students")
plt.show()
```

### 2. Bar chart: compare categories

```python
import matplotlib.pyplot as plt

totals = {"food": 412.5, "transport": 96.0, "rent": 650.0, "health": 38.2}
plt.bar(totals.keys(), totals.values())
plt.title("Spending by category, September")
plt.xlabel("Category")
plt.ylabel("Amount spent")
plt.show()
```

### 3. Bar chart straight from pandas `groupby`

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "program": ["science", "arts", "science", "commerce", "arts"],
    "final_score": [81, 52, 74, 60, 88],
})
means = df.groupby("program")["final_score"].mean()
plt.bar(means.index, means.values)
plt.title("Average final score by program")
plt.ylabel("Final score (0-100)")
plt.show()
```

### 4. Scatter: relationship between two columns

```python
import matplotlib.pyplot as plt

hours = [2, 4, 5, 7, 8, 10, 12, 14]
scores = [41, 48, 55, 61, 60, 72, 80, 86]
plt.scatter(hours, scores, alpha=0.7)
plt.title("More study, higher scores")
plt.xlabel("Study hours per week")
plt.ylabel("Final score (0-100)")
plt.show()
```

### 5. Predicted vs actual (regression check, Day 47)

```python
import matplotlib.pyplot as plt

actual = [55, 62, 70, 81, 90]
predicted = [58, 60, 74, 78, 85]
plt.scatter(actual, predicted)
plt.plot([50, 95], [50, 95], linestyle="--", color="gray")   # perfect-prediction line
plt.title("Predicted vs actual final score")
plt.xlabel("Actual score")
plt.ylabel("Predicted score")
plt.show()
```

Points on the dashed line are perfect predictions; the further away, the bigger the error.

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| No `plt.show()` in a `.py` file | no window appears | End with `plt.show()` |
| `plt.savefig()` after `plt.show()` | saved image is blank | Save first, then show |
| x and y lists of different lengths | `ValueError: x and y must be the same size` (scatter) | Plot two columns from the *same* rows |
| Bar chart for a continuous number column | dozens of thin bars, unreadable | Use a histogram |
| No title or labels | readers cannot tell what the chart shows | Add title, axis labels and units |
| Plotting before cleaning | odd categories (`"Arts"`, `"arts "`) or a bar at 150 % | Clean first (see [03 pandas](03-pandas.md)) |
| Overlapping category labels | text runs together | `plt.xticks(rotation=45)` or a bigger `figsize` |
| Several charts drawn on top of each other in one cell | one messy chart | One chart per cell, each ending with `plt.show()` |

## See also

- [03 pandas](03-pandas.md): getting the numbers to plot
- [05 scikit-learn workflow](05-scikit-learn-workflow.md): the model behind a predicted-vs-actual plot
- [02 NumPy](02-numpy.md): arrays work anywhere a list does
