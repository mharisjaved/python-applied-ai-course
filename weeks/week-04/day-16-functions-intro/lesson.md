# Day 16: Why Functions? Define and Call

**Week 4 · Session 16 of 60 · Planned 75 min** · Previous: [Day 15](../../week-03/day-15-project-quiz-game/lesson.md) · Next: [Day 17](../day-17-parameters-return/lesson.md)

## Objectives

By the end of this lesson students can:

1. Explain the duplication problem (the same lines copied in several places must all be changed together) and how a function solves it.
2. Define a function with `def name():`, a colon and an indented body, and call it with `name()`.
3. Explain the difference between **defining** (storing the recipe, nothing runs) and **calling** (running it), and predict the order of output when a program calls functions.
4. Write a one-sentence docstring that says what a function does.
5. Call a function many times, including inside a loop, and fix the four common errors: missing `()`, calling before defining, missing colon, unindented body.

**Prior knowledge:** `print` and f-strings (Days 01, 04), lists and `enumerate` (Days 06, 12), `for`/`while`,
`break` (Days 11–14), and the Quiz Game (Day 15), which they wrote **without functions**.
Today's functions take **no parameters** and return nothing: parameters and `return` are tomorrow.

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:07 | Warm-up: the Quiz Game looked back on + retrieval | core |
| 0:07–0:17 | The duplication problem → first `def` and call (demo 1–2) | core |
| 0:17–0:25 | Order of execution, calling in a loop (demo 3) | core |
| 0:25–0:32 | Docstrings and naming (demo 4) | core |
| 0:32–0:40 | Function bodies with loops: the menu (demo 5, 7) | core |
| 0:40–0:45 | Common mistakes, live (demo 6) | core |
| 0:45–0:68 | Practice exercises 1–5 | core |
| 0:68–0:75 | Recap + exit ticket | core |
| +15 min | Exercise 6 together, or "refactor one part of your Quiz Game into a function" | optional (90-min session) |

**For 60 min:** show demo 7 only as a picture of "the program reads like a story" (1 min), shorten docstrings to
2 minutes and set Exercise 5 as homework.

## 1. Warm-up (7 min)

Open one student's (or your own) `quiz_game.py` from Day 15 and scroll through it. Ask:

