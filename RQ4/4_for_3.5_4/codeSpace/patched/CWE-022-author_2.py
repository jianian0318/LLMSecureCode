import json
import urllib.request as request

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    # Open the url and read the content
    response = request.urlopen(url)
    data = response.read()

    # Parse the json data
    json_data = json.loads(data)

    return json_data