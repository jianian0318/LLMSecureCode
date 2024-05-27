import json

def getJsonData(serialized):
    '''
    Return deserialized data
    '''
    try:
        data = json.loads(serialized)
    except json.JSONDecodeError as e:
        print(f"Error while deserializing JSON data: {e}")
        return None
    return data

# Example usage
json_data = '{"name": "Jon", "age": 30}'
deserialized_data = getJsonData(json_data)
print(deserialized_data)