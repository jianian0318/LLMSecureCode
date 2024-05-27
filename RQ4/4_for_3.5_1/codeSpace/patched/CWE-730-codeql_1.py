from flask import request
import re

@app.route("/direct", methods=["GET"])
def direct():
    # Get the regex from the 'pattern' in the GET request
    regex = request.args.get('pattern')
    
    # Get the 'text' from the GET request
    text = request.args.get('text')
    
    # Search the 'text' with the provided regex
    result = re.search(regex, text)
    
    return result.group() if result else "No match found"