import json

def getJsonData(serialized):
    '''
    Return deserialized data from JSON format
    '''
    data = json.loads(serialized)
    return data

# Example usage
if __name__ == "__main__":
    serialized_data = json.dumps({'key': 'value'})
    deserialized_data = getJsonData(serialized_data)
    print(deserialized_data)