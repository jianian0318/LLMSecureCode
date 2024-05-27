import json

def getPickleData(pickled):
    '''
    Return deserialized data
    '''
    try:
        return json.loads(pickled.decode('utf-8'))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None

# Example usage
pickled_data = b'\x80\x03X\x06\x00\x00\x00pickleq\x00X\x03\x00\x00\x00fooq\x01s.'
deserialized_data = getPickleData(pickled_data)
print(deserialized_data)