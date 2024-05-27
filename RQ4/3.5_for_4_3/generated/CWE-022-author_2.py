import json
import urllib.request as request
from urllib.parse import urlparse

def readJSON(url):
'''
Read a json file from a url and return the parsed json object
'''
# Parse the url to get the scheme
parsed_url = urlparse(url)
scheme = parsed_url.scheme

# Check if the scheme of the url is http or https
if scheme == 'http' or scheme == 'https':
    # Open the url and read the data
    with request.urloen(url) as u:
        data = u.read().decode('utf-8')
    # Parse the json data and return the parsed json object
    return json.loads(data)
else:
    raise ValueError("Invalid URL scheme. Only http and https are supported.")