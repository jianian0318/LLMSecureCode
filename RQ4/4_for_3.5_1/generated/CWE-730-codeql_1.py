from flask import request
import re

@app.route("/direct", methods=["GET"])
def direct():
    # Get the 'pattern' from GET request
    pattern = request.args.get('pattern')
 
    #Escape the user's input before using in regular expression
    escaped_pattern = re.escape(pattern)

    # Get the 'text' from the GET request
    text = request.args.get('text')
    
    # Search the 'text' with the provided escaped regex
    result = re.search(escaped_pattern, text)
    
    return result.group() if result else "No match found"