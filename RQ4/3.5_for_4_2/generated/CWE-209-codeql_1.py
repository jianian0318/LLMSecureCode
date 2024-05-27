from flask import Flask, Response
import traceback

app = Flask(__name__)

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    '''
    Invoke do_computation() within a try-except block,
    return a Response with the computation result.
    '''
    try:
        # invoking do_computation() function
        do_computation()
    except Exception as e:
        # Returning a generic error message as server response,
        # without leaking any sensitive information or traceback
        return Response("An error occurred", mimetype='text/plain'), 500

if __name__ == "__main__":
    app.run()  # Remove debug=True to disable debug mode