import pickle

def getPickleData(pickled):
    '''
    Return deserialized data
    '''
    try:
        data = pickle.loads(pickled)
        return data
    except (pickle.UnpicklingError, ValueError) as e:
        # handle unpickling error and value error
        print("Error: Failed to deserialize data")
        return None