import secrets

from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

def check_credentials(username, password):
    return True

@app.route('/login', methods=['POST'])
def do_login():
    if check_credentials(request.form['username'], request.form['password']):
        session_id = secrets.token_hex(16)
        resp = make_response("Logged in")
        resp.set_cookie('session_id', session_id, secure=True, httponly=True)
        return resp
    else:
        return "Invalid credentials", 401

if __name__ == '__main__':
    app.run(debug=True)