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
        do_computation()
    except Exception:
        error_message = 'Internal server error'
        tb = traceback.format_exc()
        return Response(error_message, mimetype='text/plain')

if __name__ == "__main__":
    app.run()