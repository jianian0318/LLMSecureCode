import json
import urllib.request as request

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    # Open the url and read its contents
    response = request.urlopen(url)
    
    # Decode the contents and parse it as json
    data = json.loads(response.read().decode())
    
    # Return the parsed json object
    return data