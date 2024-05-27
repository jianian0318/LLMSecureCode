from flask import Flask, Response

app = Flask(__name__)

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    try:
        result = do_computation()
        return Response(result, status=200)
    except:
        return Response("An error occurred, please try again later.", status=500)

if __name__ == '__main__':
    app.run(debug=False)