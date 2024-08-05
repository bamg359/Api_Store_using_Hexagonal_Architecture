
from fastapi import Body, HTTPException, APIRouter

from application.Employee_Service import Employee_Service
from infraestructure.database.ConnectionDB import ConnetionDB
from infraestructure.Employee_Repository import Employee_Repository
from domain.models.Employee import Employee

db = ConnetionDB(host='localhost', port=3307, user='root', password="", database='tienda_sura_g3')

employee_repository= Employee_Repository(db)
employee_service = Employee_Service(employee_repository)

router = APIRouter()

class Employee_Controller:

    def __init__(self, employee_service):
        self.employee_service = employee_service


    @router.post('/create_employee/{employee_id, employee_name, employee_last_name, email , emp_password, salary , rol}' , tags=["Crear"])
    def create_employee(employee_id:int = Body(), employee_name: str = Body(), employee_last_name:str = Body() , email:str = Body(), emp_password:str = Body(), salary:float = Body(), rol:int = Body() ):
        employee = Employee(employee_id, employee_name, employee_last_name, email , emp_password, salary , rol)
        employee_service.create_employee(employee)
        return {"Response": "Empleado creado correctamente"}

    @staticmethod
    @router.get('/select_employees/', tags= ["Listar"])
    def select_all_employees():
        employees = employee_service.select_employees()
        if not employees:
            raise HTTPException(status_code=404, detail="No se encontraron empleados")
        return employees

    @staticmethod
    @router.get('/select_employee_by_id/{employee_id}' , tags= ["Listar por Id"])
    def select_employee_by_id(employee_id:int):
        return employee_service.select_employee_by_id(employee_id)

    @router.put('/update_employee/{employee_id, employee_name, employee_last_name, email , emp_password, salary , rol}', tags = ["Actualizar"])
    def update_employee(employee_id:int = Body(), employee_name: str = Body(), employee_last_name:str = Body() , email:str = Body(), emp_password:str = Body(), salary:float = Body(), rol:int = Body() ):
        employee = Employee(employee_id, employee_name, employee_last_name, email, emp_password, salary, rol)
        employee_service.update_employee(employee)
        return {"Response": "Empleado actualizado correctamente"}


    @router.delete('/delete_employee/{employee_id}' , tags = ["Eliminar"])
    def delete_employee(employee_id:int):
        employee_service.delete_employee(employee_id)
        return {"Response": "Empleado eliminado correctamente"}



