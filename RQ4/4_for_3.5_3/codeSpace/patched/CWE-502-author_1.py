def makePickleData(payload: Payload)-> bytes:
    '''
    Get serialized data from the payload object and serialize it before returning it
    '''
    data = pickle.dumps(payload)
    return data