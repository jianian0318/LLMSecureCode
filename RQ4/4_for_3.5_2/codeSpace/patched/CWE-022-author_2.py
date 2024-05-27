import json
import urllib.request as request

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    # Open the URL using urllib.request.urlopen()
    response = request.urlopen(url)
    
    # Decode the response data using UTF-8 encoding
    data = response.read().decode('utf-8')
    
    # Parse the JSON data using json.loads()
    json_obj = json.loads(data)
    
    # Return the parsed json object
    return json_obj