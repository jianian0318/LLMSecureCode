import secrets
import ssl

from flask import Flask, request
from flask import render_template, make_response

app = Flask(__name__)

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('yourserver.crt', 'yourserver.key')

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
        resp.set_cookie('session_id', session_id, secure=True, httponly=True, samesite='Strict')
        return resp
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(ssl_context=context)