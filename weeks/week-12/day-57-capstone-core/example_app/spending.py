"""Core of the spending summary app: load expenses and calculate totals. No AI in this file."""

import csv
from pathlib import Path

# weeks/week-12/day-57-capstone-core/example_app/ -> four levels up is the course root
DATA_PATH = Path(__file__).parent / "../../../../datasets/expenses.csv"

FIXED_COSTS = {"rent", "utilities"}  # bills you cannot easily change this month


def parse_amount(text):
    """Turn text such as '12.50' into 12.5. Raise ValueError if it is not a positive number."""
    amount = float(text)  # float("abc") raises ValueError by itself
    if amount <= 0:
        raise ValueError(f"Amount must be positive, got {amount}")
    return amount


def load_expenses(path=DATA_PATH):
    """Read the expenses CSV. Returns (expenses, skipped): a list of dicts and the number of bad rows.

    Only date, category and amount are kept. The app never needs the descriptions,
    so they are not loaded at all (less personal data to protect).
    """
    expenses = []
    skipped = 0
    with open(path, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            try:
                amount = parse_amount(row["amount"])
            except ValueError:
                skipped += 1
                continue
            expenses.append({
                "date": row["date"],
                "category": row["category"].strip().lower(),
                "amount": amount,
            })
    return expenses, skipped


def filter_month(expenses, month):
    """Keep only the expenses of one month, given as 'YYYY-MM' (for example '2026-09')."""
    return [expense for expense in expenses if expense["date"].startswith(month)]


def category_totals(expenses):
    """Total amount per category, rounded to cents: {'food': 660.87, 'rent': 650.0, ...}."""
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]
    return {category: round(total, 2) for category, total in totals.items()}


def get_amount(pair):
    """Sort key: the amount in a (category, amount) pair."""
    return pair[1]


def top_categories(totals, n=3, skip_fixed=False):
    """The n biggest categories, biggest first: [('food', 660.87), ('rent', 650.0), ...]."""
    pairs = []
    for category, total in totals.items():
        if skip_fixed and category in FIXED_COSTS:
            continue
        pairs.append((category, total))
    return sorted(pairs, key=get_amount, reverse=True)[:n]


def format_table(totals):
    """A neat text table of the totals, biggest first, with a TOTAL line."""
    lines = []
    for category, total in top_categories(totals, n=len(totals)):
        lines.append(f"{category:<15}{total:>10.2f}")
    lines.append(f"{'TOTAL':<15}{sum(totals.values()):>10.2f}")
    return "\n".join(lines)
