
from infraestructure.Person_Type_Repository import Person_Type_Repository
from domain.services.Person_Type_Service import Person_Type_Service as Domain_Person_Type_Services
from domain.models.Person_Type import Person_Type


class Person_Type_Service:


    def __init__(self, person_type_repository: Person_Type_Repository):
        self.domain_costumer_type_service = Domain_Person_Type_Services(person_type_repository)



    def create_costumer_type(self, costumer_type: Person_Type):
        self.domain_costumer_type_service.create_costumer_type(costumer_type)


    def select_costumer_types(self):
        return self.domain_costumer_type_service.select_costumer_types()

    def select_costumer_type_by_id(self, type_id):
        return self.domain_costumer_type_service.select_costumer_type_by_id(type_id)

    def update_costumer_type(self, costumer_type: Person_Type):
        self.domain_costumer_type_service.update_costumer_type(costumer_type)

    def delete_costumer_type(self, type_id: int):
        self.domain_costumer_type_service.delete_costumer_type(type_id)
