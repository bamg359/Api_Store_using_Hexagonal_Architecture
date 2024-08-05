
from domain.models.Product import Product
from infraestructure.database.ConnectionDB import ConnetionDB

db = ConnetionDB(host='localhost', port=3307, user='root', password='', database='tienda_sura_g3')
db.connect()

class Product_Repository:

    def __init__(self, db):
        self.db = db


    def add_product(self, product):
        query = "INSERT INTO product (product_id,product_name,description,category,cost,profit,price,quantity,state) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (
        product.product_id, product.product_name, product.description, product.category, product.cost, product.profit, product.price,
        product.quantity, product.state)
        db.execute_query(query, values)
        print("registro validador")

    def get_products(self):
        query = "SELECT * FROM product"
        result = self.db.execute_query(query)
        if result:
            products = []
            for row in result:
                product = Product.from_row_product(row)
                products.append(product)
                print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],row[8])
            return products
        else:
            print("Productos no encontrados")
            return []


    def get_product(self , product_id):
        query = "SELECT * FROM product WHERE product_id = %s"
        result = db.execute_query(query, (product_id,))
        if result:
            return Product.from_row_product(result[0])
        else:
            return []



    def update_product(self, product):
        query = "UPDATE product SET product_name = %s , description = %s, category = %s, cost = %s , profit = %s, price = %s, quantity = %s  , state =%s WHERE product_id =%s"
        values = (
         product.product_name, product.description, product.category, product.cost, product.profit, product.price,
        product.quantity, product.state,product.product_id)
        db.execute_query(query, values)


    def delete_product(self, product_id):
        query = "DELETE FROM product WHERE product_id = %s "
        db.execute_query(query, (product_id,))







