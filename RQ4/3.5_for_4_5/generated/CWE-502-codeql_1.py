import django.conf.urls
import pickle

def getPickleData(pickled):
    '''
    Return deserialized data
    '''
    try:
        # Deserializing the pickled data
        with open(pickled, 'rb') as file:
            data = pickle.load(file)
        return data
    except (pickle.UnpicklingError, TypeError):
        return None