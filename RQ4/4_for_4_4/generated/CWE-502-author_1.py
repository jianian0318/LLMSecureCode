import json

class Payload(object):
    command = 'import os;os.system("ls")'

def make_json_data(payload: Payload):
    '''
    Get serialized data from the payload object and serialize it before returning it
    '''
    # Serialize the payload using json
    serialized_data = json.dumps(payload.__dict__)

    return serialized_data