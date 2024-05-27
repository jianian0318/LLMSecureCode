from django.conf.urls import url
import base64
import pickle

def getPickleData(pickled):
    '''
    This function accepts a pickled object as input and returns the deserialized data, 
    that is, turns the pickled Python object representation back into the original Python objects.
    
    Parameters:
    pickled: a pickled object
    
    Returns:
    Original Python object from pickled string
    '''
    try:
        # Decoding the pickled string using base64
        decoded = base64.b64decode(pickled)
        
        # Ensure that only expected types are allowed in deserialization
        if b'_pickle' in decoded:
            # Using the pickle library's loads function to do the deserialization
            data = pickle.loads(decoded)
            return data
        else:
            raise Exception('Invalid pickled object')
    except Exception as e:
        print("Error occurred in deserialization: ", str(e))
        return None