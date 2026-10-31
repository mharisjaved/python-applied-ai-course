"""Tests for the core of the spending app. Run from this folder:  uv run pytest -q"""

import pytest

from spending import category_totals, filter_month, load_expenses, parse_amount, top_categories

# Tiny, hand-made data: we can work out every expected answer in our heads.
SAMPLE = [
    {"date": "2026-09-01", "category": "rent", "amount": 650.0},
    {"date": "2026-09-02", "category": "food", "amount": 12.5},
    {"date": "2026-09-03", "category": "food", "amount": 7.5},
    {"date": "2026-10-01", "category": "transport", "amount": 3.0},
]


def test_parse_amount_normal():
    assert parse_amount("12.50") == 12.5


def test_parse_amount_rejects_text_and_negative_numbers():
    with pytest.raises(ValueError):
        parse_amount("twelve")
    with pytest.raises(ValueError):
        parse_amount("-4")


def test_category_totals_adds_up_each_category():
    assert category_totals(SAMPLE) == {"rent": 650.0, "food": 20.0, "transport": 3.0}


def test_category_totals_of_nothing_is_empty():
    assert category_totals([]) == {}


def test_filter_month_keeps_only_that_month():
    september = filter_month(SAMPLE, "2026-09")
    assert len(september) == 3
    assert filter_month(SAMPLE, "2025-01") == []


def test_top_categories_biggest_first_and_skip_fixed():
    totals = category_totals(SAMPLE)
    assert top_categories(totals, n=2) == [("rent", 650.0), ("food", 20.0)]
    assert top_categories(totals, n=1, skip_fixed=True) == [("food", 20.0)]


def test_real_file_loads_without_bad_rows():
    expenses, skipped = load_expenses()
    assert len(expenses) == 148
    assert skipped == 0

