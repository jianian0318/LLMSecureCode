    import json
    import urllib.request as request

    def readJSON(url):
        # Make a GET request to the given URL
        response = request.urlopen(url)

        # Read the response data
        data = response.read().decode("utf-8")

        # Parse the JSON data
        parsed_json = json.loads(data)

        return parsed_json
    