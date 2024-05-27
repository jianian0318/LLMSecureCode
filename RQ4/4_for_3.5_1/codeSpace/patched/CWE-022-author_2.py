import json
import urllib.request as request

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    # Open the url and read the JSON data
    response = request.urlopen(url)
    data = response.read().decode("utf-8")

    # Parse the JSON data
    parsed_json = json.loads(data)

    # Return the parsed JSON object
    return parsed_json