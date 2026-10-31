# Day 37: Data Pipelines

**Week 8 · Session 37 of 60 · Planned 75 min** · Previous: [Day 36](../day-36-csv-json/lesson.md) · Next: [Day 38](../day-38-capstone-planning/lesson.md)

## Objectives

By the end of this lesson students can:

1. Describe a data-processing program as a pipeline of stages (**load → clean → analyse → report**) and say what
   each stage takes in and gives back.
2. Write a cleaning stage that fixes what it can (spaces, capitals) and rejects what it cannot, recording a reason
   and the line number for every rejected row.
3. Test each stage on its own with tiny hand-made data whose answer they can work out in their head.
4. Write a `main()` that reads like the plan and handles a missing input file without crashing.
5. Spot the two classic boundary bugs: a stage that prints instead of returning, and a caller that forgets a stage
   returns two values.

**Prior knowledge:** functions, `return`, defaults (Days 16–18), decomposition (Day 19), `sorted(key=)` (Day 21),
comprehensions (Day 22), files and `Path` (Days 23–24), `try/except ... as error` and `raise` (Day 25), modules and
`__name__` (Day 26), pytest (Day 29), CSV/JSON (Day 36). **No new syntax today.**

**Files:** `demo.ipynb` · `practice.ipynb` · `solutions.ipynb` · `data/grades.csv` (demo, 21 rows, 5 planted
problems) · `data/attendance.csv` (practice, 25 rows) · `grade_pipeline.py` (the demo's code as a script) ·
`test_grade_pipeline.py` (7 pytest tests, one or two per stage). Outputs go to `output/`.

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: Day 36 retrieval | core |
| 0:05–0:12 | The messy file and the pipeline plan | core |
| 0:12–0:17 | Stage 1: load | core |
| 0:17–0:29 | Stage 2: clean, and testing one stage | core |
| 0:29–0:37 | Stage 3: analyse, tested on tiny data | core |
| 0:37–0:43 | Stage 4: report, and `main()` | core |
| 0:43–0:48 | Common mistakes + the script and its tests in the terminal | core |
| 0:48–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (add a stage) | optional (90-min session) |
| +5 min | Break `letter_grade` on purpose and watch exactly one pytest test fail | optional (90-min session) |

**For 60 min:** in demo section 5 show `analyse` already typed and only run the tiny test; skip the terminal part of
section 8. Practice: Exercises 1–4; Exercise 5 becomes homework.

## 1. Warm-up (5 min)

- "What does `csv.DictReader` give you, and what type is every value?" (*A list of dicts if we wrap it in
  `list(...)`; every value is a `str`.*)
- "What is wrong with `json.dump(f, data)`?" (*Data first, then the file.*)
- "Day 19: what makes a good function?" Collect answers: *one job, a name that says the job, takes inputs as
  parameters, returns a result.* Today we use exactly those rules to organise a whole program.

## 2. The messy file and the plan (7 min)

Demo section 1: print `data/grades.csv` and ask students to **spot the problems** before any code. Write them on the
board in two columns:

| Fixable (clean it) | Not fixable (reject it, with a reason) |
|--------------------|-----------------------------------------|
| `" asha khan"`: spaces and lowercase | Bilal's science score is empty |
| `Science`, `MATHS`: inconsistent capitals | Omar's maths score is `absent` |
| | Mei's maths score is `105` |

Key message: **never guess a missing value and never drop a row silently.** A report that quietly ignores three
rows is worse than one that says "3 rows skipped, here is why".

> **Analogy:** a restaurant kitchen. One station washes, one chops, one cooks, one plates. Each station gets
> something from the previous one and hands something on. If the soup is too salty, you know which station to
> visit. A program written as one 80-line block is a kitchen where one cook does everything at once.

Demo section 2 shows the plan as a table (stage, function, takes, gives back). The rules: each stage **returns**,
gets what it needs as **parameters**, does **one** job; only `main()` prints and saves.

## 3. Stage 1: load (5 min)

```python
def load_rows(path):
    """Read a CSV file and return its rows as a list of dicts (all values are text)."""
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
```

Run it: `21 rows` and `{'student': ' asha khan', 'subject': 'english', 'score': '91'}`. Say out loud: "Stage
written, stage checked. Only now do we start the next one."

## 4. Stage 2: clean (12 min)

Build `clean_row(row)` first (demo section 4): strip + `title()` the name, strip + `lower()` the subject, then the
checks in order: empty name, empty score, not a number, out of range. Each unfixable case raises a `ValueError`
with a message a human can act on.

Teaching points:
- `is_number(text)` is a tiny helper because "can this be converted?" is a yes/no question. It keeps the
  `try/except` out of `clean_row`, which then reads like a checklist.
- `clean_row` builds a **new** dict. It never edits `row` (mistake 3 in section 7 shows why).
- Test immediately with tiny rows. **Prediction question:** "What happens with `"absent"`?" (*`ValueError: score
  is not a number: 'absent'`.*) Then the `assert` block, including `is_rejected(row)`: a notebook way of checking
  that an error *is* raised. (In a pytest file we use `pytest.raises`, see `test_grade_pipeline.py`.)

Then `clean_rows(rows)`: loop with `enumerate(rows, start=2)` (line 1 of the file is the header), `try` to clean
each row, `except ValueError as error` collects `f"line {line_number}: {error}"`. It returns **two** things:
`clean, problems`.

**Prediction question:** "21 rows. How many survive?" (*18, with problems on lines 6, 11 and 14.*)

## 5. Stage 3: analyse (8 min)

Demo section 5. `group_scores(clean, column)` is used **twice**: once by student, once by subject. Point out that
a general helper saves writing the same loop twice (Day 16's "why functions" argument again).
`student_average(item)` is the named sort key (Day 21) for ranking `(name, info)` pairs.

The key testing idea: **test with data so small you can do the maths in your head.** Before running the tiny
example, ask: "Ken has 80 and 90, Zara has 60 in maths. Ken's average? Maths average? Ranking?" (*85.0, 70.0,
Ken then Zara.*) Only after the tiny test passes do we run `analyse` on the real data.

## 6. Stage 4: report and `main()` (6 min)

`build_report` **returns a string**. Ask: "Why not print inside it?" (*Because then we could not save it to a
file, test it, or reuse it. The caller decides.*)

`main()` reads like the plan from section 2:

```python
clean, problems = clean_rows(rows)
summary = analyse(clean)
report = build_report(summary, problems)
```

"If you can read `main()` aloud as a sentence, the structure is good." The `data_path=grades_path` default
(Day 18) lets us call `main(Path("data/grades_2027.csv"))` to show the friendly missing-file message.
**Prediction question:** "What will happen with a missing file?" (*The message, not a traceback.*)

## 7. Common mistakes (3 min)

Run the tagged cells in demo section 7:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| A stage prints instead of returning | `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'` | No `return` means the next stage receives `None` |
| `analyse(clean_rows(rows))` | `TypeError: list indices must be integers or slices, not str` | `clean_rows` returns a tuple; unpack it first: `clean, problems = ...` |
| A stage edits its input (`row["student"] = ...`) | no error, but the caller's data changed | Day 07 aliasing: build and return a new dict instead |
| Passing the wrong stage's output (`analyse(rows)` instead of `analyse(clean)`) | `TypeError` from `sum` on strings, or silently wrong numbers | Name variables after the stage (`rows`, `clean`, `summary`) and read `main()` aloud |
| `enumerate(rows)` for line numbers | no error; every line number is off by two | Line 1 is the header and `enumerate` starts at 0 → `start=2` |

## 8. The same pipeline as a script, with tests (2 min)

In the terminal, from the day folder:

```
cd weeks/week-08/day-37-data-pipelines
uv run python grade_pipeline.py      # prints the report, writes output/grade_report.txt + grade_summary.json
uv run pytest -q                     # 7 passed
```

Show `grade_pipeline.py` briefly: the same functions, grouped under `# Stage` comments, and `main()` under
`if __name__ == "__main__":` (Day 26) so the test file can import the stages without running the program.
`DATA_FILE` is written in UPPER_CASE: the Python convention for a setting that is set once and never changed.

Optional (90 min): change `>= 90` to `> 90` in `letter_grade`, rerun pytest, and show that **exactly one** test
fails and its name points straight at the broken stage. Undo the change.

## 9. Practice (22 min)

Students build an attendance pipeline in `practice.ipynb`, one stage per exercise.

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Which stage? | classifying jobs into stages; predicting a cleaning helper | recall |
| 2 Stage 1, load | `DictReader` inside a function, checking the result | application |
| 3 Fix the broken stages | missing `return`, print vs return, adding asserts | modification |
| 4 Stage 2, clean | raising with clear messages, collecting problems with line numbers | application |
| 5 Stages 3 and 4, then `main()` | rates, report string, connecting the stages | problem solving |
| 6 Add a new stage (challenge) | extending a pipeline without editing working stages | challenge |

While circulating, look for:
- functions that print their result "to check it" and then return nothing;
- `clean_record` checking `status not in [...]` *before* checking for an empty status (unhelpful message);
- students who write all stages before running any of them. Ask "which stage have you checked?";
- Ken's 80% in Exercise 5: `<` vs `<=` (the task says *below*).

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

## 10. Recap and exit ticket (5 min)

Recap (students supply):
1. A pipeline is a chain of small stages; each returns its result and takes its input as parameters.
2. Cleaning fixes what it can and rejects the rest **with a reason**.
3. Test every stage alone with tiny data; only `main()` prints and saves.

**Exit ticket:** what is wrong with this `main()`, and what happens when it runs on `grades.csv`?

```python
def main():
    rows = load_rows(DATA_FILE)
    clean, problems = clean_rows(rows)
    summary = analyse(rows)
    print(build_report(summary, problems))
```

Answer: `analyse` receives the **raw** rows instead of `clean`. The scores are still text (and some are `""` or
`"absent"`), so `sum` fails with a `TypeError`. Fix: `analyse(clean)`.

## Homework (25 min)

1. Finish Exercise 5.
2. Capstone preparation: read the [Python Capstone brief](../../../projects/05-python-capstone/README.md) and the
   [plan template](../../../projects/05-python-capstone/PLAN-TEMPLATE.md). Choose an option and write down 5
   things a user should be able to do with your app. Bring them to Day 38.

## Next class

Day 38 starts the **Python Capstone**. Students choose a project, write user stories, decide what the minimum
version (MVP) must do, choose CSV or JSON for its data, and plan modules, functions and a class, exactly the
"stages with clear inputs and outputs" thinking from today, applied to a whole application.

## Instructor notes

- **No new syntax.** If students ask for "a better way", the answer today is *better structure*, not new
  features. Do not introduce classes for the pipeline (a function pipeline is the clearer model here) and do not
  preview pandas.
- **Floats in tests.** `assert summary["class_average"] == 76.67` works because `analyse` rounds. If a student's
  test fails with `76.66666666666667 != 76.67`, that is the lesson: round before comparing, or compare
  `round(value, 2)`.
- **`except ValueError as error`**: `error` holds the exception, and putting it in an f-string gives its message.
  If students have not used `as` much since Day 25, show `print(error)` once.
- **Why `is_number` instead of `try` inside `clean_row`?** Raising a new `ValueError` inside an `except` block makes
  Python print *two* tracebacks ("During handling of the above exception…"), which confuses beginners. The helper
  avoids that. Do not go into exception chaining.
- **Fast students:** Exercise 6, then add a duplicate check to the grade pipeline (what if Sara's maths row appears
  twice?). Which stage should own that decision? (*clean*)
- **Slow students:** give them the shape of `clean_records` (the `enumerate`/`try`/`except` loop) from the demo and
  let them write only `clean_record`. Exercises 2–4 are the core skill for the capstone.
