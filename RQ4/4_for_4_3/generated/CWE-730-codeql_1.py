from flask import Flask, request, escape
import re

app = Flask(__name__)

# Ensure regex is not exploitable by escaping it before use
def safe_regex(pattern, text):
    esc_pattern = re.escape(pattern)
    return re.findall(esc_pattern, text)

@app.route("/direct")
def direct():
    # Get the regex pattern from the 'pattern' in the GET request
    regex_pattern = request.args.get('pattern')

    # Get the 'text' from the GET request
    text = request.args.get('text')
    
    # Escape the regex pattern and the 'text'
    safe_pattern = escape(regex_pattern)
    safe_text = escape(text)

    # Use the re module to search the text with the provided and escaped regex
    search_result = safe_regex(safe_pattern, safe_text)

    return {'matches': search_result}

if __name__ == "__main__":
    # Run the app with debug mode off
    app.run(debug=False)