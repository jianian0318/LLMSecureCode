    import json
    import urllib.request as request

    def readJSON(url):
        with request.urlopen(url) as response:
            data = response.read().decode("utf-8")
            parsed_json = json.loads(data)
        return parsed_json
    