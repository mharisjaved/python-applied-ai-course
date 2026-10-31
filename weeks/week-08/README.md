# Week 8: Consolidation and Python Capstone

**Goal:** students learn the two file formats every later week relies on (CSV and JSON) and combine everything from
Weeks 1–8 into data pipelines of small, tested functions. Then they plan, build and present their own application,
the Python Capstone, and take the Python readiness assessment that decides the support each student gets in the
AI phase.

| Day | Topic | Lesson | Demo | Practice | Solutions |
|-----|-------|--------|------|----------|-----------|
| 36 | CSV and JSON | [lesson](day-36-csv-json/lesson.md) | [demo](day-36-csv-json/demo.ipynb) | [practice](day-36-csv-json/practice.ipynb) | [solutions](day-36-csv-json/solutions.ipynb) |
| 37 | Data pipelines (load → clean → analyse → report) | [lesson](day-37-data-pipelines/lesson.md) | [demo](day-37-data-pipelines/demo.ipynb) | [practice](day-37-data-pipelines/practice.ipynb) | [solutions](day-37-data-pipelines/solutions.ipynb) |
| 38 | 🎓 Capstone: plan and structure | [lesson](day-38-capstone-planning/lesson.md) | [demo](day-38-capstone-planning/demo.ipynb) | [practice](day-38-capstone-planning/practice.ipynb) | [solutions](day-38-capstone-planning/solutions.ipynb) |
| 39 | 🎓 Capstone: build, debug and test | [lesson](day-39-capstone-build/lesson.md) | [demo](day-39-capstone-build/demo.ipynb) | [practice](day-39-capstone-build/practice.ipynb) | [solutions](day-39-capstone-build/solutions.ipynb) |
| 40 | 🎓 Presentations + readiness assessment | [lesson](day-40-capstone-demo/lesson.md) | [demo](day-40-capstone-demo/demo.ipynb) | [practice](day-40-capstone-demo/practice.ipynb) | [solutions](day-40-capstone-demo/solutions.ipynb) |

**Assessment:** [Python readiness assessment](../../assessments/final/python-readiness.md) (Day 40, 50 min; replaces
the weekly checkpoint) · **Project:** [05 Python Capstone](../../projects/05-python-capstone/README.md)
([plan template](../../projects/05-python-capstone/PLAN-TEMPLATE.md),
[instructor notes](../../projects/05-python-capstone/INSTRUCTOR.md)), code due at the start of Day 40.

Supporting files: `day-36-csv-json/data/purchases.csv` (quoted commas) · `day-37-data-pipelines/data/grades.csv` and
`data/attendance.csv` (messy on purpose) · `day-37-data-pipelines/grade_pipeline.py` + `test_grade_pipeline.py`.
Notebooks write their output into an `output/` folder inside the day folder (safe to delete).

## Prepare before the week

- [ ] Mark Project 04 so students get feedback before planning their capstone.
- [ ] Run `uv run python grade_pipeline.py` and `uv run pytest -q` in `day-37-data-pipelines` (7 passed).
- [ ] Run `uv run pytest -q` in `projects/05-python-capstone/reference` (23 passed) and try its menu in a copy of the
      folder, including bad input. Read the reference `README.md`: you will show it as the model README on Day 39.
- [ ] Print the plan template (one per student) and decide how plans are approved (paper initials or a shared doc).
- [ ] **Decide the Day 40 timing** (assessment 50 min + ~8 min per presenter; see the Day 40 lesson) and, if
      needed, book an overflow slot for presentations. Tell students on Day 38.
- [ ] Print the student part of the readiness assessment (above the answer key); check that every student can
      reach `datasets/expenses.csv` for section F.

## Common difficulties this week

| Difficulty | How to respond |
|------------|----------------|
| Treating CSV values as numbers (`TypeError: ... 'int' and 'str'`) | "What type does `DictReader` give you?" Convert once, in the load or clean stage. |
| `json.dump` vs `json.dumps`, argument order | Board table: *the s means string*; `dump(data, file)`, data first. |
| Functions that print instead of return, so the next stage gets `None` | Day 37 rule: stages return; only `main()` prints and saves. |
| Capstone scope too big | Approve "with cuts": MVP = 3–5 Must stories including saving. Could features only after tests pass. |
| Students stuck alone on Day 39 | Unblocking questions in the capstone INSTRUCTOR.md; toolbox exercises in Day 39 practice; never type in their files. |
