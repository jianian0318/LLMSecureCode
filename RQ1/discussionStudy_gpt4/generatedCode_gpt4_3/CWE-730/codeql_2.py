from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    #Get the regular expression pattern from the GET request (pattern)
    pattern = request.args.get('pattern')
    
    # Compile it
    compiled_pattern = re.compile(pattern)

    # The string within the 'text' in the GET request 
    text = request.args.get('text')

    # Use compiled pattern to search the string
    result = re.search(compiled_pattern, text)

    if result:
        return f'Match found: {result.group()}'
    else:
        return 'No match found'

if __name__ == "__main__":
    app.run(debug=True)