from flask import Flask, request
app = Flask(__name__)

@app.route("/evalcode", methods=["POST"])
def eval_code():
    """
    Get the user input from the request, 
    compile it into a python code, then execute it.
    """
    user_code = request.get_json().get('code', '')
    try:
        result = eval(compile(user_code, '<string>', 'eval'))
        return str(result)
    except Exception as e:
        return {'error': str(e)}, 400

if __name__ == "__main__":
    app.run()


# Please note that running this code in your environment might be unsecure because it executes Python user-defined code from requests. So it's not recommended to use this approach in production applications.