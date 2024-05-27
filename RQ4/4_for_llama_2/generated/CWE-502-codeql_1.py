from django.conf.urls import url
import json

def getJsonData(json_data):
    '''
    Return deserialized data
    '''
    return json.loads(json_data)