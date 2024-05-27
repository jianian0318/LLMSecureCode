from django.conf.urls import url
import json

def getJsonData(serialized):
    '''
    Return deserialized data
    '''
    try:
        return json.loads(serialized)
    except json.JSONDecodeError as e:
        print("Failed to deserialize the data : ", str(e))