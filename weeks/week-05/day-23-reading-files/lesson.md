# Day 23: Reading Text Files

**Week 5 · Session 23 of 60 · Planned 75 min** · Previous: [Day 22](../day-22-comprehensions/lesson.md) · Next: [Day 24](../day-24-writing-files-pathlib/lesson.md)

## Objectives

By the end of this lesson students can:

1. Open a text file with `with open(path, encoding="utf-8") as f:` and explain what `with` does for them.
2. Read a whole file with `.read()` or go through it line by line with a `for` loop.
3. Clean lines with `.strip()`, skip blank lines, and split a line into fields with `.split(",")`.
4. Explain a relative path (where Python starts looking) and diagnose a `FileNotFoundError`.
5. Compute simple statistics (lines, words, counts per name) from a file.

**Prior knowledge:** `\n`, `.strip()`, `.count()` (Day 04), slicing (Day 05), `.split()`/`" ".join()` and
unpacking (Day 07), `.get()` (Day 08), counting with a dict and `enumerate` (Day 12), `continue` (Day 14),
functions returning values (Day 17), built-ins and `sorted(key=)` (Day 21), comprehensions (Day 22).

**Files:** `demo.ipynb` · `practice.ipynb` · `solutions.ipynb` · `data/class_diary.txt` (demo, Ex 6),
`data/attendance.txt` (demo, Ex 5), `data/shopping_list.txt` (Ex 1, 2, 4), `data/temperatures.txt` (Ex 3, 4).
The notebooks only **read** these files. Students must keep the `data` folder next to the notebooks.

## Timing

| Time | Segment | Core / optional |
|------|---------|-----------------|
| 0:00–0:05 | Warm-up: "where does real data come from?" + comprehension recall | core |
| 0:05–0:18 | `open`, `with`, `.read()`, `encoding` | core |
| 0:18–0:30 | Looping over lines, `\n`, `.strip()`, skipping blanks | core |
| 0:30–0:38 | Lines with fields: `split(",")` + counting | core |
| 0:38–0:43 | Relative paths and the working directory | core |
| 0:43–0:48 | Common mistakes (live debugging) | core |
| 0:48–0:52 | Real-world example: statistics for a text file | optional (skip for 60 min) |
| 0:52–0:70 | Practice exercises 1–5 | core |
| 0:70–0:75 | Recap + exit ticket | core |
| +15 min | Exercise 6 (challenge), or open the data files in VS Code and compare with Python's view | optional (90-min session) |

**For 60 min:** skip demo section 7 and the `cp1252` demonstration (just state the rule), and set Exercise 5 as homework.

## 1. Warm-up (5 min)

Ask: "Where does the data in real programs come from? Who types `marks = [72, 85, 64]`?" Collect answers: files,
databases, websites, sensors. Today: **text files**, the simplest and most common.

Retrieval (Day 22): "Write a comprehension that turns `["  rice\n", "milk  \n"]` into `['rice', 'milk']`."
(*`[item.strip() for item in items]`.*) Tell them they will write exactly this today.

Before the demo, open `data/class_diary.txt` in VS Code so students see that a text file is nothing special: just
lines of text.

## 2. `open`, `with`, `.read()` and `encoding` (13 min)

**Analogy:** reading a library book. You **open** it, read, and must **close** it again (and return it). Forgetting
to close is a real bug in long-running programs. `with` is like a librarian who closes the book for you the moment
you leave the reading room (the indented block).

```python
with open("data/class_diary.txt", encoding="utf-8") as diary_file:
    text = diary_file.read()
print(text)
```

Walk through the table in demo section 2: `open(...)` connects, `encoding="utf-8"` decodes, `with ... as name`
gives the open file a name and closes it automatically, `.read()` returns **one string**.

**Prediction question:** `type(text)` → `<class 'str'>`; `text.count("\n")` → `11` (one per line). The file is
541 characters long.

