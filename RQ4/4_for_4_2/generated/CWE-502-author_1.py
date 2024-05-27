import json

class Payload(object):
    def __init__(self):         # Added init method to define some properties for payload
        self.command = "ls"

    # convert object to a dict
    def payload_to_dict(self):
        return {
            'command': self.command
        }


def makeJsonData(payload: Payload):
    # Serializing the payload object using json
    serialized_data = json.dumps(payload.payload_to_dict())
    return serialized_data

# Example usage:
payload_instance = Payload()
serialized_payload = makeJsonData(payload_instance)
print(serialized_payload)  # This will print the serialized data