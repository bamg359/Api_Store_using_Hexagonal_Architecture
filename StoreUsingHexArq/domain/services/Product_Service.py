




class Product_Service:

    def __init__(self, product_repository):
        self.product_repository = product_repository


    def create_product(self, product):
        self.product_repository.add_product(product)

    def select_products(self):
        return self.product_repository.get_products()


    def select_product(self, product_id):
        return self.product_repository.get_product(product_id)


    def update_product(self, product):
        self.product_repository.update_product(product)

    def delete_product(self, product_id):
        self.product_repository.delete_product(product_id)


