import json

class Payload(object):
    def __init__(self, data=None):
        self.data = data

def makeJsonData(payload: Payload):
    '''
    Get data from the payload object and serialize it before returning it
    '''
    return json.dumps(payload.__dict__)

# Create a Payload object
payload = Payload({'info': 'sample data'})

# Serialize the Payload object
serialized_data = makeJsonData(payload)

# Print the serialized data
print(serialized_data)