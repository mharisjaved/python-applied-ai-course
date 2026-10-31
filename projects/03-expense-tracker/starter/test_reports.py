"""Tests for reports.py. Run from this folder with:  uv run pytest

These tests FAIL until you complete the TODOs in reports.py. That is expected:
make them pass one by one, then add your own tests at the bottom.
"""

from reports import expenses_in_month, largest_expense, sort_by_date, total, total_by_category

# A small list to test with. The tests only read it, never change it.
EXPENSES = [
    {"date": "2026-11-03", "category": "food", "description": "Lunch", "amount": 12.5},
    {"date": "2026-10-30", "category": "transport", "description": "Train", "amount": 6.8},
    {"date": "2026-11-01", "category": "rent", "description": "November rent", "amount": 450.0},
    {"date": "2026-11-07", "category": "food", "description": "Coffee beans", "amount": 8.4},
]


def test_total():
    assert total(EXPENSES) == 477.7


def test_total_by_category():
    assert total_by_category(EXPENSES) == {"food": 20.9, "transport": 6.8, "rent": 450.0}


# TODO: add your own tests, for example:
#   - total([]) is 0
#   - largest_expense(EXPENSES) is the rent; largest_expense([]) is None
#   - expenses_in_month(EXPENSES, "2026-11") has 3 expenses; "2026-1" gives []
#   - sort_by_date puts "2026-10-30" first
