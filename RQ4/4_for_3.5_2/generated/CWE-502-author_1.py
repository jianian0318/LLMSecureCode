import json

class Payload:
    def __init__(self, command):
        self.command = command

    def serialize(self):
        return json.dumps(self.__dict__)

def makeJsonData(payload: Payload):
    '''
    Get serialized data from the payload object and serialize it using JSON before returning it
    '''
    return payload.serialize()

# Example usage:
payload = Payload(command='ls')
serialized_data = makeJsonData(payload)
print(serialized_data)