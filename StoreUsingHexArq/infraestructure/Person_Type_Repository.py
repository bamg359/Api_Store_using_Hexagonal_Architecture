from infraestructure.database.ConnectionDB import ConnetionDB

from domain.models.Person_Type import Person_Type


db = ConnetionDB(host='localhost', port=3307, user='root', password='', database='tienda_sura_g3')
db.connect()

class Person_Type_Repository:


    def __init__(self, db):
        self.db= db



    def add(self, costumer_type):
        query = "INSERT INTO costumer_type(costumer_type)VALUES(%s)"
        params = (costumer_type.type,)
        db.execute_query(query, params)


    def get_all(self):
        query = "SELECT * FROM costumer_type"
        result = db.execute_query(query)
        if result:
            types = []
            for row in result:
                type = Person_Type.from_row_type(row)
                types.append(type)
                print(row[0], row[1])
            return types
        else:
            print("Tipos no encontrados")
            return []

    def get_costumer_type_by_id(self, type_id:int):
        query = "SELECT * FROM costumer_type WHERE type_id = %s "
        result = db.execute_query(query, (type_id,))
        if result:
            return Person_Type.from_row_type(result[0])
        else:
            return []


    def update(self, costumer_type):
        query = "UPDATE costumer_type SET costumer_type = %s WHERE type_id = %s"
        values = (costumer_type.type, costumer_type.type_id)
        db.execute_query(query, values)

    def delete(self, type_id: int):
        query = "DELETE FROM costumer_type WHERE type_id=%s"
        db.execute_query(query, (type_id,))