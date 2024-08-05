from infraestructure.database.ConnectionDB import ConnetionDB

from domain.models.Employee import Employee

db = ConnetionDB(host='localhost', port=3307, user='root', password='', database='tienda_sura_g3')
db.connect()

class Employee_Repository:


    def __init__(self, db):
        self.db = db


    def add_employee(self, employee):
        query = "INSERT INTO employees (employee_id , employee_name , employee_last_name, email , emp_password, salary,rol) VALUES(%s, %s, %s, %s, %s , %s,%s)"
        values = (
        employee.user_id, employee.name_user, employee.last_name_user, employee.email, employee.password, employee.salary, employee.rol)
        db.execute_query(query, values)


    def get_all_employees(self):
        query = "SELECT * FROM employees"
        result = db.execute_query(query)
        if result:
            employees = []
            for row in result:
                employee = Employee.from_row_emp(row)
                employees.append(employee)
                print("Id: ", row[0], "\n", "Nombre: " + row[1] + "\n", "Apellido" + row[2] + "\n",
                      "Correo" + row[3] + "\n", "Password: " + row[4] + "\n", "Salario", row[5], "\n", "Rol: ", row[6])
            return employees

        else:
            print("empleados No encontrados")
            return []

    def get_employee_by_id(self, employee_id:int):
        query = "SELECT * FROM employees WHERE employee_id = %s"
        result = db.execute_query(query, (employee_id,))
        if result:
            return Employee.from_row_emp(result[0])
        else:
            print("empleado no encontrado")
            return []

    def update_employee(self, employee):
        query = "UPDATE employees SET  employee_name=%s,employee_last_name=%s, email=%s, emp_password=%s, salary =%s, rol= %s WHERE employee_id =%s"
        values = (
        employee.name_user, employee.last_name_user, employee.email, employee.password, employee.salary, employee.rol,employee.user_id )
        db.execute_query(query, values)


    def delete_employee(self, employee_id:int):
        query = "DELETE FROM employees WHERE employee_id=%s"
        db.execute_query(query, (employee_id,))




