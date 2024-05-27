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
    # 在此处添加检查用户名和密码是否有效的逻辑
    if check_credentials(request.form['username'], request.form['password']):
        # 创建一个新的用户会话
        session_id = secrets.token_hex(16)
        # 存储会话ID在cookie中
        resp = make_response("Logged in")
        resp.set_cookie('session_id', session_id)
        return resp
    else:
        return "Invalid credentials", 401

if __name__ == '__main__':
    app.run(debug=True)
