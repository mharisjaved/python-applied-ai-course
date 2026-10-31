# Day 49: Evaluation, Overfitting and Data Leakage

**Week 10 · Session 49 of 60 · Planned 75 min** · Previous: [Day 48](../day-48-classification/lesson.md) · Next: [Day 50](../day-50-project-ml-predictor/lesson.md)

## Objectives

By the end of this lesson students can:

1. Recognise **underfitting** and **overfitting** from a table or plot of training vs test scores.
2. Run a `max_depth` experiment in a loop, collect the results in a DataFrame and plot both curves.
3. Compute **precision** and **recall** for the class they care about, by hand from a confusion matrix and with scikit-learn, and explain them with the "flag students who need support" story.
4. Spot **data leakage** in an experiment (a feature known only afterwards, decisions made with the test set, duplicates across the split) and fix it.
5. Explain why a near-perfect score should make them suspicious first.

**Prior knowledge:** Day 46 (split, baseline, the memorising tree), Day 47 (MAE, results in a loop), Day 48
(confusion matrix in words, `predict_proba`, the `final_score` warning), `drop_duplicates` (Day 45), lists of dicts
→ DataFrame (Day 48).

**New today:** overfitting/underfitting vocabulary, `precision_score`, `recall_score` with `pos_label`,
`plt.axhline`, `get_n_leaves()`, `pd.concat`, a validation split, optional `cross_val_score`.

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: the tree with no limit (demo section 1) | core |
| 0:05–0:20 | Underfitting/overfitting, the depth experiment and plot (sections 2–3) | core |
| 0:20–0:32 | Precision and recall: the support story (section 4) | core |
| 0:32–0:45 | Data leakage: too good to be true, then two more leaks (sections 6–7) | core |
| 0:45–0:47 | Common mistakes (section 9) | core |
| 0:47–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket, preview the project | core |
| +5 min | Moving the threshold (section 5) | optional |
| +5 min | Cross-validation as "five mini-exams" (section 8) | optional (90-min session) |

**For 60 min:** show the depth plot without building the table live, skip Leak A's validation code (say it in
words), and set Exercises 4–5 as homework.

## 1. Warm-up: the tree with no limit (5 min)

**Prediction question:** "A tree may ask as many questions as it likes. Training accuracy? Test accuracy?"
Run demo section 1: **1.0** on training, **0.733** on test, **45 leaves** for 238 students. "Some leaves describe
one single student. Is that learning?"

## 2. Underfitting and overfitting (15 min)

**Analogy** (table in demo section 2), three students preparing with past papers:
- Omar learns one trick ("always answer C"): poor everywhere → **underfitting** (too simple).
- Sara memorises every past answer, typos included: perfect on past papers, poor on the real exam → **overfitting**.
- Mei understands the main ideas: good on both → **good fit**.

**The warning sign of overfitting is the gap between training and test.**

Live code (demo section 3), a loop students will reuse in the project:

```python
rows = []
for depth in range(1, 13):
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree.fit(X_train, y_train)
    rows.append({"max_depth": depth,
                 "train_accuracy": round(tree.score(X_train, y_train), 3),
                 "test_accuracy": round(tree.score(X_test, y_test), 3)})
experiment = pd.DataFrame(rows)
```

**Prediction question** before running: "As depth grows, what happens to each line?" Then the plot:

| depth | train | test | reading |
|-------|-------|------|---------|
| 1 | 0.727 | 0.650 | underfitting (says "pass" to everyone; equals the baseline) |
| 3 | 0.849 | 0.767 | sweet spot |
| 8 | 0.975 | 0.700 | overfitting: gap 0.275 |
| 11–12 | 1.000 | 0.733 | memorised every training student |

Remind them: 60 test students → one student = 0.017. Read the **shape**, not single bumps.

## 3. Precision and recall (12 min)

**Story first** (demo section 4): "In week 3 the school flags students likely to fail so a tutor can contact them.
Which is worse: a student who needed help and was **missed**, or a **false alarm** (a tutor spends 30 minutes with a
student who would have passed)?" Let students argue for a minute. Most agree: missing is worse.

Use the logistic model from Day 48, `[[15 6] [3 36]]`. The class we hunt for is **fail (0)**.

- **Recall** = of the students who really failed, what share did we flag? **15 / 21 = 0.71**
- **Precision** = of the students we flagged, what share really failed? **15 / 18 = 0.83**

Point at the grid: recall uses the **row** of real fails; precision uses the **column** of flags.
Then check with sklearn; `pos_label=0` says "fail is the class we hunt":

```python
recall_score(y_test, predictions, pos_label=0)      # 0.71
precision_score(y_test, predictions, pos_label=0)   # 0.83
```

Plain words for the board: **"We find 71% of the students who need help, and 83% of our flags are correct."**
Memory trick: *recall* = did we find (recall) them all? *precision* = were our flags precise?

Optional (section 5): flag when P(pass) < 0.7 instead of 0.5 → recall 0.86, precision 0.67; at 0.8 recall 1.0 with
33 flagged. **Prediction question:** "What happens to each number if we flag more?" Key message: choosing the
threshold is a human decision about costs (number of tutors), not a maths question.

## 4. Data leakage (13 min)

**Definition:** the model gets information during training that it would **not** have when making real predictions.

**Too good to be true** (demo section 6): add `final_score` to the features → test accuracy **1.0**.
**Prediction question:** "Is this our best model?" Then `export_text`: one question, `final_score <= 50`, which is
the definition of `passed`. Useless in week 3, when nobody knows the final score. Remove it → back to the honest 0.767.

