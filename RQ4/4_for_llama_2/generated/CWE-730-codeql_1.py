from flask import Flask, request
import re
from cgi import escape
import html

def escape_regex(pattern):
    return re.escape(pattern)

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = escape_regex(request.args.get('pattern', ''))
    text = html.escape(request.args.get('text', ''))
    matches = re.findall(pattern, text)
    safe_matches = html.escape(str(matches))
    
    return safe_matches

if __name__ == "__main__":
    app.run()