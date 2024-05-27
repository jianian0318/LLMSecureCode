from django.conf.urls import url
import pickle

def getPickleData(pickled):
    '''
    Return deserialized data
    '''
    try:
        data = pickle.loads(pickled)
    except pickle.PickleError:
        data = None
    return data