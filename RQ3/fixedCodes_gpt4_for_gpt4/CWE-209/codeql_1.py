from flask import Flask, Response
app = Flask(__name__)

def do_computation():
    raise Exception("Secret info")

@app.route('/safe')
def server_safe():
    try:
        do_computation()
    except Exception as e:
        return Response("An error occurred", 200) 

if __name__ == '__main__':
    app.run(debug=True)