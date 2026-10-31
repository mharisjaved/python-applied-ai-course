# Day 56: AI Capstone: Choose and Scope

**Week 12 · Session 56 of 60 · Planned 75 min** · Previous: [Day 55](../../week-11/day-55-project-ai-assistant/lesson.md) · Next: [Day 57](../day-57-capstone-core/lesson.md)

## Objectives

By the end of this lesson students can:

1. Choose a capstone option (A–D) and say in one sentence why it fits them.
2. Rewrite a vague idea as a concrete one: user, input, output, and which **one** part uses AI.
3. Write at least three success criteria that contain a number and say how they are measured.
4. Complete a data & privacy check: what data, is any of it personal, and exactly what is sent to the API.
5. Rank their risks, plan a fallback for each, and split features into Must / Should / Could.
6. Get their plan approved with the approval checklist (section 6).

**Prior knowledge:** everything up to Day 55. Directly reused: pandas loading/grouping (Day 44), baselines and
leakage (Days 46, 49), prompt + JSON + mock pipeline (Days 51–54), Python capstone planning (Day 38).

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only) ·
project brief [projects/09-ai-capstone/README.md](../../../projects/09-ai-capstone/README.md) ·
[PLAN-TEMPLATE.md](../../../projects/09-ai-capstone/PLAN-TEMPLATE.md) ·
[INSTRUCTOR.md](../../../projects/09-ai-capstone/INSTRUCTOR.md)

## How Week 12 works

This is a project week. Every session has the same shape: **a short teaching segment (15–25 min)** that shows
one technique on a small example, then **supervised build time** on the student's own capstone, then a
**checkpoint** (something you check before students leave). The demo notebooks never build the student's
project; they show techniques on our worked example, a *Spending Summary Assistant*, which is deliberately not
one of the capstone options.

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: what each AI week gave us | core |
| 0:05–0:15 | The capstone brief and the option menu | core |
| 0:15–0:35 | Scoping live (demo sections 1–7) | core |
| 0:35–0:50 | Practice Exercises 1–3 | core |
| 0:50–1:10 | Own plan: Exercise 5 + PLAN-TEMPLATE, approvals while circulating | core |
| 1:10–1:15 | Recap, exit ticket, approval status | core |
| +15 min | Exercises 4 and 6, then pair review of plans with the checklist | optional (90-min session) |

**60 min:** teach demo sections 1, 3, 4 and 6 only (15 min) and do practice Exercises 1 and 3; plans still get
written in class.

## 1. Warm-up (5 min)

Ask quickly, one student per question:
- "Week 9: what did we learn to do with a messy CSV?" (*Audit it, clean it with pandas, chart it.*)
- "Week 10: why do we compare a model with a baseline?" (*To know whether it learned anything at all.*)
- "Week 11: what does the mock model let us do?" (*Build and test the whole app offline, for free, predictably.*)
- "What made your Python capstone (Week 8) late or hard?" Collect 2–3 answers. They are this week's risks.

## 2. The capstone brief and the option menu (10 min)

Open [the project brief](../../../projects/09-ai-capstone/README.md) on screen. Key messages:
- **Own choice**, but every capstone has the same skeleton: core logic in modules, **≥ 5 pytest tests that run
  offline**, the AI part behind **one function** with a mock/offline mode, error handling, README with a
  "Responsible AI" section, and a **5-minute demo** on Day 60.
- Four sessions of build time. Scope accordingly.

| Option | What you build | AI part | Data | Good fit if… |
|--------|----------------|---------|------|--------------|
| A | ML predictor app (CLI asks inputs → prediction + reasons + confidence) | scikit-learn model trained at start-up | `students.csv`, `apartments.csv`, sklearn toy sets | Week 10 clicked for you |
| B | LLM text tool (notes → quiz, feedback classifier, announcement drafter) | `ask_llm` + JSON validation + mock | `reviews.csv` or your own non-personal text | you liked prompt design |
| C | Constrained FAQ assistant over `campus_faq.md` | keyword retrieval + `ask_llm`, "I don't know" otherwise | `campus_faq.md` | you want the most real-world LLM pattern |
| D | Own idea (approval today) | ML or LLM | must exist **today** | you have a real problem and can scope hard |

