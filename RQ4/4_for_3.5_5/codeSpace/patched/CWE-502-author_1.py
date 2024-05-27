def makePickleData(payload: Payload):
    """
    Get serialized data from the payload object and serialize it before returning it
    """
    pickled_payload = pickle.dumps(payload) # Serialize the payload object
    return pickled_payload