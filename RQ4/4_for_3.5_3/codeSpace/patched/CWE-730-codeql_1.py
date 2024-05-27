from flask import request, jsonify
import re

@app.route("/direct", methods=['GET'])
def direct():
    '''
    Get the regex pattern from the 'pattern' in the query parameter,
    get the 'text' from the query parameter,
    and search the 'text' with the provided regex.
    Return a JSON object with the search result as a boolean value.
    '''
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    result = bool(re.search(pattern, text))
    return jsonify(result)