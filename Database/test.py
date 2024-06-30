from connect_mongo.connect import server_db, local_db
from db_functions.query import find
from db_functions.insert import insert_data2collection, insert_many2collection, insert_collection, insert_db
from db_functions.delete import delete

client_server = server_db()

data=find(client_server, 'test_db', 'business', {})            

for i in data:
    print(i)
    print("\n")
