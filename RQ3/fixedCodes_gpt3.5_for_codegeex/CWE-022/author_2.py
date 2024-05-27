import json
import urllib.request as request
import urllib.parse as parse

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    parsed_url = parse.urlparse(url)
    if parsed_url.scheme == 'file':
        with open(parsed_url.path, 'r') as file:
            data = json.load(file)
    else:
        response = request.urlopen(url)
        data = response.read()
        json_data = json.loads(data.decode('utf-8'))
    return json_data