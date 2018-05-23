from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id):
        self.id = id
        self.name = "mood-user"
        self.password = "bla"

