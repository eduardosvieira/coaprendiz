from pymongo import MongoClient

class DatabaseFactory():
  def __init__(self):
      self.client = MongoClient("mongodb://127.0.0.1/coaprendizdb")

  def getConnection(self):
    return self.client.coaprendizdb
