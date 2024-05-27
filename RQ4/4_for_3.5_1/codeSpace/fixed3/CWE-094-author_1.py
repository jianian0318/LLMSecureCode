from flask import Flask, request

app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    '''
    Get the user input from the request, 
    and then safely return the result of the evaluation if the input is safe.
    '''
    code = request.form.get('code')

    # Check if the code input is valid/safe
    if not is_valid(code): 
        return {'error': 'Invalid input!'}, 400

    # Execute only safe operations
    result = safe_execute(code)
    
    return {'result': result}, 200

def is_valid(code):
    """Validate the code for safe operations only."""
    # In a real-world scenario, consider more robust methods than simple keyword checking
    illegal_keywords = ["import", "exec", "eval", "open", "os", "subprocess", "input", "compile", "__builtins__", "getattr", "setattr", "delattr"]
    for keyword in illegal_keywords:
        if keyword in code:  # Simple containment check (not complete)
            return False
    # Ensure no built-in functions are used
    if "__" in code:
        return False
    # Add further checks if needed
    return True

def safe_execute(code):
    try:
        # Execute only the passed code limiting the passed functions and variables
        safe_globals = {"__builtins__": {}}
        safe_locals = {}
        exec(code, safe_globals, safe_locals)
        # We don't return anything as real "safe execution" would require much more validation
    except Exception as e:
        # Return error string, or log the error as needed
        return f'An exception occurred: {str(e)}'
    return safe_locals.get('result')  # The user must set 'result' variable in their code

if __name__ == '__main__':
    app.run()