from flask import request
import re
from flask import Flask

app = Flask(__name__)

@app.route("/direct", methods=['GET'])
def direct():
    '''
    Get the regex from the 'pattern' in the GET request,
    get the 'text' from the GET request,
    and search the 'text' with the provided regex.
    '''
    pattern = request.args.get('pattern', '')    # Default is empty string if 'pattern' is not provided
    text = request.args.get('text', '')          # Default is empty string if 'text' is not provided
    match = re.search(pattern, text)

    if match is None:
        return "No match found."
    else:
        return "Match found: " + match.group(0)

if __name__ == "__main__":
    app.run()