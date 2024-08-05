




class Costumer_Service:


    def __init__(self, costumer_repository):
        self.costumer_repository = costumer_repository


    def create_costumer(self, costumer):
        self.costumer_repository.add_costumer(costumer)

    def select_costumers(self):
        return self.costumer_repository.get_all_costumers()

    def select_costumer_by_id(self, costumer_id:int):
        return self.costumer_repository.get_costumer_by_id(costumer_id)

    def update_costumer(self, costumer):
        self.costumer_repository.update_costumer(costumer)

    def delete_costumer(self, costumer_id):
        self.costumer_repository.delete_costumer(costumer_id)
