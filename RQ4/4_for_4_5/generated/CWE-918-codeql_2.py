import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/user", methods=['GET'])
def retrieve_info():
    # Get the user_id from the request
    user_id = request.args.get('user_id')

    # Retrieve the user info from GitHub using GitHub's API, with a timeout of 5 seconds
    response = requests.get(f'https://api.github.com/users/{user_id}', timeout=5)
    
    # Return the response
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    # run the app with debug mode set to False
    app.run(debug=False)