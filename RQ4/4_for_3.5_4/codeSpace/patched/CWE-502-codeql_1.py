from django.conf.urls import url
import pickle


def getPickleData(pickled):
    '''
    Return deserialized data
    
    Parameters:
    pickled (str): Pickled data
    
    Returns:
    object: Deserialized data
    '''
    return pickle.loads(pickled)