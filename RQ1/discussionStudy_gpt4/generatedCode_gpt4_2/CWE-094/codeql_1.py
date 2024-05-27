import base64
from flask import Flask, request, jsonify

app = Flask(__name__)

def setname(name):
    # Assuming the setname function exists in your module.
    pass

@app.route("/execute", methods = ['POST'])
def code_execution():
    first_name_encoded = request.form['first_name']
    first_name = base64.b64decode(first_name_encoded).decode('utf-8')
    setname(first_name)
    return jsonify({"message": "operation successful"}), 200

if __name__ == '__main__':
    app.run()