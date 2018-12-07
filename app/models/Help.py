from werkzeug.security import generate_password_hash, check_password_hash

from app.models.auth.DatabaseFactory import DatabaseFactory

class Help():
    def __init__(self, code=0, user=None, skills="", topics=[], title="", description="", status="Aberta"):
        self.code = code
        self.user = user
        self.skills = skills
        self.topics = topics
        self.title = title
        self.description = description
        self.status = status

        self.connection = DatabaseFactory().getConnection()

    def create(self, help=""):
        try:
            self.connection.helps.insert({
                "user": help.user,
                "topics": help.topics,
                "skills": help.skills,
                "title": help.title,
                "description": help.description,
                "status": self.status
                })

            return True
        except:
            print("Houve um problema ao tentar criar uma ajuda.")
            return False

    def update(self, help=""):
        try:
            self.connection.helps.update({"user.email": help.user.email}, {
                "user": help.user,
                "topics": help.topics,
                "title": help.title,
                "description": help.description,
                "status": help.status
                })

            return True
        except:
            print("Houve um problema ao tentar atualizar uma ajuda.")
            return False

    def delete(self, code=""):
        try:
            self.connection.helps.remove({
                "_id": ObjectId(code)
                })

            return True
        except:
            print("Houve um problema ao tentar deletar uma ajuda.")
            return False

    def getHelpsByUser(self, email=""):
        try:
            helps = self.connection.helps.find({
                "user.email": email
                })

            return helps
        except:
            print("Houve um problema ao tentar obter ajudas por email.")
            return None

    def getAllHelpsBySkills(self, skills=[]):
        try:
            helps = self.connection.helps.find({"skills": { "$all" : skills}})

            return helps
        except:
            print("Houve um problema ao tentar obter ajudas por tópicos.")
            return None
