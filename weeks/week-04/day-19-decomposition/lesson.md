# Day 19: Problem Decomposition

**Week 4 · Session 19 of 60 · Planned 75 min** · Previous: [Day 18](../day-18-scope-defaults/lesson.md) · Next: [Day 20](../day-20-project-hangman/lesson.md)

## Objectives

By the end of this lesson students can:

1. Break a problem into steps top-down, write the steps as pseudocode, and turn each step into a function with one job.
2. Write a **stub** (`def` line + docstring) for each planned function before writing its body.
3. Check a function with `print(f(x) == expected)` for a normal case and edge cases, and use a `False` result to locate a bug.
4. Build a text-statistics tool from small, checked functions.
5. Produce a function plan for Hangman: names, inputs, outputs, one-line jobs, and which functions can be checked.

**Prior knowledge:** functions, parameters, `return`, defaults, composition (Days 16–18); string methods and
`.split()` (Days 04, 07); dict counting with `.get` (Days 08, 12); `.isdigit()` (Day 13).
**New today:** the `print(f(x) == expected)` check pattern and the string method `.isalpha()` (introduced
explicitly in demo section 4 as the sibling of `.isdigit()`; Hangman needs it tomorrow). Day 21 can treat it as recap.

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: scope/default retrieval | core |
| 0:05–0:13 | The problem + top-down design and pseudocode (demo 1–2) | core |
| 0:13–0:23 | Stubs and checks, `.isalpha()`, `clean_word` (demo 3–4) | core |
| 0:23–0:35 | Build the rest function by function; assemble the report (demo 5–6) | core |
| 0:35–0:38 | Common mistakes with checks (demo 7) | core |
| 0:38–0:48 | Planning Hangman together (demo 8) | core |
| 0:48–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 together, or improve `count_sentences` using `split_sentences` | optional (90-min session) |

**For 60 min:** in demo 5 show only `get_words` and the `average_word_length` crash (run the other functions
without discussing them); move demo 7 into the practice circulation; Exercise 4 becomes homework. **Do not cut the
Hangman plan**: tomorrow depends on it.

## 1. Warm-up (5 min)

Two questions on the board:

1. `def area(width, height=1): return width * height`. What are `area(4)` and `area(4, height=3)`? (*`4`, `12`*)
2. A function sets `count = 10` inside its body. What is `count` outside the function? (*Unchanged/undefined: the
   local whiteboard is wiped.*)

Then ask: "When you started the Quiz Game, what did you type first?" Most will say "the first line of the
program". Today we learn to start **one level higher**: with a plan.

## 2. Top-down design and pseudocode (8 min)

**Why.** Big programs are not written top to bottom. They are designed from the goal down, then built from the
bottom up, one small checked piece at a time.

> **Analogy: planning a trip.** "Visit Lahore" is too big to do. Break it down: book transport, book a room, plan
> each day. "Plan each day" is still big: break it down again. You stop when each item is something you know how
> to do in one go. In code, each of those items is a function.

Demo section 1 states the text-statistics problem. Before showing section 2, ask the class: "What steps does
this tool need?" Collect answers on the board in plain words. Then compare with the pseudocode in demo section 2.

Key points:
- **Pseudocode** is plain-language steps with indentation. No syntax rules; it just has to be clear.
- If a step still feels big ("get the words"), break it down again.
- Each step becomes a function. Fill the plan table: *name · gets · gives back · job*.
- Design rule: **one job per function**. Only `print_report` prints; everything else returns.

## 3. Stubs and checks (10 min)

Demo section 3: a **stub** is a `def` line plus a docstring and no body. It is valid Python and returns `None`.
Show `print(clean_word("Hello,"))` → `None`.

Demo section 4: write the **checks before the body**:

```python
print(clean_word("Hello,") == "hello")
print(clean_word("WORLD!") == "world")
print(clean_word("don't") == "dont")
print(clean_word("42") == "")
```

All four print `False`. That is the target. Then introduce `.isalpha()` in one cell (`"a".isalpha()` → `True`,
`"7".isalpha()` → `False`, `"".isalpha()` → `False`) and write the body with a loop and an accumulator.

**Prediction question:** "How many `True`s now?" (*four*)

Key points to say explicitly:
- A check is just a comparison (Day 09) that prints `True` or `False`. Nothing new, just used systematically.
- Work out the expected value **by hand**, not by copying the function's output.
- Choose checks deliberately: a **normal** case, then **edge** cases (capitals, punctuation in the middle, nothing
  left, empty input, a tie, the exact boundary value).

## 4. Build function by function (12 min)

Demo section 5, one function at a time, running its checks each time:

1. `get_words` **calls** `clean_word`. Because `clean_word` is already checked, we trust it (composition, Day 18).
2. `count_sentences`: ask the 🤔 question about `"Wait... what?!"` (*5*). Bug or acceptable limitation? Either is
   a fine answer as long as the decision is written in the docstring. Checks force you to decide.
3. `average_word_length`: the normal check passes, then the **edge-case check crashes** with
   `ZeroDivisionError: division by zero`. Fix with an `if len(words) == 0: return 0` guard and re-run *all* checks.
   This is the strongest argument for edge cases: the crash happens in class, not in front of a user.
