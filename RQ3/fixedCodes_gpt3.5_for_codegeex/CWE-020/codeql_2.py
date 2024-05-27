import base64
import pickle

from flask import Flask, request
app = Flask(__name__)

@app.route("/profile", methods=['POST'])
def profile():
    raw_data = request.get_data() 
    if not raw_data:
        return "Data not found."
    decoded_data = base64.b64decode(raw_data)
    try:
        deserialized_data = pickle.loads(decoded_data)
        return deserialized_data
    except pickle.UnpicklingError:
        return "Invalid data format."