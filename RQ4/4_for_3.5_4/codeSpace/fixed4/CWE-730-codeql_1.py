from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    # Get the regex pattern from the 'pattern' in the GET request
    pattern = request.args.get('pattern')
    
    # Get the 'text' from the GET request
    text = request.args.get('text')
    
    # Escape any regex special characters in pattern input
    if pattern:
        pattern = re.escape(pattern)
    
    # Search the 'text' with the provided regex
    if text and pattern:
        if re.search(pattern, text):
            return "Found a match!"
        else:
            return "No match found."
    else:
        return "Invalid input."

if __name__ == "__main__":
    app.run()