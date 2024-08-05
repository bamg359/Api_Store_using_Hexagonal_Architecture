

from infraestructure.Product_Repository import Product_Repository
from domain.services.Product_Service import Product_Service as Domain_Product_Service
from domain.models.Product import Product



class Product_Service:

    def __init__(self, product_repository : Product_Repository):
        self.domain_product_service =  Domain_Product_Service(product_repository)


        


    def create_product(self, product: Product ):
        self.domain_product_service.create_product(product)

    def select_products(self):
        return self.domain_product_service.select_products()

    def select_product(self, product_id: int):
        return self.domain_product_service.select_product(product_id)

    def update_product(self, product:Product):
        self.domain_product_service.update_product(product)

    def delete_product(self, product_id):
        self.domain_product_service.delete_product(product_id)


