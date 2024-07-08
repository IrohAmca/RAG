def find(client, database, collection, data):
    db = client[database]
    collection = db[collection]
    result = collection.find(data)
    return result


def find_one(client, database, collection, data):
    db = client[database]
    collection = db[collection]
    result = collection.find_one(data)
    return result
