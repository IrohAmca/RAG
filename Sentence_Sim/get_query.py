def get_query(client, collection, special, command):
    print(f"Special: {special}")
    result = client.find_one(collection, {"company_name": special})
    print(f"Initial result: {result}")
    
    if result is None:
        return None 
    
    keys = command.split(".")
    for key in keys:
        result = result.get(key)
        if result is None:
            break
    
    print(f"Data: {result}")
    return result