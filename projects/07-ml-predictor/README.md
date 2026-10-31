# Project 07: ML Predictor

**Week 10 · Launched Day 50 · Individual project · About 4 hours (1 in class, the rest homework) · Due: two days after Day 50 (e.g. start of Day 52)**

## The story

A learning centre, a flat-hunting website and a wine co-operative have one thing in common: they have past
examples with known answers and want a **prediction for the next case**. This week you learned the honest way to
build one: hold out a test set, beat a baseline, pick the right metric, check for leakage and say clearly what the
model cannot do.

Your job: a notebook that takes **one prediction task from start to finish**: a problem statement, a fair
evaluation of at least two models against a baseline, a plot, a `predict_one(...)` function that answers for a
brand-new example, and an honest "Limitations & responsible use" section that a non-programmer can understand.

## Choose your task

| Option | Data | Predict | Task | Main metric |
|--------|------|---------|------|-------------|
| **a** | `datasets/students.csv` | `passed` (1/0) | classification | accuracy + recall/precision for "fail" |
| **b** | `datasets/students.csv` | `final_score` (0–100) | regression | MAE in points |
| **c** | `datasets/apartments.csv` | `price_k` (thousands) | regression | MAE in thousands |
| **d** | `load_wine` or `load_breast_cancer` from `sklearn.datasets` (**ask your instructor first**) | `target` | classification | accuracy (+ recall for the class that matters) |

Option d loads without a download:

```python
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer(as_frame=True)
df = data.frame               # features + a "target" column
print(data.target_names)      # what 0 and 1 mean
```

## What you will practise

The workflow from Day 46 (question → data → `X`/`y` → split → baseline → fit → evaluate → predict) · regression
and MAE (Day 47) · classification, accuracy and the confusion matrix (Day 48) · overfitting, precision/recall and
leakage (Day 49) · functions with checks and `raise` (Days 17, 25) · explaining numbers in plain words.

## What it should look like

A short extract from a finished option (a) notebook:

```
## 5. Baseline, two models and a results table
                    model  train_accuracy  test_accuracy  recall_fail  precision_fail
0  baseline (always pass)           0.727          0.650         0.00            0.00
1     logistic regression           0.849          0.850         0.71            0.83
2  decision tree, depth 3           0.849          0.767         0.57            0.71

## 6. What the numbers mean
Logistic regression classifies 85% of the 60 test students correctly (the baseline: 65%). More important for
the centre: it finds 71% of the students who will fail (15 of 21), and 83% of the students it flags really
need help.

## 9. Using the model
>>> predict_one({"study_hours": 6, "attendance_pct": 78, "sleep_hours": 6.5,
...              "previous_score": 58, "assignments_done": 7, "has_job": "yes"})
{'prediction': 'fail', 'chance_of_passing': 0.15}
```

Your numbers, wording and choices will differ. Every number in your text must come from your own output.

## Requirements

**Must** (needed to pass)

1. **Problem statement:** what you predict, for whom, how the prediction would be used, classification or
   regression, and what a useful result looks like.
2. **Features with justification:** a table with one line per feature ("why it might help") and an explicit
   **leakage check** ("known at the moment of prediction?"). List the columns you left out and why.
3. **Train/test split** with `test_size` and `random_state=42`.
4. **Baseline:** `DummyClassifier(strategy="most_frequent")` or `DummyRegressor(strategy="mean")`.
5. **At least two real models** compared with the baseline in a **results table** (a DataFrame), all measured on
   the **test** set.
6. **The right metric(s), explained in plain words**: accuracy (plus the confusion matrix, and recall/precision
   for the class you care about) for classification; MAE in the target's units for regression.
7. **At least one plot** with a title and axis labels (e.g. a confusion matrix, or predicted vs actual).
8. **`predict_one(example)`**: takes one new example (a dict) and returns a single prediction. It raises a clear
   `ValueError` when a feature is missing. Show it on at least two examples.
9. **Limitations & responsible use:** at least four specific points (data size, who is harmed by which mistake,
   fairness of features, when the model would stop working, how it should and should not be used).
10. **Restart → Run All** works without errors.

**Should**

11. Try **one improvement** (feature selection, `max_depth` tuning, …) and report its test result next to the
    original, **honestly, even if it is worse**. Decide the improvement in advance, or choose its setting with a
    validation split or cross-validation on the **training** data (Day 49), never by trying settings on the test set.
12. Record training scores too, and comment on any sign of overfitting.

**Could**

