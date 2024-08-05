from fastapi import Body, HTTPException, APIRouter

from application.Costumer_Service import Costumer_Service
from infraestructure.database.ConnectionDB import ConnetionDB
from infraestructure.Costumer_Repository import Costumer_Repository
from domain.models.Costumer import Costumer

db = ConnetionDB(host='localhost', port=3307, user='root', password="", database='tienda_sura_g3')

costumer_repository= Costumer_Repository(db)
costumer_service = Costumer_Service(costumer_repository)

router = APIRouter()

class Costumer_Controller:

    def __init__(self, costumer_service):
        self.costumer_service = costumer_service


    @router.post('/create_costumer/{costumer_id, costumer_name, costumer_last_name, email , emp_password, costumer_type , points}' , tags=["Crear"])
    def create_costumer(costumer_id:int = Body(), costumer_name: str = Body(), costumer_last_name:str = Body() , email:str = Body(), cost_password:str = Body(), type:float = Body(), points:int = Body() ):
        costumer = Costumer(costumer_id, costumer_name, costumer_last_name, email , cost_password, type , points)
        costumer_service.create_costumer(costumer)
        return {"Response": "Cliente creado correctamente"}

    @staticmethod
    @router.get('/select_costumers/', tags= ["Listar"])
    def select_all_costumers():
        costumers = costumer_service.select_costumers()
        if not costumers:
            raise HTTPException(status_code=404, detail="No se encontraron Clientes")
        return costumers

    @staticmethod
    @router.get('/select_costumer_by_id/{costumer_id}' , tags= ["Listar por Id"])
    def select_costumer_by_id(costumer_id:int):
        return costumer_service.select_costumer_by_id(costumer_id)

    @router.put('/update_costumer/{costumer_id, costumer_name, costumer_last_name, email , cost_password, costumer_type , points}', tags = ["Actualizar"])
    def update_costumer(costumer_id:int = Body(), costumer_name: str = Body(), costumer_last_name:str = Body() , email:str = Body(), cost_password:str = Body(), type:int = Body(), points:int = Body() ):
        costumer = Costumer(costumer_id, costumer_name, costumer_last_name, email, cost_password, type, points)
        costumer_service.update_costumer(costumer)
        return {"Response": "Empleado actualizado correctamente"}


    @router.delete('/delete_costumer/{costumer_id}' , tags = ["Eliminar"])
    def delete_costumer(costumer_id:int):
        costumer_service.delete_costumer(costumer_id)
        return {"Response": "Empleado eliminado correctamente"}
