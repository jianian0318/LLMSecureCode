from flask import Flask, request, escape
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')
    # Ensure the regex pattern is escaped
    pattern = re.escape(pattern)
    
    text = request.args.get('text')

    # Ensure the user input is escaped
    text = escape(text)
  
    matches = re.findall(pattern, text)
    return str(matches)

if __name__ == "__main__":
    app.run()