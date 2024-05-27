from flask import request
import re

@app.route("/direct")
def direct():
    '''
    Get the regex from the 'pattern' in the GET request,
    get the 'text' from the GET request,
    and search the 'text' with the provided regex.
    '''
    pattern = request.args.get('pattern', '')
    text = request.args.get('text', '')
    match = re.search(pattern, text)
    if match:
        return f"Found match: {match.group(0)}"
    else:
        return "No match found"