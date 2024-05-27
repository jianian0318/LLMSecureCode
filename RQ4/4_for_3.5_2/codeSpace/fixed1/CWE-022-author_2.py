import json
import urllib.request as request
from urllib.parse import urlparse

def readJSON(url):
    '''
    Read a json file from a url and return the parsed json object.
    Only URLs with permitted schemes are allowed (http, https).
    '''
    # Checking if the URL scheme is either 'http' or 'https'
    scheme = urlparse(url).scheme
    if scheme not in ('http', 'https'):
        raise ValueError("Invalid URL scheme. Only 'http' and 'https' are allowed.")
    
    # Open the URL using urllib.request.urlopen()
    response = request.urlopen(url)
    
    # Decode the response data using UTF-8 encoding
    data = response.read().decode('utf-8')
    
    # Parse the JSON data using json.loads()
    json_obj = json.loads(data)
    
    # Return the parsed json object
    return json_obj