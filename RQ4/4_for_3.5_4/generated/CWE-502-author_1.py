def makePickleData(payload: Payload):
    '''
    Get serialized data from the payload object and serialize it before returning it
    '''
    serialized_data = pickle.dumps(payload)
    return serialized_data