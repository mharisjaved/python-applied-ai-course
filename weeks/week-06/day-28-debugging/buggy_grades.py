"""Class grade report: a program with bugs to practise debugging (Day 28).

Run it from this folder:

    uv run buggy_grades.py

When every bug is fixed, the output should be:

    Class report
    Asha     85.0  pass
    Bilal    54.7  pass
    Sara     91.0  pass
    Omar      0.0  FAIL
    Mei      50.0  pass
    Passed: 4 of 5
"""

PASS_MARK = 50

class_marks = {
    "Asha": [78, 85, 92],
    "Bilal": [55, 61, 48],
    "Sara": [90, 88, 95],
    "Omar": [],
    "Mei": [48, 52, 50],
}


def average(marks):
    """Return the mean of a list of marks, or 0 for an empty list."""
    total = 0
    for mark in marks:
        total = mark
    return total / len(marks)


def has_passed(avg):
    """Return True if the average reaches the pass mark (exactly 50 passes)."""
    return avg > PASS_MARK


def build_report(marks_by_student):
    """Return a list of report lines and the number of students who passed."""
    lines = []
    passed = 0
    for name, marks in marks_by_student.items():
        avg = average(marks)
        if has_passed(avg):
            status = "pass"
            passed += 1
        else:
            status = "FAIL"
        lines.append(f"{name:<8}{avg:>5.1f}  {status}")
    return lines, passed


def main():
    print("Class report")
    lines, passed = build_report(class_marks)
    for line in lines:
        print(line)
    print(f"Passed: {passed} of {len(class_marks)}")


if __name__ == "__main__":
    main()
