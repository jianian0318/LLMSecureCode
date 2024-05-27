import json
import urllib.request as request
import os

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    filename = url.split("/")[-1]
    with request.urlopen(url) as response:
        data = response.read().decode("utf-8")
    with open(filename, "w") as file:
        file.write(data)
    with open(filename) as file:
        json_data = json.load(file)
    os.remove(filename)
    return json_data