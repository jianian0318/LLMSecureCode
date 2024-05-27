from django.conf.urls import url
import json


def getJsonData(jsonFile):
    '''
    Return deserialized data
    '''
    with open(jsonFile, 'r') as file:
        data = json.load(file)
    return data