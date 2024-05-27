import secrets

from flask import Flask, request, session
from flask import render_template, make_response

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


def check_credentials(username, password):
    return True


@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    if check_credentials(username, password):
        session['session_id'] = secrets.token_urlsafe(16)
        return render_template('success.html')
    else:
        return render_template('login.html', error='Invalid credentials')