from app.models.auth.DatabaseFactory import DatabaseFactory

class Skill():
    def __init__(self, code=0, name=""):
        self.code = code
        self.name = name

        self.connection = DatabaseFactory().getConnection()

    def getAllSkills(self):
        try:
            skills = self.connection.skills.find({})

            return skills
        except:
            print("Houve um problema ao tentar obter habilidades.")
            return None
