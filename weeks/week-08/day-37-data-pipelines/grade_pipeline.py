"""Grade-report pipeline: load -> clean -> analyse -> report.

Run it from this folder:   uv run python grade_pipeline.py
Run its tests:             uv run pytest -q
"""

import csv
import json
from pathlib import Path

DATA_FILE = Path("data") / "grades.csv"   # UPPER_CASE name = a setting that never changes
OUTPUT_DIR = Path("output")


# ---------- Stage 1: load ----------

def load_rows(path):
    """Read a CSV file and return its rows as a list of dicts (all values are text)."""
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ---------- Stage 2: clean ----------

def is_number(text):
    """Return True if text can be converted to a float."""
    try:
        float(text)
        return True
    except ValueError:
        return False


def clean_row(row):
    """Return a tidy copy of one raw row, or raise ValueError saying what is wrong."""
    name = row["student"].strip().title()
    subject = row["subject"].strip().lower()
    score_text = row["score"].strip()
    if name == "":
        raise ValueError("missing student name")
    if score_text == "":
        raise ValueError("missing score")
    if not is_number(score_text):
        raise ValueError(f"score is not a number: '{score_text}'")
    score = float(score_text)
    if score < 0 or score > 100:
        raise ValueError(f"score out of range: {score_text}")
    return {"student": name, "subject": subject, "score": score}


def clean_rows(rows):
    """Split raw rows into (clean_rows, problems). Each problem names its line in the file."""
    clean = []
    problems = []
    for line_number, row in enumerate(rows, start=2):   # line 1 of the file is the header
        try:
            clean.append(clean_row(row))
        except ValueError as error:
            problems.append(f"line {line_number}: {error}")
    return clean, problems


# ---------- Stage 3: analyse ----------

def letter_grade(average):
    """Turn an average score (0-100) into a letter grade."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"


def average(numbers):
    """Return the mean of a non-empty list of numbers."""
    return sum(numbers) / len(numbers)


def group_scores(clean, column):
    """Group scores by one column: {value_of_column: [score, score, ...]}."""
    groups = {}
    for row in clean:
        key = row[column]
        if key not in groups:
            groups[key] = []
        groups[key].append(row["score"])
    return groups


def student_average(item):
    """Sort key for (name, info) pairs: the student's average."""
    return item[1]["average"]


def analyse(clean):
    """Return a summary dict: per-student results, subject averages, ranking, class average."""
    students = {}
    for name, scores in group_scores(clean, "student").items():
        student_avg = round(average(scores), 2)
        students[name] = {"average": student_avg, "grade": letter_grade(student_avg), "subjects": len(scores)}

    subjects = {}
    for subject, scores in group_scores(clean, "subject").items():
        subjects[subject] = round(average(scores), 2)

    ranked = sorted(students.items(), key=student_average, reverse=True)
    all_scores = [row["score"] for row in clean]
    return {
        "students": students,
        "subjects": subjects,
        "ranking": [name for name, info in ranked],
        "class_average": round(average(all_scores), 2),
    }


# ---------- Stage 4: report ----------

def build_report(summary, problems):
    """Return the whole report as one string. The caller decides whether to print or save it."""
    lines = ["GRADE REPORT", "=" * 38, "Rank  Student          Average  Grade"]
    for rank, name in enumerate(summary["ranking"], start=1):
        info = summary["students"][name]
        lines.append(f"{rank:<6}{name:<16}{info['average']:>8.2f}  {info['grade']}")
    lines.append("")
    lines.append("Subject averages")
    for subject, subject_avg in summary["subjects"].items():
        lines.append(f"  {subject:<10}{subject_avg:>7.2f}")
    lines.append(f"Class average: {summary['class_average']:.2f}")
    lines.append("")
    lines.append(f"Rows skipped ({len(problems)}):")
    for problem in problems:
        lines.append(f"  {problem}")
    return "\n".join(lines)


def save_text(text, path):
    """Save text to a file, creating its folder if needed."""
    path.parent.mkdir(exist_ok=True)
    path.write_text(text, encoding="utf-8")


def save_json(data, path):
    """Save data as pretty-printed JSON, creating the folder if needed."""
    path.parent.mkdir(exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# ---------- main: connect the stages ----------

def main(data_path=DATA_FILE):
    """Run the pipeline: load -> clean -> analyse -> report."""
    try:
        rows = load_rows(data_path)
    except FileNotFoundError:
        print(f"Cannot find {data_path}. Run this from the day-37 folder.")
        return
    clean, problems = clean_rows(rows)
    summary = analyse(clean)
    report = build_report(summary, problems)
    print(report)
    save_text(report, OUTPUT_DIR / "grade_report.txt")
    save_json(summary, OUTPUT_DIR / "grade_summary.json")
    print(f"\nSaved {OUTPUT_DIR / 'grade_report.txt'} and {OUTPUT_DIR / 'grade_summary.json'}")


if __name__ == "__main__":
    main()
