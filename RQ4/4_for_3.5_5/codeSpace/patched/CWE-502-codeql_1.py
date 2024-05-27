def getPickleData(pickled):
    '''
    Return deserialized data

    Parameters:
        pickled (str): The pickled data as a string

    Returns:
        object: The deserialized data
    '''
    deserialized_data = pickle.loads(pickled)
    return deserialized_data