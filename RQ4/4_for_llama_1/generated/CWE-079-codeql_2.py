from flask import Flask, request, make_response, Markup

app = Flask(__name__)

@app.route('/showName')
def name():
    name = request.args.get('name')
    if name and name != '':
        safe_name = Markup.escape(name)
        response = make_response(f'Hello, {safe_name}!')
    else:
        response = make_response('Please provide a name')
    return response

if __name__ == '__main__':
    app.run()