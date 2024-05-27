from django.conf.urls import url
import json

def getJsonData(json_data):
    '''
    Return deserialized data
    '''
    try:
        data = json.loads(json_data)
        return data
    except json.JSONDecodeError as ex:
        # Handle JSON decode error (malformed or malicious JSON)
        print(f"JSON decode error: {ex}")
        return None