from flask import Flask, request
import re
import html

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = html.escape(request.args.get('pattern'))
    text = html.escape(request.args.get('text'))
    
    regexp = re.compile(re.escape(pattern))
    matches = regexp.findall(text)
    return f"Matches: {html.escape(str(matches))}"

if __name__ == "__main__":
    app.run()