4. `longest_word` and `most_common_word`: run them quickly with their checks; point at the tie rule in each docstring.

Demo section 6: `print_report(sample_text)` reads like the pseudocode. Expected output:

```
Words:            28
Sentences:        4
Avg word length:  4.1
Longest word:     evening
Most common word: and
```

## 5. Common mistakes with checks (3 min)

| Mistake | What you see | How to explain it |
|---------|--------------|-------------------|
| Function prints instead of returning | the value appears, then `False` | `print` shows, `return` gives back. A check needs a returned value |
| Expected value of the wrong type (`== "3"`) | `False` although the function works | `3` and `"3"` are different values (Day 02) |
| Only checking the easy case | all `True`, but it crashes on `[]` | Add at least one edge case per function |
| Expected value copied from the output | always `True`, proves nothing | Work the answer out by hand first |
| Checks call `input()` | the notebook waits for typing | Keep `input()` out of checked functions (see the Hangman plan) |

## 6. Planning Hangman together (10 min)

This is the most important 10 minutes for tomorrow. Do it **with** the class on the board, then show demo
section 8 as the "clean copy".

1. Ask a student to explain the rules of Hangman. Write them down.
2. Write `play_game` and `play_round` in pseudocode together (top-down).
3. Turn steps into functions. Fill the plan table: name, gets, gives back, job.
4. Add the last column: **can it be checked with `print(... == ...)`?** Students discover that anything using
   `input()` or randomness cannot be checked that way.
5. State the design rule: **keep `input()`/`print()` in a few functions and make the rest return values.** That is
   why `get_guess` calls `is_valid_guess`.

The agreed function list (it matches the project starter): `choose_word`, `display_progress`, `is_word_guessed`,
`is_valid_guess`, `get_guess`, `play_round`, `ask_play_again`, `play_game` (the starter adds `draw_gallows` and
`show_status` for the *Should* requirements).

Show the two stubs + checks at the end of demo section 8. They print `False`. "Tomorrow you make them `True`."
**Do not write any function bodies for Hangman today.**

## 7. Practice (22 min)

Students open `practice.ipynb`. Walk around and look for:
- bodies written before checks (ask them to write the checks first, even for Exercise 4);
- expected values copied from the function's output;
- Exercise 4 functions that recalculate instead of calling earlier ones;
- Exercise 5 checks that call `input()` or check `choose_word` against one exact word.

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the checks | reading checks, boundary bug | recall |
| 2 Write the checks | choosing normal and edge cases | application |
| 3 Let the checks find the bug | debugging with checks (accumulator bug) | modification |
| 4 Attendance report from a plan | implementing a given decomposition, composition | problem solving |
| 5 Hangman stubs and checks | stubs + checks before code | planning |
| 6 Sentence tools (challenge) | decomposition of a string task | challenge |

Expected outcome: everyone completes 1–3 and 5 (**5 is required for tomorrow**); most complete 4; fast students
try 6. If time is short, have students do Exercise 5 before Exercise 4.

## 8. Recap and exit ticket (5 min)

Ask students to supply the recap:
1. Top-down: goal → pseudocode → one function per step.
2. Stub first, then checks, then the body.
3. A good set of checks has a normal case and edge cases; a `False` means the function or the expectation is wrong.
4. Functions that use `input()` can't be checked this way, so keep the logic in separate returning functions.

**Exit ticket:** write two checks for a function `count_words(text)` that returns the number of words in `text`:
one normal case and one edge case.

Answer (any equivalent): `print(count_words("Mei likes tea") == 3)` and `print(count_words("") == 0)`.

## Homework (30 min)

1. Finish Exercise 5 (required for Day 20) and Exercise 4.
2. Read the Project 02 brief ([projects/02-hangman/README.md](../../../projects/02-hangman/README.md)) and write
   down one question you have about it.
3. Optional head start: write the body of `display_progress` in your practice notebook until its checks print `True`.

## Next class

Day 20 is **Project 02: Hangman**, built function by function from today's plan, plus Checkpoint 4. Students
start from a starter file whose functions are exactly today's stubs, with today's kind of checks at the bottom.

## Instructor notes

- `print(f(x) == expected)` is the course's checking tool until Day 29, when `assert` and pytest replace it. Don't
  show `assert` today.
- Writing `== True` in a check is fine and keeps every check the same shape. Don't fight it.
- `.isalpha()` is new today. Keep it to one cell and one sentence. Accented letters (`"é".isalpha()` is `True`) are
  not worth discussing.
- Pseudocode has no "correct syntax". Accept any clear, indented plain-language steps; reject only steps that
  are actually Python code with the colons removed.
- Do not let the Hangman planning turn into coding. If students start writing bodies, redirect them: "make the
  checks first; the bodies are tomorrow".
- Fast students: Exercise 6, then make `count_sentences` use `split_sentences`, re-running all checks.
  Slow students: Exercises 1–3 with a partner, then Exercise 5 (use demo section 8 as a model).
