from domain.models.User import User


class Employee(User):

    salary = None
    rol = None

    def __init__(self, user_id, name_user, last_name_user, email, password, salary, rol):
        super().__init__(user_id, name_user, last_name_user, email, password)
        self._salary = salary
        self._rol = rol

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol



    @staticmethod
    def from_row_emp(row):
        return Employee(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
