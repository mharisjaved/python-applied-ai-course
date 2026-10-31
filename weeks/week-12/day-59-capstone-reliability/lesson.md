# Day 59: AI Capstone: Reliability, Responsible AI and Demo Prep

**Week 12 · Session 59 of 60 · Planned 75 min** · Previous: [Day 58](../day-58-capstone-ai-integration/lesson.md) · Next: [Day 60](../day-60-final-presentations/lesson.md)

## Objectives

By the end of this lesson students can:

1. Build a failure-case table for their app (input/situation · what happens now · what should happen) and
   turn its rows into tests.
2. Add at least one hallucination check in code: numbers must come from the data, or answers must quote a real
   source section.
3. Protect privacy: send the minimum, redact contact details, and state what redaction misses.
4. Ask bias questions about their data and run a counterfactual probe (change one thing that should not matter).
5. Write a README with run instructions (offline and online), evaluation results and a Responsible AI section.
6. Write and rehearse a 5-minute demo script with an offline backup plan.

**Prior knowledge:** bias and limitations (Day 41), data quality (Day 42), pandas `groupby` (Day 44), leakage
(Day 49), hallucination (Day 52), keys and `.env` (Day 53), validation and mocks (Day 54), Days 56–58.

**Files:** `demo.ipynb` · `practice.ipynb` · `solutions.ipynb` · option C reference (uses the quote check):
[projects/09-ai-capstone/reference/option-c-faq-assistant](../../../projects/09-ai-capstone/reference/option-c-faq-assistant/)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: "what would break your app?" | core |
| 0:05–0:28 | Teaching: demo sections 1–8 | core |
| 0:28–0:43 | Practice Exercises 1–3 | core |
| 0:43–1:08 | Build time: own failure table, checks, README, demo script (Exercise 5) | core |
| 1:08–1:15 | Demo rehearsal in pairs (timed) + checkpoint | core |
| +15 min | Exercises 4 and 6; a second rehearsal with Wi-Fi off | optional (90-min session) |

**60 min:** teach demo sections 1, 2 (or 3 for option C), 4 and 8 (15 min); practice Exercises 1 and 2; keep the
rehearsal.

## 1. Warm-up (5 min)

Ask every student to write down, in 60 seconds, **three ways their app could fail during the demo**. Collect a
few aloud. Expect: no Wi-Fi, typing nonsense, empty input, the model saying something wrong, a crash on a file
path. Today turns that list into a table, tests and fallbacks.

## 2. Teaching: reliability and responsible AI (23 min)

**Failure-case table (demo section 1).** Run `summarise_month` on six inputs.
**Prediction question:** "What does pressing Enter (empty input) do?" (*It summarises all 148 expenses, because
every date starts with the empty string.*) This bug exists in the Day 57 and Day 58 `example_app` versions, on
purpose; nobody tried it until now. Fix: `is_valid_month` + `.strip()`. Every row of the table becomes a test.

**Hallucination check 1: numbers (demo section 2).** The prompt said "only use numbers that appear above"; code
checks it. `numbers_in` uses `try/except` around `float()`; `invented_numbers` compares with the totals.
**Prediction question:** which numbers are flagged in the invented summary? (*`12.0` from "12%" and `700.0`.*)
Apply it to the summary only; tips are advice, not claims about the data. If the check fails → template fallback.

**Hallucination check 2: quotes (demo section 3).** For Q&A over documents (option C): ask for a
`section_id` **and** a short quote; check the quote appears in that section.
**Prediction question:** which replies pass? (*Only the first: the second invented "8", the third cited `S07`,
which was never sent.*) "We cannot check meaning, but we can check that the evidence exists."

**Privacy (demo section 4).** First rule: don't send what you don't need (Day 56). Second rule: redact contact
details from user text. Run `redact` on review R33, then on *"I'm Jo Smith, call 555 0142"*.
**Prediction question:** what does it miss? (*The name, and the number written with a space.*) Redaction reduces
risk; it is not a guarantee. That belongs in the README.

**Bias (demo section 5).** Two questions for every project: *who is in the data and who is missing?* and *does the
output change for a reason that should not matter?* In `students.csv`, students with a job pass less often
(0.51 vs 0.80). A model trained with `has_job` gives two students with identical habits **77 % vs 42 %**.
Discuss: true in the data, but fair to act on? This is why the option A reference uses only changeable habits.
For LLM apps: swap names/pronouns in test inputs and compare outputs.

**Offline switch (demo section 6).** `COURSE_OFFLINE=1` forces the mock. Show the one-line commands for
macOS/Linux and PowerShell. Every app prints its mode at start-up.

