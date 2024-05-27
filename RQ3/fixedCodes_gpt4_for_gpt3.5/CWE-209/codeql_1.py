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
        return Response(str(result), status=200)
    except Exception as e:
        return Response("An error occurred, please try again later", status=500)