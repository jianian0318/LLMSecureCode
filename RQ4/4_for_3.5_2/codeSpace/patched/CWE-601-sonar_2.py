from flask import request, redirect, Flask

app = Flask(__name__)

@app.route('/flask_redirect', methods=['GET'])
def flask_redirect():
    '''
    Get the url from the request and redirect to it
    '''
    url = request.args.get('url')
    if url:
        return redirect(url)

# Run the Flask app
if __name__ == '__main__':
    app.run()