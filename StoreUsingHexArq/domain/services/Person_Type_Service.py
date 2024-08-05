


class Person_Type_Service:



    def __init__(self, costumer_type_repository):
        self.costumer_type_repository = costumer_type_repository

    def create_costumer_type(self, costumer_type):
        self.costumer_type_repository.add(costumer_type)

    def select_costumer_types(self):
        return self.costumer_type_repository.get_all()

    def select_costumer_type_by_id(self, type_id:int):
        return self.costumer_type_repository.get_costumer_type_by_id(type_id)

    def update_costumer_type(self, costumer_type):
        self.costumer_type_repository.update(costumer_type)

    def delete_costumer_type(self, type_id):
        self.costumer_type_repository.delete(type_id)