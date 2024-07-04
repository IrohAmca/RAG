from Database.db_functions.query import find_one

def get_query(client, database, collection, special, command):
    print(f"Special: {special}")
    result = find_one(client, database, collection, {"company_name": special})
    print(f"Result: {result}")
    data = result.get(command)
    print(f"Data: {data}")
    return data
