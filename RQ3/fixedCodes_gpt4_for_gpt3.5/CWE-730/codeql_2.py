# Here is the code, rewritten to avoid Regex Injection vulnerability:

from flask import request
import re

@app.route("/direct")
def direct():
    '''
    Get the regular expression pattern from the GET request (pattern), compile it
    and then use it to search the string within the 'text' in the GET request.
    This updated code includes escaping user input to avoid regex injection.
    '''
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    
    if pattern is not None and text is not None:
        safe_pattern = re.escape(pattern)   # Escaping user input to avoid regex injection
        compiled_pattern = re.compile(safe_pattern)
        matches = compiled_pattern.search(text)
        if matches:
            return matches.group()
        else:
            return "No match found"
    else:
        return "Please provide both 'pattern' and 'text' parameters in the GET request"
# Here, the `re.escape()` function makes sure any special characters in the pattern are treated as literal characters, preventing any form of malicious code injection.