from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/showName', methods=['GET'])
def name():
    name_param = request.args.get('name', None)  # Get "name" from the request
    if name_param is None:  # validate it
        response = make_response("No name provided", 400)
    else:
        response = make_response(f"Name is: {name_param}", 200)
    return response  # Return the response object

if __name__ == "__main__":
    app.run(debug=True)