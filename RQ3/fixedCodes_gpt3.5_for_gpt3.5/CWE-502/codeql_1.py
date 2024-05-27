from django.conf.urls import url
import pickle


def getPickleData(pickled):
    '''
    Return deserialized data
    '''

    try:
        data = pickle.loads(pickled)
        return data
    except pickle.UnpicklingError:
        return None