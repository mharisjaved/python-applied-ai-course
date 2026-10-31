"""checkout: shop functions to write tests for (Day 29 practice).

Write your tests in a new file called test_checkout.py in this folder, then run:

    uv run pytest
"""


def apply_discount(price, percent):
    """Return price after a percent discount, rounded to 2 decimals.

    Raise ValueError if percent is below 0 or above 100.
    """
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (100 - percent) / 100, 2)


def split_bill(total, people):
    """Return each person's share of total, rounded to 2 decimals.

    Raise ValueError if people is less than 1.
    """
    if people < 1:
        raise ValueError("people must be at least 1")
    return round(total / people, 2)


def is_valid_username(name):
    """Return True if name is 3-12 characters long, has no spaces and starts with a letter."""
    if len(name) < 3 or len(name) > 12:
        return False
    if " " in name:
        return False
    return name[0].isalpha()
