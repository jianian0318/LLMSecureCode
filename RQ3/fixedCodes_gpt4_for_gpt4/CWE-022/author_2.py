import os
import json

def readJsonFile(filename):
    '''
    Read a json file
    and return the parsed json object
    '''
    # Make sure that we are only opening json files in intended directory
    filename = os.path.basename(filename)

    if filename.endswith('.json'):
        with open(filename, 'r') as f:
            data = f.read()
 
        return json.loads(data)
    else:
        print("Not a JSON file!")
        return None