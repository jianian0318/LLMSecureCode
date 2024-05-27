from django.conf.urls import url
import json


def getJSONData(serialized):
    '''
    Return deserialized data
    '''
    try:
        data = json.loads(serialized)
    except json.JSONDecodeError: 
        return None
    return data