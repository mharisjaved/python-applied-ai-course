"""Tests for grades.py.

Run them from this folder with:  uv run pytest
pytest finds this file because its name starts with test_, and runs every function whose
name starts with test_. A test passes if none of its asserts fail.
"""

import pytest

from grades import average, letter_grade, parse_marks


# ---- average -------------------------------------------------------------

def test_average_normal():
    assert average([70, 80, 90]) == 80


def test_average_single_mark():
    assert average([65]) == 65


def test_average_empty_list_is_zero():
    assert average([]) == 0.0


# ---- letter_grade --------------------------------------------------------

def test_letter_grade_normal():
    assert letter_grade(72) == "B"


def test_letter_grade_boundaries():
    assert letter_grade(80) == "A"
    assert letter_grade(79) == "B"
    assert letter_grade(65) == "B"
    assert letter_grade(64) == "C"
    assert letter_grade(50) == "C"
    assert letter_grade(49) == "F"


def test_letter_grade_extremes():
    assert letter_grade(0) == "F"
    assert letter_grade(100) == "A"


def test_letter_grade_above_100_raises():
    with pytest.raises(ValueError):
        letter_grade(101)


def test_letter_grade_negative_raises():
    with pytest.raises(ValueError):
        letter_grade(-1)


# ---- parse_marks ---------------------------------------------------------

def test_parse_marks_normal():
    assert parse_marks("78, 85, 92") == [78, 85, 92]


def test_parse_marks_empty_text():
    assert parse_marks("") == []


def test_parse_marks_word_raises():
    with pytest.raises(ValueError):
        parse_marks("78, eighty, 92")
