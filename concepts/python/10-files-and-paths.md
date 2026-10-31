# Files and Paths

**What it is:** `open()` reads and writes text files; `pathlib.Path` builds file paths and checks folders.
**Why it exists:** variables vanish when the program stops. Files let you load data and keep results for next time.

**Taught on:** [Day 23](../../weeks/week-05/day-23-reading-files/lesson.md) (reading) ·
[Day 24](../../weeks/week-05/day-24-writing-files-pathlib/lesson.md) (writing, `pathlib`)

## Syntax at a glance

| You want to… | Write | Note |
|--------------|-------|------|
| Read everything | `with open("notes.txt", encoding="utf-8") as f:` `text = f.read()` | one big string |
| Read line by line | `for line in f:` `line = line.strip()` | each line ends with `"\n"` |
| Overwrite / create | `open("out.txt", "w", encoding="utf-8")` | `"w"` **empties** the file first |
| Add to the end | `open("log.txt", "a", encoding="utf-8")` | keeps old content |
| Write text | `f.write("Total: 42\n")` | you add the `"\n"` yourself; only strings |
| A path object | `from pathlib import Path` · `p = Path("data") / "marks.txt"` | `/` joins path parts on every OS |
| Does it exist? | `p.exists()` | `True` / `False` |
| Make a folder | `Path("reports").mkdir(exist_ok=True)` | no error if it is already there |
| Quick read / write | `p.read_text(encoding="utf-8")`, `p.write_text(text, encoding="utf-8")` | opens and closes for you |

**`with` closes the file for you** when the indented block ends, even if an error happens.
**Relative paths** start from the folder you run the program in (the notebook's folder in Jupyter).
From a lesson notebook the course datasets are at `Path("../../../datasets")`.

## Examples

Run example 1 first: it creates the file the next examples read.

### 1. Create a small file

```python
from pathlib import Path

Path("shopping.txt").write_text("milk\neggs\nbread\n", encoding="utf-8")
print(Path("shopping.txt").exists())   # True
```

### 2. Read the whole file

```python
with open("shopping.txt", encoding="utf-8") as f:
    text = f.read()
print(text.split())   # ['milk', 'eggs', 'bread']
print(len(text))      # 16   (letters plus three "\n")
```

### 3. Loop over lines and strip the newline

```python
count = 0
with open("shopping.txt", encoding="utf-8") as f:
    for line in f:
        count += 1
        print(f"{count}. {line.strip()}")
# 1. milk
# 2. eggs
# 3. bread
```

### 4. Write `"w"`, then append `"a"`

```python
from pathlib import Path

with open("study_log.txt", "w", encoding="utf-8") as f:
    f.write("Mon: 30 min\n")
with open("study_log.txt", "a", encoding="utf-8") as f:
    f.write("Tue: 45 min\n")
print(Path("study_log.txt").read_text(encoding="utf-8"))
# Mon: 30 min
# Tue: 45 min
```

### 5. Folders and paths with `pathlib`

```python
from pathlib import Path

reports = Path("reports")
reports.mkdir(exist_ok=True)
report_file = reports / "week1.txt"
report_file.write_text("Total spent: 182.40\n", encoding="utf-8")
print(report_file.exists())                         # True
print(report_file.read_text(encoding="utf-8").strip())   # Total spent: 182.40
```

### 6. Check before reading

```python
from pathlib import Path

settings = Path("settings.txt")
if settings.exists():
    print(settings.read_text(encoding="utf-8"))
else:
    print("No settings yet, using defaults")   # No settings yet, using defaults
```

### 7. Reading a course dataset from a lesson notebook

```python
# (needs a file)
from pathlib import Path

DATA_DIR = Path("../../../datasets")
lines = (DATA_DIR / "expenses.csv").read_text(encoding="utf-8").split("\n")
print(lines[0])   # date,category,description,amount,payment_method
```

### 8. A file that is not there

```python
# (shows an error)
with open("missing.txt", encoding="utf-8") as f:
    print(f.read())
# FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'
```

## Common mistakes

| Mistake | Error / symptom | Fix |
|---------|-----------------|-----|
| Opening with `"w"` to add a line | old content is gone | Use `"a"` to append |
| `f.write("line")` with no `"\n"` | everything ends up on one line | `f.write("line\n")` |
| Not stripping lines | items like `'milk\n'`; blank lines between printed lines | `line.strip()` |
| Path relative to the wrong folder | `FileNotFoundError: [Errno 2] No such file or directory: …` | Check where you run from; print `Path("x.txt").exists()` |
| `f.write(42)` | `TypeError: write() argument must be str, not int` | `f.write(str(42) + "\n")` or an f-string |
| Reading after the `with` block ended | `ValueError: I/O operation on closed file.` | Do the reading inside the indented block |
| No `encoding="utf-8"` | `UnicodeDecodeError` on some computers (accents, emoji) | Always pass `encoding="utf-8"` |
| Windows path in a normal string: `"C:\new\data.txt"` | `\n` becomes a newline, path breaks | Use `Path("C:/new/data.txt")` or `/` between `Path` parts |

## See also

- [11 Exceptions](11-exceptions.md): handling `FileNotFoundError` without crashing
- [14 CSV and JSON](14-csv-and-json.md): structured files
- [12 Modules, uv and testing](12-modules-uv-and-testing.md): `if __name__ == "__main__":` for scripts that write files
