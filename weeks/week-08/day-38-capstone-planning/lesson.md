# Day 38: Python Capstone, Plan and Structure

**Week 8 · Session 38 of 60 · Planned 75 min** · Previous: [Day 37](../day-37-data-pipelines/lesson.md) · Next: [Day 39](../day-39-capstone-build/lesson.md)

## Objectives

By the end of this lesson students can:

1. Turn a vague idea into a problem statement that names a user, a problem and how the app helps.
2. Write 5–8 user stories (*As a … I want … so that …*) and separate the **MVP** (Must) from Should / Could / Won't.
3. Choose CSV or JSON by writing one real data record, and decide what happens when the file is missing.
4. Derive classes, methods, functions and modules from the stories (nouns → classes, verbs → methods).
5. Leave with an **approved plan** and a **walking skeleton**: a uv project whose menu runs and whose one test passes.

**Prior knowledge:** everything from Days 01–37, in particular classes and composition (Days 32–34), modules and
`__name__` (Day 26), uv projects (Day 27), pytest (Day 29), CSV/JSON (Day 36), pipelines (Day 37).
**New today:** the keyword `pass` (an empty placeholder body) and the planning vocabulary: user story, MVP,
walking skeleton.

**Files:** `demo.ipynb` (planning a sample *Recipe Box*) · `practice.ipynb` · `solutions.ipynb` ·
[capstone brief](../../../projects/05-python-capstone/README.md) ·
[plan template](../../../projects/05-python-capstone/PLAN-TEMPLATE.md) ·
[instructor notes](../../../projects/05-python-capstone/INSTRUCTOR.md) (plan approval questions).

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: the tools you now have | core |
| 0:05–0:12 | The capstone brief: options, Musts, rubric, schedule | core |
| 0:12–0:20 | Idea → problem statement → user stories → MVP (demo 1–2) | core |
| 0:20–0:28 | Data format; nouns → classes; modules (demo 3–4) | core |
| 0:28–0:35 | Walking skeleton and test-first (demo 5–6) | core |
| 0:35–0:62 | Students plan (practice 1–4 → `PLAN.md`); you approve plans | core |
| 0:62–0:72 | Walking skeleton in a uv project (practice 5) | core |
| 0:72–0:75 | Exit ticket | core |
| +15 min | Practice 6 (test first) while you finish approvals | optional (90-min session) |

**For 60 min:** skip demo section 6 (mention it in one sentence), students do only Exercise 1 of 1–3 and go straight
to Exercise 4 and `PLAN.md`. The skeleton becomes homework.

## 1. Warm-up (5 min)

- "Yesterday's pipeline had four stages. Name them, and the rule every stage follows." (*load, clean, analyse,
  report; takes parameters, returns a result, one job.*)
- "Name every tool we have for organising a program." Collect on the board: **functions, modules, classes, files
  (CSV/JSON), exceptions, tests.** Then say: "Your capstone uses *all* of them. That list is the Must list."

## 2. The capstone brief (7 min)

Project the [brief](../../../projects/05-python-capstone/README.md). Walk through, briefly:
- the six options (one sentence each) and the "too big / too small" line;
- the 9 Musts. Point at the board list from the warm-up;
- the rubric: 40 points for "works", and the MVP comes from **their own** approved plan;
- the schedule: plan + skeleton today, build tomorrow, ~90 min homework, demo and assessment on Day 40.

Say explicitly: there is **no starter code**; homework is part of the plan; it is an **individual** project.

## 3. From idea to stories and MVP (8 min)

Demo section 1. **Intuition:** "an app for my recipes" cannot be built because it does not say *whose* problem or
*what* the app should do. A problem statement names **a person, a problem, how the app helps**. Every later
decision is checked against it.

Demo section 2: the stories as a list of dicts. Explain the template: *As a … I want … so that …*. The "so that"
is what stops us building features nobody needs.

**Prediction question:** "How many stories are in the MVP?" (*4. Saving is one of them.*)

Key points:
- **MVP** = the smallest version that is already useful. Ask: "If you only had tomorrow, what must it do?"
- Saving is always a Must. An app that forgets everything is a demo, not a tool.
- Writing **Won't** items down (photos) ends discussions and protects the schedule.

## 4. Data format, classes and modules (8 min)

Demo section 3: write **one record** before choosing a format. The pancakes recipe has a *list* of ingredients.
Write it with `DictWriter`, read it back. **Prediction question:** "What type is `ingredients` now?" (*`str`.
The list became the text `"['flour', 'eggs', 'milk']"`.*) JSON keeps the list → decision: `recipes.json`.

Demo section 4: underline nouns and verbs in the Must stories.
- A noun with data **and rules** becomes a class (`Recipe`: a name cannot be empty, servings ≥ 1).
- A noun that is just a value stays a value (an ingredient is a `str`).
- Verbs become methods (`add_ingredient`, `uses`) or functions over many objects (`find_by_ingredient`).
- `to_dict()` is the bridge to JSON. Remind them of Day 36: JSON cannot save objects, only dicts/lists/str/numbers.

Then the module table: `models.py` (data + rules), `storage.py` (files), `search.py` (questions about the data:
no `input`, no `print`), `main.py` (talks to the user). Same idea as yesterday's stages.

## 5. Walking skeleton and test first (7 min)

Demo section 5. **Analogy:** builders put up the whole frame of a house before finishing any room. A *walking
skeleton* is the whole program with nothing finished: every module and menu option exists and runs, but only
prints `TODO`. From then on every step is "replace one TODO, run, test", and the program is never broken for long.

