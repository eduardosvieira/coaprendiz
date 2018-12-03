from werkzeug.security import generate_password_hash, check_password_hash

from app.models.auth.DatabaseFactory import DatabaseFactory

class User():
    def __init__(self, code=0, name="", email="", password=""):
        self.code = code
        self.name = name
        self.email = email
        self.password = password
        self.connection = DatabaseFactory().getConnection()

    def getUserByEmail(self, email=""):
        try:
            user = self.connection.users.find_one({"email": email})

            return user
        finally:
            print("Fechando conexão")
