from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''

    # Get target URL from request
    target_url = request.args.get('url')

    # Check if target URL contains a valid domain
    if validateDomain(target_url):
        # Redirect to the target URL
        return redirect(target_url)
    else:
        return 'Invalid domain'

def validateDomain(url):
    '''
    Validate if the given URL contains a valid domain
    '''
    # You can implement your domain validation logic here
    return True  # Placeholder implementation, modify as needed

if __name__ == '__main__':
    app.run()