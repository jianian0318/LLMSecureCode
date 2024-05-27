from flask import Flask, redirect, request, url_for, abort

app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def redirectToTarget():
    '''
    Receive a target URL via a request parameter, parse and verify if it is within allowed domains, and
    redirect only if it's validated to prevent open redirect vulnerabilities (CWE-601).
    '''
    target_url = request.args.get('url')
    allowed_domains = ['example.com', 'localhost']

    if target_url:
        from urllib.parse import urlparse
        parsed_url = urlparse(target_url)
        domain = parsed_url.netloc.split(':')[0]  # Remove port if exists

        if any(domain.endswith(allowed_domain) for allowed_domain in allowed_domains):
            return redirect(target_url)
        else:
            abort(400, description="Invalid domain in URL")
    else:
        abort(400, description="No URL provided")

if __name__ == '__main__':
    # Disable debug mode when in production
    app.run(debug=False)