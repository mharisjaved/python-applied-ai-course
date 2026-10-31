# Project 06: Data Analysis Report

**Week 9 · Launched Day 45 · Individual project · About 4 hours (mostly homework) · Due: start of Day 47**

## The story

The student-success team at a learning centre has exported a year of data about its students: study habits,
attendance, sleep, part-time jobs and exam results. They want to know **which habits go with passing**, so they can
decide where to offer support. The export is messy (you met it on Day 42), and nobody on the team writes code.

Your job: a short, honest **report notebook** that a non-programmer can read from top to bottom. It loads the data,
cleans it (and says how), answers at least five questions with pandas, shows the answers in clear charts, and ends
with findings and limitations written in plain words.

Prefer another topic? You may analyse `expenses.csv` (three months of personal spending) or `apartments.csv`
(apartment features and prices) instead. The requirements are the same.

## What you will practise

Datasets, features and data quality (Day 42) · NumPy-style thinking: masks, means, medians (Day 43) · pandas:
filtering, sorting, new columns, `value_counts`, `groupby` (Day 44) · cleaning and matplotlib charts (Day 45) ·
writing conclusions that match the evidence (Day 41's bias and limitations discussion).

## What it should look like

Your report is a notebook with these sections (the starter already has them). A short extract of a finished
report on `students_raw.csv`:

```
## 2. Cleaning
| Step | What I did                        | Why                                     | Rows      |
| 1    | removed exact duplicate rows      | one student counted twice weighs double | 304 → 300 |
...
(304, 10) → (298, 10)
No missing values left: True
No duplicate rows left: True

## 3. Questions and answers
Q2: Do students with a part-time job pass less often?
    has_job   passed
    no        0.80
    yes       0.51
Answer: yes, clearly. 80 % of students without a job passed, but only 51 % of those with one.

## 5. Findings
- A part-time job is the strongest pattern: 51 % of working students passed against 80 % of the others.
...
## 6. Limitations
- Correlation is not causation: working students also study a little less, so the job itself may not be the cause.
```

Your questions, numbers and wording will differ. Every number you mention must come from your own code.

## Requirements

**Must** (needed to pass)

1. **Load and inspect:** `shape`, `head`, `info`, `describe`, and a check for missing values, duplicates,
   inconsistent categories and impossible values. Write 3–5 first observations.
2. **Clean and document:** a cleaning table in markdown (*what* you did, *why*, rows before → after) and the code
   that does it. For `students_raw.csv` this includes duplicates, categories, impossible values and missing values.
   For an already-clean dataset, show how you checked and say "no problems found".
3. **Sanity checks** after cleaning that print `True` (or `assert`s that pass): no missing values, no duplicates,
   plus at least one check of your own.
4. **At least 5 questions**, each with pandas code **and** a one- or two-sentence answer in words.
5. **At least 3 charts**, each with a title and axis labels (with units), the question it answers, and one sentence
   about what it shows. Use at least two different chart types.
6. **Findings:** 3–5 bullet points, each with a number from your analysis.
7. **Limitations:** at least (a) the data is synthetic/small, (b) correlation is not causation, (c) how your
   missing-data and cleaning choices could affect the results.
8. The notebook runs top to bottom with **Restart → Run All**, without errors.

**Should**

9. At least one question compares groups with `groupby`.
10. At least one **new column** you derived (e.g. `final_score - previous_score`, or `study_hours >= 10`).
11. The summary box at the top states your most important finding in 2–3 sentences.

**Could**

- A simple interactive filter: a variable at the top (e.g. `PROGRAM = "all"`) that, when changed, repeats the whole
  analysis for one group.
- Compare two datasets (e.g. a pattern in `students.csv` vs `students_raw.csv` before cleaning: what changes?).
- A fourth chart type (line chart over time for `expenses.csv`).
- Wrap your cleaning in a function and test it with a few `assert`s on a tiny hand-made DataFrame.

## Starter files and how to run them

| File | What is in it |
|------|---------------|
| `starter/report.ipynb` | all section headings, a working setup cell, a `clean_data()` function to finish, sanity checks, and `TODO` cells for questions, charts, findings and limitations |

1. Copy the `starter/` folder to a new folder **next to it**, e.g. `projects/06-data-analysis-report/my-report/`,
   so the relative path to the datasets still works. If you move the notebook anywhere else (e.g. your portfolio),
   change `DATA_DIR` in the setup cell so it points at the course `datasets` folder.
2. Open it in VS Code, select the course `.venv` kernel, and run the setup cell.
3. To switch dataset, change `DATASET = "students_raw.csv"` to `"expenses.csv"` or `"apartments.csv"`.

At the start, every cell runs; the sanity check "No missing values left" prints `False` until your cleaning is done.

Question ideas if you are stuck: *students*: Does sleep matter? Do students who do all 10 assignments pass more
often? *expenses*: Which category grows from month to month? How much is spent in cash vs card?
*apartments*: How much more does each extra bedroom cost on average? Are apartments near the centre (≤ 3 km) more
expensive? Does parking add to the price?

## Build plan

1. **Load and inspect** (Day 45 evening, 30 min). *Checkpoint:* shape printed, problems listed in "First observations".
2. **Clean** (45 min). Fill in `clean_data()` and the cleaning table. *Checkpoint:* both sanity checks print `True`;
   for `students_raw.csv` the result has 298 rows.
3. **Questions** (60 min). Write all 5 questions *before* coding, then answer them one by one.
   *Checkpoint:* every question has code output and an answer in words.
4. **Charts** (45 min). *Checkpoint:* 3 charts, each with title, axis labels and a "what it shows" sentence.
5. **Findings and limitations** (30 min), then the summary box. *Checkpoint:* **Restart → Run All** works, and
   every number in your text matches the output above it.

## Submission checklist

- [ ] `report.ipynb` runs top to bottom with Restart → Run All, no errors.
- [ ] No `TODO` left in the notebook.
- [ ] The cleaning table says what, why, and rows before → after.
- [ ] ≥ 5 questions, each answered in code **and** in words.
- [ ] ≥ 3 charts with titles, axis labels and units; at least two chart types.
- [ ] Findings with numbers; Limitations covering data, causation and cleaning choices.
- [ ] Should/Could items you did are listed in the first markdown cell.

## Evaluation rubric (100 points)

| Criterion | Points | Full points when… |
|-----------|--------|-------------------|
| Works as specified | 40 | all Must items present and the notebook runs top to bottom; see the project-specific split below |
| Code readability | 20 | clear variable names, short cells that each do one thing, comments where a choice is not obvious |
| Data problems handled | 15 | every quality problem is found, handled deliberately, and the choice is explained (missing values, duplicates, categories, impossible values) |
| Evidence it works | 10 | sanity checks pass; numbers in the text match the code output; results cross-checked where possible |
| Explanation / demo | 15 | you can explain any cell and defend one cleaning choice and one conclusion |

**Project-specific criteria** (the 40 points for "works as specified"):

| Criterion | Points | Full points when… |
|-----------|--------|-------------------|
| Correctness of analysis | 15 | each pandas answer really answers its question (right filter, right group, right column) |
| Clarity of charts | 13 | right chart type for the question, title, labelled axes with units, readable, one message each |
| Quality of written conclusions | 12 | findings are specific and use numbers; limitations are honest; no claim of cause from a correlation |

Should and Could items earn up to 10 bonus points (total capped at 100).

## Extension ideas

- Add a "What would I tell the student-success team?" section: 3 recommendations, each linked to a finding, and
  one thing you would want to measure next.
- Repeat your analysis with `PROGRAM` set to each program in turn: does the part-time job pattern hold everywhere?
- After Week 10: use your strongest finding as the starting point for Project 07's ML Predictor.
