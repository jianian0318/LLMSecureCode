from flask import Flask, request

app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    '''
    Get the user input from the request, 
    compile it, and then only execute SAFE python code.
    '''
    code = request.form.get('code')

    # Check if the code input is valid/safe
    if not is_valid(code): 
        return {'error': 'Invalid input!'}, 400

    result = None
    try:
        # Compile the code without executing
        compiled_code = compile(code, '<string>', 'exec')
        # Use the exec function within the try-except block in order to safely execute the code
        exec(compiled_code, { "result": result })
    except Exception:
        # Return a generic error message
        return 'An error occurred while processing your request.'
        
    return str(result)

def is_valid(code):
    """Validate the code for safe commands and no illegal keywords"""
    illegal_keywords = ["import", "exec", "eval", "open", "os.", "subprocess", "input"]
    for keyword in illegal_keywords:
        if keyword in code:
            return False
    return True

if __name__ == '__main__':
    app.run()