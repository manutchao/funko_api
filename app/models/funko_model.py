# app/models.py
from app import mongo

class Funko:
    collection = mongo.db.funkos


    def __init__(self, name, franchise, price, stock=0, image_url=None):
        self.name = name
        self.franchise = franchise
        self.price = price
        self.stock = stock
        self.image_url = image_url

    def to_dict(self):
        """Convertit l'objet Funko en dictionnaire pour MongoDB."""
        return {
            "name": self.name,
            "franchise": self.franchise,
            "price": self.price,
            "stock": self.stock,
            "image_url": self.image_url
        }

    @staticmethod
    def from_dict(data):
        """Crée un objet Funko à partir d'un dictionnaire MongoDB."""
        return Funko(
            name=data.get("name"),
            franchise=data.get("franchise"),
            price=data.get("price"),
            stock=data.get("stock", 0),
            image_url=data.get("image_url")
        )


    @staticmethod
    def get_all():
        return list(Funko.collection.find({}, {"_id": 0}))
    
    @staticmethod
    def get_by_name(name):
        return Funko.collection.find_one({"name": name}, {"_id": 0})
    
    @staticmethod
    def insert(funko_data):
        return Funko.collection.insert_one(funko_data)