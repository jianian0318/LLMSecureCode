import os


class Payload(object):
    def __reduce__(self):
        return os.system, ('ls',)


def makePickleData(payload: Payload) -> bytes:
    '''
    Get serialized data from the payload object and serialize it before returning it
    '''
    # serializing the payload object
    serialized_data = pickle.dumps(payload)

    return serialized_data