import requests

@app.route("/user", methods=['GET'])
def retrieve_info():
    # Get the user_id from the request query params
    user_id = request.args.get('user_id')

    # Make a GET request to GitHub's API with a specified timeout of 5 seconds
    response = requests.get(f"https://api.github.com/users/{user_id}", timeout=5)

    # Return the response from GitHub's API
    return response.json()