**README and demo script (demo section 8).** Show the README headings and the 5-minute script table. Stress
the backup plan line and "one failure handled on purpose" in the live run: it is the most convincing 20 seconds
of any demo.

## 3. Common mistakes

| Mistake | Symptom | How to explain it |
|---------|---------|-------------------|
| Only the happy path tested | demo crashes on Enter or a typo | the failure table finds what nobody tries |
| `float(word)` without `try` (demo section 7) | `ValueError: could not convert string to float` | text is messy; skip what is not a number |
| Trusting the prompt's rules | invented numbers or sources slip through | instructions are requests; checks are code |
| "It's anonymised" because names were removed | IDs, phone numbers, unique details remain | minimise first, redact second, warn users |
| "The data says so, so it's fair" | a group is penalised for something irrelevant | counterfactual probe; remove or justify the feature |
| Limitations written as "may have bugs" | says nothing | specific: what fails, when, measured how |
| Demo needs Wi-Fi | demo fails live | rehearse offline; command written in the script |
| `changed = student` in a probe | original dict modified (Day 07 aliasing) | `student.copy()` makes a copy |

## 4. Practice (15 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 A failure-case table | finding and fixing silent and loud failures | application |
| 2 Redact contact details | privacy helper | application |
| 3 Are the numbers in the answer supported? | hallucination check, false alarms | application |
| 4 A counterfactual bias probe | testing a black box for bias | analysis |
| 5 Your README's Responsible AI section and demo script | own project writing | independent |
| 6 An automatic failure table (challenge) | a mini test harness | challenge |

Look for: Exercise 1 students who do not see why `"9, 1"` → `5.0` is the most dangerous case (silently wrong);
Exercise 3 students surprised that a correct answer is flagged (discuss false alarms as acceptable);
Exercise 4 `changed = student` without a copy.

## 5. Build time (25 min)

Each student, on their own project:
1. Write their failure-case table (8+ rows: bad inputs, empty input, missing file, invalid reply, refusal, no
   key, no network, one domain-specific case). Fix the worst two; turn rows into tests.
2. Add **one** hallucination or sanity check suited to the option:

   | Option | Check |
   |--------|-------|
   | A | predictions inside a sensible range; direction tests; test score vs baseline shown at start-up |
   | B | output fields valid; labels from the allowed list; numbers/names in the output exist in the input |
   | C | `section_id` was one of the sections sent; quote appears in that section; "I don't know" when retrieval finds nothing |
   | D | whichever of the above fits |

3. README: *How to run* (offline + online + tests), *Evaluation*, *Responsible AI*.
4. Demo script (Exercise 5), including the backup command.

## 6. Rehearsal and checkpoint (7 min)

Pairs: one student runs their demo **with a timer** (stop at 5:00), the partner notes one strength and one thing
to cut. Swap if time allows; otherwise the second rehearsal is homework.

**Checkpoint:**
- [ ] Failure-case table exists; the two worst failures are fixed and tested.
- [ ] At least one hallucination/sanity check is in the code (and tested).
- [ ] README has *How to run* (offline and online) and a *Responsible AI* section.
- [ ] Demo script written; the app runs with `COURSE_OFFLINE=1` (or locally, option A) end to end.

**Exit ticket:** "Name one thing your app sends to the API (or 'nothing') and one thing it deliberately does
not send."

## Homework (40–60 min)

Finish the README and the checkpoint items. Rehearse the full demo twice at home, once with Wi-Fi **off**.
Make sure `uv run pytest -q` passes from a fresh terminal. Bring the project ready to present. Optional revision
for the final assessment: Day 60 `practice.ipynb` (final review).

## Next class

Day 60: 5-minute presentations with questions and peer feedback, the 30–45 minute final assessment, the course
feedback form, and a learning path for after the course.

## Instructor notes

- The empty-month bug in the example apps is deliberate. If a student spots it on Day 57 or 58, praise them and
  ask them not to tell the class yet.
- Keep bias discussion concrete and respectful; use the synthetic data, not students' own circumstances. Do not
  ask students to share whether they have a job.
- Do not go into formal fairness metrics, differential privacy or regex libraries. String methods and a
  counterfactual probe are the right level.
- Students who are behind: priority order is (1) app runs offline end to end, (2) ≥ 5 tests pass, (3) README run
  instructions, (4) Responsible AI section, (5) extra checks. A working, honest, smaller app beats an ambitious
  broken one, and the rubric reflects that.
- Fast students: add the quote/number check *inside* their boundary function with a fake-model test proving the
  fallback triggers, or run their evaluation loop online and report both numbers.
- Collect demo order preferences (who wants to go first) at the end, or decide the order randomly (Day 60 demo).
