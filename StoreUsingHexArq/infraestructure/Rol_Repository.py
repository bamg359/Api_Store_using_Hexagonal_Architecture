from infraestructure.database.ConnectionDB import ConnetionDB

from domain.models.Rol import Rol


db = ConnetionDB(host='localhost', port=3307, user='root', password='', database='tienda_sura_g3')
db.connect()

class Rol_Repository:


    def __init__(self, db):
        self.db= db



    def add(self, rol):
        query = "INSERT INTO rol(rol_name)VALUES(%s)"
        params = (rol.rol_name,)
        db.execute_query(query, params)


    def get_all(self):
        query = "SELECT * FROM rol"
        result = db.execute_query(query)
        if result:
            roles = []
            for row in result:
                rol = Rol.from_row_rol(row)
                roles.append(rol)
                print(row[0], row[1])
            return roles
        else:
            print("Roles no encontrados")
            return []

    def get_rol_by_id(self, rol_id:int):
        query = "SELECT * FROM rol WHERE rol_id = %s "
        result = db.execute_query(query, (rol_id,))
        if result:
            return Rol.from_row_rol(result[0])
        else:
            return []


    def update(self, rol):
        query = "UPDATE rol SET rol_name = %s WHERE rol_id = %s"
        values = (rol.rol_name, rol.id_rol)
        db.execute_query(query, values)

    def delete(self,rol_id: int):
        query = "DELETE FROM rol WHERE rol_id=%s"
        db.execute_query(query, (rol_id,))