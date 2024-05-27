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
        return Response(result, status=200)
    except Exception as e:
        traceback.print_exc()
        return Response(str(e), status=500)