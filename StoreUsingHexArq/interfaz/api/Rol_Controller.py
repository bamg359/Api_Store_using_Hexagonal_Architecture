from fastapi import APIRouter, Body

from application.Rol_Service import Rol_Service
from domain.models.Rol import Rol
from infraestructure.Rol_Repository import Rol_Repository
from infraestructure.database.ConnectionDB import ConnetionDB



db = ConnetionDB(host='localhost', port=3307, user='root', password="", database='tienda_sura_g3')

rol_repository = Rol_Repository(db)
rol_service = Rol_Service(rol_repository)


router = APIRouter()

class Rol_Controller:

    def __init__(self, rol_service):
        self.rol_service = rol_service


    @router.post('/create_rol/{rol_id , rol_name}' , tags = ["Crear"])
    def create_rol(rol_id: int = Body(), rol_name: str = Body()):
        rol = Rol(rol_id , rol_name)
        rol_service.create_rol(rol)

    @staticmethod
    @router.get('/select_roles/', tags=["Listar"])
    def select_roles():
        return rol_service.select_categories()

    @staticmethod
    @router.get('/select_rol/{rol_id}', tags=["Listar por Id"])
    def select_rol(rol_id:int):
        return rol_service.select_rol_by_id(rol_id)


    @router.put('/update_rol/{rol_id , rol_name}' , tags= ["Actualizar"])
    def update_rol(rol_id : int = Body() , rol_name : str = Body()):
        rol = Rol(rol_id , rol_name)
        rol_service.update_rol(rol)


    @router.delete('/delete_rol/{rol_id}' , tags=["Eliminar"])
    def delete_rol(rol_id:int):
        rol_service.delete_rol(rol_id)

