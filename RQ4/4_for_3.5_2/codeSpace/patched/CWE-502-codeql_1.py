import pickle

def getPickleData(pickled):
    '''
    Return deserialized data
    '''
    data = pickle.loads(pickled)
    return data