- A small command-line script (`.py`) that loads the data, trains the final model and asks the user for the
  inputs (with input validation: Day 25), then prints a prediction. Keep the `input()` loop in `main()` under
  `if __name__ == "__main__":` and add a few pytest tests for the non-interactive functions.
- `predict_one` that also returns how confident the model is (`predict_proba`) or a "give or take" based on the MAE.
- A second plot: a depth experiment (train vs test) or a bar chart of the results table.

## Starter files and how to run them

| File | What is in it |
|------|---------------|
| `starter/ml_predictor.ipynb` | all sections with `TODO`s, a working setup cell (all imports, `DATA_DIR`), a `predict_one` skeleton and a **self-check** cell that reports what is still missing |

1. Copy the starter notebook **into the same `starter/` folder** under a new name (e.g. `ml_predictor_asha.ipynb`)
   so `DATA_DIR = Path("../../../datasets")` still works. If you move it elsewhere, change `DATA_DIR`.
2. Open it in VS Code, select the course `.venv` kernel and **Run All**. Everything runs at the start; the
   self-check prints ❌ for the parts you have not done yet.
3. Option (c): change the file name in section 2. Option (d): replace the `read_csv` line with the loader above.

## Build plan

1. **Choose and plan** (in class, 10 min). Problem statement and the feature table with the leakage column.
   *Checkpoint:* your instructor has seen your feature table.
2. **Split and baseline** (15 min). *Checkpoint:* the self-check shows ✅ for the split; you can say the
   baseline's score in one sentence.
3. **Two models and the results table** (30 min). *Checkpoint:* a table with at least 3 rows, all test scores.
4. **Metric in words and a plot** (30 min). *Checkpoint:* a sentence a non-programmer understands, compared
   with the baseline; one labelled plot.
5. **`predict_one` and the improvement** (45 min). *Checkpoint:* the self-check is all ✅; the improvement is
   reported even if it did not help.
6. **Limitations, tidy up, Restart → Run All** (30 min). *Checkpoint:* no `TODO` left, every number in your text
   matches the output.

## Submission checklist

- [ ] The notebook runs with Restart → Run All, no errors, and the self-check is all ✅.
- [ ] No `TODO` left. Your name and option are in the first cell.
- [ ] Feature table with a reason **and** a leakage answer for every feature; left-out columns explained.
- [ ] Baseline + at least two models in one results table, measured on the test set.
- [ ] Metric(s) explained in plain words, compared with the baseline.
- [ ] At least one plot with title and axis labels.
- [ ] `predict_one` works on two examples and rejects a bad one with a clear message.
- [ ] Limitations & responsible use: at least four specific points.
- [ ] Should/Could items you did are listed in the first markdown cell.

## Evaluation rubric (100 points)

| Criterion | Points | Full points when… |
|-----------|--------|-------------------|
| Works as specified | 40 | all Must items present and the notebook runs top to bottom; see the project-specific split below |
| Code readability | 20 | clear names, short cells, a small `evaluate`-style function or clean repetition, comments where a choice is not obvious |
| Handles bad input / edge cases | 15 | `predict_one` checks for missing (and, where sensible, impossible) values with clear messages; text columns converted correctly |
| Testing / evidence it works | 10 | self-check all ✅; `predict_one` shown on contrasting examples (e.g. bigger flat → higher price); numbers in text match output |
| Explanation / demo | 15 | you can explain any cell, why your metric fits, and what your best model gets wrong |

**Project-specific criteria** (the 40 points for "works as specified"):

| Criterion | Points | Full points when… |
|-----------|--------|-------------------|
| Honest evaluation | 15 | test set used only for final scores, baseline included, no leaking feature, improvement reported truthfully |
| Right metric, explained | 13 | metric fits the task; result stated in plain words and units, compared with the baseline; confusion matrix read in words (classification) |
| Responsible-use thinking | 12 | limitations are specific to the problem: who is harmed by which mistake, fairness, scope of the data |

Should and Could items earn up to 10 bonus points (total capped at 100).

## Extension ideas

- Option a or b: include `program` by giving each programme its own 0/1 column (look up `pd.get_dummies`), and
  report whether it helps.
- Compare your model's mistakes for students **with** and **without** a job (or cheap vs expensive flats). Is the
  model equally good for both groups?
- Option a: choose the probability threshold for flagging students (Day 49) based on a fixed number of tutoring
  places, and explain the trade-off.
- Turn the command-line script into a small module with a `predict_one` function and tests, ready to plug into the
  Week 12 AI Capstone.
