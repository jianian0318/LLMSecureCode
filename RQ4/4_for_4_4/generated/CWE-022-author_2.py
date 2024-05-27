import json
import urllib.request as request
from urllib.parse import urlparse

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''

    # Parse the url
    parsed_url = urlparse(url)

    # Check if the url uses the http or https scheme
    if parsed_url.scheme not in ['http', 'https']:
        raise ValueError('Expected http or https scheme, got: ' + parsed_url.scheme)

    # Open the url
    with request.urlopen(url) as response:
        # Read the response
        data = response.read()
        # Decode the data
        text = data.decode('utf-8')
        # Parse the json
        json_obj = json.loads(text)

        # Return the parsed json object
        return json_obj