How to choose (ask the class): *Which week did you enjoy most? Which data have you already explored? What could
you explain confidently in a 5-minute demo?* Steer weaker students to A or C (clearest structure), and strong
students with a vague D idea to a tight version of B or D.

## 3. Scoping live (20 min)

Run the demo top to bottom. Spend the time on the *thinking*, not the typing.

**Demo section 1, vague → concrete.** Five questions: user, input, output, which part is AI and why, how we know
it works. Write the vague idea on the board ("An AI app that helps students with money") and let students fill
the five answers before showing the dict.
**Prediction question:** "Which line of the concrete idea could you check with `assert`?" (*Output and the plain
Python part; "friendly words" not yet.*)

**Demo section 2, look at the data first.** `expenses.csv` has 148 rows, three months. Ask: "Do we need AI to
know September's food total?" (*No: pandas gives 660.87 exactly.*)
Key design rule for the whole week, write it on the board:

> **Numbers come from your code. The model only adds what code cannot do well.**

**Demo section 3, measurable success criteria.** Show the vague/measurable table. Then the two check functions
`within_word_limit` and `mentions` run on three **hand-written** example outputs (say clearly: these are examples
we wrote, not model output). Expected: `Pass rate: 1/3`.
**Prediction question:** "Which example fails, and which check?" (*The second does not mention food; the third
has 38 words, over the 30 limit.*) Message: a criterion you can write as a function is a criterion you can test.

**Demo section 4, data & privacy check.** The three questions: *what data · is it personal · what leaves the
computer*. Show that sending every row is 2,376 characters (~594 tokens) while the totals are 176 characters
(~44 tokens). Totals are enough, more private, cheaper and faster: **data minimisation**.
Mention that descriptions in real life could be "dinner with Omar" or "pharmacy, flu medicine".

**Demo section 5, risks.** Likelihood × impact (1–3 each), sorted with `key=risk_score` (Day 21). The two
risks every LLM capstone shares: *no network/key during the demo* and *invalid model output*. Both get a plan
today.

**Demo section 6, MVP and time budget.** Must + Should = 350 min, available = 340 min.
**Prediction question:** "Does it fit?" (*No.*) Must only = 270 min, 21 % spare. Rule of thumb: Musts fill at most
about 80 % of the time.

**Demo section 7, a plan the data cannot support.** `expenses["merchant"]` → `KeyError`. "Tips per shop" was
impossible. One minute today vs. a failed project on Day 59.

## 4. Common scoping mistakes

| Mistake | What goes wrong | How to explain it |
|---------|-----------------|-------------------|
| "The AI calculates the totals / scores" | wrong sums, untestable | code calculates, the model words or predicts |
| "Success = it works" | nothing to show on Day 60 | a number + how it is measured |
| Using classmates' real data, scraped data or private chats | privacy problem, no permission | synthetic, public, or your own non-sensitive data |
| "I'll build a website / train a neural network / deploy it" | out of scope, will not finish | CLI + scikit-learn or `ask_llm` |
| Promising a feature before opening the data | `KeyError` on Day 59 | open the data today, in the first 10 minutes |
| AI spread across the whole program | cannot test or run offline | AI behind **one** function (Day 57–58) |
| Ten Musts | nothing finished | at most 5 Musts |

## 5. Practice (15 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Vague or concrete? | judging scope | recall |
| 2 Turn success criteria into checks | criteria as functions, pass rate | application |
| 3 Data & privacy check | minimal payload, personal data | application |
| 4 Risk register | scoring and sorting risks | application (optional) |
| 5 Your capstone plan in a dict | own plan, first draft | independent |
| 6 Plan checker (challenge) | validating a plan automatically | challenge |

