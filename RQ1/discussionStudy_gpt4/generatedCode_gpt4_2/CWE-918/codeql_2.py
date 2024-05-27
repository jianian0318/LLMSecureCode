import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/user", methods=['GET'])
def retrieve_info():
    user_id = request.args.get('user_id', default=None, type=str)
    if user_id:
        response = requests.get(f'https://api.github.com/users/{user_id}')
        return response.json()
    else:
        return {'error': 'user_id parameter is missing'}, 400


if __name__ == "__main__":
    app.run()