from flask import Flask, Response

app = Flask(__name__)

def do_computation():
    # Keeping "Secret info" for program's debugging purposes.
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    try:
        result = do_computation()
        return Response(result, status=200)
    except Exception as e:
        # The user does not see the original error message. 
        # "Internal Server Error" is a common, generic message that doesn't leak information.
        return Response("Internal Server Error", status=500)

if __name__ == '__main__':
    # Debug mode has been turned off.
    app.run(debug=False)