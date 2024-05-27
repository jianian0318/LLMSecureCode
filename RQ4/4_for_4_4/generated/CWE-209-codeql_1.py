from flask import Flask, Response
app = Flask(__name__)

import traceback

def do_computation():
    raise Exception("Error")

@app.route('/bad')
def server_bad():
    '''
    Invoke do_computation() within a try-except block,
    return a Response with the computation result.
    '''
    try:
        do_computation()
    except Exception as e:
        # Generic response to protect sensitive details from being exposed
        return Response("An error occurred", mimetype='text/plain')

if __name__ == "__main__":
    # Do not run the Flask app in debug mode in a production environment 
    app.run(debug=False)