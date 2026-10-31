"""Tests for inventory.py. Run from this folder with:  uv run pytest -q

At the start, the first three tests pass and the others fail. Each TODO you finish in
inventory.py should turn at least one more test green.
Must: add at least 4 tests of your own at the bottom (2 of them for error cases with pytest.raises).
"""

import pytest

from inventory import Inventory, Product


def make_shop():
    """A small inventory that several tests start from."""
    shop = Inventory()
    shop.add_product(Product("Notebook", 2.5, 40))
    shop.add_product(Product("Pen", 0.75, 3))
    shop.add_product(Product("Glue stick", 1.25, 5))
    return shop


# ---------- these pass already (the code is given) ----------

def test_new_product_keeps_its_values():
    pen = Product("Pen", 0.75, 3)
    assert pen.name == "Pen"
    assert pen.price == 0.75
    assert pen.quantity == 3


def test_product_rejects_bad_price():
    with pytest.raises(ValueError):
        Product("Pen", 0, 3)


def test_restock_adds_to_quantity():
    pen = Product("Pen", 0.75, 3)
    pen.restock(10)
    assert pen.quantity == 13


# ---------- these fail until you finish the TODOs ----------

def test_sell_reduces_quantity_and_returns_money():          # TODO 1-3
    notebook = Product("Notebook", 2.5, 40)
    money = notebook.sell(4)
    assert money == 10.0
    assert notebook.quantity == 36


def test_sell_more_than_stock_raises_and_changes_nothing():  # TODO 2
    pen = Product("Pen", 0.75, 3)
    with pytest.raises(ValueError):
        pen.sell(4)
    assert pen.quantity == 3


def test_product_total_value():                              # TODO 4
    assert Product("Notebook", 2.5, 40).total_value() == 100.0


def test_find_ignores_case_and_spaces():                     # TODO 6-7
    shop = make_shop()
    assert shop.find("pen").name == "Pen"
    assert shop.find("  GLUE STICK ").name == "Glue stick"


def test_add_product_rejects_duplicate_in_any_case():        # TODO 6
    shop = make_shop()
    with pytest.raises(ValueError):
        shop.add_product(Product("PEN", 1.0, 1))


def test_low_stock_default_threshold_lowest_first():         # TODO 10
    names = [product.name for product in make_shop().low_stock()]
    assert names == ["Pen", "Glue stick"]  # 3 left, then 5 left (5 counts as low)


def test_inventory_total_value():                            # TODO 11
    # 40 * 2.5 + 3 * 0.75 + 5 * 1.25 = 100 + 2.25 + 6.25
    assert make_shop().total_value() == 108.5


# ---------- your tests (Must: at least 4 more) ----------
# Ideas: sell(0) raises · __str__ contains the name · remove_product works / raises for an unknown
# name · Inventory.sell changes the stock · low_stock(0) is empty · report() of an empty inventory.
