# Day 41: What AI, ML, DL and GenAI Are

**Week 9 · Session 41 of 60 · Planned 75 min** · Previous: [Day 40](../../week-08/day-40-capstone-demo/lesson.md) · Next: [Day 42](../day-42-datasets/lesson.md)

## Objectives

By the end of this lesson students can:

1. Place AI, machine learning (ML), deep learning (DL) and generative AI (GenAI) in nested circles and give one example of each.
2. Explain the difference between a **hand-written rule** and a rule **learned from examples**.
3. Measure a rule's **accuracy** on a dataset (correct predictions ÷ all predictions).
4. Describe "training" as *trying many candidate rules and keeping the one that scores best*, and "prediction" as *using that rule on a new case*.
5. Classify a use case as *rules*, *ML* or *GenAI*, and name one limitation or bias risk.

**Prior knowledge:** reading a CSV with `csv.DictReader` (Day 36), the "DictReader gives strings" trap (Day 36),
functions with parameters and `return` (Day 17), accumulators (Day 11), `pathlib.Path` (Day 24),
f-string format specs (Day 05). **No new syntax today.** It is a concepts day built on Python they already know.

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only) ·
dataset `datasets/students.csv` (read only).

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: what will a computer "learn"? | core |
| 0:05–0:15 | AI / ML / DL / GenAI: the nested circles (demo section 1) | core |
| 0:15–0:25 | A hand-written rule and its accuracy (demo sections 2–3) | core |
| 0:25–0:37 | Learning a threshold from examples = training (demo sections 4–5) | core |
| 0:37–0:47 | Use cases, limitations, bias, when *not* to use AI (demo section 6) | core |
| 0:47–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (challenge) together: two features beat one | optional (90-min session) |
| +5 min | Extra discussion round: "AI in your own field" | optional (90-min session) |

**60-minute version:** shorten section 6 to the use-case table only (5 min) and set Exercise 5 as homework.

## 1. Warm-up (5 min)

Students just finished an 8-week Python foundation. Start by connecting it to the AI half:

- "Everything we wrote so far was **rules we typed**: `if score >= 50: ...`. Who decided the 50?" (*We did.*)
- "How would you write rules to recognise a cat in a photo?" Let them try for 30 seconds. The point: some tasks are
  easy for people but impossible to write down as rules. That gap is why machine learning exists.

Retrieval question (Day 36): "What type is every value that `csv.DictReader` gives you?" (*`str`, always. We will
need `float()` and `int()` today.*)

## 2. The nested circles (10 min)

Draw four nested circles on the board (also in demo section 1):

| Circle | Plain-words meaning | Example |
|--------|---------------------|---------|
| **AI** (outer) | any technique that makes a computer do something we would call "intelligent" (including hand-written rules, search, planning) | a chess program, a route planner |
| **ML** | AI that **learns patterns from examples** instead of being given every rule | spam filter, price predictor |
| **DL** | ML with very large "neural networks" (many layers of simple maths units), needs lots of data | face unlock, speech-to-text |
| **GenAI** | DL models that **create** new text, images, code or audio | chat assistants, image generators |

Key points to say out loud:
- Every GenAI system is ML, but most ML is **not** GenAI. Week 10 is classic ML; Weeks 11–12 are GenAI.
- "AI" in the news usually means GenAI. In industry most deployed ML is still the boring kind: predicting a number
  or a category from a table. That is exactly what we will do next week.
- Do **not** explain neural networks in any depth. One sentence is enough.

**Analogy:** rules are a **recipe** someone writes down. ML is a cook who tastes 300 dishes and works out the
recipe on their own. The cook might get it slightly wrong, and might copy bad habits from the dishes they tasted.

## 3. A hand-written rule and its accuracy (10 min)

Live code (demo section 2): load `students.csv` with `csv.DictReader` (298 students). Show one row and point out
the target column `passed` (1 = passed, 0 = failed).

