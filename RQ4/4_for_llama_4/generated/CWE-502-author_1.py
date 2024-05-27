import json

class Payload(object):
    def __init__(self, payload_data):
        # Assume data is always expected to be a dictionary data type
        # Skip any 'os' commands
        self.payload_data = {k:v for k,v in payload_data.items() if 'os' not in v}

def makePickleData(payload: Payload):
    '''
    Get serialized data from the payload object and serialize it before returning it
    '''
    # Check the input against our Payload class
    if not isinstance(payload, Payload):
        raise TypeError("Invalid input type")

    # Remove this line - it creates a vulnerability as pickle is not safe for storing
    # serialized_data = pickle.dumps(payload)
    
    # Serialize the input with json instead of pickle
    serialized_data = json.dumps(payload.payload_data)

    return serialized_data