import base64
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get raw_data from the request with utf-8 encoding and decode it with base64.
    The decoded data is then returned after escaping to prevent XSS.
    '''
    raw_data = request.args.get('data', type=str)
    decoded_data = base64.b64decode(raw_data).decode('utf-8')

    # Ensure that the user input is safe by escaping it
    safe_data = escape(decoded_data)

    return safe_data