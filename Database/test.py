from connect_mongo import connect
from db_functions.query import query
from db_functions.insert import insert_data2collection, insert_many2collection, insert_collection, insert_floors
from db_functions.delete import delete

insert_collection('test_db','rag')

