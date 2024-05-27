import json
import urllib.request as request
from urllib.parse import urlparse

def readJSON(url):
    '''
    Read a json file from a URL and return the parsed json object.
    Only URLs with permitted schemes are allowed (http, https).
    '''
    # Verifying the URL uses a safe scheme
    scheme = urlparse(url).scheme
    if scheme not in ('http', 'https'):
        raise ValueError("Invalid URL scheme. Only 'http' and 'https' are allowed.")
    
    try:
        # Open the URL and read the response safely
        with request.urlopen(url) as response:
            # Decode and parse the JSON data
            data = response.read().decode('utf-8')
            json_obj = json.loads(data)
    
    except Exception as e:
        # Handle exceptions by re-raising them
        raise RuntimeError(f"Failed to read JSON from {url}") from e
    
    return json_obj

# Example usage:
if __name__ == "__main__":
    url = "https://api.example.com/data.json"
    try:
        json_data = readJSON(url)
        print(json_data)
    except ValueError as e:
        print(e)
    except Exception as other_exception:
        print("An error occurred:", other_exception)