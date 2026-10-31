"""Tests for storage.py. Run from this folder with:  uv run pytest

These tests FAIL until you complete the TODOs in storage.py. That is expected:
make them pass one by one, then add your own tests at the bottom.
"""

from pathlib import Path

import pytest

from storage import format_line, load_expenses, parse_line, save_expense

# __file__ is the path of this test file, so these paths work from any folder.
HERE = Path(__file__).parent
SAMPLE_FILE = HERE / "sample_expenses.txt"


def test_parse_line_normal():
    expense = parse_line("2026-11-03,food,Lunch with Sara,12.50\n")
    assert expense == {"date": "2026-11-03", "category": "food",
                       "description": "Lunch with Sara", "amount": 12.5}


def test_parse_line_amount_not_a_number_raises():
    with pytest.raises(ValueError):
        parse_line("2026-11-03,food,Lunch,twelve")


# TODO: add your own tests, for example:
#   - parse_line with the wrong number of values raises ValueError
#   - format_line gives "2026-11-05,transport,Bus pass,25.00" (two decimals)
#   - load_expenses(SAMPLE_FILE) returns 9 expenses (the file has 10 lines, one is broken)
#   - save_expense then load_expenses gives the expense back. Write to HERE / "test_save_tmp.txt"
#     and delete the file at the end (path.unlink(missing_ok=True) inside a finally: block).
