"""Classes for the Inventory Manager.

Product   = one item on the shelf (state: name, price, quantity).
Inventory = the whole shop. It HAS many products, stored in a dict keyed by lowercase name.

Work through the TODOs from top to bottom. After each one, run the tests:  uv run pytest -q
Replace each `pass` with your code.
"""


class Product:
    """One product the shop sells."""

    def __init__(self, name, price, quantity):
        name = name.strip()
        if name == "":
            raise ValueError("A product needs a name.")
        if price <= 0:
            raise ValueError(f"Price must be more than 0, got {price}.")
        if quantity < 0:
            raise ValueError(f"Quantity cannot be negative, got {quantity}.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, amount):
        """Add `amount` items to the stock. (Done for you: use it as a model for sell.)"""
        if amount <= 0:
            raise ValueError(f"Restock amount must be at least 1, got {amount}.")
        self.quantity += amount

    def sell(self, amount):
        """Take `amount` items out of stock and return the money for them."""
        # TODO 1: raise ValueError if amount is 0 or negative.
        # TODO 2: raise ValueError if amount is more than the quantity in stock.
        # TODO 3: reduce the quantity, then return amount * price.
        pass

    def total_value(self):
        """Value of all items of this product on the shelf."""
        # TODO 4: return price times quantity.
        pass

    def __str__(self):
        # TODO 5: return a friendly description, e.g. "Pen: 3 in stock at 0.75 each"
        #         (use :.2f for the price).
        pass


class Inventory:
    """All products in the shop. Names are matched without caring about upper/lower case."""

    def __init__(self):
        self.products = {}  # lowercase name -> Product
        self.sales = []     # (Should) one (name, amount, money) tuple per sale

    def add_product(self, product):
        """Add a new product. Raises ValueError if a product with that name already exists."""
        # TODO 6: the key is product.name.lower(). Raise ValueError if the key is already
        #         in self.products, otherwise store the product under that key.
        pass

    def find(self, name):
        """Return the product called `name`, or None if there is no such product."""
        # TODO 7: strip and lowercase the name, then look it up safely (hint: .get()).
        pass

    def remove_product(self, name):
        """Remove a product and return it. Raises ValueError if it does not exist."""
        # TODO 8: use self.find(). If the result is None, raise ValueError.
        #         Otherwise delete it from self.products and return it.
        pass

    def sell(self, name, amount):
        """Sell `amount` of a product and return the money taken."""
        # TODO 9: find the product (raise ValueError if it does not exist), then let the
        #         Product do the work: money = product.sell(amount). Return money.
        # (Should) record the sale: self.sales.append((product.name, amount, money))
        pass

    def low_stock(self, threshold=5):
        """Return the products with `threshold` items or fewer, lowest stock first."""
        # TODO 10: build a list of products whose quantity <= threshold.
        #          Then sort it by quantity (sorted() with key= a small function you write).
        pass

    def total_value(self):
        """Value of everything on the shelves."""
        # TODO 11: add up total_value() of every product.
        pass

    def report(self):
        """Return (not print!) a table of all products A to Z, with the total stock value."""
        # TODO 12: build a list of lines and return "\n".join(lines).
        #          Return "The inventory is empty." when there are no products.
        pass
