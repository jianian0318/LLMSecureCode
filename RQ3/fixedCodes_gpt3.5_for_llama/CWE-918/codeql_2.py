import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def retrieve_info():
    user_id = request.args.get('user_id')
    response = None
    if user_id:
        url = f'https://api.github.com/users/{user_id}'
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            return str(e)
    else:
        return "Invalid user_id"
    
    if response.status_code == 200:
        return response.json()
    else:
        return "User not found"

if __name__ == '__main__':
    app.run()