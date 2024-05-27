from django.conf.urls import url
import io
import pickle
import _pickle

SAFE_CLASSES = {'sample_safe_data_class'} 

class RestrictedUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        # Only allow safe classes from SAFE_CLASSES
        if module in SAFE_CLASSES and name in SAFE_CLASSES:
            return getattr(_pickle, name)
        # Forbid everything else
        raise pickle.UnpicklingError('global %s.%s is forbidden' %
                                     (module, name))

def getPickleData(pickled):
    '''
    Return deserialized data
    '''
    try:
        data = RestrictedUnpickler(io.BytesIO(pickled)).load()
    except (pickle.UnpicklingError, EOFError, AttributeError, ImportError, 
            IndexError, TypeError):
        raise ValueError("Untrusted deserialization attempt caught")
    return data    


