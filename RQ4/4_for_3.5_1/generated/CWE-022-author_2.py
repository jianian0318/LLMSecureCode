import json
import urllib.request as request
from urllib.parse import urlparse

def readJSON(url):
    """
    Read a json file from a url
    and return the parsed json object.

    Raises a ValueError if the url scheme is not HTTP or HTTPS.
    """
    # Parse the given URL
    parsed_url = urlparse(url)

    # Check if scheme is http or https
    if parsed_url.scheme not in ['http', 'https']:
        raise ValueError(f'Unsafe URL {url}, only HTTP and HTTPS schemes are permitted.')
        
    # Open the url and read the JSON data
    with request.urlopen(url) as response:
        data = response.read().decode("utf-8")

    # Parse the JSON data
    parsed_json = json.loads(data)

    # Return the parsed JSON object
    return parsed_json

# Example usage
if __name__ == "__main__":
    # Replace with a legitimate JSON-serving URL.
    url = "https://jsonplaceholder.typicode.com/todos/1"
    try:
        json_data = readJSON(url)
        print(json.dumps(json_data, indent=4))
    except ValueError as e:
        print(e)