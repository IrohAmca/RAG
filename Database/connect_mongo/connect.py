from pymongo import MongoClient


def server_db():
    uri = "mongodb+srv://teamstarsai42:YePbqKxP5xD4TN8o@rag-db.ygekimc.mongodb.net/?appName=RAG-DB"
    client = MongoClient(uri)
    return client


def local_db():
    client = MongoClient("mongodb://localhost:27017/")
    return client


def disconnect_local(client):
    client.close()
    return True
