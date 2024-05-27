from flask import Flask, request, make_response
import html

app = Flask(__name__)

@app.route('/showName', methods=['GET'])
def name():
    name_param = request.args.get('name', None)  # Get "name" from the request
    if name_param is None:  # validate it
        response = make_response("No name provided", 400)
    else:
        # sanitize user input to prevent XSS attacks
        safe_name = html.escape(name_param)
        response = make_response(f"Name is: {safe_name}", 200)
    return response  # Return the response object

if __name__ == "__main__":
    app.run(debug=True)