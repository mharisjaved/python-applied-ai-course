# Week 10: Introductory Machine Learning

Students train their first scikit-learn models and, above all, learn to **evaluate them honestly**: hold out a test
set, beat a baseline, choose a metric that fits the question, read the mistakes, and recognise overfitting and
leakage. The week ends with Project 07, where each student takes one prediction task from question to a working
`predict_one` function.

| Day | Topic | Lesson | Demo | Practice | Solutions |
|-----|-------|--------|------|----------|-----------|
| 46 | ML workflow & train/test split | [lesson](day-46-ml-workflow/lesson.md) | [demo](day-46-ml-workflow/demo.ipynb) | [practice](day-46-ml-workflow/practice.ipynb) | [solutions](day-46-ml-workflow/solutions.ipynb) |
| 47 | Regression | [lesson](day-47-regression/lesson.md) | [demo](day-47-regression/demo.ipynb) | [practice](day-47-regression/practice.ipynb) | [solutions](day-47-regression/solutions.ipynb) |
| 48 | Classification | [lesson](day-48-classification/lesson.md) | [demo](day-48-classification/demo.ipynb) | [practice](day-48-classification/practice.ipynb) | [solutions](day-48-classification/solutions.ipynb) |
| 49 | Evaluation, overfitting & leakage | [lesson](day-49-evaluation-overfitting/lesson.md) | [demo](day-49-evaluation-overfitting/demo.ipynb) | [practice](day-49-evaluation-overfitting/practice.ipynb) | [solutions](day-49-evaluation-overfitting/solutions.ipynb) |
| 50 | 🏗 Project 07: ML Predictor | [lesson](day-50-project-ml-predictor/lesson.md) | [demo](day-50-project-ml-predictor/demo.ipynb) | [practice](day-50-project-ml-predictor/practice.ipynb) | [solutions](day-50-project-ml-predictor/solutions.ipynb) |

**Project:** [Project 07: ML Predictor](../../projects/07-ml-predictor/README.md) (notebook deliverable), started in
class on Day 50, due at the start of Day 52. Instructor notes: [INSTRUCTOR.md](../../projects/07-ml-predictor/INSTRUCTOR.md).
**Checkpoints:** [Checkpoint 9](../../assessments/weekly/week-09-checkpoint.md) in the first 15 minutes of **Day 46**;
[Checkpoint 10](../../assessments/weekly/week-10-checkpoint.md) in the first 20 minutes of **Day 50**.
Project 06 (data analysis report) is handed in at the start of Day 47.

## Datasets and conventions

`students.csv` (Days 46–49, project options a/b) · `apartments.csv` (Day 47 practice, project option c) ·
`load_iris` / `load_wine` (bundled with scikit-learn, no download: Day 48 optional, Day 50 demo, project option d).
Every split this week uses `test_size=0.2, random_state=42`, so the **same 60 test students** appear all week and
the baseline to beat for `passed` is always **0.65**. Text columns become numbers with
`(df["has_job"] == "yes").astype(int)` from Day 47 on. `final_score` is never a feature for `passed`.

## Prepare before the week

- [ ] `uv run python -c "import sklearn; print(sklearn.__version__)"` works on every student laptop (scikit-learn
      is in `pyproject.toml`; a stale environment needs `uv sync`).
- [ ] Run the validator: `uv run python scripts/validate_notebooks.py weeks/week-10 projects/07-ml-predictor --jobs 2`
      and the CLI tests: `cd projects/07-ml-predictor/reference && uv run pytest -q`.
- [ ] Print Checkpoint 9 (Day 46) and Checkpoint 10 (Day 50).
- [ ] Read both Project 07 reference notebooks and the reference numbers table in INSTRUCTOR.md.
- [ ] Prepare a board corner for the workflow (question → data → X/y → split → baseline → fit → evaluate →
      predict) and the 2 × 2 confusion-matrix grid; both stay up all week.

## Common difficulties and how to respond

1. **`X = df["col"]` (1-D)**: `Expected a 2-dimensional container`. It returns every day. Ask "one column or a
   table?" and point at the double brackets.
2. **Scores without context:** "my model is 85% accurate". Always ask "and the baseline, on the same test set?"
   Make the baseline row compulsory in every results table.
3. **Reading the confusion matrix by columns.** Rows = reality, columns = the model's answer. Fill the grid in
   words (caught / missed / false alarm / correctly cleared) before using vocabulary.
4. **Too good to be true is celebrated.** A perfect score on new data means "look for a leak" (Day 49). Ask "would
   you know this value at the moment you need the prediction?"
5. **Coefficients as causes or as importance.** "Linked to", not "causes"; and a bigger number is not a more
   important feature when the units differ (hours vs percent).
