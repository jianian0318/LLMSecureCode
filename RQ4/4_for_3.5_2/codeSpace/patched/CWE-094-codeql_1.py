import base64
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/execute", methods=["POST"])
def code_execution():
    # Get "first_name" from the post request object, and decode the string using base64.
    first_name = base64.b64decode(request.form.get("first_name")).decode()

    # Call the setname function with the decoded first_name as argument.
    setname(first_name)

    # Return a response indicating that the code execution was successful.
    return make_response("Code executed successfully")

def setname(name):
    # Dummy function to set the name. Replace with your actual implementation.
    print("Setting name:", name)

if __name__ == "__main__":
    app.run()