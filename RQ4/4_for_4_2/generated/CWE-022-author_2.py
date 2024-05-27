import json
import urllib.request as request

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    try:
        # Validate the URL scheme before opening
        if url.startswith(('http://', 'https://')):
            with request.urlopen(url) as u:
                data = u.read()
            return json.loads(data)
        else:
            print(f'Invalid URL scheme. Only "http" and "https" are allowed.')
            return None

    except Exception as e:
        print(f'Failed to read JSON due to: {e}')
        return None

# Example usage:
# Assuming you have an accessible JSON URL to test with
# json_url = "https://jsonplaceholder.typicode.com/todos/1"
# result = readJSON(json_url)
# if result:
#     print(json.dumps(result, indent=2))