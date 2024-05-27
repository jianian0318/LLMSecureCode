from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/showName')
def name():
    name = request.args.get('name')  # Get 'name' from the request's query parameters

    if not name:
        # If 'name' is None or empty, return a response saying that name is required
        response = make_response('Name parameter is required.', 400)
    else:
        # Encode the 'name' to prevent XSS
        safe_name = escape(name)

        # If 'name' is valid (and safe), create a response that includes the name
        response_text = f'Hello, {safe_name}!'
        response = make_response(response_text, 200)
    
    return response

if __name__ == '__main__':
    app.run(debug=False)