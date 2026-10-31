# Day 60: Final Presentations, Assessment and Next Steps

**Week 12 · Session 60 of 60 · Planned 75 min** · Previous: [Day 59](../day-59-capstone-reliability/lesson.md) · Next: none, this is the last session

> **Date note:** Day 60 falls on 1 January in the planned calendar, which is likely a holiday. Move it to the next
> available session and record the actual date in `PROGRESS.md`. If you need two sessions (see Timing), use the
> next two.

## Objectives

By the end of this session students can:

1. Present their AI capstone in 5 minutes: problem, live run (including one handled failure), how the AI part
   works, limitations.
2. Answer questions about their own design decisions: why this data, why this check, what is sent to the API.
3. Give specific, kind peer feedback ("two stars and a wish").
4. Show what they learned in Weeks 9–12 in the final assessment.
5. Choose one learning path for after the course.

**Prior knowledge:** the whole course; directly Days 56–59 and the capstone brief.

**Files:** `demo.ipynb` (your toolkit: running order, feedback summary, learning path) · `practice.ipynb`
(final review, best given as homework after Day 59) · `solutions.ipynb` ·
[final assessment](../../../assessments/final/ai-final-assessment.md) ·
[capstone brief and rubric](../../../projects/09-ai-capstone/README.md) ·
[INSTRUCTOR.md](../../../projects/09-ai-capstone/INSTRUCTOR.md)

## Timing

The timing depends on class size. Each presentation takes **7 minutes** (5 demo + 2 questions/changeover).

**Plan A: up to 6 students, one 75-min session**

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:03 | Set-up: running order (demo section 1), feedback forms out | core |
| 0:03–0:45 | Presentations, 6 × 7 min, peer feedback during each | core |
| 0:45–1:15 | Final assessment, short version (30 min: Sections B–D) | core |
| +15 min | Course feedback form (10 min) + celebration and next steps (5 min) | optional (90-min session) |

**Plan B: 7 or more students, two sessions**

| Session | Content |
|---------|---------|
| 60a (75 min) | up to 10 presentations (70 min) + 5 min for the course feedback form |
| 60b (75 min) | final assessment, full version (45 min) · learning paths (demo section 4) · celebration |

**60 min (Plan A):** presentations only; give the assessment at the start of an extra session or, if that is
impossible, as a supervised 30-minute block the following day. Do not give it as unsupervised homework.

## 1. Before students arrive

- Laptops charged; each student has their app open in a terminal **and** has run `uv run pytest -q` once.
- A spare laptop with the course repository, in case a student's machine fails (they can run from a USB copy).
- Print or share the peer feedback form (section 4) and the assessment (one copy per student).
- Decide whether the projector machine has internet. If not, announce: *"Today everyone demos offline, with the
  mock or a local model."* That is fully acceptable; the rubric never requires the real API.

## 2. Presentation format (tell students at the start)

Five minutes, timed, then two minutes of questions. Suggested structure (from the Day 59 demo script):

| Time | Content |
|------|---------|
| 0:00–0:30 | the problem and the user |
| 0:30–3:00 | live run: one normal case, one edge case, **one failure handled on purpose** |
| 3:00–4:00 | how it works: the one AI function, one test |
| 4:00–5:00 | limitations, privacy/bias, what next |

Rules: the mode (online / offline mock / local model) is visible on screen; if something fails, switch to the
backup (`COURSE_OFFLINE=1`, then the README transcript) without apologising for long. A recovered failure
counts *for* a student, not against them.

Run the running order cell in demo section 1 (replace the names with your class list; the seed makes it fair
and repeatable). Keep strict time with a visible timer; give a 1-minute warning.

## 3. Questions to ask (pick 1–2 per student)

Choose questions that check understanding of **their own** code (the "Explanation" rubric row, 15 points):

- "Show me the one function where your app talks to the AI. What happens if the reply is not valid JSON?"
- "What exactly is sent to the API? Is any of it personal?"
- "Which test are you proudest of? What would break if you deleted it?"
- Option A: "What is your baseline, and by how much do you beat it? Which feature did you leave out, and why?"
- Option B: "How did you check your success criterion? What did you measure, and with which model or mock?"
- Option C: "What does the app do when no FAQ section matches? How do you know an answer came from the FAQ?"
- "Tell me one input that still breaks your app or gives a bad answer."
- "If you had two more weeks, what would you change first?"

A student who cannot explain their code (for example because an AI assistant wrote it) scores low on
"Explanation" whatever the app does. Ask a follow-up about a specific line before deciding.

**Common presentation mistakes** (mention them before the first presenter starts):

