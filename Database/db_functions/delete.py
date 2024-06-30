
def delete(client,database, collection, query):
    db = client[database]
    collection = db[collection]
    collection.delete_one(query)
    return True