import json

class Payload(object):
    def __init__(self, data):
        self.data = data

def makeJsonData(payload: Payload):
    '''
    Get serialized data from the payload object and serialize it before returning it
    '''
    return json.dumps(payload.__dict__)


