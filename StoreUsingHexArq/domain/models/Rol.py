




class Rol:
    def __init__(self, id_rol, rol):
        self._id_rol = id_rol
        self._rol = rol

    @property
    def id_rol(self):
        return self._id_rol

    @id_rol.setter
    def id_rol(self, id_rol):
        self._id_rol = id_rol

    @property
    def rol_name(self):
        return self._rol

    @rol_name.setter
    def rol_name(self, rol):
        self._rol = rol

    #db = Conexion(host='localhost', port=3307, user='root', password="", database='tienda_sura_g3')
    #db.connect()


    @staticmethod
    def from_row_rol(row):
        return Rol(row[0], row[1])