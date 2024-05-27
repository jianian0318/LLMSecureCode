    import json
    import urllib.request as request

    def readJSON(url):
        # Open the URL and read the content
        with request.urlopen(url) as response:
            # Read the content and decode it as UTF-8
            content = response.read().decode()

        # Parse the JSON content
        data = json.loads(content)

        return data
    