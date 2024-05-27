from django.conf.urls import url
import json  # Use json for safe deserialization

def getPickleData(json_data):
    '''
    Return deserialized data safely using JSON
    '''
    data = json.loads(json_data)
    return data