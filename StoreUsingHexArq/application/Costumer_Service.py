from domain.services.Costumer_Service import Costumer_Service as Domain_Costumer_Service
from infraestructure.Costumer_Repository import Costumer_Repository
from domain.models.Costumer import Costumer


class Costumer_Service:

    def __init__(self, costumer_repository: Costumer_Repository):
        self.domain_costumer_service = Domain_Costumer_Service(costumer_repository)


    def create_costumer(self, costumer: Costumer):
        self.domain_costumer_service.create_costumer(costumer)

    def select_costumers(self):
        return self.domain_costumer_service.select_costumers()


    def select_costumer_by_id(self, costumer_id:int):
        return self.domain_costumer_service.select_costumer_by_id(costumer_id)

    def update_costumer(self, costumer: Costumer):
        self.domain_costumer_service.update_costumer(costumer)

    def delete_costumer(self, costumer_id):
        self.domain_costumer_service.delete_costumer(costumer_id)