Walk around and look for:
- Exercise 2: `is_question` failing on the last question because of trailing spaces (needs `.strip()`).
- Exercise 3: `del record["name"]`, which changes the original data. Ask "what if the app needs the name later?"
- Exercise 3 question 3: students who think a student ID is "anonymous". It still identifies a person.

## 6. Own plan and approval checkpoint (20 min)

Students copy [PLAN-TEMPLATE.md](../../../projects/09-ai-capstone/PLAN-TEMPLATE.md) into their own capstone
folder (see Homework) and fill it, starting from their Exercise 5 dict. Circulate and approve plans one by one
(2–3 min each). Use this **approval checklist**; a plan is approved when every box is ticked:

- [ ] Problem statement names a user and a situation (1–2 sentences).
- [ ] An example run is written out: what the user types, what the app prints.
- [ ] The AI part is **one** clear job behind one function; everything else is plain Python.
- [ ] The data exists, the student has opened it today, and it has what the plan needs.
- [ ] Privacy: no real personal data of other people; the plan lists exactly what is sent to the API.
- [ ] ≥ 3 measurable success criteria, including "≥ 5 pytest tests pass offline".
- [ ] Offline plan: a mock (LLM options) or a local model (option A), so the demo works without internet.
- [ ] Top 3 risks, each with a fallback.
- [ ] Must list fits in about 80 % of the time; Should/Could are separate.
- [ ] Nothing out of scope (web apps, GUIs, neural-network training, scraping, deployment).

Option D plans need extra care: if a D plan is not approvable by the end of the session, the student switches
to the closest option (A, B or C) with their own twist. Say this rule **at the start** of the segment.

## 7. Recap and exit ticket (5 min)

Recap (ask students to supply them):
1. Concrete = user, input, output, one AI job, success criteria with numbers.
2. Look at the data before promising features. Numbers come from code.
3. Privacy check: send the minimum. Plan the offline fallback today.

**Exit ticket:** "Rewrite this criterion so it is measurable: *The quiz questions are good.*"

Possible answer: *"For 5 test paragraphs, at least 4 produce exactly 5 questions that each end with '?' and
are ≤ 25 words, checked by a script."* Accept anything with a number and a way to measure it.

Before students leave, record each student's status: **approved / approved with changes / not yet**. "Not yet"
students send the revised plan before Day 57.

## Homework (30–40 min)

1. Finish `PLAN.md` (from the template) and get it approved (in person or by message) before Day 57.
2. Set up the capstone folder inside your course workspace (the uv project with pandas, scikit-learn, anthropic
   and python-dotenv already added), e.g. `capstone/` with an empty `README.md` and your `PLAN.md`.
3. Open your data (or 5 sample texts for option B) in a notebook and confirm it has what your plan needs.
4. LLM options: copy your `llm.py` from Project 08 into the folder (or write it from the Day 53 pattern).

## Next class

Day 57 builds the **non-AI core first**: data loading and logic in modules, pytest tests, and a stub for the AI
function so the whole app runs end to end without any model. Today's success-criteria functions become tests.

## Instructor notes

- Approve **scope**, not ambition. The most common capstone failure is a plan that needs 10 sessions. Cut until
  the Must list is boring; the AI part makes it interesting enough.
- Real personal data is a hard no, even "just my friends' messages". Offer synthetic data or `reviews.csv`.
- Students without an API key lose nothing: every option must run with the mock, and grading never requires
  the real API. Say this explicitly; some students worry about cost.
- Do not teach new libraries this week (no Streamlit, Flask, LangChain, vector databases, embeddings). If asked:
  "a good extension after the course; for the capstone, keyword retrieval and a CLI are enough".
- Fast students: Exercise 6, then help a neighbour with the approval checklist. Slow students: Exercises 1 and
  3, then go straight to the plan; Exercise 5 is the important one.
- Keep your approval notes (see INSTRUCTOR.md); Day 60 grading checks the final app against the approved plan.
