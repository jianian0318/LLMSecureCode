import json

class Payload(object):
    def __init__(self, data):
        self.data = data

def make_json_data(payload: Payload):
    '''
    Get serialized data from the payload object and serialize it before returning it using JSON
    '''
    # Assuming that Payload has a simple structure that can be serialized by json
    # If not, you may need to customize this part to properly serialize complex objects
    return json.dumps(payload.__dict__)

def load_json_data(serialized_data: str):
    '''
    Deserialize the JSON back into a Payload object without executing arbitrary code.
    '''
    data = json.loads(serialized_data)
    # Reconstruct the Payload object or use the data as needed
    
    # If more complex reconstruction is required, do it here safely without executing the data
    return Payload(data)

# Example usage
payload = Payload({'key': 'value'})
serialized_data = make_json_data(payload)
print(serialized_data)  # This will output the JSON string
loaded_payload = load_json_data(serialized_data)
print(loaded_payload.data)  # This will output the original data dictionary