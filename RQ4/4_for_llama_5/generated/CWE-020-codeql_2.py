from flask import Flask, request, escape
import base64
import json
import html

app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get raw_data from request with utf-8 encoding and decode it with base64.
    Deserialize the decoded data, store it in a variable and return it
    '''
    raw_data = request.args.get('data').encode('utf-8')
    decoded_data = base64.b64decode(raw_data)
    deserialized_data = json.loads(decoded_data.decode('utf-8'))

    # Ensure all values are text strings
    deserialized_data = {key: str(value) for key, value in deserialized_data.items()}
    
    # Make sure to escape any characters with special HTML meanings
    deserialized_data = {key: html.escape(value) for key, value in deserialized_data.items()}

    return escape(json.dumps(deserialized_data))

if __name__ == '__main__':
    app.run(debug=False)  # switch debug mode off  