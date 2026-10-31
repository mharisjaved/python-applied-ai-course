# Day 15: 🏗 Project 01: Quiz Game

**Week 3 · Session 15 of 60 · Planned 75 min** · Previous: [Day 14](../day-14-break-continue-nested/lesson.md) · Next: [Day 16](../../week-04/day-16-functions-intro/lesson.md)

## Objectives

By the end of this lesson students can:

1. Describe and follow a project workflow: **read the brief → plan in comments → build the smallest working
   version → test → extend**.
2. Turn a written brief into a plan of 6–10 ordered comment steps, and say which step is the smallest working
   version.
3. Build a playable quiz from the starter (questions loop, answer check, score) by the end of class.
4. Test their own program on purpose with valid, invalid and edge-case inputs.
5. Show what they have learned in Weeks 1–3 on Checkpoint 3.

**Prior knowledge:** everything from Days 02–14, in particular lists of dicts and `.items()` (Days 08, 12),
accumulators (Day 11), validation loops (Day 13), `random.shuffle` and the "play again" wrapper (Day 14, demo
section 6). Students read the brief for homework on Day 14.

**Files:** `demo.ipynb` (you: a planning demo on a *different*, tiny program) · `practice.ipynb` (warm-ups +
planning exercise) · `solutions.ipynb` (you only) · Project brief
[projects/01-quiz-game/README.md](../../../projects/01-quiz-game/README.md) · Starter
`projects/01-quiz-game/starter/quiz_game.py` · Instructor notes
[projects/01-quiz-game/INSTRUCTOR.md](../../../projects/01-quiz-game/INSTRUCTOR.md) · Checkpoint
[assessments/weekly/week-03-checkpoint.md](../../../assessments/weekly/week-03-checkpoint.md) (print copies)

## Why Checkpoint 3 goes at the start

1. **It is the warm-up.** The checkpoint is about loops, validation and dicts: exactly what the project needs.
   Retrieving them right before building works better than after.
2. **It tells you whom to help first.** Scan the two write-code questions (Q7, Q8) at the start of build time: the
   students who struggled there are the ones to visit first.
3. **Build time is not cut off.** Students who are in the middle of fixing a bug at 0:60 are not interrupted by a
   test, and the session ends with show-and-tell, a positive close for the first milestone project.

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:15 | Checkpoint 3 (individual, no notes) | core |
| 0:15–0:20 | How to work on a project | core |
| 0:20–0:28 | Kickoff: read the brief together, run the starter | core |
| 0:28–0:38 | Live demo: plan → smallest version → test → extend (flashcards) | core |
| 0:38–0:68 | Build time (practice Exercise 4 first, then the build plan) | core |
| 0:68–0:75 | Mini show-and-tell + homework | core |
| +15 min | Longer build time, or a second round of show-and-tell | optional (90-min session) |

**60-minute version:** shorten the live demo to sections 2 and 3 only (plan + smallest version, 5 min), and the
build time to 20 minutes. Keep the checkpoint and show-and-tell.

## 1. Checkpoint 3 (15 min)

Hand out the checkpoint. Rules: individual, pen and paper (or a blank notebook with no access to old files),
15 minutes. Collect at 0:15 sharp, even if unfinished: it is a diagnostic, not a final exam. While they write,
check that the starter runs on the classroom machine.

## 2. How to work on a project (5 min)

Demo section 1. Ask first: "Imagine I ask you to write the whole quiz in one go and run it once at the end. What
will happen?" (*Twenty errors at once, and no idea which line caused which.*)

| Step | What it means | Why |
|------|---------------|-----|
| 1. Read the brief | Underline the **Must** requirements; look at the example run | You cannot build what you have not understood |
| 2. Plan in comments | Write the program's steps as `#` comments, in order | Thinking and typing are separate jobs |
| 3. Smallest working version | The tiniest thing that runs and does *something* real | A working base you never break |
| 4. Test | Run it with normal, wrong and odd input | Bugs are cheapest when the code is new |
| 5. Extend | Add **one** feature, run, test, repeat | Each new error is in the few lines you just wrote |

> **Analogy:** to get across town, first build a skateboard (it moves!), then a bicycle, then a car. Do not build
> four wheels and an engine that only move once everything is finished.

**Must / Should / Could** (the brief uses this): Must = needed to pass · Should = expected for a good grade ·
Could = extras if there is time. Always finish the Musts first.

## 3. Kickoff: read the brief together (8 min)

Project the [brief](../../../projects/01-quiz-game/README.md). Walk through it in this order:
1. **The problem** and the **example run**. Ask: "What happens when the player types `e`?" (*They are asked again;
   it is not marked wrong.*)
2. **Must** list: read all seven aloud. Then the Should/Could lists quickly.
3. **Build plan** and **rubric**: point out the 10 points for example runs and 15 for explaining their code.
4. Answer 2–3 of the questions students wrote for homework.

Everyone copies the starter into their own project folder and runs `uv run quiz_game.py`. Show the "how to read
one question" lines, especially `first["options"]["b"]` (a dict inside a dict). Advice: **logic first, content
last**: build with the starter's questions and write your own themed questions at the end (TODO 7).

