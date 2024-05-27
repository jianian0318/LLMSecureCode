import json
import urllib.request as request
from urllib.parse import urlparse

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ('http', 'https'):
        raise ValueError(f'Unexpected URL scheme: {parsed_url.scheme}')

    with request.urlopen(url) as u:
        data = u.read()
        
    return json.loads(data)