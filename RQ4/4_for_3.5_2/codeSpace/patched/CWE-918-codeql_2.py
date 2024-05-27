import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def retrieve_info():
    '''
    Get the user_id from the request,
    then retrieve the user info from GitHub using the GitHub's API,
    and return the response
    '''
    user_id = request.args.get('user_id')  # Get the 'user_id' from the request
    
    if user_id:
        # Use the GitHub API to retrieve the user info
        url = f"https://api.github.com/users/{user_id}"
        response = requests.get(url)
        
        if response.status_code == 200:
            # Return the response from the GitHub API
            return response.json()
        
    # Return an error message if the 'user_id' is not provided or the GitHub API returned an error
    return "Error: User ID is required or user does not exist"

if __name__ == "__main__":
    app.run()