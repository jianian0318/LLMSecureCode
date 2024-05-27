import json
from urllib.parse import urlparse
from urllib.request import urlopen

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    valid_schemes = ['http', 'https']  # List of valid schemes
    parsed_url = urlparse(url)  # Parse the url

    if parsed_url.scheme not in valid_schemes:  # Check if the url scheme is allowed
        raise ValueError('Invalid url scheme')  # Raise an error if the scheme is not allowed

    if parsed_url.scheme == 'file':  # Check if the url scheme is 'file'
        raise ValueError('Invalid url scheme')  # Raise an error if the scheme is 'file'

    response = urlopen(url)  # Open the url
    data = response.read().decode('utf-8')  # Read the response data
    json_data = json.loads(data)  # Parse the json data
    return json_data  # Return the parsed json object