from django.conf.urls import url
import pickle

def getPickleData(pickled):
    '''
    Return deserialized data
    '''
    data = pickle.loads(pickled)
    return data