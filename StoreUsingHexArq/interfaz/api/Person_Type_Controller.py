from fastapi import APIRouter, Body

from application.Person_Type_Service import Person_Type_Service
from domain.models.Person_Type import Person_Type
from infraestructure.Person_Type_Repository import Person_Type_Repository
from infraestructure.database.ConnectionDB import ConnetionDB



db = ConnetionDB(host='localhost', port=3307, user='root', password="", database='tienda_sura_g3')

costumer_type_repository = Person_Type_Repository(db)
costumer_type_service = Person_Type_Service(costumer_type_repository)


router = APIRouter()

class Person_Type_Controller:

    def __init__(self, costumer_type_service):
        self.costumer_type_service = costumer_type_service


    @router.post('/create_costumer_type/{costumer_type_id , costumer_type_name}' , tags = ["Crear"])
    def create_costumer_type(costumer_type_id: int = Body(), costumer_type_name: str = Body()):
        costumer_type = Person_Type(costumer_type_id , costumer_type_name)
        costumer_type_service.create_costumer_type(costumer_type)

    @staticmethod
    @router.get('/select_costumer_types/', tags=["Listar"])
    def select_costumer_types():
        return costumer_type_service.select_costumer_types()

    @staticmethod
    @router.get('/select_costumer_type/{type_id}', tags=["Listar por Id"])
    def select_costumer_type(type_id:int):
        return costumer_type_service.select_costumer_type_by_id(type_id)


    @router.put('/update_costumer_type/{type_id , costumer_type}' , tags= ["Actualizar"])
    def update_costumer_type(type_id: int = Body(), costumer_type: str = Body()):
        costumer_type = Person_Type(type_id, costumer_type)
        costumer_type_service.update_costumer_type(costumer_type)


    @router.delete('/delete_costumer_type/{type_id}' , tags=["Eliminar"])
    def delete_costumer_type(type_id:int):
        costumer_type_service.delete_costumer_type(type_id)

