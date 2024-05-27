import json
import urllib.request as request

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''

    # Check if the url scheme is http or https
    if url.startswith('http://') or url.startswith('https://'):
        # Send request to the URL
        with request.urlopen(url) as u:
            # Read the response
            data = u.read().decode('utf-8')
            u.close()
    else:
        return None
    
    # Parse the JSON object
    parsed_json = json.loads(data)

    return parsed_json