import base64
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/execute")
def code_execution():
    first_name = request.args.get("first_name")
    try:
        decoded_name = base64.b64decode(first_name).decode("utf-8")
        setname(decoded_name)
    except:
        # handle the error caused by incorrect input
        return "Invalid input"
  
def setname(first_name):
    # code to set the name
    pass

if __name__ == "__main__":
    app.run()