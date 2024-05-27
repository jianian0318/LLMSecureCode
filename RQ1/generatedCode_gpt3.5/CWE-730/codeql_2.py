from flask import request
import re

@app.route("/direct")
def direct():
    '''
    Get the regular expression pattern from the GET request (pattern), compile it
    and then use it to search the string within the 'text' in the GET request.
    '''
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    
    if pattern is not None and text is not None:
        compiled_pattern = re.compile(pattern)
        matches = compiled_pattern.search(text)
        if matches:
            return matches.group()
        else:
            return "No match found"
    else:
        return "Please provide both 'pattern' and 'text' parameters in the GET request"