# Day 24: Writing Files and `pathlib`

**Week 5 · Session 24 of 60 · Planned 75 min** · Previous: [Day 23](../day-23-reading-files/lesson.md) · Next: [Day 25](../day-25-exceptions/lesson.md)

## Objectives

By the end of this lesson students can:

1. Write text to a file with `open(path, "w")` and `.write()`, adding newlines themselves.
2. Explain the difference between `"w"` (replace) and `"a"` (append), and predict a file's contents after a mix of both.
3. Build paths with `Path("output") / "notes.txt"`, check them with `.exists()`, and create folders with `.mkdir(exist_ok=True)`.
4. Read and write whole files with `.read_text()` / `.write_text()`.
5. Say which folder a relative path starts from (the working directory, `Path.cwd()`).

**Prior knowledge:** reading files with `with open(...)`, `.strip()`, relative paths, `FileNotFoundError`
(Day 23), `import random` (Day 14), f-strings (Days 04–05), functions (Days 16–19), comprehensions (Day 22).

**New today and introduced explicitly:** `from pathlib import Path`. Present it as "taking one tool from Python's
standard library, like we did with `import random`". The general rules of `import` come on Day 26.

**Files:** `demo.ipynb` · `practice.ipynb` · `solutions.ipynb`. The notebooks only create **new** files next to
themselves (`greeting.txt`, `no_newlines.txt`, `trap_demo.txt`, `predict.txt`, `output/`, `reports/`). Students can
delete them at any time.

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: "what happens to variables when the kernel restarts?" | core |
| 0:05–0:15 | Writing with `"w"`, `.write()` and newlines | core |
| 0:15–0:25 | `"w"` vs `"a"`: the data-loss trap | core |
| 0:25–0:40 | `pathlib.Path`: `/`, `.exists()`, `.mkdir()`, `.read_text()`, `.write_text()` | core |
| 0:40–0:43 | The working directory | core |
| 0:43–0:47 | Common mistakes (live debugging) | core |
| 0:47–0:52 | Real-world example: the journal saver + kernel-restart test | optional (skip for 60 min, students build it in Ex 5) |
| 0:52–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +15 min | Exercise 6 (challenge): expense logger + report | optional (90-min session) |

**For 60 min:** skip demo section 7 and the `.name/.suffix/.parent` cell; set Exercise 5 as homework.

## 1. Warm-up (5 min)

In the demo notebook from yesterday (or any notebook): create `score = 42`, **restart the kernel**, then
`print(score)` → `NameError`. Ask: "Where did 42 go? How do apps remember your settings after you close them?"
(*Memory is wiped; files on disk survive.*)

Retrieval (Day 23): "What does this print if `items.txt` contains `pen` and `ruler` on two lines?"

```python
with open("items.txt", encoding="utf-8") as f:
    print(f.read().count("\n"))
```

(*`2`: one newline per line.*)

## 2. Writing with `"w"` (10 min)

**Intuition:** the second argument of `open()` is the **mode**: what you plan to do with the file. Yesterday we
used the default `"r"` (read) without writing it.

```python
with open("greeting.txt", "w", encoding="utf-8") as out_file:
    out_file.write("Hello from Python!\n")
    out_file.write("This line was written by a program.\n")
```

Show the new file appearing in the VS Code explorer, open it, then read it back in Python (demo section 2).

**Prediction question:** three `.write()` calls with `"apples"`, `"bananas"`, `"cherries"` and no `\n` → the file
contains `applesbananascherries`. Key sentence: **`.write()` writes exactly what you give it; `print()` adds a
newline for you, `.write()` never does.**

Then the standard "list to file" pattern:

```python
for item in items:
    out_file.write(f"{item}\n")
```

## 3. `"w"` vs `"a"`: the data-loss trap (10 min)

This is the most important 10 minutes of the day. Do it slowly on a **new** file (`trap_demo.txt`) so nothing real
is at risk.

