    from flask import Flask, request
    import re
    import html
    from werkzeug.utils import escape

    app = Flask(__name__)

    @app.route("/direct", methods=['GET'])
    def direct():
        pattern = request.args.get('pattern')
        text = request.args.get('text')
        
        if pattern and text:
            # sanitize the input to prevent against Regular Expression Denial of Service attack
            safe_pattern = re.escape(pattern)
            # sanitize the input to prevent against XSS attack
            safe_text = html.escape(text)

            regex = re.compile(safe_pattern)
            
            match = regex.search(safe_text)
            if match:
                # Resulting match should also be sanitized
                return "Match found: {}".format(html.escape(match.group()))
            else:
                return "No match found"
        else:
            return "Please provide both 'pattern' and 'text' in the GET request"

    if __name__ == "__main__":
        app.run()