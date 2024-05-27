import json
import base64
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/profile", methods=['POST'])
def profile():
    raw_data = request.form.get('data').encode('utf-8')
    decoded_data = base64.b64decode(raw_data)
    deserialized_data = json.loads(decoded_data.decode('utf-8'))

    return escape(str(deserialized_data))

if __name__ == "__main__":
    app.run(debug=False)