1. Write three "important notes" with `"w"` and read them back.
2. **Prediction question:** "We open the same file with `"w"` again and write `Note 4`. What is in the file now?"
   Let students vote: (a) notes 1–4, (b) only note 4, (c) an error. Answer: **(b)**. `"w"` empties the file
   the moment `open()` runs, before anything is written. No warning, no undo.
3. Open with `"a"` and write `Note 5` → `Note 4`, `Note 5`.

**Analogy:** `"w"` is a fresh, blank page that **replaces** the old page in the folder. `"a"` is adding a line at the
bottom of the existing page.

Put the mode table from the demo on the board and leave it there all lesson:

| Mode | If the file exists | If it does not exist |
|------|--------------------|----------------------|
| `"r"` (default) | read from the start | `FileNotFoundError` |
| `"w"` | **emptied first** | created |
| `"a"` | add to the end | created |

Practical rule: logs, journals, history → `"a"`. Reports that are rebuilt from data each time → `"w"`.
Warn about notebooks: **running an `"a"` cell twice appends twice.**

## 4. `pathlib.Path` (15 min)

**Why:** so far a path is just a string like `"output/notes.txt"`. Strings cannot tell us whether the file exists,
cannot create folders, and Windows uses `\` instead of `/`. A `Path` object can do all of that.

**Introducing the import** (say it explicitly): "Python ships with a *standard library* of extra tools. On Day 14 we
wrote `import random` to use one. Today we write `from pathlib import Path`: *from* the `pathlib` module, take the
`Path` tool. We will look at imports properly on Day 26."

```python
from pathlib import Path

