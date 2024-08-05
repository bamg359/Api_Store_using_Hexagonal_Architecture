from infraestructure.database.ConnectionDB import ConnetionDB

from domain.models.Category import Category


db = ConnetionDB(host='localhost', port=3307, user='root', password='', database='tienda_sura_g3')
db.connect()

class Category_Repository:


    def __init__(self, db):
        self.db= db



    def add(self, category):
        query = "INSERT INTO category(category_name)VALUES(%s)"
        params = (category.category_name,)
        db.execute_query(query, params)


    def get_all(self):
        query = "SELECT * FROM category"
        result = db.execute_query(query)
        if result:
            categories = []
            for row in result:
                category = Category.from_row(row)
                categories.append(category)
                print(row[0], row[1])
            return categories
        else:
            print("Categorias no encontradas")
            return []

    def get_category_by_id(self, id_category:int):
        query = "SELECT * FROM category WHERE category_id = %s "
        result = db.execute_query(query, (id_category,))
        if result:
            return Category.from_row(result[0])
        else:
            return []


    def update(self, category):
        query = "UPDATE category SET category_name = %s WHERE category_id = %s"
        values = (category.category_name, category.category_id)
        db.execute_query(query, values)

    def delete(self,category_id: int):
        query = "DELETE FROM category WHERE category_id=%s"
        db.execute_query(query, (category_id,))





