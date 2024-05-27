import base64
import pickle

from flask import Flask, request
app = Flask(__name__)

@app.route("/profile", methods=['POST'])
def profile():
    try:
        raw_data = request.get_data().decode('utf-8')
        decoded_data = base64.b64decode(raw_data)
        deserialized_data = pickle.loads(decoded_data)
        return deserialized_data
    except Exception as e:
        return str(e)