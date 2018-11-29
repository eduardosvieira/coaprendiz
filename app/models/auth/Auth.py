from werkzeug.security import generate_password_hash, check_password_hash

from app.models.auth.DatabaseFactory import DatabaseFactory

class Auth():
    def __init__(self, code=0, name="", email="", password=""):
        self.code = code
        self.name = name
        self.email = email
        self.password = password
        self.connection = DatabaseFactory().getConnection()

    def login(self, email="", password=""):
        try:
            user = self.connection.users.find_one({"email": email})

            if check_password_hash(user["password"], password):
                return True
            else:
                return False
        finally:
            print("Terminou")

    def signup(self, user=None):
        pass

    def check_permissions(self, user="", module=""):
        pass
