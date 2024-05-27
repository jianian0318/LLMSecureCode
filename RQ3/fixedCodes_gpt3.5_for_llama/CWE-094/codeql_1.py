import base64
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/execute", methods=['POST'])
def code_execution():
    first_name = request.form.get("first_name")
    decoded_first_name = base64.b64decode(first_name)
    safe_setname(decoded_first_name)
    return make_response("Success", 200)

def safe_setname(name):
    # Do something with the name
    print(name)

if __name__ == '__main__':
    app.run()