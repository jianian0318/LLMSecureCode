from django.conf.urls import url
import pickle

def getPickleData(pickled):
    '''
    Return deserialized data
    '''
    try:
        # Load data (deserialize)
        with open(pickled, 'rb') as handle:
            deserialized_data = pickle.load(handle)

        return deserialized_data
    except pickle.UnpicklingError as e:
        print("Error: UnpicklingError -", str(e))
        return None
    except Exception as e:
        print("Error: ", str(e))
        return None