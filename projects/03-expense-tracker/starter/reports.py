"""reports: calculations on a list of expense dicts.

None of these functions read files, ask for input or print. They take a list and return a result,
which makes them easy to test (see test_reports.py).
"""


def total(expenses):
    """Return the sum of all amounts, rounded to 2 decimals (0 for an empty list)."""
    # TODO 8: add up expense["amount"] for every expense and round the result to 2 decimals.
    return 0


def total_by_category(expenses):
    """Return a dict {category: total amount}, each total rounded to 2 decimals.

    Example: two food expenses of 12.5 and 8.4 and one rent of 450 -> {"food": 20.9, "rent": 450.0}
    """
    # TODO 9: start with an empty dict and add each amount to its category (dict.get helps).
    return {}


def get_amount(expense):
    """Return the amount of one expense (use it as a key for max or sorted)."""
    return expense["amount"]


def get_date(expense):
    """Return the date of one expense (use it as a key for sorted)."""
    return expense["date"]


def largest_expense(expenses):
    """Return the expense with the biggest amount, or None if the list is empty."""
    # TODO 10: return None for an empty list; otherwise use max(..., key=get_amount).
    return None


def expenses_in_month(expenses, month):
    """Return the expenses whose date is in month, given as "YYYY-MM" (e.g. "2026-11")."""
    # TODO 11: keep the expenses whose date starts with the month.
    #          Careful: "2026-1" must NOT match "2026-11-03". (Hint: what comes after the month?)
    return []


def sort_by_date(expenses):
    """Return a new list of the expenses, oldest first. (Done for you: an example of key=.)"""
    return sorted(expenses, key=get_date)
