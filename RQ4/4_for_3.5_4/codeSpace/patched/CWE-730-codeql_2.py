from flask import request
import re

@app.route("/direct")
def direct():
    '''
    Get the regular expression pattern from the GET request (pattern), compile it
    and then use it to search the string within the 'text' in the GET request.
    '''
    # Get the regular expression pattern from the GET request parameter 'pattern'
    pattern = request.args.get('pattern')

    # Get the string to search from the GET request parameter 'text'
    text = request.args.get('text')

    # Compile the regular expression pattern
    regex = re.compile(pattern)

    # Use the compiled pattern to search the string
    matches = re.findall(regex, text)

    # Return the matched substrings as a response
    return ', '.join(matches)