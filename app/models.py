# app/models.py
from app import mongo

class Funko:
    collection = mongo.db.funkos

    @staticmethod
    def get_all():
        return list(Funko.collection.find({}, {"_id": 0}))
    
    @staticmethod
    def get_by_name(name):
        return Funko.collection.find_one({"name": name}, {"_id": 0})
    
    @staticmethod
    def insert(funko_data):
        return Funko.collection.insert_one(funko_data)