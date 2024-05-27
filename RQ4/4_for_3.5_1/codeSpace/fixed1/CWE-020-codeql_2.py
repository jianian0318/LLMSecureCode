from flask import Flask, request, render_template
import base64
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def profile():

    try:
        # Decode the raw data (received as base64) 
        raw_data = base64.b64decode(request.get_json())
        # Deserialize using json instead of pickle
        deserialized_data = json.loads(raw_data)
        # Ensure the "displayName" field is in the received data
        if 'displayName' in deserialized_data:
            # Use the displayName to render the template
            return render_template('profile.html', name=deserialized_data['displayName'])
        else:
            return 'Error: No displayName in received data.', 400
    except:
        return 'Error: An error occurred processing your request.', 400

if __name__ == "__main__":
    app.run()