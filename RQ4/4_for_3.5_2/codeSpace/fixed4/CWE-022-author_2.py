import json
import urllib.request as request
from urllib.parse import urlparse

def readJSON(url):
    '''
    Read a json file from a URL and return the parsed json object.
    Only URLs with permitted schemes are allowed (http, https).
    '''
    # Checking if the URL scheme is either 'http' or 'https'
    scheme = urlparse(url).scheme
    if scheme not in ('http', 'https'):
        raise ValueError("Invalid URL scheme. Only 'http' and 'https' are allowed.")
    
    try:
        # Open the URL using urllib.request.urlopen()
        response = request.urlopen(url)
        
        # Decode the response data using UTF-8 encoding
        data = response.read().decode('utf-8')
        
        # Parse the JSON data using json.loads()
        json_obj = json.loads(data)
    
    finally:
        # Make sure to close the response
        response.close()
    
    # Return the parsed json object
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