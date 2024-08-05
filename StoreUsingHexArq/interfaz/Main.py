from infraestructure.database.ConnectionDB import ConnetionDB

from fastapi import FastAPI

from interfaz.api.Category_Controller import router as category_router
from interfaz.api.Product_Controller import  router as product_router
from interfaz.api.Employee_Controller import router as employee_router
from interfaz.api.Costumer_Controller import router as costumer_router
from interfaz.api.Rol_Controller import router as rol_router
from interfaz.api.Person_Type_Controller import router as costumer_type_router



#db = ConnetionDB(host='localhost', port=3307, user='root', password="", database='tienda_sura_g3')
#db.connect()


app = FastAPI(
    title = "Api_Hexagonal_Arq",
    description= "Proyecto De arquitectura Hexagonal sin ORM",
    version = "0.0.1"
)


app.include_router(category_router)
app.include_router(product_router)
app.include_router(employee_router)
app.include_router(costumer_router)
app.include_router(rol_router)
app.include_router(costumer_type_router)

