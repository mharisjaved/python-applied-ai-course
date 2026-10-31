# Day 02: Variables and Basic Data Types

**Week 1 · Session 2 of 60 · Planned 75 min** · Previous: [Day 01](../day-01-environment/lesson.md) · Next: [Day 03](../day-03-numbers-input/lesson.md)

## Objectives

By the end of this lesson students can:

1. Open a Jupyter notebook in VS Code, select the course kernel and run a cell with **Shift+Enter**.
2. Create a variable with `=` and explain that `=` means "attach this name to this value", not "is equal to".
3. Store an `int`, a `float`, a `str` and a `bool`, and confirm each with `type()`.
4. Predict a variable's value after it has been reassigned several times.
5. Choose valid, descriptive `snake_case` names, and fix a `NameError` caused by a typo, a missing assignment or missing quotes.

**Prior knowledge (Day 01):** VS Code is installed, uv is installed, students wrote `print("Hello, World!")` in
`hello.py` and ran it with `uv run hello.py`. **They have not used Jupyter yet.**

**Files:** `demo.ipynb` (you, projected) · `practice.ipynb` (students) · `solutions.ipynb` (you only)

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: re-run `hello.py`, recap questions | core |
| 0:05–0:15 | First notebook in VS Code | core |
| 0:15–0:25 | Variables and assignment | core |
| 0:25–0:40 | The four basic data types + `type()` | core |
| 0:40–0:48 | Reassignment and naming rules | core |
| 0:48–0:52 | Common errors (live debugging) | core |
| 0:52–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +10 min | Exercise 6 (challenge) together, or "variables can change type" discussion | optional (90-min session) |

## 1. Warm-up (5 min)

Ask a student to open their Day 1 project and run `uv run hello.py`. Fix any setup problems now (see
[setup/troubleshooting.md](../../../setup/troubleshooting.md)) because today needs a working environment.

