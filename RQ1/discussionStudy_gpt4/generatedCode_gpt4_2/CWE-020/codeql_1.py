from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/profile", methods=['GET'])
def profile():
    username = request.args.get('username', default = "", type = str)

    # Make a response with the username and return it
    resp = make_response("Username: " + username)
    return resp

if __name__ == "__main__":
    app.run(debug=True)