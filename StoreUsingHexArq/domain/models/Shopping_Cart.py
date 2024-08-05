


class Shopping_Cart:

    def __init__(self, owner_id, product_id, product_price, quantity, total,cart_state):
        self._owner_id = owner_id
        self._product_id = product_id
        self._product_price = product_price
        self._quantity = quantity
        self._total = total
        self._cart_state = cart_state


    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        self._owner_id = owner_id

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        self._product_id = product_id

    @property
    def product_price(self):
        return self._product_price

    @product_id.setter
    def product_price(self, product_price):
        self._product_price = product_price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def cart_state(self):
        return self._cart_state

    @cart_state.setter
    def cart_state(self, cart_state):
        self._cart_state = cart_state

    @staticmethod
    def from_row_cart(row):
        return Shopping_Cart(row[0], row[1], row[2], row[3], row[4], row[5])
