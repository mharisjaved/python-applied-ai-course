# Week 9: Introduction to AI & Data

Students meet AI as "learning a rule from examples" (in plain Python), then learn to inspect, audit, clean,
summarise and chart a dataset with NumPy, pandas and matplotlib. By Friday they can turn a messy CSV into a
clean table, answer questions about it and explain the answers honestly: the foundation for machine learning
in Week 10.

| Day | Topic | Lesson | Demo | Practice | Solutions |
|-----|-------|--------|------|----------|-----------|
| 41 | What AI, ML, DL & GenAI are | [lesson](day-41-what-is-ai/lesson.md) | [demo](day-41-what-is-ai/demo.ipynb) | [practice](day-41-what-is-ai/practice.ipynb) | [solutions](day-41-what-is-ai/solutions.ipynb) |
| 42 | Datasets, features, labels & quality | [lesson](day-42-datasets/lesson.md) | [demo](day-42-datasets/demo.ipynb) | [practice](day-42-datasets/practice.ipynb) | [solutions](day-42-datasets/solutions.ipynb) |
| 43 | NumPy essentials | [lesson](day-43-numpy/lesson.md) | [demo](day-43-numpy/demo.ipynb) | [practice](day-43-numpy/practice.ipynb) | [solutions](day-43-numpy/solutions.ipynb) |
| 44 | pandas DataFrames | [lesson](day-44-pandas/lesson.md) | [demo](day-44-pandas/demo.ipynb) | [practice](day-44-pandas/practice.ipynb) | [solutions](day-44-pandas/solutions.ipynb) |
| 45 | Cleaning, EDA & visualisation | [lesson](day-45-cleaning-visualization/lesson.md) | [demo](day-45-cleaning-visualization/demo.ipynb) | [practice](day-45-cleaning-visualization/practice.ipynb) | [solutions](day-45-cleaning-visualization/solutions.ipynb) |

**Project:** [Project 06: Data Analysis Report](../../projects/06-data-analysis-report/README.md), launched at the
end of Day 45, due at the start of Day 47 (notebook deliverable, mostly homework).
**Checkpoint:** [Checkpoint 9](../../assessments/weekly/week-09-checkpoint.md) in the **first 15 minutes of Day 46**
(Day 45 is full with cleaning, charts and the project launch).

## Datasets used

All in `datasets/` (read [datasets/README.md](../../datasets/README.md)). Notebooks load them with
`Path("../../../datasets")`. `students.csv` (D41, D43–45) · `students_raw.csv` (D42, D45, Project 06) ·
`expenses.csv` (D42 practice, D44, D45 practice) · `apartments.csv` (D42 practice, Project 06 option).

## Prepare before the week

- [ ] In the course environment, `uv run python -c "import numpy, pandas, matplotlib"` works on every student laptop
      (they are in `pyproject.toml`; a stale environment needs `uv sync`).
- [ ] Run the validator once: `uv run python scripts/validate_notebooks.py weeks/week-09 --jobs 2`.
- [ ] Re-read `datasets/README.md`: the planted problems in `students_raw.csv` and the exact Day 45 cleaning recipe.
- [ ] Open a demo notebook in VS Code and check that charts appear inline (Day 45).
- [ ] Print or share the Project 06 brief and rubric for Day 45; prepare paper copies of Checkpoint 9 for Day 46.
- [ ] Plan the Day 41 discussion groups (pairs work well for the bias questions).

## Common difficulties and how to respond

1. **CSV values are text** (Days 41–42): accuracy of exactly 0.0 or `TypeError` on `>=` means a missing `int()`/
   `float()`. Ask "what type does DictReader give you?" before fixing it for them.
2. **`and` vs `&`, and missing brackets** (Days 43–45): the same `ValueError: … ambiguous` keeps coming back. Write
   the rule on a permanent corner of the board: `&` `|` and brackets around every condition.
3. **Missing values fail every comparison** (Day 45): the `study_hours >= 0` filter silently loses 8 rows. Treat it
   as the key lesson of the week: silent bugs are worse than crashes, so always check shapes.
4. **Too many new names at once** (Days 43–45): keep the recap tables from each demo visible; students should
   copy them into their own notes rather than memorise them.
5. **Numbers without meaning:** students stop when the code runs. Ask every time "what does that number say, in
   words?" Project 06 grades exactly this.
