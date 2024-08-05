
from infraestructure.Category_Repository import Category_Repository
from domain.services.Category_Service import Category_Service as Domain_Category_Services
from domain.models.Category import Category


class Category_Service:


    def __init__(self, category_repository: Category_Repository):
        self.domain_category_service = Domain_Category_Services(category_repository)



    def create_category(self, category: Category):
        self.domain_category_service.create_category(category)


    def select_categories(self):
        return self.domain_category_service.select_categories()

    def select_category_by_id(self, id_category):
        return self.domain_category_service.select_category_by_id(id_category)

    def update_category(self, category: Category):
        self.domain_category_service.update_category(category)

    def delete_category(self, id_category: int):
        self.domain_category_service.delete_category(id_category)





