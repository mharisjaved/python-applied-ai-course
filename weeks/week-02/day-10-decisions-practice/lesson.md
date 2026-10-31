# Day 10: Decision Problems and Weekly Review

**Week 2 · Session 10 of 60 · Planned 75 min** · Previous: [Day 09](../day-09-conditionals/lesson.md) · Next: [Day 11](../../week-03/day-11-for-loops/lesson.md)

## Objectives

By the end of this lesson students can:

1. Turn a written specification into inputs, an output and a list of rules.
2. Write a test table **before** coding: one row per branch, both sides of each boundary, invalid and messy input.
3. Implement a decision problem combining a dictionary, `input()` cleaning and `if/elif/else`.
4. Choose between an `elif` chain (choose one) and separate `if`s (independent rules).
5. Find logic bugs by running a test table, and fix them.
6. Pass Checkpoint 2 (Days 06–09 plus Week 1 retrieval).

**Prior knowledge (Days 02–09):** everything from Weeks 1–2. **No new syntax today.** `score += 1` (Day 03) is
used as a counter in Exercise 4; `set(text) & set("0123456789")` (Day 08) checks for a digit.

**Files:** `demo.ipynb` (you, projected; section 3 calls `input()`) · `practice.ipynb` (students) ·
`solutions.ipynb` (you only) · [Checkpoint 2](../../../assessments/weekly/week-02-checkpoint.md) (print one copy per student)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: one line per day (Days 06–09) | core |
| 0:05–0:20 | The method + worked example: shipping cost | core |
| 0:20–0:45 | Practice exercises 1–3 | core |
| 0:45–0:52 | Review: compare test tables, which rows caught the bugs | core |
| 0:52–0:55 | Checkpoint instructions | core |
| 0:55–0:75 | **Checkpoint 2** (20 min, on paper) | core |
| +10 min | Exercise 4 (password strength) in class | optional (90-min session) |
| +5 min | Go through the checkpoint answers straight after collecting | optional (90-min session) |

**For 60 min:** skip demo section 3 (the `input()` version), give 15 min for Exercises 1–2 only, shorten the
review to 2 min, and keep the full 20 min for the checkpoint. Exercise 3 becomes homework.

## 1. Warm-up (5 min)

Demo section 0: five lines, one per day. Students write predictions on paper, then run.
Answers: `90 4` · `[60, 70]` · `none` · `['a', 'b', 'c']` · `True`. Ask which line they were least sure about;
that tells you what to emphasise in the review before the checkpoint.

## 2. The method (3 min)

**Why:** yesterday students wrote decisions that "looked right" but the wrong `elif` order or `>` instead of `>=`
gives no error message. The only way to know code is right is to **compare actual output with expected output for
carefully chosen inputs**. That is what professionals call testing.

Write the four steps on the board and leave them up all lesson:

1. **Read the spec**: underline inputs, output, every rule.
2. **Test table first**: one row per rule + boundaries + invalid input, expected output worked out by hand.
3. **Code**: inputs at the top, decisions in the middle, output at the end.
4. **Run every row**; mark ✅/❌; after any fix, re-run **all** rows.

## 3. Worked example: shipping cost (12 min)

Read the spec in demo section 2 aloud. Ask students to name the inputs (`zone`, `order_total`, `weight_kg`) and
the rules (3 zone prices, free from 100 for non-international, +4.00 above 5 kg, unknown zone).

**Build the test table with the class** before showing the one in the notebook. Prompt: "Which row proves the
'100 or more' rule? Which row proves 99.99 is *not* free? Which row shows free *and* heavy?" Then compare with the
8-row table in the demo.

Run the first attempt with **row 3** (`national`, 100.00, 2.0):

```text
Shipping: 6.50      ← expected Shipping: 0.00  ❌
```

**Prediction question:** "Which character is wrong?" (*`>` should be `>=`: "100.00 or more".*) Fix, re-run:
`Shipping: 0.00` ✅. Point out that rows 1, 2 and 4 pass with the bug. Without a boundary row, nobody would notice.

Then **live-test two more rows** by editing the three input lines and re-running (row 7, free and heavy → `4.00`;
row 8, `mars` → `Unknown zone: mars`). Model ticking the table as you go.

**Design question:** "Why two separate `if`s for free shipping and the heavy surcharge, not `if/elif`?"

| Use | When | Example |
|-----|------|---------|
| one `if/elif/else` chain | exactly **one** option applies | a grade; a ticket discount |
| separate `if`s | each rule is checked **independently** | free shipping **and** heavy surcharge; password checks |

