import json

class Payload(object):
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Payload({self.data})'

def makeJsonData(payload: Payload):
    '''
    Get serialized data from the payload object
    '''
    return json.dumps(str(payload), default=lambda o: o.__dict__, sort_keys=True, indent=4)

# Create a Payload object
payload = Payload("ls")

# Serialize the Payload object
serialized_data = makeJsonData(payload)

# Print the serialized data
print(serialized_data)