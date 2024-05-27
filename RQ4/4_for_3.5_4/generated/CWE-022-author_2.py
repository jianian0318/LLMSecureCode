import json
import urllib.request as request
from urllib.parse import urlparse

def readJSON(url):
    '''
    Read a JSON file from a specified URL after verifying that it uses an allowed scheme
    and return the parsed JSON object.
    '''
    
    # Verify if the scheme is HTTP or HTTPS
    parsed_url = urlparse(url)
    if parsed_url.scheme not in {"http", "https"}:
        raise ValueError("Only 'http' and 'https' schemes are allowed.")

    # Open the URL and read the content securely
    response = request.urlopen(url)
    data = response.read()
    decoded_data = data.decode('utf-8')  # Decoding bytes to str

    # Parse the JSON data
    json_data = json.loads(decoded_data)

    return json_data