from flask import Flask, Response
app = Flask(__name__)
import traceback

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    try:
        do_computation()
    except Exception as e:
        return Response(str(e), 200) 

if __name__ == '__main__':
    app.run(debug=True)