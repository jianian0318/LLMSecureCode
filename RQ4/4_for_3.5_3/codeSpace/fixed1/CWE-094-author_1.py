from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/evalcode", methods=["POST"])
def eval_code():
    '''
    Endpoint that confirms receipt of the code without execution.
    This method safely acknowledges the code input without the risk of arbitrary code execution.
    '''
    code = request.form.get('code')  # Get the code from the request
    
    if code:
        # Instead of executing, we simply return a success message without processing the code.
        return 'Code received successfully'
    else:
        abort(400, description="No code provided")  # Return an error if no code is provided

if __name__ == '__main__':
    app.run()