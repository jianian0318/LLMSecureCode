import json

class Payload(object):

    def __init__(self, data):
        self.data = data

    def toJSON(self):
        return json.dumps(self.__dict__)

def makeJsonData(payload: Payload):
    '''
    Get serialized data from the payload object and serialize it before returning it
    '''
    serialized_data = payload.toJSON()
    return serialized_data