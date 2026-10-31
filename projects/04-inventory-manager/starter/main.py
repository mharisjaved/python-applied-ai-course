"""Inventory Manager: a menu-driven console app for a small shop.

Run it from this folder with:  uv run main.py
The menu already runs. Options marked "not written yet" are your TODOs.
"""

from inventory import Inventory, Product

DATA_FILE = "inventory.txt"
LOW_STOCK_LIMIT = 5

MENU = """
=== Zara's Corner Shop ===
1. List products
2. Add a product
3. Restock a product
4. Sell a product
5. Low-stock report
6. Remove a product
0. Quit"""


# ---------- input helpers: keep asking until the answer is usable ----------

def ask_text(prompt):
    """Ask for a non-empty piece of text without commas (commas would break the save file)."""
    while True:
        text = input(prompt).strip()
        if text == "":
            print("Please type something.")
        elif "," in text:
            print("Please do not use commas.")
        else:
            return text


def ask_int(prompt, minimum):
    """Ask until the user types a whole number that is at least `minimum`."""
    while True:
        text = input(prompt).strip()
        try:
            number = int(text)
        except ValueError:
            print(f"'{text}' is not a whole number.")
            continue
        if number < minimum:
            print(f"Please enter {minimum} or more.")
        else:
            return number


def ask_price(prompt):
    """Ask until the user types a price greater than 0."""
    # TODO M1: same idea as ask_int, but convert with float() and require a price above 0.
    pass


# ---------- one function per menu option ----------

def add_product(inventory):
    # TODO M2: ask for a name (ask_text), a price (ask_price) and a quantity (ask_int, minimum 0),
    #          create a Product and add it with inventory.add_product(...). Print a confirmation.
    print("Add: not written yet.")


def restock_product(inventory):
    # TODO M3: ask for a name and use inventory.find(). If it is None, print a message and return.
    #          Otherwise ask how many (minimum 1), call product.restock(...) and show the new quantity.
    print("Restock: not written yet.")


def sell_product(inventory):
    """Done for you: a model for the other options."""
    name = ask_text("Product to sell: ")
    product = inventory.find(name)
    if product is None:
        print(f"There is no product called {name}.")
        return
    amount = ask_int("How many? ", 1)
    money = inventory.sell(name, amount)  # raises ValueError if there is not enough stock
    print(f"Sold {amount} x {product.name} for {money:.2f}.")


def show_low_stock(inventory):
    # TODO M4: call inventory.low_stock(LOW_STOCK_LIMIT) and print each product (print(product)
    #          uses your __str__). Print a friendly message if the list is empty.
    print("Low-stock report: not written yet.")


def remove_product(inventory):
    # TODO M5: ask for a name and call inventory.remove_product(name). Print what was removed.
    print("Remove: not written yet.")


def main():
    inventory = Inventory()
    # (Should) replace the line above with:  inventory = load_inventory(DATA_FILE)
    # and add `from storage import load_inventory, save_inventory` at the top.
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                print(inventory.report())
            elif choice == "2":
                add_product(inventory)
            elif choice == "3":
                restock_product(inventory)
            elif choice == "4":
                sell_product(inventory)
            elif choice == "5":
                show_low_stock(inventory)
            elif choice == "6":
                remove_product(inventory)
            # (Should) add option 7: today's sales from inventory.sales, with the total takings.
            elif choice == "0":
                # (Should) save_inventory(inventory, DATA_FILE) before saying goodbye.
                print("Goodbye!")
                break
            else:
                print(f"'{choice}' is not on the menu.")
        except ValueError as error:
            # The classes raise ValueError with a clear message; show it instead of crashing.
            print(f"Sorry: {error}")


if __name__ == "__main__":
    main()
