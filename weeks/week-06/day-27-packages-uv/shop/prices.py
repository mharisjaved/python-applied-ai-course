"""Price calculations for the shop package."""

TAX_RATE = 0.15


def add_tax(price, rate=TAX_RATE):
    """Return price with tax added, rounded to 2 decimals."""
    return round(price * (1 + rate), 2)


def apply_discount(price, percent):
    """Return price after a percent discount, rounded to 2 decimals."""
    return round(price * (100 - percent) / 100, 2)


def format_price(amount):
    """Return amount as text with 2 decimals and thousands commas, e.g. 1250 -> "1,250.00"."""
    return f"{amount:,.2f}"
