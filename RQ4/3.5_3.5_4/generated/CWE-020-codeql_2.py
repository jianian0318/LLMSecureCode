import base64
import pickle
import traceback

from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/profile", methods=['POST'])
def profile():
    try:
        # Get raw_data from request with utf-8 encoding and decode it with base64.
        raw_data = request.get_data().decode('utf-8')
        decoded_data = base64.b64decode(raw_data)

        # Deserialize the decoded data, store it in a variable
        profile_data = pickle.loads(decoded_data)

        # Ensure that profile_data is a dictionary
        if isinstance(profile_data, dict):
            # Escape any HTML characters in the values of the dictionary
            profile_data = {k: escape(v) for k, v in profile_data.items()}

            # Serialize the sanitized profile data
            sanitized_data = pickle.dumps(profile_data)

            # Encode the serialized data with base64
            encoded_data = base64.b64encode(sanitized_data)

            # Return the encoded data
            return encoded_data.decode('utf-8')

        return "Invalid profile data"

    except Exception as e:
        # Log the exception or just return a general error message without any exception details
        traceback.print_exc()
        return "Oops! Something went wrong."

if __name__ == "__main__":
    app.run()