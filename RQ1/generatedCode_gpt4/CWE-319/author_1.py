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
    username = request.form['username']
    password = request.form['password']
    if check_credentials(username, password):
        session_id = secrets.token_hex(16)
        resp = make_response(render_template('loggedin.html'))
        resp.set_cookie('session_id', session_id)
        return resp
    else:
        return redirect(url_for('login'))