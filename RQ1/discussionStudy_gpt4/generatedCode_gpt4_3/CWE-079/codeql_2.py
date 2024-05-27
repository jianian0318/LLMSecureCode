from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/showName', methods=['GET'])
def name():
    name = request.args.get('name', default = None, type = str)
    
    if name is None:
        return make_response('Name not provided', 400)
    
    response = make_response('Hello, ' + name, 200)
    return response
    
if __name__ == "__main__":
    app.run(debug=True)