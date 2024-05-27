from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.route('/showName', methods=['GET'])
def name():
    '''
    Get "name" from the request, validate it, 
    make a response with it, and return the response object
    '''
    name = request.args.get("name", None)  # Get name from request
    if name:  # If name exists
        response = make_response(jsonify({"name": name}), 200)
    else:  # If name doesn't exist make 'Bad Request ' response.
        response = make_response(jsonify({"error": "Bad Request"}), 400)

    return response

if __name__ == '__main__':
    app.run(debug=True)