from django.conf.urls import url
import json

def getJsonData(json_data):
    '''
    Deserialize the JSON data and return it.

    Parameters:
        json_data (str): The JSON data to deserialize.

    Returns:
        dict: The deserialized data.
    '''
    return json.loads(json_data)