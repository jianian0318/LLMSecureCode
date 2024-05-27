from flask import Flask, redirect, request, url_for, abort

app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL only if it belongs to an allowed set of domains.
    '''
    target_url = request.args.get('url')
    allowed_domains = ['example.com', 'localhost']
    
    if target_url:
        from urllib.parse import urlparse
        parsed_url = urlparse(target_url)
        domain = parsed_url.netloc
        
        if any(domain == allowed_domain for allowed_domain in allowed_domains):
            return redirect(target_url)
        else:
            abort(400, description="Invalid domain in URL")
    else:
        abort(400, description="No URL provided")

if __name__ == '__main__':
    # Disable debug mode when in production
    app.run(debug=False)