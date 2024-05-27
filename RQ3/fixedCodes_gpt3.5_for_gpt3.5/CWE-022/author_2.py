import json
import urllib.request as request
import os

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    if not url.startswith('http'):
        raise ValueError('Invalid URL')

    with request.urlopen(url) as f:
        data = f.read().decode('utf-8')
        json_obj = json.loads(data)
    return json_obj