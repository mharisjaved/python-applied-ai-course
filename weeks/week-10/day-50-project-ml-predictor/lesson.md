# Day 50: Project 07: ML Predictor (+ Checkpoint 10)

**Week 10 · Session 50 of 60 · Planned 75 min** · Previous: [Day 49](../day-49-evaluation-overfitting/lesson.md) · Next: [Day 51](../../week-11/day-51-how-llms-work/lesson.md)

## Objectives

By the end of this lesson students can:

1. Show what they learned this week in Checkpoint 10 (split, baseline, MAE, confusion matrix, overfitting, leakage).
2. Choose a prediction task, write a problem statement and a feature table with a leakage check.
3. Start the Project 07 notebook: split, baseline and at least two models in one results table, all scored on the test set.
4. Describe what a complete, honest ML notebook contains (walk-through on the iris flowers).

**Prior knowledge:** all of Week 10: workflow and baselines (Day 46), `LinearRegression` and MAE (Day 47),
classifiers, confusion matrix, `predict_proba` (Day 48), overfitting, precision/recall, leakage, validation and
optional cross-validation (Day 49). Functions with `raise` (Days 17, 25).

**New today:** nothing new. The demo combines the week's pieces; the `evaluate(name, model)` helper that returns a
dict is a pattern, not a new concept.

**Files:** `demo.ipynb` (the "ML Predictor in miniature" on iris) · `practice.ipynb` (skill drills for the
project: use when stuck) · `solutions.ipynb` (you only) ·
[Checkpoint 10](../../../assessments/weekly/week-10-checkpoint.md) ·
[Project 07 brief](../../../projects/07-ml-predictor/README.md) ·
[Project 07 instructor notes](../../../projects/07-ml-predictor/INSTRUCTOR.md)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:20 | Checkpoint 10 (paper, closed notes) | core |
| 0:20–0:32 | Kick-off: options, rubric, iris walk-through at speed (demo sections 1–10) | core |
| 0:32–0:40 | Build step 1: problem statement + feature table; you sign off feature tables | core |
| 0:40–0:70 | Build steps 2–3: split, baseline, two models, results table | core |
| 0:70–0:75 | Two students show their results table; homework | core |
| +15 min | Project clinic, or practice drills 1–3 together for students who need them | optional (90-min session) |

**For 60 min:** keep the checkpoint, show only demo sections 3–4 and 8 (features/leakage, results table,
`predict_one`), and start building at 0:30.

## 1. Checkpoint 10 (20 min)

Hand out [week-10-checkpoint.md](../../../assessments/weekly/week-10-checkpoint.md). Collect it; go through the
two most-missed questions at the start of Day 51 (5 min) if needed. The checkpoint covers exactly what the project
needs, so weak spots tell you whom to visit first during build time.

## 2. Kick-off (12 min)

Open the [Project 07 brief](../../../projects/07-ml-predictor/README.md) and cover three things:

1. **The options** (a–d). Recommend: (a) if you liked Day 48–49, (b) or (c) if you liked Day 47. Option (d)
   (wine / breast cancer) only with your approval, for students who finished the Day 48 challenge.
2. **The rubric**, especially the 15 points for **honest evaluation**: test set used only for final scores, a
   baseline row, no leaking features, improvements reported even when they fail.
3. **The walk-through** (demo.ipynb on iris, a dataset nobody uses for the project). Scroll quickly, stopping at:
   - section 1: a problem statement says *what, for whom, how it is used, task type, what "good" means*;
   - section 3: the feature table with the "known at prediction time?" column;
   - section 4: `evaluate(name, model)` returns a dict; a list of dicts becomes the results table;
   - section 5: the metric in one plain sentence, compared with the baseline (0.29 vs 1.0 on 38 flowers);
   - section 7: an improvement chosen by cross-validation on the training data, reported honestly;
   - section 8: `predict_one` checks for missing values, builds a one-row DataFrame in `FEATURES` order and
     returns a single value (the tagged cell shows the clear error message);
   - section 9: limitations, specific to the problem.

**Prediction question** during the walk-through (section 5): "The baseline gets 0.29. Why so low, when on
`students.csv` it was 0.65?" (*Three balanced classes: always guessing one species is right about one time in
three. Two unbalanced classes: always saying "pass" is right 65–71% of the time.*)

## 3. Build time (38 min)

Students copy `starter/ml_predictor.ipynb` inside the `starter/` folder (so the data path works), then follow the
build plan in the brief. Run the room in this order:

