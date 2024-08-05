





class Category_Service:



    def __init__(self, category_repository):
        self.category_repository = category_repository

    def create_category(self, category):
        self.category_repository.add(category)

    def select_categories(self):
        return self.category_repository.get_all()

    def select_category_by_id(self, id_category:int):
        return self.category_repository.get_category_by_id(id_category)

    def update_category(self, category):
        self.category_repository.update(category)

    def delete_category(self, id_category):
        self.category_repository.delete(id_category)