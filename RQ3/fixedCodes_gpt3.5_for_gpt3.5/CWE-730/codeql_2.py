from flask import request
import re

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')

    if pattern is not None and text is not None:
        try:
            compiled_pattern = re.compile(rf'{pattern}')
            matches = compiled_pattern.search(text)
            
            if matches:
                return matches.group()
            else:
                return "No match found"
        
        except re.error:
            return "Invalid regular expression pattern"
    
    else:
        return "Please provide both 'pattern' and 'text' parameters in the GET request"