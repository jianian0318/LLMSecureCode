from flask import Flask,render_template_string, Response
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": "password1",
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return users.get(username) == password
    return False

@app.route('/settings') 
@auth.login_required
def settings(): 
    return Response('These are your confidential settings!', 200)

if __name__ == '__main__':
    app.run()



