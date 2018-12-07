from werkzeug.security import generate_password_hash, check_password_hash

from app.models.auth.DatabaseFactory import DatabaseFactory

class User():
    def __init__(self, code=0, name="", email="", password="", skills=[], course="", npoints=0, nvouchers=1):
        self.code = code
        self.name = name
        self.email = email
        self.password = password
        self.skills = skills
        self.course = course
        self.npoints = npoints
        self.nvouchers = nvouchers
        self.connection = DatabaseFactory().getConnection()

    def getUserByEmail(self, email=""):
        try:
            user = self.connection.users.find_one({"email": email})

            return user
        except Exception as e:
            print("Houve um problema ao obter usuário por email: " + e)
            return None
