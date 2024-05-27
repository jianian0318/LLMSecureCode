import django.conf.urls
import pickle

def getPickleData(pickled):
    '''
    Return deserialized data
    '''
    try:
        # validating the pickled data
        if isinstance(pickled, bytes):
            # loading the pickle module
            pickle_module = __import__('pickle')
            
            # unpickling the pickled data
            data = pickle_module.loads(pickled)
            return data
        else:
            return None
    except (pickle_module.UnpicklingError, AttributeError, EOFError, ImportError, IndexError, TypeError):
        return None