output_dir = Path("output")
notes_path = output_dir / "notes.txt"
print(notes_path)                 # output/notes.txt (output\notes.txt on Windows)
```

- `/` between paths **joins** them. It is not division: Python picks the right separator for the computer.
- **Prediction question:** "Does the `output` folder exist now?" (*`False`. A `Path` is only a description of a
  place; creating it does not touch the disk.*)
- `output_dir.mkdir(exist_ok=True)` creates it; `exist_ok=True` = "fine if it is already there".
- `notes_path.write_text(text, encoding="utf-8")` = open with `"w"` + write + close. **It replaces the file.**
- `notes_path.read_text(encoding="utf-8")` = open + read + close.
- To **append** with a `Path`, use `open(notes_path, "a", encoding="utf-8")`. `open()` accepts `Path` objects.
- `.name` → `notes.txt`, `.suffix` → `.txt`, `.parent` → `output`.

## 5. The working directory (3 min)

`print(Path.cwd())` shows where relative paths start. In a notebook: the notebook's folder. With
`uv run journal.py`: the folder the terminal is in. Connect to Day 23: the same script can write `output/` into a
different place depending on where you run it. Optional: show it live in the terminal from two different folders.

## 6. Common mistakes (live debugging, 4 min)

Run the tagged cells in demo section 6:

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| `notes_file.write(125.5)` | `TypeError: write() argument must be str, not float` | Files hold text. Use an f-string: `f"{total}\n"` |
| writing to `Path("reports") / "summary.txt"` | `FileNotFoundError: ... 'reports/summary.txt'` | Writing creates **files**, not **folders**. `.mkdir(exist_ok=True)` first |
| `output_dir.mkdir()` a second time | `FileExistsError: [Errno 17] File exists: 'output'` | Add `exist_ok=True` |
| `open(path)` then `.write(...)` | `UnsupportedOperation: not writable` | The default mode is `"r"`. Say `"w"` or `"a"` |
| `"w"` inside a loop | no error, only the last line survives | Each `open(..., "w")` empties the file. Open once before the loop, or use `"a"` |

## 7. Real-world example: a journal that remembers (5 min, optional)

Demo section 7 builds three functions: `add_entry(path, date, text)` (appends, creating the folder with
`path.parent.mkdir(exist_ok=True)`), `read_entries(path)` (returns `[]` if the file does not exist yet, which is
defensive code without `try`), and `show_journal(path)`. The last cell uses `input()` to add the user's own entry.

```
Journal: 3 entries
1. 2026-11-12 | Learned the difference between w and a
2. 2026-11-12 | The / operator joins folder and file names
3. 2026-11-12 | Remember: mode w empties the file first
```

**The payoff moment:** restart the kernel, run only the `import` and function cells, then `show_journal(journal_path)`:
the entries are still there. Then run the "add" cell again and show the journal growing (because of `"a"`).

## 8. Practice (18 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict the file | `"w"` vs `"a"`, `.write()` without `\n` | recall / predict |
| 2 Save a shopping list | `mkdir`, write a list one per line, `.read_text()` | application |
| 3 Fix the broken code | non-text write, missing `\n`, missing folder, `"w"` in a loop | modification |
| 4 Before and after | `.exists()`, `.write_text()`, `.name`, `.suffix`, why files persist | application |
| 5 Notes saver | append + count with print-checks, repeatable tests | problem solving |
| 6 Expense logger (challenge) | log with `"a"`, parse back, write a formatted report | challenge |

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

While circulating, look for:
- students who change `"w"` to `"a"` in Exercise 3d and then run the cell several times. Ask them to count the
  lines and explain;
- `count_notes` returning 3 instead of 2 (the empty item after the last `\n`);
- forgetting `encoding="utf-8"` on `.write_text()`/`.read_text()`. Same rule as `open()`;
- confusion when `Exists before` prints `True` on a second run. Great: it proves the file survived.

## 9. Recap and exit ticket (5 min)

Recap:
1. `"w"` replaces, `"a"` appends; `.write()` takes text only and adds no newline.
2. `Path("folder") / "file.txt"` builds a path; `.exists()`, `.mkdir(exist_ok=True)`, `.read_text()`, `.write_text()`.
3. Relative paths start from the working directory.

**Exit ticket:** `log.txt` does not exist yet. What does it contain after this code?

```python
for word in ["red", "green"]:
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(word)
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("\nblue\n")
```

Answer: two lines, `redgreen` and `blue`. `"a"` creates the file and keeps adding, and there is no `\n` between
`red` and `green`.

## Homework (25 min)

Finish Exercise 5. Then write `daily_log.py` (a normal `.py` file in the day folder) that asks for one sentence with
`input()` and appends it with a number to `output/daily_log.txt`, then prints the whole log. Run it three times with
`uv run daily_log.py` and bring the file to class.

## Next class

Day 25: **exceptions**. Today we avoided crashes by checking first (`.exists()`, `exist_ok=True`). Tomorrow we learn
the other strategy, `try`/`except`: attempt the risky thing and handle the failure (bad numbers from `input()`,
missing files). Day 25 ends with the Week 5 checkpoint.

## Instructor notes

- Do not teach other modes (`"x"`, `"r+"`, `"b"`), `os`/`os.path`, `shutil`, deleting files (`.unlink()`) or
  `parents=True`. If a student asks how to create nested folders, mention `mkdir(parents=True, exist_ok=True)`
  privately.
- `.write()` returns the number of characters written. In a notebook, if `.write_text(...)` is the **last line** of
  a cell, that number appears as output (e.g. `44`). If a student asks, explain it and move on.
- `print(type(notes_path))` shows `PosixPath` on Mac/Linux and `WindowsPath` on Windows. Not worth showing.
- Never demonstrate `"w"` on a file students care about (homework, notes). Always use a fresh practice file.
- Some editors (and OneDrive) lock open files on Windows; if a write fails with `PermissionError`, close the file in
  the editor and try again.
- Slow students: give them the `with open(..., "a")` line for Exercise 5 and let them focus on `count_notes`.
- Fast students: Exercise 6, then add a function that deletes nothing but **archives**: copies the log's contents
  into `output/archive.txt` (using `"a"`) and then empties the log with `"w"`.
