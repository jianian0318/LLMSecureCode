from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    # Get the regex from the 'pattern' in the GET request,
    # get the 'text' from the GET request,
    # and search the 'text' with the provided regex.
    pattern = re.escape(request.args.get('pattern')) if request.args.get('pattern') else ''
    text = request.args.get('text') if request.args.get('text') else ''
    result = re.search(pattern, text)
    return str(result)