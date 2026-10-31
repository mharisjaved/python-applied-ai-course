# Project 04: Inventory Manager

**Week 7 · Day 35 · Individual project · About 3–4 hours (class + homework) · Due: start of Day 37**

## The story

Zara runs a small corner shop near campus: notebooks, pens, glue sticks, staplers. She keeps her stock in a paper
notebook and keeps running out of the best-sellers. She asks you for a small console program: she wants to see what
is on the shelves, restock and sell products, get warned when something is running low, and know what her stock is
worth. And she never wants it to crash when she mistypes.

You will build it with **classes**: a `Product` that knows its own price and stock and refuses impossible changes,
and an `Inventory` that **has** many products. A menu in `main.py` talks to Zara; tests prove the classes work.

## What you will practise

Classes, `__init__`, methods, validation with `raise ValueError`, `__str__` (Days 32–33) · composition: an object
that holds other objects (Day 34) · a multi-file program with a menu, `try/except` and pytest tests (Days 25–30).

## What it should do

Example run of a finished version (what Zara types is shown after each prompt; the menu is printed again after
every action, shortened here to `(menu)`):

```
$ uv run main.py
Loaded 6 products from inventory.txt.

=== Zara's Corner Shop ===
1. List products
2. Add a product
3. Restock a product
4. Sell a product
5. Low-stock report
6. Remove a product
7. Today's sales
0. Save and quit
Choose an option: 1
Product            Price   Qty     Value
Glue stick          1.25     5      6.25
Graph paper         3.25    18     58.50
Highlighter         1.50    12     18.00
Notebook            2.50    40    100.00
Pen                 0.75     3      2.25
Stapler             6.00     2     12.00
Total stock value                 197.00
(menu)
Choose an option: 4
Product to sell: notebook
How many? 3
Sold 3 x Notebook for 7.50.
(menu)
Choose an option: 4
Product to sell: pen
How many? ten
'ten' is not a whole number.
How many? 10
Sorry: Only 3 x Pen in stock, cannot sell 10.
(menu)
Choose an option: 5
Products with 5 or fewer items (reorder soon):
  Stapler: 2 in stock at 6.00 each
  Pen: 3 in stock at 0.75 each
  Glue stick: 5 in stock at 1.25 each
(menu)
Choose an option: 2
Product name: Ruler
Price: 1.20
Quantity in stock: 4
Added Ruler.
(menu)
Choose an option: 7
    3 x Notebook            7.50
Total takings: 7.50
(menu)
Choose an option: 0
Saved 7 products to inventory.txt. Goodbye!
```

Your wording and layout may differ. The behaviour must be the same.

## Requirements

**Must** (needed to pass)

1. `Product(name, price, quantity)` in `inventory.py` with:
   `restock(amount)`, `sell(amount)` (returns the money for the sale), `total_value()` and `__str__`.
   `restock` and `sell` raise `ValueError` for an amount of 0 or less; `sell` also raises when there is not enough
   stock. **A failed call changes nothing.**
2. `Inventory()` in `inventory.py` that stores products in a dict keyed by **lowercase name**, with:
   `add_product(product)` (raises `ValueError` for a duplicate name in any case), `remove_product(name)` (raises for
   an unknown name), `find(name)` (returns the product or `None`), `sell(name, amount)`, `low_stock(threshold=5)`
   (a list of products with `threshold` or fewer items, lowest first), `total_value()` and `report()` (**returns**
   the table as a string).
3. `main.py` with a menu loop: list, add, restock, sell, low-stock report, remove, quit. Bad input (letters, negative
   numbers, unknown products, selling too much) shows a message and **never crashes** the program.
4. The classes never call `input()` or `print()`. Only `main.py` talks to the user.
5. `uv run pytest -q` passes, with all 10 starter tests **plus at least 4 tests of your own** (at least 2 of them
   for error cases with `pytest.raises`).

**Should**

6. Saving: `storage.py` loads `inventory.txt` when the program starts and saves it on quit (one product per line,
   `name,price,quantity`). A damaged line is skipped with a warning, not a crash. Add at least 2 tests for
   `line_to_product` / `product_to_line`.
7. Sales log: `Inventory.sell` records every sale as `(name, amount, money)` in `self.sales`; menu option 7 shows
   today's sales and the total takings.

**Could**