| Mistake | What happens | Better |
|---------|--------------|--------|
| Reading code line by line | the audience is lost by minute 2 | show the one AI function and one test only |
| Only the happy path | looks fragile, wastes the best minute | include one handled failure on purpose |
| Hiding the mode | audience thinks mock output is the real model | mode printed at start-up |
| No limitations | sounds like overclaiming | one specific limitation, one privacy/bias point |
| Running over time | the next student loses time | rehearsed script, stop at 5:00 |

## 4. Peer feedback (during presentations)

Each listener fills one row per presenter. Collect the forms and give each student their own rows afterwards
(anonymous). Demo section 2 shows how to summarise the scores.

| Presenter | Clear (1–5) | Works (1–5) | Responsible AI (1–5) | ⭐ Star 1 | ⭐ Star 2 | 💡 Wish |
|-----------|-------------|-------------|----------------------|----------|----------|---------|
| | | | | | | |

Rules for comments: specific (*"the fallback when the model refused was smooth"*, not *"nice"*), about the work
not the person, and the wish is something they could actually do next.

## 5. Final assessment (30 or 45 min)

[assessments/final/ai-final-assessment.md](../../../assessments/final/ai-final-assessment.md): 15 questions,
50 points, Sections A (Python and data, retrieval), B (ML), C (LLM apps), D (capstone and responsible AI). Short
version: Sections B–D, 38 points, 30 minutes. Paper or a fresh notebook, no internet, no AI assistants.

**Final review practice** (`practice.ipynb`, best as homework after Day 59; same style, different questions):

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the pandas output | filtering, groupby, value_counts | recall |
| 2 Find and fix the experiment | leakage, train/test split, baseline | modification |
| 3 Read a confusion matrix | accuracy, precision, recall, which error matters | application |
| 4 Validate a model's JSON reply | `json.loads` + field checks | application |
| 5 One AI function, a fallback and a fake | boundary, fallback, fake-model tests | independent |
| 6 Explain a model in plain words (challenge) | coefficients as sentences | challenge |

Before handing it out: phones away, explain that partial credit is given for reasoning, and that "explain"
questions are marked on ideas, not wording. Collect at the exact end time. The answer key and bands are in
the file.

## 6. Course feedback form

Give 10 minutes (anonymous, on paper or an online form you create). Questions:

1. Overall, how useful was this course for you? (1–5)
2. The pace in Weeks 1–8 (Python) was: too slow / about right / too fast.
3. The pace in Weeks 9–12 (AI) was: too slow / about right / too fast.
4. Which week or topic helped you most? Why?
5. Which topic was hardest to understand? What would have helped?
6. The balance of explanation and practice in a lesson was: too much talk / about right / too little explanation.
7. How useful were the demo notebooks, practice notebooks and projects? (1–5 each)
8. Did you use the real API or only the mock? Was that a problem?
9. How confident are you now to write a small Python program on your own? (1–5) An AI app? (1–5)
10. One thing to keep, one thing to change, one thing to add.

Read the answers within a week and write the three biggest changes into `PROGRESS.md` for the next run.

## 7. Celebration and next steps (5–10 min)

Run demo section 3 ("the journey") on the projector: from `city = "Lahore"` on Day 02 to apps that train or call a
model behind one function, test themselves offline and explain their limits. Name one specific strength you saw
in each presentation.

Then demo section 4, the learning paths: **data analysis**, **machine learning**, **LLM applications**,
**software engineering**. Advice: pick one path, build one project in the next 2–3 months, publish it with a good
README. Portfolio checklist: every capstone in its own repository, tests passing, README with an offline run,
no `.env` committed.

**Exit ticket** (on the back of the feedback form): *"The path I choose is … and my first project will be …"*
There is no right answer; read them, and reply to any student who asks for a resource.

## 8. Grading the capstone

Grade with the rubric in the [capstone brief](../../../projects/09-ai-capstone/README.md) (shared 100-point rubric
plus capstone-specific checks). Notes for consistency are in
[INSTRUCTOR.md](../../../projects/09-ai-capstone/INSTRUCTOR.md). In short: run `uv run pytest -q` and the app
**offline** yourself; compare with the approved plan from Day 56; the presentation feeds the "Explanation/demo" row.
Return grades with two specific comments (one strength, one next step).

## Homework

None required. Optional: publish the capstone (repository + README), and write a short post about what you built.

## Instructor notes

- Nervous students: offer to go early (less waiting) or to present with the demo already running. Never force a
  live online demo; offline is a first-class option.
- If a demo crashes, give the student 30 seconds to switch to the backup, then move on and let them show it
  at the end. Grade the recovered version.
- Keep questions friendly and specific. The goal is to see that they understand their decisions, not to catch
  them out.
- Do not discuss assessment answers until everyone has finished (Plan B: until after session 60b).
- Practice notebook: assign it after Day 59 as revision; it uses the same style as the assessment with
  different questions. Fast finishers of the assessment can start the feedback form.
