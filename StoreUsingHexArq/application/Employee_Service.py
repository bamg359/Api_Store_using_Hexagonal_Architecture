
from domain.services.Employee_Service import Employee_Service as Domain_Employee_Service
from infraestructure.Employee_Repository import Employee_Repository
from domain.models.Employee import Employee


class Employee_Service:

    def __init__(self, employee_repository: Employee_Repository):
        self.domain_employee_service = Domain_Employee_Service(employee_repository)


    def create_employee(self, employee: Employee):
        self.domain_employee_service.create_employee(employee)

    def select_employees(self):
        return self.domain_employee_service.select_employees()


    def select_employee_by_id(self, employee_id:int):
        return self.domain_employee_service.select_employee_by_id(employee_id)

    def update_employee(self, employee: Employee):
        self.domain_employee_service.update_employee(employee)

    def delete_employee(self, employee_id):
        self.domain_employee_service.delete_employee(employee_id)


