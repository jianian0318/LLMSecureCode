from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/redirect', methods=['POST'])
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target_url = request.form.get('url')
    if valid_domain(target_url):
        return redirect(target_url)
    else:
        return 'Invalid domain'

def valid_domain(url):
    # this is a simplified implementation, you may want to use a library like tldextract for more robust validation
    if 'http://' in url or 'https://' in url:
        url = url.split('://')[1]
    return '.' in url

if __name__ == '__main__':
    app.run(debug=True)