Introduce **`pass`**: a function body cannot be empty, and `pass` means "do nothing for now".

`handle_choice` returns a message instead of calling `input()`, so the notebook can try it with a list of choices.
**Prediction question:** the four messages for `"1"`, `"3"`, `"9"`, `"0"`.

Demo section 6: write `test_find_by_ingredient()` while `find_by_ingredient` is still a stub → `AssertionError`
(red). Implement it with a comprehension → the test passes (green). The test was written from the *plan*, before
the code.

## 6. Common planning mistakes

| Mistake | Symptom on Day 39 | How to explain it |
|---------|-------------------|-------------------|
| MVP too big (8 Musts, a second and third class) | Nothing works by the deadline | "Which 3–5 stories make it useful?" Cut the rest to Should/Could |
| Saving left for "later" | Data lost on restart; storage rushed on the last evening | Saving is a Must story; build-plan step 4 |
| Stories without a user or a reason ("Add delete button") | Features nobody needs, unclear demo | Rewrite with *As a … I want … so that …* |
| Format chosen without a record | Lists stuffed into CSV cells, as in demo section 3 | "Write one record exactly as it will be in the file" |
| A class with no rules (just a dict with methods that print) | Fails the class Must; nothing to test | "What must your class *refuse*?" That becomes a `raise ValueError` |
| `input()` and `print()` inside logic functions | Nothing can be tested | Logic returns values; only `main.py` talks to the user |
| No test ideas | Tests written in a panic at the end | Plan section 7: normal, edge and error case per function |

## 7. Students plan (27 min)

Students open `practice.ipynb`. Exercises 1–3 are **quick** practice on sample projects (≈ 10 min in total; push
students on); Exercise 4 produces their own stories, MVP and data record, which they copy into `PLAN.md`
(a copy of `projects/05-python-capstone/PLAN-TEMPLATE.md` saved in their project folder).

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 MVP or not? (Habit Tracker) | separating MVP from extras | recall |
| 2 Nouns, verbs and a class (Library) | stories → class with validation | application |
| 3 Which format? | choosing CSV/JSON and proving the round trip | application |
| 4 Your plan, part 1 | own stories, MVP, data record | problem solving |
| 5 Your walking skeleton menu | own `handle_choice` + asserts | application |
| 6 Test first (challenge) | stub → failing test → implementation | challenge |

**Approving plans.** While students work, call them up one at a time (2–3 minutes each) with their `PLAN.md`
sections 1–6 filled in. Use the approval checklist at the bottom of the template and the questions in
[INSTRUCTOR.md](../../../projects/05-python-capstone/INSTRUCTOR.md). Initial and date the plan. Typical fixes:
cut the MVP, add saving to the MVP, add a rule to the class, write a concrete data record.

While circulating, look for: students choosing an option they cannot describe in one sentence (offer (b) or (d)
as safe defaults), stories that are really features without a user, and students who start coding before
section 5 (data) of the plan exists.

## 8. Walking skeleton in a uv project (10 min)

In the terminal, **next to** (not inside) their course project folder:

```
uv init my-capstone
cd my-capstone
uv add pytest
```

(If someone must create it inside another uv project, use `uv init --no-workspace my-capstone`; otherwise uv adds
it to the outer project.) Then:
1. Replace the generated `main.py` with a menu `MENU`, `main()` looping over `input()`, and the
   `if __name__ == "__main__":` guard. Exercise 5's `handle_choice` (or one function per option) goes in here.
2. Create the other modules from the plan with a module docstring and stub functions (docstring + `pass` or a
   placeholder `return`).
3. Create `test_models.py` with **one** trivial test, e.g. that the class stores its name.
4. Run `uv run python main.py` (menu appears, `0` quits) and `uv run pytest -q` (`1 passed`).

## 9. Exit ticket (3 min)

Each student writes on paper (or in chat): **their MVP in one sentence and their data file's name and format.**

Example answer: *"Habit Tracker: add habits, tick them off today and see today's checklist; saved in
`habits.json` (JSON, because each habit has a list of dates)."*
Check: does it include saving? Is the format justified?

## Homework (30 min)

1. Finish the walking skeleton if it does not run yet, and get the plan approved (by message if needed).
2. Write your class's `__init__` and `__str__` and one method that refuses invalid values, with two tests.
3. Read build-plan steps 3–4 in the brief.

## Next class

Day 39 is a **build session**: a short mini-lesson on building in small steps, finding bugs with tests, refactoring
a long function and validating input, then a long block of building with a mid-session peer code review. Target by
the end of Day 39: your class is tested and your data survives a restart (build-plan step 4).

## Instructor notes

- **Approvals are the bottleneck.** Approve in the order hands go up, keep it to 2–3 minutes, and approve "with
  changes" rather than asking for a rewrite. Students waiting for approval build the skeleton, which is the same
  for every option.
- **Do not** teach git today. If students already use it, encourage one commit per working step; otherwise they
  can copy their project folder at the end of each session as a checkpoint.
- **Individual work.** Two students may choose the same option, but each plans and writes their own code.
- **Own ideas (option f):** insist on a concrete data record and a class with a rule before approving. "Can you
  show me one line of your data file?" settles most vague ideas.
- **Out of scope:** GUIs, web apps, databases, logins/passwords, internet access. Redirect to the console version
  of the idea.
- **Fast students:** Exercise 6, then start build-plan step 3 (the class with tests) today.
- **Slow students:** offer option (b) or (d) with the MVP from the brief's table; their job today is a skeleton
  that runs and a plan with saving in the MVP.
