"""Expense Tracker (Project 03): a console app that saves your expenses to a file.

Run it from this folder:

    uv run main.py

main.py only talks to the user. Reading and writing the file is storage.py's job,
and every calculation is reports.py's job. The menu already works; the TODOs make it useful.
"""

from datetime import date

import reports
import storage

DATA_FILE = "expenses.txt"

MENU = """
=== Expense Tracker ===
1) Add an expense
2) List all expenses
3) Summary by category
4) Monthly total
5) Quit"""


# ---- asking for input ------------------------------------------------------------

def ask_date():
    """Ask for a date as YYYY-MM-DD; pressing Enter means today. Return it as text."""
    # TODO 12: ask the user. Empty answer -> today's date. Otherwise check the text with
    #          date.fromisoformat(...) inside try/except and keep asking until it is valid.
    return date.today().isoformat()


def ask_text(prompt):
    """Ask until the user types some text without commas (commas separate the values in the file)."""
    while True:
        text = input(prompt).strip()
        if text == "":
            print("  Please type something.")
        elif "," in text:
            print("  Please don't use commas.")
        else:
            return text


def ask_amount():
    """Ask until the user types a number greater than 0. Return it as a float."""
    # TODO 13: this crashes if the user types "abc"! Use a loop with try/except ValueError
    #          and keep asking until the amount is a number greater than 0.
    return float(input("Amount: "))


# ---- menu actions -----------------------------------------------------------------

def add_expense(path):
    """Ask for one expense, save it to the file and return it."""
    expense = {
        "date": ask_date(),
        "category": ask_text("Category (e.g. food, transport, rent): ").lower(),
        "description": ask_text("Description: "),
        "amount": ask_amount(),
    }
    storage.save_expense(path, expense)
    print(f"Saved: {expense['description']} ({expense['amount']:.2f})")
    return expense


def show_expenses(expenses):
    """Print every expense, oldest first, with the total underneath."""
    if len(expenses) == 0:
        print("No expenses yet. Choose 1 to add one.")
        return
    # TODO 14 (Should): print a neat table with column headings, sorted with reports.sort_by_date,
    #                   using f-string widths like {text:<12} and {amount:>9.2f}.
    for expense in expenses:
        print(expense)
    print("Total:", reports.total(expenses))


def show_summary(expenses):
    """Print the total per category, the overall total and the largest expense."""
    if len(expenses) == 0:
        print("No expenses yet. Choose 1 to add one.")
        return
    totals = reports.total_by_category(expenses)
    # TODO 15: print one line per category (sorted A-Z) with the amount to 2 decimals,
    #          then the overall total and the largest expense (reports.largest_expense).
    print(totals)


def show_month(expenses):
    """Ask for a month (YYYY-MM) and print how many expenses it had and their total."""
    # TODO 16: ask for a month (check it with date.fromisoformat(month + "-01")),
    #          then use reports.expenses_in_month and reports.total.
    print("Monthly total is not built yet.")


def main():
    print("Welcome to the Expense Tracker!")
    expenses = storage.load_expenses(DATA_FILE)
    print(f"Loaded {len(expenses)} expenses from {DATA_FILE}.")
    while True:
        print(MENU)
        choice = input("Choose 1-5: ").strip()
        if choice == "1":
            expenses.append(add_expense(DATA_FILE))
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            show_month(expenses)
        elif choice == "5":
            print(f"Goodbye! Your expenses are saved in {DATA_FILE}.")
            break
        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
