def getPickleData(pickled):
    '''
    Return deserialized data

    Parameters:
    pickled (str): A pickled string

    Returns:
    object: The deserialized data
    '''
    # Deserialize the pickled data
    data = pickle.loads(pickled)

    return data