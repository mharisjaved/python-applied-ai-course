# Day 01: Environment Setup and Hello World

**Week 1 · Session 1 of 60 · ✅ Taught on 2026-10-12** · Next: [Day 02](../day-02-variables/lesson.md)

> This is a **reconstructed record** of what was taught, so the course history is complete and the lesson can be
> re-used with a future cohort. Only the activities below were covered; nothing else should be assumed.

## What was covered

1. Introduction to Python development: what Python is, where it is used (automation, data, AI, web), what a program is.
2. Installing and configuring **Visual Studio Code** (with the Python extension).
3. Installing and configuring **uv** (Python version + project/environment manager).
4. Writing and running the first program, `hello.py`, containing `print("Hello, World!")`.

## Objectives (for re-teaching)

By the end of this lesson students can:

1. Explain in one sentence what the Python **interpreter** does (reads a `.py` file top to bottom and runs each instruction).
2. Create a uv project and a `hello.py` file in VS Code.
3. Run the file with `uv run hello.py` in the VS Code terminal and see the output.
4. Change the message and re-run it.

**Files:** [`hello.py`](hello.py) (the program) · `demo.ipynb` (the same ideas in notebook form, used when re-teaching
after notebooks exist) · `practice.ipynb` / `solutions.ipynb` (print-only warm-ups, also usable at the start of Day 02).

## Timing (as a 75-min session)

| Time | Segment |
|------|---------|
| 0:00–0:10 | What is programming? What is Python? Course overview (8 weeks Python, 4 weeks AI, projects) |
| 0:10–0:35 | Install VS Code + Python extension, install uv (students follow along) |
| 0:35–0:50 | `uv init`, open folder in VS Code, create `hello.py` |
| 0:50–0:65 | Run with `uv run hello.py`; change the message; fix first errors |
| 0:65–0:75 | Recap, what's next, troubleshooting stragglers |

## Steps used in class

Full commands per operating system: [setup/environment.md](../../../setup/environment.md).

```bash
uv --version                 # check uv is installed
uv init python-class         # create a project folder with a pyproject.toml
cd python-class
code .                       # open the folder in VS Code (or File → Open Folder)
```

Create `hello.py`:

```python
print("Hello, World!")
```

Run it in the VS Code terminal (**Terminal → New Terminal**):

```bash
uv run hello.py
```

Expected output:

```
Hello, World!
```

## Explanations that worked

- **Interpreter = a translator reading a recipe aloud.** It reads your file line by line, top to bottom, and carries out each instruction.
- **`print()` = "show this on the screen".** The text goes inside quotes so Python knows it is text, not code.
- **uv = the toolbox manager.** It makes sure every student has the same Python version and (later) the same libraries, so "it works on my laptop" problems disappear.

## Common Day 1 problems (see [setup/troubleshooting.md](../../../setup/troubleshooting.md))

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `uv: command not found` | terminal opened before install finished / PATH not refreshed | close and reopen the terminal (or VS Code); re-run the installer |
| `No such file or directory: hello.py` | terminal is in a different folder than the file | `cd` into the project folder; check with `ls` (macOS/Linux) or `dir` (Windows) |
| `SyntaxError: unterminated string literal` | missing closing quote | `print("Hello, World!")`, with quotes on both sides |
| `NameError: name 'Print' is not defined` | capital P | Python is case-sensitive: `print` |
| Nothing happens when clicking ▶ in VS Code | wrong interpreter selected | use the terminal command `uv run hello.py`, or select the `.venv` interpreter |

## Recap questions to open Day 02

1. What does the interpreter do with `hello.py`?
2. What command runs a Python file in our setup? (`uv run hello.py`)
3. Why does `print(Hello)` (no quotes) fail while `print("Hello")` works? (Without quotes Python looks for a name `Hello`. This leads straight into Day 02's variables.)

## Next class

[Day 02](../day-02-variables/lesson.md) introduces Jupyter notebooks in VS Code (students need `uv add ipykernel`
in their project), then variables and the four basic data types.
