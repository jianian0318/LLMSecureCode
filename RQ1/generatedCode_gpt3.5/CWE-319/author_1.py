import secrets

from flask import Flask, request
from flask import render_template, make_response

app = Flask(__name__)


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
    username = request.form.get('username')
    password = request.form.get('password')

    if check_credentials(username, password):
        session_id = secrets.token_hex(16)
        response = make_response('Logged in successfully')
        response.set_cookie('session_id', session_id)
        return response
    else:
        return 'Invalid credentials. Please try again.'