from flask import Flask, redirect, request, abort
import re
import urllib.parse

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    target_url = request.args.get('target')
    if target_url:
        # Validate the target URL
        parsed_url = urllib.parse.urlparse(target_url)
        safe_url = re.sub(r'\s', '', target_url)  # Remove whitespace in the target URL
        if parsed_url.scheme in ('http', 'https') and parsed_url.netloc and target_url == safe_url:
            # Validate the host of the target URL
            if not re.match(r'^example\.com$', parsed_url.netloc):
                abort(400)  # Return a bad request response if the host is not allowed
            return redirect(target_url, code=302)  # Redirect to the valid target URL
        else:
            return "Invalid target URL.", 400  # Return a bad request response for invalid URLs
    else:
        return "No target URL provided.", 400  # Return a bad request response if no target URL

if __name__ == "__main__":
    app.run()