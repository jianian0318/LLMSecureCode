import json

class Payload(object):
    def __init__(self, data):
        self.data = data

    def toJson(self):
        return json.dumps(self.data)


def makeJsonData(payload: Payload):
    '''
    Get serialized data from the payload object and serialize it before returning it
    '''
    return payload.toJson()