import base64
import pickle

from flask import Flask, request
app = Flask(__name__)

@app.route("/profile", methods=['POST'])
def profile():
    raw_data = request.form['data']
    decoded_data = base64.b64decode(raw_data.encode())
    deserialized_data = pickle.loads(decoded_data)
    
    if isinstance(deserialized_data, str):
        return deserialized_data
    else:
        return "Invalid data format"

if __name__ == "__main__":
    app.run()