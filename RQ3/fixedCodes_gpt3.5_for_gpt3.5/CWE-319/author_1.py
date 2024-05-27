import secrets
import hashlib

from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

def check_credentials(username, password):
    '''
    Verify the provided credentials by comparing the username and password with
    the values stored in a secure database, such as a hashed and salted password.
    '''
    # Example secure database lookup and comparison logic
    stored_username = 'example_username'
    stored_password_hash = 'de3f2b7cebfd19a53f235e3fef150870'  # Example hashed and salted password

    # Hash the provided password using the same salt and hashing algorithm used to
    # create stored_password_hash, and compare the resulting hash with stored_password_hash
    salt = 'example_salt'
    password_hash = hashlib.md5((password + salt).encode()).hexdigest()

    if username == stored_username and password_hash == stored_password_hash:
        return True
    else:
        return False

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
        
        # Store the session ID securely on the server side, such as in a secure database or cache
        # ...

        response = make_response('Logged in successfully')
        response.set_cookie('session_id', session_id, secure=True, httponly=True)
        return response
    else:
        return 'Invalid credentials. Please try again.'