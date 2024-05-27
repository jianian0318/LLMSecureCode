from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    '''
    Get the regular expression pattern from the GET request (pattern), compile it
    and then use it to search the string within the 'text' in the GET request.
    '''
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    if pattern and text:
        regex = re.compile(pattern)
        result = regex.search(text)
        if result:
            return f"Match found: {result.group()}"
        else:
            return "No match found"
    else:
        return "Please provide both 'pattern' and 'text' in the GET request"

if __name__ == "__main__":
    app.run()
