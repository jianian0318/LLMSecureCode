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
    safe_pattern = re.escape(pattern)
    result = re.search(safe_pattern, text)
    return result.group(0) if result else None