import pickle

def getPickleData(pickled):
    '''
    Return deserialized data
    '''
    try:
        return pickle.loads(pickled)
    except pickle.UnpicklingError as e:
        print("Error loading pickled data:", e)
        return None
    except AttributeError as e:
        print("Error loading pickled data:", e)
        return None