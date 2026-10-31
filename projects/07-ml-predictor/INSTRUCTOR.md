# Project 07: Instructor Notes (keep private)

**Brief:** [README.md](README.md) · **Starter:** `starter/ml_predictor.ipynb` · **Reference:**
`reference/classification_passed.ipynb` (option a) · `reference/regression_apartments.ipynb` (option c) ·
`reference/apartment_price_cli.py` + `reference/test_apartment_price_cli.py` (the "Could" CLI, option c).

Both reference notebooks run offline and are checked by `scripts/validate_notebooks.py projects/07-ml-predictor`.
The CLI tests run with `cd projects/07-ml-predictor/reference && uv run pytest -q` (6 tests). The CLI was also
run by hand with piped input, including a non-number answer, which it rejected and asked again.

The deliverable is a notebook, so there is no failing pytest suite in the starter. Instead, the starter's
**self-check** cell prints ✅/❌ for the split, the results table, `final_model` and `predict_one`, plus an
obvious-leak check, without ever stopping the notebook.

## Timing plan

| When | What | Time |
|------|------|------|
| Day 49, last minute | Preview the brief; homework: choose an option, write problem statement + feature table | 1 min |
| Day 50, 0:00–0:20 | Checkpoint 10 | 20 min |
| Day 50, 0:20–0:32 | Kick-off: options, rubric, the iris walk-through (`weeks/week-10/day-50-.../demo.ipynb`) at speed | 12 min |
| Day 50, 0:32–0:70 | Build plan steps 1–3 in class; you circulate and sign off feature tables (step 1 checkpoint) | 38 min |
| Day 50, 0:70–0:75 | Two students show their results table; homework = steps 4–6 | 5 min |
| Homework (≈ 3 h) | Steps 4–6 | |
| Start of Day 52 | Submission. Optional: 2–3 volunteers show `predict_one` live (1 min each) | 5 min |

Day 51 starts Week 11 (LLMs), so do not spend class time on the project after Day 50. A 10-minute "clinic" at
the end of Day 51 is a good safety net if many students are stuck.

## Reference numbers (`test_size=0.2, random_state=42`)

| Option | Baseline | Models (test) | Notes |
|--------|----------|---------------|-------|
| a `passed`, 6 features | accuracy 0.650 | logistic 0.850 (recall fail 0.71, precision 0.83) · tree depth 3: 0.767 (0.57 / 0.71) | CV picks depth 2 → 0.733 test (worse) |
| b `final_score`, 6 features | MAE 8.8 | linear 5.04 (R² 0.67) · tree depth 3: 8.1 | with `study_hours` only: MAE 7.3 |
| c `price_k`, 6 features | MAE 54.2 | linear 12.2 (R² 0.94) · tree depth 4: 28.8 | without `floor` and `has_parking`: 16.5 (worse) |
| d wine, 4 features, `test_size=0.25` | accuracy 0.40 | tree depth 2: 0.867 | from Day 48 practice Exercise 6 |

Students who choose other features or depths get other numbers; that is expected. What matters is that their
numbers come from the test set and are compared with their own baseline.

## Common pitfalls

| Pitfall | Symptom | What to ask (not tell) |
|---------|---------|------------------------|
| `final_score` used to predict `passed` (or `passed` to predict `final_score`) | accuracy 1.0 with a 1-question tree, or a suspiciously low MAE | "Would the centre know this value in week 3?" |
| results measured on the training data | suspiciously high scores, no gap | "Which rows did this model learn from? Which rows did you score it on?" |
| `max_depth` chosen by trying values on the test set | "I tried 1–15 and depth 6 was best" | "Is the test set still a surprise exam for this model?" (point to Day 49 section 7) |
| baseline missing or computed on all rows | no baseline row, or `df[TARGET].mean()` | "What score do you get without any model, on the same test rows?" |
| text column in `X` | `ValueError: could not convert string to float` | "What does a model do with the word 'yes'?" (Day 47 section 4) |
| `X = df["col"]` | `Expected a 2-dimensional container` | "Is that one column or a table?" |
| `predict_one` returns an array | `[1]` or `array([225.4])` printed | "How do you get the first value out of a list?" |
| `predict_one` builds the DataFrame without `[FEATURES]` | feature-name error when the dict order differs | "Which column order did the model see in training?" |
| MAE explained without units, or accuracy without the baseline | "MAE is 12.2" | "12.2 what? Better than what?" |
| generic limitations | "the model might be wrong" | "Wrong how, and who pays for that mistake?" |
| improvement only reported when it helped | one model silently swapped | "What happened to the version that did not help?" |

## How to unblock without giving the answer

- Stuck choosing an option: options a and c are the safest; b is a good fit for students who liked Day 47. Only
  approve d for students who finished Day 48's challenge.
- Stuck on features: "Name one column you would check if you were the tutor / the buyer. Would you know it
  before the event?"
- Stuck on the results table: point to the Day 48 demo section 6 (list of dicts → DataFrame) or Day 50 practice
  Exercise 6; do not write the `evaluate` function for them.
- Stuck on `predict_one`: Day 50 practice Exercise 3 (the café) has the same three steps on different data.
- Stuck on limitations: ask them to finish two sentences out loud: "If my model is wrong about someone, that
  person…" and "My model would not work for…". Then write down what they said.

## Grading notes

- Grade one notebook in about 12 minutes: Restart → Run All first (errors cap "Works as specified" at 20/40), read
  the self-check, then the markdown sections, then skim the code.
- **Honest evaluation (15):** any leaking feature in the final model costs 8; scores measured on training data
  cost 8; missing baseline costs 5; a test-set-tuned setting reported without comment costs 3 (no penalty if the
  student says so in the text).
- **Right metric, explained (13):** a metric without units or without the baseline comparison scores at most half.
  Classification without reading the confusion matrix in words loses 4.
- **Responsible-use thinking (12):** four generic bullets ("small data", "might be wrong") score at most 6.
  Full points need at least one point about *which* mistake harms *whom* in this problem.
- **Handles bad input (15):** `predict_one` must reject a missing feature with a clear message (8). The rest for
  range checks, converting text inputs (e.g. `has_job` "yes"/"no") or a CLI with validated input.
- **Readability (20):** repeated fit/score code for three models is acceptable; a small helper function is better.
  Do not penalise not using cross-validation: it was optional.
- **AI assistant use:** look for things the course never used (`Pipeline`, `GridSearchCV`, `StandardScaler`,
  `seaborn`, `fig, ax`) or limitations that do not match the student's own numbers. Ask the student to explain that
  cell; grade the explanation.
- The reference notebooks are deliberately thorough. A passing submission can be half as long.
