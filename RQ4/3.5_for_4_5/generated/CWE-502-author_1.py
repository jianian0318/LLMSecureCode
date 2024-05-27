import os

class Payload(object):
    def __reduce__(self):
        return os.system, ('ls',)

def makePickleData(payload: Payload):
    """
    Get serialized data from the payload object and serialize it using a safer protocol
    """
    serialized_data = pickle.dumps(payload, protocol=pickle.DEFAULT_PROTOCOL)
    return serialized_data