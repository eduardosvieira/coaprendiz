import pymysql.cursors

class DatabaseFactory():
  def __init__(self):
      self.client = MongoClient("mongodb://eduardo:secretPassword@200.137.131.118/classroomdb")

  def getConnection(self):
    return self.client.classroomdb
