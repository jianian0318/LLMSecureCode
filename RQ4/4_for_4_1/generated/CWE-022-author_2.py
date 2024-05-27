import json
import urllib.request as request
from urllib.parse import urlparse

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''

    url_parts = urlparse(url)
    
    # Only permit specific schemes
    if url_parts.scheme not in ('http', 'https'):
        raise Exception(f'Invalid URL schema: {url_parts.scheme}')
    
    with request.urlopen(url) as response:
        data = response.read()
        json_data = json.loads(data)
        return json_data

# Example usage:
# Replace 'your_json_url' with the exact URL pointing to a JSON file
your_json_url = 'https://example.com/data.json'
try:
    print(readJSON(your_json_url))
except Exception as e:
    print(e)