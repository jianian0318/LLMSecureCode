from flask import request
import re
import json

@app.route("/direct", methods=['GET'])
def direct():
    # Get the regex pattern from the 'pattern' parameter in the GET request
    pattern = re.escape(request.args.get('pattern'))

    # Get the text from the 'text' parameter in the GET request
    text = request.args.get('text')

    # Search the text with the provided regex pattern
    matches = re.findall(pattern, text)

    # Return the matches as a JSON response
    return json.dumps(matches)