## 4. Live demo: plan → smallest version → test → extend (10 min)

Use the demo notebook. It builds a **vocabulary flashcard drill**, deliberately *not* the quiz, so students see the
process without receiving the answer.

- **Section 2, plan:** a code cell containing only comments. Read the plan aloud. Ask "Which step would you build
  first?"
- **Section 3, smallest working version:** one card, one `input()`, one `if`. Run it (mock input `cat`).
- **Section 4, test:** run the same code as a real user would type: ` Cat` → *No, it means 'cat'*. A bug that
  the first test did not show! Fix with `.strip().lower()`, run again → *Correct!* Make the point: **testing with
  odd input found the bug, not reading the code**.
- **Section 5, extend:** a list of two cards, a `for` loop with `enumerate`, a score. Inputs `Cat`, `house` →
  `Score: 1/2`.
- **Section 6:** what the next increments would be (shuffle, more cards, retry wrong cards), one at a time.

Ask: "What does the quiz need that the flashcards do not?" (*Four options per question, a validation loop for
a–d, a percentage and message, play again.*) Those are their job.

## 5. Build time (30 min)

1. **First 5 minutes:** practice Exercise 4. Students write their plan as comments at the top of their own
   `quiz_game.py` (not just in the notebook). Check two or three plans quickly.
2. **Then** the build plan from the brief: TODO 1 → TODO 2 → TODO 3. **Target for today: step 3** (a playable
   quiz with a score). Validation is the next priority.
3. Students who feel shaky on loops do one warm-up first: Exercise 1 (list of dicts), 2 (validation) or 3
   (percentage and tiers), whichever matches what they are stuck on.

Circulate in this order: students whose checkpoint Q7/Q8 were weak → students with no plan → everyone else.
The full troubleshooting table is in [INSTRUCTOR.md](../../../projects/01-quiz-game/INSTRUCTOR.md); the most
frequent issues:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| Comparing `"B"` with `"b"` (or `" b"`) | no error, always "Wrong" | Print the answer between brackets to *see* it; normalise with `.strip().lower()` |
| `score = 0` inside the question loop | no error, score ends at 0 or 1 | Day 11: accumulators go before the loop (but inside the play-again loop) |
| Validation loop that does not ask again | infinite loop | Day 13: the body must change the variable in the condition |
| `questions = random.shuffle(questions)` | `TypeError: 'NoneType' object is not subscriptable` | Day 14: `shuffle` changes the list and returns nothing |
| `print(q["options"])` | no error, ugly dict output | Day 12: loop over `.items()` |
| `score // len(questions) * 100` | no error, 0% | Day 03: `//` throws away the fraction; use `/` |

Practice notebook overview:

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Stock check | looping over a list of dicts, building a list | warm-up (retrieval Days 08, 12) |
| 2 Menu choice | validation loop with a set of allowed answers | warm-up (retrieval Day 13) |
| 3 Challenge progress | percentage + message tiers | warm-up (retrieval Days 03, 09) |
| 4 Plan the Quiz Game | turning a brief into a plan + test cases | everyone, start of build time |
| 5 Deal some cards (challenge) | `random.shuffle` on a list of dicts + slicing | challenge |

**Do not** project or hand out the reference solution. When a student is stuck, ask questions (INSTRUCTOR.md,
"General unblocking moves") instead of typing in their file.

## 6. Mini show-and-tell (7 min)

At 0:68, ask 2–3 volunteers (pick a range of progress, not only the fastest) to run their quiz for 2 minutes each:
1. one thing that works;
2. one bug they found today and **how** they found it.

The class asks one question each time. Then give the homework and deadline.

## 7. Recap and exit ticket

Recap in one sentence each (students supply): read the brief · plan in comments · smallest working version · test
with odd input · extend one feature at a time.

**Exit ticket** (sticky note, as they leave): "The next feature I will add is … and I will test it by typing …"

Example of a good answer: *"The a–d validation loop. I will test it by typing `x`, an empty answer and ` B `."*
Vague answers ("finish it", "test it") show who needs a planning nudge on Day 16.

## Homework (about 60 min, project week)

Finish build-plan steps 4–6, write at least 8 questions on your own theme, and save two example runs in
`example_runs.txt` (see the submission checklist in the brief). **Deadline: before Day 17.**

## Next class

Day 16 introduces **functions**. Open it by asking students to look at their quiz: "Which lines appear twice
(the `input` + `.strip().lower()` + validation, the separator lines)? Which part would you like to give a name?"
That repetition is exactly the problem `def` solves.

## Instructor notes

- **No `def` in this project.** Students who already know functions may use them, but must explain them; the
  reference and the starter deliberately use none.
- Mark Checkpoint 3 before Day 16 if possible; the Q7/Q8 results tell you who needs a loops recap during Week 4.
- Students absent on Day 14 lack `random` and the play-again wrapper: point them to Day 14 demo sections 4–6 and
  pair them with a neighbour for the first 10 minutes.
- Students who finish the Musts in class: Could features (lives, streak bonus, best score). Do not let them skip
  the Should list first.
- If the checkpoint overruns, take the minutes from the live demo (skip demo section 6), never from build time.
