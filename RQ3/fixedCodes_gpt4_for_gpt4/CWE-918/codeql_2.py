import requests
from flask import Flask, request
from urllib.parse import urlparse

app = Flask(__name__)

ALLOWED_HOSTS = ["api.github.com"]

def is_valid_url(url):
    parts = urlparse(url)
    if parts.netloc not in ALLOWED_HOSTS:
        return False
    return True

@app.route("/user", methods=['GET'])
def retrieve_info():
    '''
    Get the user_id from the request,
    the retrieve the user info from GitHub using the GitHub's API,
    and return the response
    '''
    user_id = request.args.get('user_id')
    url = f'https://api.github.com/users/{user_id}'
    if user_id is not None and is_valid_url(url):
        response = requests.get(url)
        return response.json()
    else:
        return {"error": "Bad request, please check your data and make sure you are calling the right API."}, 400

if __name__ == "__main__":
    app.run(debug=True)

# Here, an is_valid_url function is added, which uses the urlparse method from the urllib.parse package to parse the URL and validate if the netloc part (the network location, which usually contains the hostname and port information) is within the allowed hosts. Here, the allowed host is only "api.github.com". Before making a request, this function is called to make sure that the URL is valid. If it's not, the function returns a 400 status code along with a suitable error message. This will help prevent any SSRF (Server Side Request Forgery) attacks by ensuring that only allowed URLs are used to fetch data.