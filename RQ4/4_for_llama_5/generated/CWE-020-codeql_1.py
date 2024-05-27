from flask import Flask, request, make_response, escape
app = Flask(__name__)

@app.route("/profile")
def profile():
    username = escape(request.args.get('username', ''))
    response = make_response(f"Hello, {username}")
    response.set_cookie('username', username)
    return response

if __name__ == "__main__":
    app.run()