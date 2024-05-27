import requests
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/user")
def retrieve_info():
    user_id = request.args.get('user_id')

    if not user_id.isalnum():
        return "Invalid user ID.", 400

    url = f"https://api.github.com/users/{escape(user_id)}"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        #Return a generic error message
        return "An error occurred while processing the request.", 500

    safe_response = {key: escape(str(value)) for key, value in response.json().items()}
    return safe_response

if __name__ == "__main__":
    app.run()