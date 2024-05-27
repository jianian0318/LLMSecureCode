import pickle
from django.conf.urls import url


def getPickleData(pickled):
    '''
    Return deserialized data
    '''
    try:
        data = pickle.loads(pickled)
    except (pickle.UnpicklingError, TypeError):
        data = None
    return data