from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')  # Get the regular expression pattern from the GET request
    text = request.args.get('text')  # Get the string from the GET request

    compiled_pattern = re.compile(pattern)  # Compile the regular expression pattern
    
    match = re.search(compiled_pattern, text)  # Use the compiled pattern to search the string

    if match:
        return "Pattern found in text"
    else:
        return "Pattern not found in text"

if __name__ == "__main__":
    app.run()