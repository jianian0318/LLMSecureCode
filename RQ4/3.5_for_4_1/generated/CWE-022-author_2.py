import json
from urllib.request import urlopen
from urllib.parse import urlparse

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ['http', 'https']:
        raise ValueError("Invalid URL scheme. Only 'http://' and 'https://' are allowed.")
    elif parsed_url.scheme == 'file':
        raise ValueError("Invalid URL scheme. 'file://' is not allowed.")

    with urlopen(url) as u:
        data = u.read().decode('utf-8')
    return json.loads(data)

# Example usage
url = 'http://example.com/data.json'
result = readJSON(url)
print(result)