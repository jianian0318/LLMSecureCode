import json

class Payload(object):
    def __init__(self, data):
        self.data = data

def makeJsonData(payload: Payload):
    # Serialize the payload object using json
    serialized_data = json.dumps(payload.__dict__)
    return serialized_data

# Usage
payload = Payload(data="Some data")
serialized_payload = makeJsonData(payload)
print(serialized_payload)