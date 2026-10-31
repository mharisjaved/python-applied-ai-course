"""Tests for grade_pipeline.py: one small test per stage, no files needed.

Run from this folder:  uv run pytest -q
"""

import pytest

from grade_pipeline import analyse, build_report, clean_row, clean_rows, letter_grade


def test_clean_row_tidies_names_and_subjects():
    row = {"student": " asha khan", "subject": "English ", "score": "91"}
    assert clean_row(row) == {"student": "Asha Khan", "subject": "english", "score": 91.0}


def test_clean_row_rejects_missing_score():
    with pytest.raises(ValueError):
        clean_row({"student": "Bilal Ahmed", "subject": "science", "score": ""})


def test_clean_row_rejects_text_and_impossible_scores():
    with pytest.raises(ValueError):
        clean_row({"student": "Omar Farouk", "subject": "maths", "score": "absent"})
    with pytest.raises(ValueError):
        clean_row({"student": "Mei Chen", "subject": "maths", "score": "105"})


def test_clean_rows_keeps_good_rows_and_reports_bad_ones():
    rows = [
        {"student": "Ken Ito", "subject": "maths", "score": "80"},
        {"student": "Ken Ito", "subject": "science", "score": "n/a"},
    ]
    clean, problems = clean_rows(rows)
    assert len(clean) == 1
    assert problems == ["line 3: score is not a number: 'n/a'"]


def test_letter_grade_boundaries():
    assert letter_grade(90) == "A"
    assert letter_grade(89.99) == "B"
    assert letter_grade(60) == "D"
    assert letter_grade(59.5) == "F"


def test_analyse_small_example():
    clean = [
        {"student": "Ken Ito", "subject": "maths", "score": 80.0},
        {"student": "Ken Ito", "subject": "science", "score": 90.0},
        {"student": "Zara Malik", "subject": "maths", "score": 60.0},
    ]
    summary = analyse(clean)
    assert summary["students"]["Ken Ito"] == {"average": 85.0, "grade": "B", "subjects": 2}
    assert summary["subjects"] == {"maths": 70.0, "science": 90.0}
    assert summary["ranking"] == ["Ken Ito", "Zara Malik"]
    assert summary["class_average"] == 76.67


def test_report_lists_skipped_rows():
    summary = analyse([{"student": "Ken Ito", "subject": "maths", "score": 80.0}])
    report = build_report(summary, ["line 4: missing score"])
    assert "Ken Ito" in report
    assert "Rows skipped (1):" in report
    assert "line 4: missing score" in report
