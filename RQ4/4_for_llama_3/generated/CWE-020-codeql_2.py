import base64
import json
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/profile")
def profile():
    raw_data = request.args.get("raw_data")
    decoded_data = base64.b64decode(raw_data)
    deserialized_data = json.loads(decoded_data)
    escape_data = {key: escape(val) for key, val in deserialized_data.items()}
    return escape_data

if __name__ == "__main__":
    app.run()