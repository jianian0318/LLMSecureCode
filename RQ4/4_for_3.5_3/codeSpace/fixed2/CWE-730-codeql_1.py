from flask import Flask, request, jsonify
import re

app = Flask(__name__)

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
    
    # Escape the pattern to avoid undesired regex injection
    escaped_pattern = re.escape(pattern)

    result = bool(re.search(escaped_pattern, text))
    return jsonify(result)

if __name__ == "__main__":
    # Turn off debug mode for production use to enhance security
    app.run(debug=False)