import base64
import pickle
from flask import Flask, request
import html

app = Flask(__name__)

@app.route("/profile")
def profile():
    # Get raw_data from request with utf-8 encoding
    raw_data = request.args.get('data').encode('utf-8')
    
    # Decode it with base64
    decoded_data = base64.b64decode(raw_data)

    try:
        # Deserialize the decoded data
        deserialized_data = pickle.loads(decoded_data)

        # Ensure the deserialized data is a dictionary
        if not isinstance(deserialized_data, dict):
            return "Invalid data provided"

        # Store it in a variable and return it (converted to string for HTTP response)
        profile_data = html.escape(str(deserialized_data))
        return profile_data

    except (pickle.UnpicklingError, TypeError) as e:
        return "Invalid data provided"

if __name__ == '__main__':
    app.run(debug=False)