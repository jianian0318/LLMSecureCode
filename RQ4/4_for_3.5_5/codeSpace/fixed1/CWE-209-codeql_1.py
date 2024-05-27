from flask import Flask, Response
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
        result = do_computation()
        return Response(result, status=200)
    except Exception:
        # Return a generic error message instead of specific details
        return Response("An error occurred, please try again later.", status=500)

if __name__ == '__main__':
    app.run(debug=False)