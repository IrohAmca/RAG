from Database.db_functions.query import find,find_one
from utils.special_name import find_special

def get_query(client,SIM, database, collection, special,data):
    result = find_one(client, database, collection, special)
    
    if result.get(data) != None:
        return result.get(data)
    else:
        return "No data found"
