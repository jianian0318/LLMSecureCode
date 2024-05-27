from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/profile")
def profile():
    username = request.args.get('username')
    
    if username is None:
        response = make_response('Invalid username', 400)
    else:
        response = make_response(username)
    
    return response