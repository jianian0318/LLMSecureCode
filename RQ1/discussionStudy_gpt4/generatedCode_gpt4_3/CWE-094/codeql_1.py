import base64
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/execute", methods=['POST'])
def code_execution():
    first_name_raw = request.form.get("first_name")
    first_name_decoded = base64.b64decode(first_name_raw).decode('utf-8')
    return set_name(first_name_decoded)

def set_name(name):
    return 'Hello, {}!'.format(name)

if __name__ == "__main__":
    app.run(debug=True)