The habit: **for each feature, ask "would I know this value at the moment I need the prediction?"**
And: **a perfect score on new data means "look for a leak", not "celebrate".**

Two more leaks (demo section 7):
- **Leak A, deciding with the test set.** We picked depth 3 *because* it scored best on the test set. Now the test
  set helped choose, so 0.767 is optimistic (best of 12 tries on the same exam). Honest way: split the training
  data again into **fit** and **validation** parts, choose on validation, use the test set **once**. Validation picks
  depth 2; its honest test score is **0.733**.
- **Leak B, duplicates across the split.** `pd.concat([df, df])` simulates a file where every student appears twice.
  The memorising tree jumps from 0.733 to **0.867**: it recognises twins it saw in training. Fix: `drop_duplicates()`
  **before** splitting. Real-world versions: the same house listed twice, the same patient's repeated visits.

Mention (no code): statistics computed on all rows (for example filling gaps with the median of the whole file)
also leak a little; the strict rule is "compute on the training rows only".

## 5. Common mistakes (2 min)

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `recall_score(..., pos_label="fail")` | `ValueError: pos_label=fail is not a valid label. It should be one of [0 1]` | Our classes are the numbers 0 and 1 |
| Forgetting `pos_label=0` | **no error**: recall for *pass* (0.92) | Default is class 1; say which class you hunt |
| Precision = caught / row total | **no error**, wrong number | Recall uses the row (reality), precision the column (flags) |
| Choosing `max_depth` by test score | **no error**, optimistic score | Choose on validation (or cross-validation), test once |
| Removing duplicates after the split | **no error**, inflated score | Clean first, then split |

## 6. Practice (23 min)

Circulate and watch for:
- Exercise 1, experiment D: students calling it "the best model";
- Exercise 2: forgetting `round`, or plotting with `plt.scatter` (fine) without labels/legend (not fine);
- Exercise 3: dividing by the wrong total; ask "is that a row or a column?";
- Exercise 4: dropping duplicates **after** splitting, or keeping the test set inside the depth loop.

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Diagnose the experiment | under/overfitting/leak from numbers | recall/reasoning |
| 2 Your own depth experiment | loop → table → plot, reading the gap | application |
| 3 Precision and recall by hand | formulas from the grid, sklearn check, choosing a model | application |
| 4 Leakage hunt | three leaks, honest rewrite with a validation split | modification |
| 5 How many students can the tutors take? | threshold vs capacity | problem solving |
| 6 Choose the depth honestly (challenge) | `cross_val_score` | challenge |

Expected numbers: Ex 2 test peaks at depth 3 (0.767), falls to 0.667 at depth 9–10 · Ex 3 recall 0.57, precision
0.71 · Ex 4 honest: depth 3, test 0.767 · Ex 5: 0.5 → 18 flagged, 0.6 → 22 flagged · Ex 6: CV picks depth 2, test 0.733.

## 7. Recap and exit ticket (5 min)

Ask students to supply:
1. Overfitting = great on training, much worse on test. Underfitting = poor on both.
2. Recall = share of real cases we found; precision = share of our flags that were right.
3. Leakage = information the model would not have at prediction time. Perfect score → look for a leak.

**Exit ticket:** Diego predicts whether a customer will return a parcel. His features include `refund_amount`
(filled in after a return is processed). Train accuracy 0.99, test accuracy 0.99. What is wrong, and how does he
fix it?

Answer: *Leakage: `refund_amount` is only known after the return happened, so the model reads the answer. Remove it
(and any other after-the-event columns) and re-evaluate; expect a lower, honest score.*

End with a 1-minute preview of tomorrow: Project 07 (choose classification or regression, compare ≥ 2 models with a
baseline, explain your metric, leakage check, `predict_one`). Students should glance at
[projects/07-ml-predictor/README.md](../../../projects/07-ml-predictor/README.md) tonight.

## Homework (25 min)

Read the Project 07 brief and pick an option (a–d). Write your problem statement (2 sentences) and a feature list
with a "known before the prediction?" column. Bring it tomorrow.

## Next class

Day 50: **Project 07, ML Predictor**, plus Checkpoint 10. Everything from this week in one notebook: split,
baseline, two models, the right metric in plain words, a leakage check, a plot and a `predict_one` function.

## Instructor notes

- Students' depth curves are bumpy because the test set is small. If someone's "best depth" is 6, that is fine;
  the lesson is the gap, not the exact number.
- The demo deliberately catches *us* leaking (Leak A after section 3). Own it: "I just did it in front of you." This
  makes the point stick better than any definition.
- Do not introduce F1, ROC curves or AUC. Precision/recall with one story is enough. If asked about "true
  positive" vocabulary, map it once: TP = caught, FN = missed, FP = false alarm, TN = correctly cleared.
- Cross-validation is optional and only as "five mini-exams on the training data". Do not explain folds in detail.
- The Day 45 cleaning recipe filled gaps with the median of the whole file. If a sharp student points out that this
  is a (tiny) leak, praise them: they are right, and in a real project you would compute the median on `X_train`.
- Fast students: Exercise 6, then repeat Exercise 2 with `LogisticRegression` (no depth: its gap stays small).
- Slow students: Exercises 1, 3 and 4 are about reasoning; make sure they do those even if Exercise 2 is unfinished.
