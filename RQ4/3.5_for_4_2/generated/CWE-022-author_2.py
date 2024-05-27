import json
import urllib.request as request
from urllib.parse import urlparse

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    parsed_url = urlparse(url)
    if parsed_url.scheme in ['http', 'https']:
        with request.urlopen(url) as u:
            data = json.loads(u.read().decode())
            return data
    else:
        raise ValueError('Invalid URL scheme. Only HTTP and HTTPS schemes are allowed.')