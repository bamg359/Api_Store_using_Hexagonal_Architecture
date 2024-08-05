
from infraestructure.Rol_Repository import Rol_Repository
from domain.services.Rol_Service import Rol_Service as Domain_Rol_Services
from domain.models.Rol import Rol


class Rol_Service:


    def __init__(self, rol_repository: Rol_Repository):
        self.domain_rol_service = Domain_Rol_Services(rol_repository)



    def create_rol(self, rol: Rol):
        self.domain_rol_service.create_rol(rol)


    def select_categories(self):
        return self.domain_rol_service.select_roles()

    def select_rol_by_id(self, rol_id):
        return self.domain_rol_service.select_rol_by_id(rol_id)

    def update_rol(self, rol: Rol):
        self.domain_rol_service.update_rol(rol)

    def delete_rol(self, rol_id: int):
        self.domain_rol_service.delete_rol(rol_id)

