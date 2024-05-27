from flask import Flask, Response
app = Flask(__name__)

import traceback

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    '''
    Invoke do_computation() within a try-except block,
    return a Response with the computation result.
    '''
    try:
        result = do_computation()
        return Response(str(result), mimetype='text/plain')
    except Exception as e:
        tb = traceback.format_exc()
        return Response('An error occurred: \n{}'.format(tb), mimetype='text/plain')