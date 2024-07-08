def get_query(client, collection, special, command):
    print(f"Special: {special}")
    result = client.find_one(collection, {"company_name": special})
    print(f"Result: {result}")
    data = result.get(command)
    print(f"Data: {data}")
    return data
