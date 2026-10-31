"""(Should) Save and load an Inventory as a text file: one product per line, name,price,quantity.

Start this file only when the Must requirements work and their tests pass.
Then switch main.py over to load_inventory/save_inventory (see the TODOs in main.py).
"""

from pathlib import Path

from inventory import Inventory, Product


def product_to_line(product):
    """Turn a Product into one line of text, e.g. Pen,0.75,3"""
    # TODO S1: return an f-string with the three attributes separated by commas.
    pass


def line_to_product(line):
    """Turn a line such as Pen,0.75,3 back into a Product. Raises ValueError for a bad line."""
    # TODO S2: strip and split the line on ",". If there are not exactly 3 parts, raise ValueError.
    #          Otherwise convert price with float() and quantity with int() and return a Product.
    pass


def save_inventory(inventory, path):
    """Write every product to the file at `path` (the old content is replaced)."""
    # TODO S3: open the file in "w" mode (encoding="utf-8") and write one line per product.
    pass


def load_inventory(path):
    """Read an Inventory from `path`. A missing file gives an empty inventory; bad lines are skipped."""
    inventory = Inventory()
    if not Path(path).exists():
        return inventory
    # TODO S4: open the file, and for every non-empty line try to add line_to_product(line)
    #          to the inventory. If that raises ValueError, print a warning and carry on.
    return inventory
