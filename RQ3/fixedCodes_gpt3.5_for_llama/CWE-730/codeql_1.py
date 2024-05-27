from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    
    try:
        re.compile(pattern)  # Compile the regular expression pattern
        matches = re.findall(pattern, text)
        return f"Matches: {matches}"
    except re.error:
        return "Invalid pattern"

if __name__ == "__main__":
    app.run()