- "Which lines appear more than once, almost identical?" (*Usually the "print the question, read the answer,
  check it, update the score" block, and the separator lines.*)
- "If we wanted to change the separator from `---` to `===`, how many places would we edit?"

Retrieval questions (answers in italics):

1. `for i in range(3): print("Hi")` prints how many lines? (*3*)
2. What does `enumerate(["tea", "coffee"], start=1)` give us inside a loop? (*pairs `(1, "tea")`, `(2, "coffee")`*)
3. What does `break` do? (*leaves the loop immediately*)

If Checkpoint 3 results are in, spend 2 of these minutes on the weakest question (see `assessments/README.md`).

## 2. The duplication problem → first function (10 min)

**Why first.** Show demo section 1: two café receipts, each starting with the same 4-line header. Ask the 🤔
question: "The café changes its name. How many lines do we edit? What if we miss one?" Let students feel the pain
before any syntax appears.

> **Analogy: a recipe card.** Writing `def` is writing a recipe card and filing it under a name. Nobody eats
> anything yet. **Calling** the function is cooking from the card. You can cook from the same card as often as
> you want, and if you improve the recipe, every future meal improves.

Live code (demo section 2):

```python
def print_receipt_header():
    print("=" * 30)
    print("        CORNER CAFE")
    print("   12 Garden Road, Lahore")
    print("=" * 30)
```

Running this cell prints **nothing**. Ask the 🤔 question before explaining. Then call it:

```python
print_receipt_header()
```

Point at the parts on the board:

```
def print_receipt_header():      <- keyword def · name · () · colon
    print("=" * 30)              <- body: every line indented 4 spaces
    ...
print_receipt_header()           <- the call: name + ()
```

Key points:
- The body is everything indented under the `def` line, exactly like the body of an `if` or a `for`.
- Function names follow the same rules as variable names (`snake_case`, no spaces, no leading digit).
- To change the café name we edit **one line**, re-run the `def` cell, and every receipt changes.

## 3. Order of execution (8 min)

Live code (demo section 3):

```python
def say_hello():
    print("Hello!")

print("1. before")
say_hello()
print("2. after")
say_hello()
```

**Prediction question:** "What is the exact order of the output?" (*`1. before`, `Hello!`, `2. after`, `Hello!`*)

Draw the flow with arrows on the board: the program runs top to bottom; at a call it **jumps into** the function,
runs the body, then **returns** to the line after the call. This picture is the foundation for the whole week.

Then call a function inside a loop (`print_divider()` after each `"Table", table` line). Ask "how many dividers?"
before running (*3*).

**In a `.py` file** (type it live, 1 minute): create `cafe.py` with the `def` *below* the call, run `uv run cafe.py`
and show the `NameError`. Move the `def` to the top and run again. Rule: **definitions at the top, calls below.**

## 4. Docstrings and naming (7 min)

Demo section 4. A docstring is a string in triple quotes on the **first line of the body**:

```python
def print_divider():
    """Print a line of 30 dashes."""
    print("-" * 30)
```

- It is not printed when the function runs. It is documentation for whoever **uses** the function.
- In VS Code, hover over `print_divider()` in a later cell: the docstring pops up. Show this, it convinces students
  docstrings are useful.
- Style: one sentence, starts with a verb, ends with a full stop: *Print…*, *Show…*, *Draw…*.
- Docstring vs `#` comment: the docstring says **what** the function does (for users of it); comments inside the
  body explain **how/why** (for readers of the code).

Naming: a function *does* something, so its name is usually a verb phrase: `print_divider`, `show_menu`,
`draw_box`. Never call a function `print`, `input` or `type` (same reason as on Day 02: it hides Python's own).

From today, **every function in this course has a docstring**. Say it as a rule; it is in the Project 02 rubric.

## 5. A body can contain anything (8 min)

Demo section 5: `show_menu()` keeps a list of items, loops with `enumerate(items, start=1)` and prints them.
Point out that a function body can hold variables, loops and `if`s: everything students already know.

**Prediction question** (demo section 5, second cell): "We greet two customers and show the menu to each. How many
lines are printed?" (*2 greetings + 2 × 5 menu lines = 12*)

Demo section 7 ("the café screen reads like a story"): `show_welcome()`, `show_menu()`, loop over pretend
choices, `show_goodbye()`. Read the main part aloud as if it were English. That readability is the second big
benefit of functions, after "change it in one place".

End with the cliffhanger in demo section 7: we can only print the item **number**, because the list of names lives
inside `show_menu` and the rest of the program cannot see it. "Tomorrow: getting information into and out of
functions." (Do **not** explain scope yet; that is Day 18.)

## 6. Common mistakes (live debugging, 5 min)

Run demo section 6. Read the last line of each error together.

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `print_divider` without `()` | none! The notebook shows `<function print_divider at 0x…>`; in a `.py` file nothing happens | The name is the recipe card; `()` means "cook it now" |
| Calling before the `def` has run | `NameError: name 'print_footer' is not defined` | Python only knows functions it has already read. Definitions go at the top |
| `def print_title()` without `:` | `SyntaxError: expected ':'` | Same rule as `if` and `for`: a line that starts a block ends with `:` |
| Body not indented | `IndentationError: expected an indented block after function definition` | The indentation *is* the body. No indentation, no body |
| Calls indented inside the function itself | `RecursionError` (the function calls itself forever) | Calls go back at the left margin. Watch for this in Exercise 2 |

The silent one (missing `()`) is the most dangerous because nothing complains. Say so.

## 7. Practice (23 min)

Students open `practice.ipynb`. Walk around and look for:
- calls indented inside the `def` (see last row of the table above);
- functions defined but never called ("my code doesn't print anything");
- the changing part (the day, the customer) put *inside* the function in Exercise 4;
- missing docstrings: ask "what would you write on the recipe card's title line?"

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the output | define vs call, order of execution | recall |
| 2 Your first function | `def`, body, call twice | application |
| 3 Fix the broken code | colon, `()`, indentation, define-before-call | modification |
| 4 Remove the duplication | refactor repeated lines into a function | application |
| 5 Menu printer | loop inside a function + calling from a loop | problem solving |
| 6 Hollow box (challenge) | nested loops inside a function | challenge |

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

## 8. Recap and exit ticket (7 min)

Ask students to supply the recap:
1. A function is a named block of code: write it once, use it many times, change it in one place.
2. `def name():` + indented body *defines* it; `name()` *calls* it. Defining runs nothing.
3. A call jumps into the function, runs the body and comes back to the next line.
4. Every function gets a one-sentence docstring.

**Exit ticket:** what does this print?

```python
def cheer():
    """Print a cheer."""
    print("Go team!")

print("Start")
for i in range(2):
    cheer()
print("End")
```

Answer: `Start`, `Go team!`, `Go team!`, `End` (four lines). Anyone who writes `Go team!` three times (once for
the `def`) has not yet separated defining from calling: check in with them at the start of Day 17.

## Homework (20 min)

1. Finish Exercises 5–6.
2. Open your `quiz_game.py` and find one block of lines that is repeated or that does one clear job (for example
   printing the welcome text or the rules). Move it into a function with a docstring and call it. Run the game to
   check it still works. Bring the before/after to class.

## Next class

Day 17 gives functions **inputs** (parameters, "make the header show *any* café name") and **outputs** (`return`,
"give me back the price after discount"). Today's cliffhanger, that the menu list is stuck inside `show_menu`, is
the motivation. The single most important idea tomorrow is *print vs return*.

## Instructor notes

- Keep today strictly to functions **without parameters**. If a student asks "can I pass the name in?", answer
  "yes, and that is exactly tomorrow" and move on. Do not introduce `return` or scope rules today.
- `enumerate(..., start=1)` uses a *keyword argument*. Students have used it since Day 12; no need to name the idea
  until tomorrow.
- Do not go into functions as objects, `print_divider` memory addresses, or `help()`. If asked about the
  `<function ... at 0x...>` output, say "that's Python telling you *what* the name is: a function, stored somewhere
  in memory. Add `()` to run it."
- A function can call another function. Some students will discover this in the homework. It is fine; we teach it
  formally on Day 18 (composition).
- Fast students: Exercise 6, then ask them to draw a *filled triangle* function. Slow students: make sure Exercises 1
  and 2 are solid; Exercise 3 can be done together on the board.
