import json
import urllib.request as request
from urllib.parse import urlparse

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    # Parse the given URL
    parsed_url = urlparse(url)

    # Check if scheme is http or https
    if parsed_url.scheme not in ['http', 'https']:
        raise ValueError(f'Unsafe URL {url}, only HTTP and HTTPS schemes are permitted.')
        
    # Open the url and read the JSON data
    response = request.urlopen(url)
    data = response.read().decode("utf-8")

    # Parse the JSON data
    parsed_json = json.loads(data)

    # Return the parsed JSON object
    return parsed_json