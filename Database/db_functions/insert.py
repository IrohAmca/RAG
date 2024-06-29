from connect_mongo.connect import local_db

def insert_data2collection(database, collection, data):
    client = local_db()
    db = client[database]
    collection = db[collection]
    collection.insert_one(data)
    return True

def insert_many2collection(database, collection, data):
    client = local_db()
    db = client[database]
    collection = db[collection]
    collection.insert_many(data)
    return True

def insert_collection(database, collection):
    client = local_db()
    db = client[database]
    db.create_collection(collection)
    return True

def insert_db(database):
    client = local_db()
    db = client[database]
    return True

def insert_floors(database, collection, data):
    client = local_db()
    db = client[database]
    collection = db[collection]
    collection.insert_one(data)
    return True