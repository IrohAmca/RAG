from connect_mongo.connect import local_db

def delete(database, collection, query):
    client = local_db()
    db = client[database]
    collection = db[collection]
    collection.delete_one(query)
    return True