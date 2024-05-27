import os
import pickle


class Payload(object):
    def __reduce__(self):
        return os.system, ('ls',)


def makePickleData(payload: Payload):
    '''
    Get serialized data from the payload object and serialize it before returning it
    '''
    pickle_data = pickle.dumps(payload, protocol=0)
    return pickle_data


# Test the function
payload = Payload()
serialized_data = makePickleData(payload)

try:
    deserialized_data = pickle.loads(serialized_data)
    print(deserialized_data)
except pickle.UnpicklingError:
    print('Error: Unable to unpickle the data')