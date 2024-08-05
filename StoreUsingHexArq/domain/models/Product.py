




class Product:

    def __init__(self, product_id, product_name , description , category, cost , profit, price, quantity , state):
        self._product_id = product_id
        self._product_name = product_name
        self._description = description
        self._category = category
        self._cost = cost
        self._profit = profit
        self._price = price
        self._quantity = quantity
        self._state = state


    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        self._product_id = product_id

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        self._product_name = product_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = cost

    @property
    def profit(self):
        return self._profit

    @profit.setter
    def cost(self, profit):
        self._profit = profit

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price


    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @staticmethod
    def from_row_product(row):
        return Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],row[8])
