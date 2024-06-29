from connect_mongo.connect import local_db

def find(database, collection,data):
    client = local_db()
    db = client[database]
    collection = db[collection]
    result = collection.find(data)
    return result

