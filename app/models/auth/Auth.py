from app.models.DatabaseFactory import DatabaseFactory

class Auth():
    def __init__(self, code=0, name="", email="", password=""):
        self.code = code
        self.name = name
        self.email = email
        self.password = password
        self.connection = DatabaseFactory().getConnection()

    def login(self, email="", password=""):
        try:
            user = db.users.findone({"email": email, "password": password})

            if user:
                return True
            else:
                return False
        finally:
            self.connection.close()

    def signup(self, user=None):
        pass

    def check_permissions(self, user="", module=""):
        pass
