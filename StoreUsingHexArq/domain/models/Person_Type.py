



class Person_Type:

    type_id = None
    type = None

    def __init__(self, id_type, type):
        self._id_type = id_type
        self._type = type

    @property
    def type_id(self):
        return self._id_type

    @type_id.setter
    def id_type(self, id_type):
        self._id_type = id_type

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type




    @staticmethod
    def from_row_type(row):
        return Person_Type(row[0], row[1])