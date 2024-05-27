from flask import request
from flask import jsonify
import re
import re


@app.route("/direct")
def direct():
    pattern = re.escape(request.args.get('pattern'))  # Get the regular expression pattern from the GET request and escape it
    text = request.args.get('text')  # Get the text string from the GET request

    compiled_pattern = re.compile(pattern)  # compile the regular expression pattern

    match = re.search(compiled_pattern, text)  # search the string 'text' using the compiled pattern

    if match:
        result = match.group()  # extract the matched string
    else:
        result = "No match found"

    return jsonify({"result": result})