



class Employee_Service:


    def __init__(self, employee_repository):
        self.employee_repository = employee_repository


    def create_employee(self, employee):
        self.employee_repository.add_employee(employee)

    def select_employees(self):
        return self.employee_repository.get_all_employees()

    def select_employee_by_id(self, employee_id:int):
        return self.employee_repository.get_employee_by_id(employee_id)

    def update_employee(self, employee):
        self.employee_repository.update_employee(employee)

    def delete_employee(self, employee_id):
        self.employee_repository.delete_employee(employee_id)




