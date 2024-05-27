from flask import Flask, request
import base64
import pickle

app = Flask(__name__)

@app.route("/profile")
def profile():
    # Get the raw_data from the request object with utf-8 encoding
    raw_data = request.get_data(as_text=True)
    
    # Decode the raw_data with base64
    decoded_data = base64.b64decode(raw_data)
    
    # Deserialize the decoded_data using pickle
    deserialized_data = pickle.loads(decoded_data)
    
    # Store the deserialized_data in a variable
    variable = deserialized_data
    
    # Return the variable
    return variable