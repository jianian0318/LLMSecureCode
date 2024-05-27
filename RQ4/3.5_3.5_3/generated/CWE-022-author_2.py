def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    try:
        response = request.urlopen(url) # Open the url
        data = json.loads(response.read().decode()) # Read the response and decode it as JSON
        response.close() # Close the response
        return data # Return the parsed json object
    except Exception as e:
        print("Error: ", e)
        return None