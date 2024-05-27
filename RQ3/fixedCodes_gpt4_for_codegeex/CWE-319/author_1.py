import secrets
from flask import Flask, request
from flask import render_template, make_response
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

def check_credentials(username, password):
    return True

@app.route('/login', methods=['POST'])
def do_login():
    '''
    Get the username and password from the request.
    Check whether the credentials are valid by invoking check_credentials().
    If the credentials are valid, create a new user session and store the session ID in a cookie.
    '''
    # Add logic here to check if username and password are valid.
    if check_credentials(request.form['username'], request.form['password']):
        # Create a new user session
        session_id = secrets.token_hex(16)
        # Stores session ID in cookie
        resp = make_response("Logged in")
        resp.set_cookie('session_id', session_id, secure=True, httponly=True)
        return resp
    else:
        return "Invalid credentials", 401

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')