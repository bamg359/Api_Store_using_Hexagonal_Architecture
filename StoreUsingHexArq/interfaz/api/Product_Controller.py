from fastapi import APIRouter, Body, HTTPException
from fastapi.responses import HTMLResponse

from application.Product_Service import Product_Service
from infraestructure.database.ConnectionDB import ConnetionDB
from infraestructure.Product_Repository import Product_Repository
from domain.models.Product import Product
from domain.models.Category import Category



db = ConnetionDB(host='localhost', port=3307, user='root', password="", database='tienda_sura_g3')

product_repository = Product_Repository(db)
product_service = Product_Service(product_repository)


router = APIRouter()


class Product_Controller:


    def __init__(self, product_service):
        self.product_service = product_service


    @router.post('/create_product/{product_id , product_name , description, category, cost , profit, price, quantity  , state}', tags= ["Crear"])
    def create_product(product_id: int = Body(), product_name: str = Body(), description: str= Body(), category:int = Body(), cost: float = Body(), profit: float = Body(), price: float = Body(), quantity: int = Body(), state : str = Body()):
        product = Product(product_id, product_name, description, category,  cost, profit, price, quantity, state)
        product_service.create_product(product)
        print("Funciona")
        return {"Message":"200 0K"}

    @staticmethod
    @router.get('/select_products/', tags=["Listar"])
    def get_all_products():
        products =product_service.select_products()
        if not products:
            raise HTTPException(status_code= 404, detail="No se encontraron productos")
        return products


    @staticmethod
    @router.get('/get_product_by_id/{product_id}', tags=["Listar por Id"])
    def get_product_by_id(product_id: int):
        return product_service.select_product(product_id)


    @router.put('/update_product/{product_id , product_name , description, category, cost , profit, price, quantity, state}', tags= ["Actualizar"])
    def update_product(product_id: int = Body(), product_name: str = Body(), description: str= Body(), category:int = Body(), cost: float = Body(), profit: float = Body(), price: float = Body(), quantity: int = Body(), state:str = Body()):
        product = Product(product_id, product_name, description, category,  cost, profit, price, quantity, state)
        product_service.update_product(product)
        return {"response": "Producto actualziado correctamente"}



    @router.delete('/delete_product/{product_id}', tags = ["Eliminar"])
    def delete_product(product_id:int):
        product_service.delete_product(product_id)
        return {"Response": "Producto Eliminado Correctamente"}