**Why `encoding="utf-8"`** (demo section 2, second part): opening the same file with `encoding="cp1252"` (the
default on many Windows machines) turns `Zoë` into `ZoÃ«` and `café` into `cafÃ©`, **without an error**. Rule:
**always write `encoding="utf-8"`**. On Mac/Linux it usually works without it, and that is exactly how the bug
reaches a Windows classmate.

## 3. Looping over lines (12 min)

A file object can go straight into a `for` loop, one line per turn.

**Prediction question** (demo section 3): "What will `for line in diary_file: print(line)` look like?" Most students
expect normal output. It is **double-spaced**. Ask why before explaining: each `line` keeps its `\n`, and `print`
adds another.

Make the invisible visible by collecting the lines into a list:
`['Week 5 class diary\n', '\n', 'Monday: We learned ...\n']`. Even the "empty" line is `'\n'`.

Then the standard pattern, combining Day 22 and Day 04:

```python
with open("data/class_diary.txt", encoding="utf-8") as diary_file:
    lines = [line.strip() for line in diary_file]
print(len(lines))   # 11
```

and numbering + skipping blanks:

```python
for number, line in enumerate(lines, start=1):
    if line == "":
        continue
    print(f"{number:>2}: {line[:45]}")
```

Key points:
- `.read()` = whole file as one string (good for counting words). `for line in f` = one line at a time (good for
  processing records).
- Lines **always** come with `\n` (except possibly the last). Strip before comparing: `"milk\n" == "milk"` is `False`.
- Read the file **once** into a list, then work with the list. Simple and fast for files of this size.

## 4. Lines with fields: `split(",")` (8 min)

Show the format of `data/attendance.txt`: `2026-11-02,Asha,present`. Each line is a small record with three
**fields** separated by commas.

**Prediction question:** `"2026-11-02,Asha,present".split(",")` → `['2026-11-02', 'Asha', 'present']`.
Then unpack: `date, name, status = sample.split(",")` (Day 07).

Demo section 4 prints the absences (4 lines) and then counts them per student with the Day 12 pattern:

```python
absences[name] = absences.get(name, 0) + 1
# {'Sara': 1, 'Omar': 2, 'Bilal': 1}
```

