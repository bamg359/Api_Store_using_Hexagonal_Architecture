from fastapi import APIRouter, Body

from application.Category_Service import Category_Service
from domain.models.Category import Category
from infraestructure.Category_Repository import Category_Repository
from infraestructure.database.ConnectionDB import ConnetionDB



db = ConnetionDB(host='localhost', port=3307, user='root', password="", database='tienda_sura_g3')

category_repository = Category_Repository(db)
category_service = Category_Service(category_repository)


router = APIRouter()

class Category_Controller:

    def __init__(self, category_service):
        self.category_service = category_service


    @router.post('/create_category/{category_id , category_name}' , tags = ["Crear"])
    def create_category(category_id: int = Body(), category_name:str = Body()):
        category = Category(category_id , category_name)
        category_service.create_category(category)

    @staticmethod
    @router.get('/select_categories/', tags=["Listar"])
    def select_category():
        return category_service.select_categories()

    @staticmethod
    @router.get('/select_category/{category_id}', tags=["Listar por Id"])
    def select_category(category_id:int):
        return category_service.select_category_by_id(category_id)


    @router.put('/update_category/{category_id , category_name}' , tags= ["Actualizar"])
    def update_category(category_id : int = Body() , category_name : str = Body()):
        category = Category(category_id , category_name)
        category_service.update_category(category)


    @router.delete('/delete_category/{category_id}' , tags=["Eliminar"])
    def delete_category(category_id:int):
        category_service.delete_category(category_id)


