# Project 04: Inventory Manager (instructor notes)

Student brief: [README.md](README.md) · Lesson plan for the session: [Day 35](../../weeks/week-07/day-35-project-inventory/lesson.md)

## Timing plan

| When | What | Notes |
|------|------|-------|
| Day 34, homework | read the brief, write one question | answer the questions at the start of the build time |
| Day 35, 0:20–0:36 | brief walkthrough, design on the board, workflow demo | demo.ipynb sections 1–6 |
| Day 35, 0:36–0:70 | build: Product, then Inventory | target: all `Product` tests green by the end of class |
| Days 35–36, homework | Inventory, menu, own tests, then Should | about 2–3 hours |
| Day 37, first 10 min | submission + 3-minute demos for a sample of students | demo the rest during practice time on Days 37–38 |

If you have a 90-minute session, give the extra 15 minutes to build time; it matters more than anything else.

## Files

- `starter/`: what students copy. `uv run pytest -q` gives **3 passed, 7 failed**; `uv run main.py` runs, and the
  unfinished options print "not written yet".
- `reference/`: complete solution with `storage.py`, the sales log and 30 tests.
  `cd projects/04-inventory-manager/reference && uv run pytest -q` → `30 passed`.

How the reference menu was tested (pipe test; run it in a **copy** of the folder, because quitting saves
`inventory.txt`):

```
printf '1\n4\nnotebook\n3\n4\npen\nten\n10\n5\n2\nRuler\n1.20\n4\n7\n0\n' | uv run python main.py
```

That session lists, sells, rejects `ten` and an oversell, shows the low-stock report, adds a product, shows the
sales log and saves; its output is the example run in the brief.

## Common pitfalls (and the question to ask instead of the answer)

| Pitfall | Symptom | Ask |
|---------|---------|-----|
| `sell` subtracts before checking | "changes nothing" test fails | "Read the test's last assert. What should the quantity be after a failed sale?" |
| `sell` doesn't return the money | `assert None == 10.0` | "What does the test expect back from `sell`?" |
| `find` doesn't lowercase/strip | `AttributeError: 'NoneType' object has no attribute 'name'` in the find test | "What are the keys in `self.products` exactly? Print them." |
| `add_product` uses `product.name` (not lowercase) as the key | duplicate test passes, find test fails (or the other way round) | "Is the key you store the same as the key you look up?" |
| `Inventory.sell` changes `product.quantity` itself | works, but duplicates `Product`'s rules | "Which class already knows how to sell safely?" |
| `low_stock` uses `<` instead of `<=` | Glue stick (5 left) is missing | "Read the docstring: '5 or fewer'." |
| `low_stock` with `key=quantity_of()` | `TypeError` | "Do you want to give `sorted` the function, or the result of calling it?" |
| `report()` prints | menu prints the table and then `None` | "Who should print: the class or the menu?" |
| `ask_price` returns the text | `TypeError: '<=' not supported between 'str' and 'int'` in `Product.__init__` | "What type does `input()` give you?" |
| `except:` or `except Exception:` around everything in `main` | real bugs disappear | "Which error do our classes raise on purpose?" |
| running pytest from the wrong folder | `import file mismatch` or tests not found | "Which folder is your terminal in? `cd` into your project folder" |

## Unblocking without giving the answer

- **Can't start a method:** ask them to say the method's job out loud in three steps ("check …, change …,
  return …") and write those as comments first.
- **Stuck on `low_stock`:** point to Day 35 practice Exercise 3 (plants that need water): same pattern, different data.
- **Stuck on `report`:** Day 35 practice Exercise 4 (cart report).
- **Stuck on `storage.py`:** Day 35 practice Exercise 2 (parsing lines safely).
- **Test failure they can't read:** have them read the **last** line of the failure aloud, then the line with `>` in
  front of it (Day 28 debugging routine).
- **Overwhelmed:** reduce the goal to "all six `Product` tests green". That alone is most of the week's learning.

## Grading notes

For each submission:

1. `cd` into the folder, run `uv run pytest -q`, note the count. Open `test_inventory.py` and check that their own
   tests exist and that at least 2 use `pytest.raises` (Testing, 10 points).
2. Search for `input(` and `print(` in `inventory.py`: there should be none (Responsibilities criterion).
3. Run `uv run main.py` and try: letters for a number, `0`, `-3`, an unknown product, a duplicate add, an oversell,
   `remove` of an unknown name (Bad input, 15 points). A traceback on any of these costs points; a message that
   still changes the state (e.g. stock goes negative) costs more.
4. Read `Product.sell` and `restock`: is the check before the change? (Check first, change second.)
5. Should items: restart the program after quitting; are the changes still there? Is there a sales option?
6. Demo (15 points): ask two of these: "Why does `find` return `None` while `remove_product` raises?", "Why are the
   keys lowercase?", "Show me where a failed sale is prevented from changing the stock", "What would break if
   `report()` printed instead of returning?"

Typical marks: Must only, clean and tested → 70–80. Must + Should with good tests → 85–95. Students who submit a
working program without tests of their own lose most of the Testing points even if all starter tests pass.

## Differences from the brief students might ask about

- Prices are `float`s. Floating-point surprises (e.g. `0.1 + 0.2`) do not appear with the sample prices; if a strong
  student asks, mention that real shops store cents as integers.
- A name with a comma is rejected by the menu (`ask_text`) because it would break the `name,price,quantity` file.
  `csv` (Day 36) solves this properly: a good Could item.
- `low_stock(threshold)` includes products with exactly `threshold` items. The README, docstring and tests all say so.
