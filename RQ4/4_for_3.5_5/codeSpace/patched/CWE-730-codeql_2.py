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

    # Compile the regular expression pattern
    regex = re.compile(pattern)

    # Search for the pattern in the text
    matches = regex.search(text)
    
    if matches:
        return matches.group()
    else:
        return "No match found."