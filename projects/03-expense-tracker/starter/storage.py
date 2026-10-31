"""storage: reading and writing expenses in a text file.

Each line of the file is one expense with four values separated by commas:

    YYYY-MM-DD,category,description,amount
    2026-11-03,food,Lunch with Sara,12.50

In the program an expense is a dict:

    {"date": "2026-11-03", "category": "food", "description": "Lunch with Sara", "amount": 12.5}

Keep the date as a "YYYY-MM-DD" string: such strings sort in date order, and the month is
just the first 7 characters ("2026-11").
"""

from datetime import date
from pathlib import Path


def parse_line(line):
    """Turn one line of the file into an expense dict.

    Raise ValueError if the line does not have exactly 4 values, the date is not a real
    YYYY-MM-DD date, the category or description is empty, or the amount is not a positive number.
    """
    # TODO 1: strip the line and split it on commas.
    #         If there are not exactly 4 parts, raise ValueError with a helpful message.
    # TODO 2: clean each part with .strip(); make the category lowercase.
    #         Convert the amount with float() (it raises ValueError for text like "abc" by itself).
    # TODO 3: check the date with date.fromisoformat(...) (it raises ValueError for "2026-02-30"),
    #         and raise ValueError if the category or description is empty or the amount is not > 0.
    # TODO 4: return the dict with the keys "date", "category", "description", "amount".
    return {}


def format_line(expense):
    """Turn an expense dict into one line of text for the file (without the newline).

    Example: {"date": "2026-11-05", "category": "transport", "description": "Bus pass", "amount": 25}
             -> "2026-11-05,transport,Bus pass,25.00"
    """
    # TODO 5: build the line with an f-string. Show the amount with 2 decimals (:.2f).
    return ""


def load_expenses(path):
    """Return all expenses in the file as a list of dicts.

    A missing file gives an empty list (nothing saved yet). Blank lines are ignored.
    Lines that cannot be parsed are skipped with a warning, so one bad line never crashes the app.
    """
    path = Path(path)
    if not path.exists():
        return []

    expenses = []
    # TODO 6: open the file (encoding="utf-8") and loop over its lines with enumerate(..., start=1).
    #         - skip blank lines
    #         - try parse_line(line) and append the result to expenses
    #         - except ValueError as error: print a warning with the line number and the error,
    #           then carry on with the next line
    return expenses


def save_expense(path, expense):
    """Add one expense to the end of the file. The file is created if it does not exist."""
    # TODO 7: open the file in append mode ("a", encoding="utf-8") and write format_line(expense)
    #         followed by "\n".
    pass
