from flask import Flask, Response
import traceback

app = Flask(__name__)

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    try:
        # Call the do_computation function
        result = do_computation()
        # Return a response with the computation result
        return Response(result, status=200)
    except Exception as e:
        # Print the traceback
        traceback.print_exc()
        # Return a response with an error message
        return Response(str(e), status=500)

if __name__ == '__main__':
    app.run()