Demo section 3 repeats the program with `input()`: `.strip().lower()` on the zone, `float()` on the numbers. The
recorded run (`"  National "`, 120, 8) matches row 7.

Demo section 4 is the **test-table checklist**: every branch · both sides of every boundary · invalid input ·
messy text · expected output written first.

## 4. Common mistakes in decision problems

Demo section 5 shows the one that **does** raise an error:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| a variable set only inside an `if` | `NameError: name 'fee' is not defined` (only for some inputs!) | give it a value before the `if`, or set it in every branch |
| `>` where the spec says "or more" | none; wrong at the boundary | read the spec's words: "or more", "up to and including" mean `>=` / `<=` |
| `elif` where rules are independent | none; second rule never applied | chain = choose one; separate `if`s = check each |
| a chain branch that catches everything (`elif minutes > 120`) | none; later branches never run | each `elif` should narrow down, not swallow the rest |
| uncleaned text (`"National" in rates`) | none; "Unknown zone" | `.strip().lower()` before comparing |
| "40% off" coded as `price * 0.4` | none; wrong price | 40% off means paying 60% |

The `NameError` one is worth stressing: it only appears for **some** inputs, which is exactly why testing several
rows matters.

## 5. Practice (25 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Week 2 review | predicting list/dict/set/condition code | recall |
| 2 Ticket-price calculator | spec → test table → dict + `elif` chain | application (the day's output) |
| 3 Find the bugs with tests | running a given test table to locate 2 logic bugs | modification |
| 4 Password strength checker | separate `if`s, counter, `.lower()`, sets, `.join` | problem solving |
| 5 Course enrolment desk (challenge) | nested dicts, set difference, rule order | challenge |

While circulating, look for:
- students who start coding Exercise 2 **before** filling in the Expected column. Stop them politely; the table
  is the exercise;
- `price * 0.4` for 40% off (row 8 catches it), and `age < 12` instead of `<= 12` (row 3);
- Exercise 3: students who "fix" the code by reading it instead of running the table. Ask "which rows failed?";
- Exercise 4: an `elif` chain for the five checks (only one point can ever be scored).

Expected outcome: everyone completes 1–2; most complete 3; Exercise 4 is homework for most; fast students try 5.

## 6. Review (7 min)

- Ask two students to read out their Exercise 2 test-table results for rows 3, 8 and 9. Discuss row 9 (70-year-old
  student): senior wins because only one discount applies and the senior check comes first.
- Exercise 3: "Which rows found bug 1? Bug 2?" (*Row 1 / rows 6 and 8.*) Note that six of the nine rows passed with
  the buggy code.
- Final question before the checkpoint: "When do we use a list, a tuple, a dict, a set?" (one sentence each).

## 7. Checkpoint 2 (3 + 20 min)

Hand out [Checkpoint 2](../../../assessments/weekly/week-02-checkpoint.md) (questions only; keep the answer key).
Rules: on paper, individual, no notebooks or internet, 20 minutes. It covers Days 06–09 plus two Week 1 retrieval
questions. Tell students it is a **diagnostic**, not a final exam: the result tells both of you what to review.

After class: mark with the 10-point guide in the answer key. Students below 5/10 should redo the matching
practice exercises before Day 11. Note the most-missed question; reteach it in the Day 11 warm-up.

## Homework (30 min)

1. Finish Exercises 3 and 4 (including the full test tables).
2. Optional: Exercise 5.
3. Write your own mini-spec (3–4 rules) for a decision from daily life (phone data plan, library late fee, gym
   membership price). Swap with a classmate next lesson: they write the test table, you write the code.

## Next class

Day 11 starts **Week 3: loops**. Today every test row meant editing values and re-running by hand. A `for` loop
repeats code for us: totals, counts and, soon, running all test rows at once. Lists from this week are what loops
walk through.

## Instructor notes

- Do not introduce functions to "avoid re-running cells", even if a student asks; that is exactly the motivation
  for Days 16–19. Say "you've just discovered why functions exist; we get there in Week 4".
- Some students will want `.isdigit()` or `.isupper()` for Exercise 4. They are not taught yet (`.isdigit()` is Day
  13). Accept them if a student already knows them, but teach the `.lower() != password` and `set` approaches.
- Passwords in these exercises are invented. Remind students never to paste real passwords into notebooks.
- The checkpoint is closed-book; if your institution prefers open notebooks, allow the Week 2 lesson notebooks only
  and add 5 minutes.
- Fast students: Exercise 5, then ask them to add a sixth rule (maximum 3 courses per student) and update their
  test table. Slow students: pair them for Exercise 2 with one person reading the spec aloud and one typing.