1. **0:32–0:40, step 1.** Every student writes the problem statement and the feature table. Walk around and sign
   off feature tables before anyone trains a model. The two leaks to catch: `final_score` for `passed`, `passed` for
   `final_score`.
2. **0:40–0:55, step 2.** Split + baseline. The self-check cell turns the split line ✅.
3. **0:55–0:70, step 3.** Two models + results table. Fast students move on to step 4 (metric sentence + plot).

**Feature-table sign-off: what to look for (30 seconds per student)**

| Option | Must be out | Fine to use | Ask about |
|--------|-------------|-------------|-----------|
| a `passed` | `final_score` (defines the label), `student_id` | the five numeric habits + `has_job` as 0/1 | `assignments_done`: the file has the end-of-term count; would the centre know it in week 3? (Accept "yes, roughly" with a note) |
| b `final_score` | `passed` (computed from the target), `student_id` | same as (a) | the same `assignments_done` question |
| c `price_k` | `apartment_id` | all six columns | "Would a 'price per m²' column be allowed?" (no: it contains the price) |
| d wine / cancer | `target` itself | any measurement columns | "What do 0 and 1 (or 0/1/2) mean? Which mistake is worse?" |

A good problem statement names **who** uses the prediction and **what they do with it**. "Predict pass/fail" is
not enough; "flag students in week 3 so a tutor can contact them" is. Push back once, then let them continue.

**Questions you will hear, and short answers:**
- "Can I use `program`?" Only by giving each programme its own 0/1 column (an extension). Leaving it out is fine
  if the feature table says why.
- "My second model is worse than the first. Is that bad?" No. Report it; the rubric rewards honesty, not winning.
- "Which `max_depth` should I use?" Start with 3 (classification) or 4 (regression). If you want to tune it, use
  cross-validation on the training data, never the test set.
- "My model does not beat the baseline." Then that is your finding. Check for bugs (training on the right rows?
  text columns?), try one other feature set, and explain in the limitations what data would be needed.
- "Can I use `random_state` other than 42?" Yes, but fix it once and never change it to get a better score.

What to watch for (details and questions to ask in the instructor notes):
- training-set scores in the table (no gap at all is suspicious);
- `max_depth` "tuned" by trying values on the test set;
- text columns in `X` (`has_job`), and `X = df["col"]`;
- students who copy the iris notebook's sentences instead of writing about their own problem.

| Practice drill | Use it when a student is stuck on… | Level |
|----------------|-------------------------------------|-------|
| 1 Leakage and usefulness check | the feature table | recall/reasoning |
| 2 Which model wins? | sorting a results table (MAE: lower is better) | application |
| 3 Write `predict_one` | step 5 (`predict_one`) | application |
| 4 Metrics in plain words | step 4 (explaining the metric) | application |
| 5 Safe input for a command-line predictor | the CLI "Could" item | problem solving |
| 6 A reusable `evaluate` function (challenge) | a cleaner results table | challenge |

## 4. Wrap-up (5 min)

Two volunteers show their results table and say their best model's result in one sentence, compared with the
baseline. Then the class answers together: "Which one is the honest number to report, and why?"

**Exit ticket** (spoken): each student tells a neighbour their option, their baseline score and their best model so
far. Anyone who cannot name a baseline score has not finished step 2: they start there tonight.

## Homework (≈ 3 h, due at the start of Day 52)

Build plan steps 4–6: metric in plain words and a plot, `predict_one` + one improvement, limitations, then
Restart → Run All. Use the submission checklist in the brief.

## Next class

Day 51 starts **Week 11: Generative AI**. Bridge: "This week the model learned from a table of examples and
predicted one number or class. Large language models also learn from examples, billions of sentences, and
predict the **next word**. Same idea, very different scale." The project is homework from now on.

## Instructor notes

- The checkpoint takes the first 20 minutes on purpose: students arrive fresh, and the project then gets a long
  uninterrupted block. If your class is anxious about tests, give it at the end instead and shorten build time.
- Expect most students to finish step 2 and half of step 3 in class. That is on plan.
- Option (b) students sometimes add `passed` as a feature for `final_score`: it is computed from the target, so it
  leaks. The self-check flags this case.
- Do not introduce new tools today (pipelines, scaling, grid search). If a strong student wants more, point them to
  the extension ideas in the brief.
- Students who finish early: the Should item (one improvement), then the CLI "Could" item with practice
  Exercise 5. The reference CLI is `projects/07-ml-predictor/reference/apartment_price_cli.py`; do not share it
  before the deadline.
- Slow students: make sure they leave with a working split + baseline + one model. Two models and the table are
  the next step at home; drill 6 or the Day 48 demo section 6 shows the table pattern.
