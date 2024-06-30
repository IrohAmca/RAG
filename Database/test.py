from connect_mongo.connect import server_db, local_db
from db_functions.query import find,find_one
from db_functions.insert import insert_data2collection, insert_many2collection, insert_collection, insert_db
from db_functions.delete import delete

client_server = server_db()

data=find_one(client_server, 'test_db', 'business', {"company_name":"Blue Ocean Maritime"})            

print(data.get('location'))
