from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/showName', methods=['GET'])
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    name = request.args.get('name')

    if name:
        # Rendering a template string with the name
        return render_template_string("<p>Hello, {{ name }}</p>", name=name)
    else:
        # Creating an error response with status code 400
        return make_response({"error": "name parameter is missing in the request"}, 400)

if __name__ == "__main__":
    app.run()