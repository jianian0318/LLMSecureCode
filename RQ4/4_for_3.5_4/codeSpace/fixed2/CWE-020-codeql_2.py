from flask import Flask, request, jsonify
import base64
import json

app = Flask(__name__)

@app.route("/profile")
def profile():
    raw_data = request.get_data(as_text=True)  # get raw data from request as text
    decoded_data = base64.b64decode(raw_data)  # decode the base64 encoded data
    decoded_data_as_str = decoded_data.decode('utf-8')  # decode bytes to string for JSON processing
    data = json.loads(decoded_data_as_str)  # deserialize the decoded data using json
    return jsonify(data)  # return the deserialized data using jsonify for proper formatting

if __name__ == "__main__":
    # Run the Flask app without debug mode to prevent vulnerabilities related to debug mode.
    app.run(debug=False)  # Set debug to False to avoid security risks in the production environment.