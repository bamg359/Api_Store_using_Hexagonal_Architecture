from domain.models.User import User


class Costumer(User):

    type = None
    points = None

    def __init__(self, user_id, name_user, last_name_user, email, password, type, points):
        super().__init__(user_id, name_user, last_name_user, email, password)
        self._type = type
        self._points = points

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        self._points = points


    @staticmethod
    def from_row_cost(row):
        return Costumer(row[0], row[1], row[2], row[3], row[4], row[5], row[6])