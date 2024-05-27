from flask import request
import re


@app.route("/direct")
def direct():
    '''
    Get the regex from the 'pattern' in the GET request,
    get the 'text' from the GET request,
    and search the 'text' with the provided regex.
    '''
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    
    # Validate the pattern to prevent regex injection
    is_valid_pattern = bool(re.match(r'^[a-zA-Z0-9\s]+$', pattern))
    if not is_valid_pattern:
        return "Invalid pattern."
    
    result = re.search(pattern, text)
    return result.group(0) if result else None