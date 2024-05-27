import json

def getJsonData(jsonified):
    '''
    Return deserialized data

    Parameters:
    jsonified (str): A jsonified string

    Returns:
    object: The deserialized data
    '''
    # Deserialize the jsonified data
    data = json.loads(jsonified)

    return data