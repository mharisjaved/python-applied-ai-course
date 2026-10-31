"""grades: small functions we write tests for on Day 29.

The tests live in test_grades.py. Run them from this folder with:

    uv run pytest
"""


def average(marks):
    """Return the mean of a list of marks, or 0.0 for an empty list."""
    if len(marks) == 0:
        return 0.0
    return sum(marks) / len(marks)


def letter_grade(score):
    """Return "A" (80+), "B" (65+), "C" (50+) or "F" for a score from 0 to 100.

    Raise ValueError if the score is below 0 or above 100.
    """
    if score < 0 or score > 100:
        raise ValueError(f"score must be between 0 and 100, got {score}")
    if score >= 80:
        return "A"
    elif score >= 65:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"


def parse_marks(text):
    """Turn text like "78, 85, 92" into a list of ints. Empty text gives [].

    Raise ValueError if a part is not a whole number.
    """
    if text.strip() == "":
        return []
    marks = []
    for part in text.split(","):
        marks.append(int(part))
    return marks
