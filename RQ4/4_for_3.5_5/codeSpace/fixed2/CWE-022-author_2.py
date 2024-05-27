import json
import urllib.request as request
import urllib.parse as parse

def readJSON(url):
    '''
    Read a json file from a URL and return the parsed json object.
    Secured to only allow HTTP or HTTPS URLs to mitigate CWE-22 concerns.
    '''
    # Parse the URL and validate the scheme
    parsed_url = parse.urlparse(url)
    if parsed_url.scheme not in ['http', 'https']:
        raise ValueError("Only HTTP and HTTPS URLs are allowed")
    
    # Open the URL and read its contents
    with request.urlopen(url) as response:
        # Decode the contents and parse it as json
        data = json.loads(response.read().decode())
    
    # Return the parsed json object
    return data