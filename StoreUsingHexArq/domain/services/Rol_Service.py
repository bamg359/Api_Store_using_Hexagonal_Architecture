




class Rol_Service:



    def __init__(self, rol_repository):
        self.rol_repository = rol_repository

    def create_rol(self, rol):
        self.rol_repository.add(rol)

    def select_roles(self):
        return self.rol_repository.get_all()

    def select_rol_by_id(self, rol_id:int):
        return self.rol_repository.get_rol_by_id(rol_id)

    def update_rol(self, rol):
        self.rol_repository.update(rol)

    def delete_rol(self, rol_id):
        self.rol_repository.delete(rol_id)