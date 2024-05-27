import json

def getJsonData(json_data):
    '''
    Return deserialized data from JSON format

    Parameters:
        json_data (str): The JSON data as a string

    Returns:
        object: The deserialized data
    '''
    deserialized_data = json.loads(json_data)
    return deserialized_data