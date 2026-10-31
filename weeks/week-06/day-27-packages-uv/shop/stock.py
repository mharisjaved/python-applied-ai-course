"""Stock checks for the shop package."""

LOW_STOCK_LIMIT = 5


def is_low(quantity):
    """Return True if quantity is below the low-stock limit."""
    return quantity < LOW_STOCK_LIMIT


def restock_list(stock):
    """Return the names of items that are running low, sorted A-Z."""
    return sorted([item for item, quantity in stock.items() if is_low(quantity)])
