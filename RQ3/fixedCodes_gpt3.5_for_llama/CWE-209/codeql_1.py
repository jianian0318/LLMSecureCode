from flask import Flask, Response
app = Flask(__name__)

def do_computation():
    raise Exception("An error occurred")

@app.route('/bad')
def server_bad():
    try:
        result = do_computation()
    except Exception as e:
        result = "An error occurred"
        # log the error without printing sensitive information
        app.logger.error(traceback.format_exc())
    return Response(result, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)