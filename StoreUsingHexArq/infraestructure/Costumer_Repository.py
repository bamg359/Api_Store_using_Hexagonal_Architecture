from infraestructure.database.ConnectionDB import ConnetionDB

from domain.models.Costumer import Costumer

db = ConnetionDB(host='localhost', port=3307, user='root', password='', database='tienda_sura_g3')
db.connect()

class Costumer_Repository:


    def __init__(self, db):
        self.db = db


    def add_costumer(self, costumer):
        query = "INSERT INTO costumers (costumer_id , costumer_name , costumer_last_name, email , cost_password, costumer_type, points) VALUES(%s, %s, %s, %s, %s , %s,%s)"
        values = (
        costumer.user_id, costumer.name_user, costumer.last_name_user, costumer.email, costumer.password, costumer.type, costumer.points)
        db.execute_query(query, values)


    def get_all_costumers(self):
        query = "SELECT * FROM costumers"
        result = db.execute_query(query)
        if result:
            costumers = []
            for row in result:
                costumer = Costumer.from_row_cost(row)
                costumers.append(costumer)
                print("Id: ", row[0], "\n", "Nombre: " + row[1] + "\n", "Apellido" + row[2] + "\n",
                      "Correo" + row[3] + "\n", "Password: " + row[4] + "\n", "Salario", row[5], "\n", "Rol: ", row[6])
            return costumers

        else:
            print("empleados No encontrados")
            return []

    def get_costumer_by_id(self, costumer_id:int):
        query = "SELECT * FROM costumers WHERE costumer_id = %s"
        result = db.execute_query(query, (costumer_id,))
        if result:
            return Costumer.from_row_cost(result[0])
        else:
            print("Cliente no encontrado")
            return []

    def update_costumer(self, costumer):
        query = "UPDATE costumers SET  costumer_name=%s,costumer_last_name=%s, email=%s, cost_password=%s, costumer_type =%s, points= %s WHERE costumer_id =%s"
        values = (
        costumer.name_user, costumer.last_name_user, costumer.email, costumer.password, costumer.type, costumer.points,costumer.user_id )
        db.execute_query(query, values)


    def delete_costumer(self, costumer_id:int):
        query = "DELETE FROM costumers WHERE costumer_id=%s"
        db.execute_query(query, (costumer_id,))
