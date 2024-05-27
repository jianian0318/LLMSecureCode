import secrets

from flask import Flask, request, session
from flask import render_template, make_response

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

def check_credentials(username, password):
    return True  # This function should actually check the credentials in a real application

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form.get('username')
    password = request.form.get('password')

    if check_credentials(username, password):
        session_id = secrets.token_hex(16)
        session['session_id'] = session_id

        resp = make_response("Logged in successfully!")
        resp.set_cookie('session_id', session_id)
        return resp

    return "Invalid credentials", 401

if __name__ == "__main__":
    app.run(debug=True)