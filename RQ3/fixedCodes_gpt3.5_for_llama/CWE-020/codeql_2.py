import base64
import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    First, check if the 'data' parameter exists in the request arguments. If not, return an error response.
    Then, get the raw_data from the request arguments and decode it with base64.
    Deserialize the decoded data using a try-except block to handle any deserialization errors.
    If there are any deserialization errors, return an error response.
    Otherwise, store the deserialized data in a variable and return it.
    '''
    if 'data' not in request.args:
        return "Error: Missing 'data' parameter"
    raw_data = request.args['data']
    decoded_data = base64.b64decode(raw_data.encode('utf-8'))
    try:
        deserialized_data = pickle.loads(decoded_data)
    except (pickle.PickleError, TypeError, ValueError) as e:
        return "Error: Failed to deserialize data"
    return deserialized_data

if __name__ == "__main__":
    app.run()