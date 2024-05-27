import json
import urllib.request as request
import urllib.parse as urlparse

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    # Parse the URL to ensure it uses http/https schemes
    parsed_url = urlparse.urlparse(url)
    if parsed_url.scheme not in ('http', 'https'):
        raise ValueError(f'Invalid URL "{url}": Only http and https schemes are allowed.')

    # Retrieve data from URL
    try:
        with request.urlopen(url) as response:
            source = response.read()
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

    # Load JSON data from source
    try:
        data = json.loads(source)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

    # Return the parsed JSON object
    return data