- Categories (`stationery`, `snacks`…) and a report per category.
- An `Order` class: several products sold in one go, with a receipt (Day 35 practice, Exercise 5).
- Export the inventory to a real CSV file with `csv.DictWriter` (after Day 36).
- A `set_price(new_price)` method with validation, and a menu option for it.
- Append every sale to `sales_log.txt` (mode `"a"`) so the log survives a restart.

## Starter files and how to run them

Copy the `starter/` folder into your own work folder (for example `inventory-manager/`) and work there.

| File | What is in it |
|------|---------------|
| `inventory.py` | `Product` and `Inventory`. `__init__` and `restock` are done, other methods are `TODO`s |
| `main.py` | the menu loop and input helpers. Option 4 (sell) is done as a model; options 2, 3, 5, 6 are `TODO`s |
| `test_inventory.py` | 10 tests: 3 pass at the start, 7 pass once the `TODO`s are done; add yours at the bottom |
| `storage.py` | (Should) save/load `TODO`s |
| `inventory.txt` | sample stock for when you do the Should part |

Run everything from **inside** your project folder, in the course's uv environment:

```
uv run pytest -q        # run the tests (start: 3 passed, 7 failed)
uv run main.py          # run the program
```

## Build plan

1. **Product.** TODOs 1–5 in `inventory.py`. *Checkpoint:* all six `Product` tests pass; the 4 remaining failures
   are `Inventory` tests. Check `__str__` yourself: add `print(Product("Pen", 0.75, 3))` under an
   `if __name__ == "__main__":` line at the bottom of `inventory.py` (Day 26) and run `uv run inventory.py`.
2. **Inventory.** TODOs 6–12. Start with `add_product` and `find`: most `Inventory` tests need them.
   *Checkpoint:* all 10 starter tests pass.
3. **Menu.** TODOs M1–M5 in `main.py`. *Checkpoint:* try every option by hand, including bad input: letters for
   numbers, `0`, `-3`, an unknown product, selling more than you have. Nothing crashes.
4. **Your tests.** Add at least 4 tests (2 with `pytest.raises`). Ideas are listed at the bottom of
   `test_inventory.py`. *Checkpoint:* `uv run pytest -q` shows at least 14 passed.
5. **Should.** `storage.py` (TODOs S1–S4) and the two lines marked `(Should)` in `main()`, then the sales log.
   *Checkpoint:* quit, restart, and your changes are still there.
6. **Could** (optional), then the submission checklist.

## Submission checklist

- [ ] `uv run pytest -q` passes (paste the summary line, e.g. `16 passed`, into your submission message).
- [ ] `uv run main.py` works from a fresh terminal; every menu option tried, including bad input.
- [ ] No `input()` or `print()` inside `inventory.py`.
- [ ] Every method has a one-line docstring; no leftover `TODO` comments for things you finished.
- [ ] `example_run.txt`: copy a short session from your terminal (at least one sell, one error, one low-stock report).
- [ ] If you did Should/Could items, list them at the top of `main.py` in the docstring.

## Evaluation rubric (100 points)

| Criterion | Points | Full points when… |
|-----------|--------|-------------------|
| Works as specified | 40 | all Must requirements work as in the example run; Should items add up to 10 of these points |
| Code readability | 20 | clear names, one job per method, docstrings, no duplicated logic between `main.py` and the classes |
| Handles bad input / edge cases | 15 | letters, zero, negatives, unknown names, duplicates, overselling: friendly messages, no crash, no state change |
| Testing | 10 | all tests pass; own tests include error cases with `pytest.raises` and "nothing changed" checks |
| Explanation / demo | 15 | you can explain your code in a 3-minute demo (see below) |

**Project-specific criteria** (checked inside the categories above):

- **Responsibilities:** `Product` guards its own stock rules; `Inventory` only finds products and delegates to them
  (it never does `product.quantity -= ...` itself); only `main.py` uses `input()`/`print()`.
- **Check first, change second:** every method that raises does so *before* changing any attribute.
- **You can answer:** "Why does `find` return `None` but `remove_product` raises?" and "Why are the dict keys lowercase?"

## Extension ideas

- Add a `Supplier` class: each product has a supplier, and the low-stock report groups products by supplier
  (composition again).
- Undo: keep a list of the last actions and add an "undo last sale" option.
- After Week 9: load the saved file with pandas and plot the stock value per product.