A teacher's rule of thumb: *"students who study at least 10 hours a week pass."*

```python
def predict_pass(student, threshold):
    """Predict 1 (pass) if the student studies at least `threshold` hours a week, else 0 (fail)."""
    if float(student["study_hours"]) >= threshold:
        return 1
    return 0
```

Try it on the first student (14 hours → predicts 1, actual `passed` is `"1"`).

Demo section 3: **accuracy** = how many predictions were right ÷ how many we made. Write `accuracy(students,
threshold)` with an accumulator. Expected: `accuracy(students, 10)` → `0.587...`, so the teacher's rule is right
for about 59 % of students.

**Prediction question:** "Is 59 % good?" Collect guesses, do not answer yet. Section 5 answers it.

## 4. Learning from examples = training (12 min)

Demo section 4. Instead of guessing the threshold, **let the data choose it**: try 0, 1, 2, … 20 hours, measure the
accuracy of each, keep the best. Print a tiny text bar for each threshold so the "hill" is visible:

```text
 0 h   71.1%  ####################################
 ...
 4 h   73.8%  #####################################
 ...
10 h   58.7%  #############################
 ...
20 h   29.2%  ###############
```

Best: **4 hours → 73.8 %**. Say it clearly:

> This loop **is** training. The data "taught" us the number 4. The learned number is our **model**.
> Real ML libraries do the same thing (try candidates, measure, keep the best), only much faster and
> with many columns at once.

Then **prediction** (demo section 5): use the learned threshold on new students who are not in the file
(Omar 6.5 h → 1, Mei 2 h → 0). Training happens once; prediction happens every time a new case arrives.

**The baseline surprise:** threshold 0 means "predict *pass* for everyone". That already scores **71.1 %**, because
71 % of students passed. Our learned rule beats it by only ~3 points. Ask: "So is study time useless?"
(*No, but one column is not enough to predict well. Other things matter too: attendance, previous score, sleep…
Next week the computer will combine many columns at once.*) This is the idea of a **baseline**, formally taught on Day 46.

**Prediction question before running the group check:** "Is the rule equally accurate for students with and without
a part-time job?"

## 5. Use cases, limitations, bias, when not to use AI (10 min)

Demo section 6 shows the learned rule is correct for **78.9 %** of students without a job but only **61.8 %** of
students with one. Same rule, very different quality for two groups. That is a small, concrete example of **bias**.

Discussion prompts (pairs, 1 minute each, then take two answers):
1. "A college wants to use our 4-hour rule to decide who gets a scholarship. What could go wrong?"
   (*Unfair to working students; it is wrong for 1 in 4 students; students who study less but pass are punished.*)
2. "The same rule is used to decide who gets a **free tutoring** offer. Is that more acceptable? Why?"
   (*Lower stakes, offers help instead of taking something away, a human can still decide.*)
3. "Where did the bias come from: the code or the data?" (*The code is neutral. The data reflects students' situations.
   A model copies the patterns in the data, including unfair ones.*)
4. "Name a task where you would **not** use AI." (*Calculating tax or a late fee: the exact rule is known and must
   be exact. Also: no data, mistakes too costly without a human check, or the decision must be fully explainable.*)

Use-case table (demo section 6, students classify in Exercise 1):

| Use case | Best fit | Why |
|----------|----------|-----|
| Late fee = days late × 0.50 | rules | rule known and must be exact |
| Spam filter | ML | rules go stale; many examples of spam exist |
| Predict next month's electricity use | ML | pattern in past data |
| Summarise a long email | GenAI | creates new text |
| Check a password has ≥ 8 characters | rules | exact policy |
| Unlock a phone with a face | DL | images; no one can write face rules |

Limitations to name: needs (good) data · makes mistakes (accuracy < 100 %) · copies past patterns, including bias ·
hard to explain why (for DL/GenAI) · GenAI can sound confident while being wrong ("hallucination", Week 11) ·
privacy of the data used.

