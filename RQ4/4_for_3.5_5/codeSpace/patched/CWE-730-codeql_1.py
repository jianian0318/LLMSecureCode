from flask import request
import re

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    result = re.search(pattern, text)
    if result:
        return result.group()
    else:
        return "No match found."