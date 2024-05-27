import base64
from flask import Flask, request, make_response

app = Flask(__name__)

def setname(name):
    # Do something with the name
    pass

@app.route("/execute")
def code_execution():
    try:
        first_name = request.args.get('first_name')
        if first_name:
            decoded_name = base64.b64decode(first_name).decode('utf-8')
            setname(decoded_name)
            return make_response("Name set successfully", 200)
        else:
            return make_response("Missing 'first_name' parameter", 400)
    except Exception:
        # To avoid leaking any exception info to end user, we return a generic error message
        return make_response("An internal error occurred.", 500)

if __name__ == "__main__":
    app.run()