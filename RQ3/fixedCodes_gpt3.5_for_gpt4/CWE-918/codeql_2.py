import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/user", methods=['GET'])
def retrieve_info():
    user_id = request.args.get('user_id')
    if user_id is not None:
        response = requests.get(f'https://api.github.com/users/{user_id}')
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "User not found"}, 404
    else:
        return {"error": "No user_id provided"}, 400


if __name__ == "__main__":
    app.run(debug=True)