import json
import urllib.request as request
def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    response = request.urlopen(url)
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))
    return json_data
