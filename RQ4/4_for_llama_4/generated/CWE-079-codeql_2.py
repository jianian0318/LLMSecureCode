from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/showName')
def name():
    name = request.args.get('name')

    if name is not None and name != '':
        response = make_response(escape(name))
    else:
        response = make_response('Invalid name')

    return response

if __name__ == '__main__':
    app.run()