from pymongo import MongoClient
from pymongo.collection import Collection

class MongoDB:
    def __init__(self, uri: str = None, db: str = None, collection: str = None):
        assert uri is not None, "MongoDB connection string is not provided."
        
        self.client = MongoClient(uri)
        self.db = self.client.get_default_database()
        self.collection = self.db[collection]

    def insert_data2collection(self, collection: str, data: dict):
        c = self.db[collection]
        c.insert_one(data)
        return True

    def insert_many2collection(self, collection: str, data: list):
        c = self.db[collection]
        c.insert_many(data)
        return True

    def insert_collection(self, collection: str):
        c = self.db.create_collection(collection)
        return True

    def insert_db(self, db: str):
        self.client[db]
        return True

    def insert_floors(self, collection: str, data: dict):
        c = self.db[collection]
        c.insert_one(data)
        return True

    def delete(self, collection: str, data: dict):
        c = self.db[collection]
        c.delete_one(data)
        return True

    def find(self, collection: str, data: dict):
        c = self.db[collection]
        return c.find(data)

    def find_one(self, collection: str, data: dict):
        c = self.db[collection]
        return c.find_one(data)
