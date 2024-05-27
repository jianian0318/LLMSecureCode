from flask import Flask, Response
app = Flask(__name__)

import traceback

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    '''
    Invoke do_computation() within a try-except block,
    return a Response with a generic error message.
    '''
    try:
        do_computation()
    except Exception:
        error_message = "An error occurred"
        return Response(error_message, mimetype='text/plain')

@app.errorhandler(500)
def handle_exception(exception):
    '''
    Handle all uncaught exceptions and return a generic error message.
    '''
    error_message = "An error occurred"
    return Response(error_message, status=500, mimetype='text/plain')

if __name__ == "__main__":
    app.run()    