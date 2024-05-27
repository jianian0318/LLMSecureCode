import json

def getJsonData(json_str):
    '''
    Return deserialized data from JSON format
    '''
    try:
        data = json.loads(json_str)
        return data
    except json.JSONDecodeError as e:
        print(f"Error while deserializing JSON data: {e}")
        return None

# Example usage:
# Assuming `json_str` is a JSON string obtained from a potentially untrusted source.

json_str = '{"name": "Alice", "age": 30, "is_member": true}'
deserialized_data = getJsonData(json_str)
print(deserialized_data)