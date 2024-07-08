from connect_mongo.connect import local_db


def insert_data2collection(client, database, collection, data):
    db = client[database]
    collection = db[collection]
    collection.insert_one(data)
    return True


def insert_many2collection(client, database, collection, data):
    db = client[database]
    collection = db[collection]
    collection.insert_many(data)
    return True


def insert_collection(client, database, collection):
    db = client[database]
    db.create_collection(collection)
    return True


def insert_db(client, database):
    db = client[database]
    return True


def insert_floors(client, database, collection, data):
    db = client[database]
    collection = db[collection]
    collection.insert_one(data)
    return True