Point out the **blank line in the middle of the file**. Without `if line == "": continue`, the line `""` splits into
`['']`, and unpacking one value into three names fails with `ValueError: not enough values to unpack (expected 3,
got 1)`. Real files are messy; check before you split. (The `csv` module on Day 36 handles commas inside fields and
header rows; today's files are deliberately simple.)

## 5. Relative paths and the working directory (5 min)

Draw the folder tree on the board:

```
python-course/
├── datasets/README.md
└── weeks/week-05/day-23-reading-files/
    ├── demo.ipynb
    └── data/class_diary.txt
```

- A **relative path** starts from the **working directory**. In a VS Code notebook, that is the notebook's folder. With
  `uv run script.py` in a terminal, it is the folder the terminal is currently in.
- `..` means "one folder up". Demo section 5 reads `../../../datasets/README.md` → `# Course datasets`.

Optional live terminal demonstration: write a two-line `read_diary.py` in the day folder, run it with
`uv run read_diary.py` from the day folder (works), then `cd ..` and run `uv run day-23-reading-files/read_diary.py`
→ `FileNotFoundError`. Same code, different working directory. Tomorrow `Path.cwd()` will show the working
directory directly.

## 6. Common mistakes (live debugging, 5 min)

| Mistake | Error | How to explain it |
|---------|-------|-------------------|
| typo: `"data/atendance.txt"` | `FileNotFoundError: [Errno 2] No such file or directory: 'data/atendance.txt'` | The message repeats the path Python tried. Compare it letter by letter |
| missing folder: `"class_diary.txt"` | `FileNotFoundError` | Python looked in the working directory, not inside `data/` |
| using the file after the `with` block | `ValueError: I/O operation on closed file.` | `with` closed it when the indentation ended. Indent the loop |
| `.read()` twice | no error, second result is `""` (`541 0`) | Reading moves a bookmark to the end. Store the text in a variable once |
| `total + line` | `TypeError: unsupported operand type(s) for +: 'int' and 'str'` | Lines are text. `float(line)` / `int(line)` first |

Say explicitly: today we **read** `FileNotFoundError` messages; on Day 25 we will **handle** them so the program
does not crash.

## 7. Real-world example: statistics for a text file (4 min, optional)

Demo section 7 splits the job into `read_lines(path)` and `print_statistics(lines)`. One new detail:
`.strip(".,!?():")` removes **those characters** from both ends, so `"line."` and `"line"` count as one word.
Expected output:

```
Lines: 11 (8 with text)
Words: 90
Average words per text line: 11.2
Longest word: comprehensions
Times 'line' appears: 3
```

Ask: "Which line would you change to analyse a different file?" (*Only the path in the call.*) That is the benefit
of putting reading and analysing in separate functions.

## 8. Practice (18 min)

| Exercise | Skill | Level |
|----------|-------|-------|
| 1 Predict, then look | lines include blanks and `\n` | recall / predict |
| 2 A clean shopping list | strip + filter + `enumerate` | application |
| 3 Temperature statistics | `float()` per line + Day 21 built-ins | application |
| 4 Fix the broken code | missing folder, closed file, text + number | modification |
| 5 Attendance report | `split(",")`, two counting dicts, percentages | problem solving |
| 6 Top words (challenge) | read → clean → count → sort by count | challenge |

Expected outcome: everyone completes 1–4; most complete 5; fast students try 6.

While circulating, look for:
- notebooks opened from the wrong folder (VS Code opened on the course root is fine; the notebook's own folder is
  still the working directory). If `FileNotFoundError` appears for a correct path, check that the `data` folder
  was copied;
- `if status == "present" or "late":` (always true, Day 09) in Exercise 5;
- numbering that skips (1, 2, 4…) in Exercise 2, because blank lines were numbered before being skipped.

## 9. Recap and exit ticket (5 min)

Recap:
1. `with open(path, encoding="utf-8") as f:` opens a file and closes it automatically.
2. `.read()` = one big string; `for line in f:` = one line at a time, `\n` included.
3. Strip, skip blanks, then `split(",")`.
4. Relative paths start from the working directory; `FileNotFoundError` = wrong name, folder or starting point.

**Exit ticket:** a file `scores.txt` contains three lines: `10`, `20` and an empty line. What does this print?

```python
with open("scores.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f]
print(len(lines), [line for line in lines if line != ""])
```

Answer: `3 ['10', '20']`. Three lines including the empty one; the numbers are still **strings**.

## Homework (20 min)

Finish Exercise 5. Then create your own text file `my_week.txt` (5–10 lines about your week) next to the practice
notebook and use `read_lines` + `print_statistics` from demo section 7 on it. Include at least one word with an
accent or an emoji to check your encoding.

## Next class

Day 24: **writing files** with modes `"w"` and `"a"`, and `pathlib.Path` for building paths and checking whether a
file exists. Today's `FileNotFoundError` in the wrong folder will come back as the reason we use `Path`.

## Instructor notes

- Out of scope today: `.readline()`, `.readlines()`, `.seek()`, binary mode, file modes other than reading (tomorrow),
  `os.path`, and the `csv` module (Day 36). If students find `.readlines()` online, it is fine but the loop or
  comprehension is all they need.
- `return` inside a `with` block (in `read_lines`) is safe: the file is still closed. Mention it only if asked.
- Character vs byte length: the diary is 541 characters but 543 bytes on disk (`ë` and `é` take 2 bytes each in
  UTF-8). Only interesting for curious students.
- Windows students with OneDrive-synced folders sometimes have paths with spaces or unusual characters. Relative
  paths avoid most of that pain. Another reason to keep `data/` next to the notebook.
- Slow students: give them the reading code for Exercise 5 and let them focus on the counting.
- Fast students: Exercise 6, then ask them to make `top_words` ignore a list of "stop words" they choose.
