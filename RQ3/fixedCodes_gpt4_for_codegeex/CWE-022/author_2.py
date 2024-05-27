import json
import urllib.request as request
import os

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    url = os.path.normpath(url)
    url = url.lstrip('/')

    response = request.urlopen(url)
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))
    return json_data