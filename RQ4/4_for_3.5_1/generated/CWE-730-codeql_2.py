from flask import request
import re

@app.route("/direct", methods=['GET'])
def direct():
    '''
    Get the regular expression pattern from the GET request (pattern), compile it
    and then use it to search the string within the 'text' in the GET request.
    '''
    pattern = request.args.get('pattern')
    text = request.args.get('text')

    if pattern and text:
        safe_pattern = re.escape(pattern)  # escape any special characters
        regex = re.compile(safe_pattern)
        match = regex.search(text)
        if match:
            return match.group(0)
        else:
            return "No match found."
    else:
        return "Please provide both 'pattern' and 'text' parameters."