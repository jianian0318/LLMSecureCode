import json
import urllib.request as request

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    with request.urlopen(url) as response:
        data = response.read().decode("utf-8")
    return json.loads(data)

