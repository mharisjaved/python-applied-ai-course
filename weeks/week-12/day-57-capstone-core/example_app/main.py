"""Spending summary app (Day 57 version: core + template summary, no AI yet).

Run from this folder:  uv run python main.py
"""

from spending import category_totals, filter_month, format_table, load_expenses
from summary import write_summary


def main():
    try:
        expenses, skipped = load_expenses()
    except FileNotFoundError:
        print("Could not find the expenses file. Is the course datasets folder in place?")
        return
    print(f"Loaded {len(expenses)} expenses ({skipped} bad rows skipped).")

    while True:
        try:
            month = input("\nMonth to summarise (YYYY-MM, e.g. 2026-09) or 'quit': ").strip()
        except EOFError:  # end of piped input
            break
        if month.lower() == "quit":
            break
        month_expenses = filter_month(expenses, month)
        if not month_expenses:
            print(f"No expenses found for '{month}'.")
            continue
        totals = category_totals(month_expenses)
        print(format_table(totals))
        result = write_summary(totals)
        print("\nSummary:", result["summary"])
        for tip in result["tips"]:
            print(" Tip:", tip)
    print("Goodbye!")


if __name__ == "__main__":
    main()
