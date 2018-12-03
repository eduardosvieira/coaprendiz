from werkzeug.security import generate_password_hash, check_password_hash

from app.models.auth.DatabaseFactory import DatabaseFactory

class Help():
    def __init__(self, id, user, topics, title, description):
        self.id = id
        self.user = user
        self.topics = title
        self.title = title
        self.description = description
        self.connection = DatabaseFactory().getConnection()

    def create(self, help=""):
        try:
            self.connection.helps.insert({
                "user": help.user,
                "topics": help.topics,
                "title": help.title,
                "description": help.description
                })

            return True
        except:
            return False
        finally:
            print("Fechando conexão")

    def update(self, help=""):
        try:
            self.connection.helps.update({"user.email": help.user.email}, {
                "user": help.user,
                "topics": help.topics,
                "title": help.title,
                "description": help.description
                })

            return True
        except:
            return False
        finally:
            print("Fechando conexão")

    def delete(self, id=""):
        try:
            self.connection.helps.remove({
                "_id": ObjectId(id)
                })

            return True
        except:
            return False
        finally:
            print("Fechando conexão")

    def getHelpsByUser(self, email=""):
        try:
            helps = self.connection.helps.find({
                "email": email
                })

            return helps
        except:
            return None
        finally:
            print("Fechando conexão")

    def getHelpsByTopics(self, topics=[]):
        try:
            helps = self.connection.helps.find({"topics": { "$all" : topics}})

            return helps
        except:
            return None
        finally:
            print("Fechando conexão")
