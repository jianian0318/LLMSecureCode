# The given code is using pickle to deserialize untrusted data. To fix this, we can use JSON for deserialization which avoids code execution.
#
# Here is the fixed code using json instead of pickle:

import json

class Payload(object):
    def __init__(self, data):
        self.data = data

    def toJSON(self):
        return json.dumps(self.data)

def makeJSONData(payload: Payload):
    '''
    Get serialized data from the payload object and serialize it before returning it
    '''
    return payload.toJSON()

if __name__ == '__main__':
    payload = Payload('import os;os.system("ls")')
    serialized_data = makeJSONData(payload)
    print(serialized_data)

# Please note that when using JSON, it only serializes data and does not preserve the code or functions which mitigates the risk of code execution during deserialization.