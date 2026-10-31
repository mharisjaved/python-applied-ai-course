# Project 06: Instructor Notes (keep private)

**Brief:** [README.md](README.md) · **Starter:** `starter/report.ipynb` · **Reference:** `reference/report.ipynb`
(complete report on `students_raw.csv`, runs offline, validated by `scripts/validate_notebooks.py`).

There is no pytest suite for this project: the deliverable is a notebook. "Evidence it works" is graded from the
sanity checks inside the notebook (print checks or `assert`s) and from numbers in the text matching the output.

## Timing plan

| When | What | Time |
|------|------|------|
| Day 45, 0:65–0:72 | Launch: walk through the brief, the rubric and the starter's sections | 7 min |
| Day 45 homework | Build plan steps 1–2: load, inspect, clean; write the 5 questions | ~75 min |
| Day 46 (end of class, optional) | 5-minute check-in: "show me your cleaning table and your 5 questions" | 5 min |
| Day 46 homework | Steps 3–4: answers and charts | ~100 min |
| Before Day 47 | Step 5: findings, limitations, Restart → Run All | ~30 min |
| Day 47 start | Submission. Optional: 2–3 volunteers show one chart + one finding (2 min each) | 5 min |

Checkpoint 9 takes the first 15 minutes of Day 46, so keep any project check-in for the end of that session.
If you have 90-minute sessions, use the extra 15 minutes on Day 46 as a project clinic.

## Reference answers (default dataset, `PROGRAM = "all"`)

| Item | Value |
|------|-------|
| Raw shape → clean shape | (304, 10) → (298, 10) |
| Duplicates / impossible rows / missing study, sleep | 4 / 2 (S018 attendance 150, S204 study −3) / 8, 6 |
| Medians used for filling | study_hours 8.9, sleep_hours 7.0 |
| Pass rate | 71.1 % |
| Pass rate with / without a job | 50.6 % / 79.9 % |
| Mean final score, 10+ study hours / fewer | 61.8 / 52.4 |
| Mean final score by program | science 57.1, arts 55.6, commerce 55.2 |
| Pass rate, sleep < 6 h | 57.1 % (42 students) |
| Pass rate, attendance < 70 % | 52.8 % (36 students) |
| Job **and** study < 6 h | 21 students, 14.3 % pass |
| Mean `final_score - previous_score` | −8.0 (28.2 % improved) |

Other datasets, for spot checks: `expenses.csv` total 5910.39, rent 33.0 % of spending, card 97 / cash 45 /
transfer 6 transactions. `apartments.csv`: mean price 191.7 k; with parking 195.9 vs without 188.0; mean price by
bedrooms 122.5 / 158.4 / 217.2 / 260.8 / 298.2 for 1–5 bedrooms; ≤ 3 km from the centre 207.0 vs > 10 km 166.5.

Students who clean in a different but well-argued way (e.g. `dropna()`) get different numbers; that is fine if the
cleaning table explains it.

## Common pitfalls

| Pitfall | Symptom | What to ask (not tell) |
|---------|---------|------------------------|
| filter `study_hours >= 0` | 290 rows | "Where did the 8 students with missing study hours go?" |
| cleaning categories without assigning back | `value_counts` still messy | "Print `value_counts()` right after that line. Did it change?" |
| percentages from 0/1 means left as 0.71 | "pass rate is 0.71 %" in text | "What does 0.71 mean as a percentage?" |
| bar chart of a column instead of group means | 298 thin bars | "One bar per what? What should its height be?" |
| charts without labels or units | unreadable chart | "Cover the code. Can I tell what the y-axis counts?" |
| conclusions not tied to numbers | "studying is important" | "How much higher? Which number shows it?" |
| causal language | "having a job **causes** failing" | "Could something else explain this? What would you need to *prove* it?" |
| numbers in text don't match output | edited the code after writing the text | "Restart → Run All, then re-read every number." |
| copying the demo's charts unchanged | 3 charts identical to Day 45 | allowed for one chart; ask for at least two of their own questions |
| `KeyError` after a filter | added a column to `clean` after creating a filtered table | "Which table did you add the column to? Which one are you using?" |

## How to unblock without giving the answer

- Stuck on questions: "Pick one column you find interesting. Who has more of it, and who has less?" That gives a
  `groupby` question immediately.
- Stuck on cleaning: point them to their own Day 45 practice Exercise 2 and Day 42 audit table; do not hand over
  the recipe again.
- Stuck on writing: ask them to *say* the finding out loud to you, then write down exactly what they said, with the
  number.
- Stuck on chart choice: show the "how to choose a chart" table from Day 45 and ask them to point to the row.

## Grading notes

- Grade one report in about 10 minutes: Restart → Run All first (errors cap "Works as specified" at 20/40), then
  read the text sections, then skim the code.
- **Correctness of analysis (15):** a question answered with the wrong filter or group loses the points for that
  question even if the code runs. Watch for `|` vs `&` mistakes and for means of the wrong column.
- **Clarity of charts (13):** −2 per chart missing a title or axis label; −3 for a chart type that does not fit its
  question; at least two chart types required.
- **Written conclusions (12):** findings without numbers score at most half; any causal claim from a correlation
  costs 3 points unless the limitations section addresses it.
- **Data problems handled (15):** for `expenses.csv`/`apartments.csv`, full points require an explicit audit (missing,
  duplicates, ranges, categories) that shows the data is clean, plus at least one sensible derived column.
- **AI assistant use:** generic findings that do not match the student's numbers, or charts nobody in class has
  used (`seaborn`, `fig, ax`), are a cue to ask the student to explain the cell. Grade the explanation.
- The reference notebook is deliberately thorough (6 questions, 4 charts, filter variable). A passing report can be
  much shorter.
