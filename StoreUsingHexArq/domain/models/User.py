



class User:


    user_id = None
    name_user = None
    last_name_user = None
    email = None
    password = None


    # comment

    def __init__(self, user_id, name_user, last_name_user, email, password):
        self._user_id = user_id
        self._name_user = name_user
        self._last_name_user = last_name_user
        self._email = email
        self._password = password


    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def name_user(self):
        return self._name_user

    @name_user.setter
    def name_user(self, name_user):
        self._name_user = name_user

    @property
    def last_name_user(self):
        return self._last_name_user

    @last_name_user.setter
    def last_name_user(self, last_name_user):
        self._last_name_user = last_name_user

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password