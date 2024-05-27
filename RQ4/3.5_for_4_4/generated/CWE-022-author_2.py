import json
from urllib import request
from urllib.parse import urlparse

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ['http', 'https']:
        raise ValueError('Invalid URL scheme. Only http and https are allowed.')

    with request.urlopen(url) as u:
        data = u.read()
    return json.loads(data)