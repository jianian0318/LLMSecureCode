def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    try:
        with request.urlopen(url) as response:
            data = response.read()
            json_obj = json.loads(data)
            return json_obj
    except Exception as e:
        print(e)
        return None