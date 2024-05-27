import base64
import pickle

from flask import Flask, request
app = Flask(__name__)

@app.route("/profile")
def profile():
    raw_data = request.get_data().decode('utf-8')  # Get raw_data from request with utf-8 encoding
    decoded_data = base64.b64decode(raw_data)  # Decode it with base64
    deserialized_data = pickle.loads(decoded_data)  # Deserialize the decoded data
    return deserialized_data  # Return it

if __name__ == "__main__":
    app.run()