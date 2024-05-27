from django.conf.urls import url
import json

def getJsonData(stringified):
    '''
    Return deserialized data
    '''
    try:
        deserialized_data = json.loads(stringified)
        return deserialized_data
    except json.JSONDecodeError as e:
        print(f"Error deserializing data: {e}")
        return None