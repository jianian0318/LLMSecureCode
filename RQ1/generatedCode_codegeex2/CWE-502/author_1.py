import pickle

class Payload(object):
    def __reduce__(self):
        return (os.system, ("echo 'Hello, World!", 1),)

def makePickleData(payload: Payload):
    '''
    Get serialized data from the payload object and serialize it before returning it
    '''
    serialized_data = pickle.dumps(payload)
    return serialized_data