Questions:
- "What does the Python interpreter do with the file `hello.py`?" (*Reads it top to bottom and runs each instruction.*)
- "What would happen if we wrote `Print("Hello")` with a capital P?" (*Error, because Python is case-sensitive. Don't run it yet; we will see errors later today.*)

## 2. First notebook in VS Code (10 min)

**Why a notebook?** A `.py` file runs everything at once. A notebook lets us run *one small piece at a time* and
see the result immediately below it, which is ideal for experimenting while learning. Real programs still live in
`.py` files; we will go back to them in Week 6.

Live steps (students follow along):
1. In the terminal, inside their project: `uv add ipykernel` (one time only; lets VS Code run notebooks with the project's Python).
2. Install the VS Code **Jupyter** extension if it is not already there (the Python extension usually brings it).
3. Open `practice.ipynb` (or create `day02.ipynb` via *File → New File → Jupyter Notebook*).
4. Top-right **Select Kernel** → *Python Environments* → choose the one in `.venv`.
5. Type `print("Hello from a notebook")` in a cell, press **Shift+Enter**.

Point out:
- **Code cells** run Python. **Markdown cells** are text (instructions, headings).
- The number in `[ ]` next to a cell shows the *order* cells were run.
- In a notebook, the **last line of a cell is displayed automatically**: typing `5 + 5` alone shows `10`. In a
  `.py` file nothing appears unless you `print()`. Students will mix this up; say it explicitly.

## 3. Variables and assignment (10 min)

**Intuition first:** programs need to *remember* things: a user's name, a score, a price. A variable is a
**name tag** we attach to a value so we can use it later.

> **Analogy:** a sticky name tag on a value. `age = 21` writes "age" on a tag and sticks it on the value 21.
> I use "name tag" rather than "box" deliberately: on Day 07 two tags can stick to the *same* list, and the box
> picture makes that confusing.

Teach the reading direction: **right side first**. `age = 21` means "take 21, attach the name `age`". Say it as
"age *gets* 21", not "age *equals* 21". `=` is an instruction, not a maths statement.

Live code (demo section 1):

```python
city = "Lahore"
print(city)
print("I live in", city)
```

`print` can take **several values separated by commas** and puts a space between them.

**Prediction question:** "If I run `print("city")`, what appears?" (*The word `city`, because quotes mean literal text, not the variable.*)

## 4. The four basic data types (15 min)

Every value has a **type** that decides what you can do with it.

| Type | Meaning | Examples | Everyday example |
|------|---------|----------|------------------|
| `int` | whole number | `21`, `-3`, `0` | number of students |
| `float` | number with a decimal point | `3.5`, `72.0`, `-0.25` | price, temperature |
| `str` | text (string of characters) in quotes | `"Asha"`, `'hello'`, `"42"` | names, messages |
| `bool` | yes/no | `True`, `False` (capital T/F, no quotes) | is the student present? |

Live code (demo section 2): create one of each, then `type(...)` on each.

Key teaching points:
- `21` and `"21"` look similar but are **different types**. Ask: "Which one can we do maths with?" Show `type(21)` vs `type("21")`.
- `72.0` is a `float` even though it is a whole number, because the decimal point decides.
- `True` must be capitalised and has **no quotes**. `"True"` is a `str`.
- `type()` is our "what is this?" tool. Encourage students to use it whenever unsure.
- `print(type(21))` shows `<class 'int'>`. Tell students to read it as "type: int"; the word *class* will make sense in Week 7.

**Prediction question:** show `type(3.0)`, `type("3.0")`, `type(False)`, `type("False")` and let students vote before running each.

Real-world mini-example (demo section 4): describe one student with variables:

```python
student_name = "Bilal"
age = 19
height_m = 1.74
is_enrolled = True
print("Name:", student_name)
print("Age:", age, "| Height:", height_m, "m | Enrolled:", is_enrolled)
```

## 5. Reassignment and naming (8 min)

**Reassignment:** a name tag can be moved to a new value. The old value is forgotten.

```python
score = 10
score = 25
print(score)   # 25
```

**Updating using the old value:** right side first!

```python
score = score + 5   # take current score (25), add 5, attach the name to 30
```

Trace it on the board with a 2-column table (line | value of score). Tracing tables are a skill we will use all course.

**Naming rules (Python enforces):** letters, digits and `_`; cannot start with a digit; no spaces; case-sensitive (`Age` ≠ `age`).
**Naming conventions (humans expect):** lowercase `snake_case`, descriptive (`total_price` not `tp` or `x`), and never
reuse built-in names such as `print`, `type`, `str` as variable names. Doing so breaks them until the kernel restarts.

## 6. Common mistakes (live debugging, 4 min)

Run each broken cell in demo section 5 (they are tagged to raise errors on purpose) and **read the last line of the error together**:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `print(nmae)` (typo) | `NameError: name 'nmae' is not defined` | Python only knows names you created. Check spelling |
| `name = Asha` (no quotes) | `NameError: name 'Asha' is not defined` | Without quotes Python thinks `Asha` is a variable name |
| `2nd_place = "Sara"` | `SyntaxError` | Names cannot start with a digit |
| Using a variable before the cell that creates it has run | `NameError` | Notebook cells run in the order *you* run them, not top-to-bottom. Use **Restart → Run All** when confused |

Message to students: **errors are normal and helpful**. The last line tells you *what* went wrong; we will learn to read the rest on Day 28.

## 7. Practice (18 min)

Students open `practice.ipynb` and work on Exercises 1–5. Walk around and look for:
- forgetting quotes around text;
- writing `true` instead of `True`;
- expecting `x = 5` alone to display output (it does not, because assignment shows nothing).

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 What type is it? | recall of types | recall |
| 2 Profile variables | creating variables | application |
| 3 Fix the broken code | debugging names/quotes | modification |
| 4 Trace the score | reassignment tracing | reasoning |
| 5 Swap two values | using a temporary variable | problem solving |
| 6 Library card (challenge) | combining everything | challenge |

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

## 8. Recap and exit ticket (5 min)

Recap in three sentences (ask students to supply them):
1. A variable is a name attached to a value; `=` assigns from right to left.
2. Basic types: `int`, `float`, `str`, `bool`. `type()` tells you which.
3. Reassignment replaces the old value; `NameError` usually means a typo or missing quotes.

**Exit ticket** (on paper or chat): What does this print, and what is the type of `b`?

```python
a = 7
b = "7"
a = a + 3
print(a, b)
```

Answer: `10 7`; `b` is a `str`.

## Homework (15 min)

Finish Exercises 5–6. In a markdown cell, write two sentences explaining the difference between `5` and `"5"`.

## Next class

Day 03 uses variables to **calculate**: arithmetic operators, `input()` to ask the user for values, and converting
text to numbers. Today's `"21"` vs `21` distinction is exactly why `input()` will surprise them. Mention that as a teaser.

## Instructor notes

- Keep the type discussion practical. Do **not** go into memory addresses, `id()`, mutability or dynamic typing
  theory today. If asked "can a variable change type?", answer "yes, Python allows it, but keep each variable's
  type consistent so your code is easy to read" and move on.
- `print` with commas is enough for today; f-strings come on Day 04.
