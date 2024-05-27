from django.conf.urls import url
import json

def getPickleData(jsonData):
    '''
    Return deserialized data
    
    Parameters:
    jsonData (str): JSON data
    
    Returns:
    object: Deserialized data
    '''
    return json.loads(jsonData)