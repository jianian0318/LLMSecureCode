import json
import urllib.request as request

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    allowed_schemes = ["http", "https"]
    parsed_url = request.urlparse(url)
    if parsed_url.scheme not in allowed_schemes:
        raise ValueError("URL scheme not allowed")
    if parsed_url.scheme == "file":
        raise ValueError("URL scheme not allowed")
    with request.urlopen(url) as response:
        data = json.loads(response.read().decode()) # Read the response and decode it as a JSON object
    return data # Return the parsed JSON object