## 6. Common mistakes

| Mistake | Error / symptom | How to explain it |
|---------|-----------------|-------------------|
| `prediction == student["passed"]` | accuracy is always 0 | DictReader gives `"1"` (text). `1 == "1"` is `False`. Convert with `int()` |
| `float(student["study_hours"])` forgotten | `TypeError: '>=' not supported between 'str' and 'int'` | Same trap: CSV values are text |
| best-so-far never updated | "best" threshold is the last one tried | Update **both** `best_accuracy` and `best_threshold` inside the `if` |
| Thinking 74 % accuracy means "74 % sure about each student" | (misconception) | It means "right for 74 of every 100 students in this file" |
| "The AI is biased because the code is biased" | (misconception) | The rule was learned from data; the data carries the pattern |

## 7. Practice (23 min)

Students open `practice.ipynb`.

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Rules, ML or GenAI? | classify use cases | recall |
| 2 Your own rule | write a rule, measure accuracy | application |
| 3 Fix the training loop | debugging str vs int, best-so-far | modification |
| 4 Learn an attendance threshold | training on a different column | problem solving |
| 5 Is the rule fair to every program? | per-group accuracy, bias reasoning | problem solving |
| 6 Two columns beat one (challenge) | combined score + threshold search | challenge |

Circulate and look for:
- comparing `int` with `str` (accuracy exactly 0.0 is the tell-tale sign);
- students who copy the demo instead of reusing `predict_pass`: ask "can a function do that for you?";
- Exercise 5 answers that stop at numbers. Push for one sentence of interpretation.

Expected outcome: everyone completes 1–3, most complete 4, many complete 5, fast students try 6 (best combined
threshold 68 → 80.9 %).

## 8. Recap and exit ticket (5 min)

Ask students to supply the recap:
1. AI ⊃ ML ⊃ DL ⊃ GenAI. ML learns patterns from examples instead of being given rules.
2. **Training** = try candidate rules on known examples, measure, keep the best. **Prediction** = apply it to new cases.
3. Accuracy alone can fool you: compare with a simple baseline (always "pass" = 71 %), and check each group.

**Exit ticket:** "A shop wants to predict whether a customer will return next month. It has 2 years of purchase
records. Rules, ML or GenAI? Name one thing that could go wrong."

Answer: ML (a prediction learned from many past examples). Possible problems: past data may not reflect new
customers; the model may be less accurate for one group (e.g. new or online-only customers); it will sometimes be wrong.

## Homework (20 min)

Finish Exercise 5. In a markdown cell, write 3–4 sentences: one AI tool you used this year, whether it is rules,
ML or GenAI, and one limitation you noticed.

## Next class

Day 42 looks closely at the **data** that ML learns from: rows and columns, features vs target, numeric vs
categorical, and the problems hidden in a messy file. Today's file was already clean; tomorrow we audit the raw
version it came from. Teaser: "the raw file has a student with 150 % attendance."

## Instructor notes

- Today is deliberately low on new syntax. Spend the saved time on **discussion**; it is the only session where
  students think about AI before they start using libraries.
- Do not teach train/test split today, even if someone asks "isn't it cheating to measure on the same data we
  learned from?" Say: "Excellent question, that is exactly Day 46." Write it on a "parking lot" corner of the board.
- Keep definitions informal. Avoid "neurons", "weights", "gradient". If asked how GenAI works: "it predicts the next
  word, very well, after reading a huge amount of text. Week 11 goes deeper."
- Avoid fear or hype. "Will AI take our jobs?" → redirect to "what tasks is it good and bad at?" (section 5).
- Fast students: Exercise 6, then ask them to try `study_hours >= t` **and** `has_job == "no"` and discuss
  whether using `has_job` is fair. Slow students: pair them for Exercise 3 and skip Exercise 4.
