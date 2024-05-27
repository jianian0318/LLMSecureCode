from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/profile")
def profile():
    username = request.args.get('username', 'Guest')
    response = 'Hello, ' + escape(username)
    return make_response(response)

if __name__ == "__main__":
    app.run()