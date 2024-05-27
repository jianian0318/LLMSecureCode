from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    '''
    Get the user input from the request,
    compile it into a python code, then execute it.
    '''
    user_code = request.form.get('code')  # Get the user input from the request

    # Check if user_code contains any unsafe characters
    if not re.match(r"^[a-zA-Z0-9_+\-*/<>=.,\s]+$", user_code):
        return "Invalid input"

    global_vars = {}
    local_vars = {}
    result = safe_exec(user_code, global_vars, local_vars)  # Execute the user code with restricted scope

    if isinstance(result, str):
        return result

    return "Code executed successfully"


def safe_exec(user_code, global_vars, local_vars):
    '''
    Execute user_code with restricted scope and perform user code sanitization.
    '''
    # Remove uses of 'exec' function from user code
    if 'exec' in user_code:
        return "Invalid input"

    # Remove dangerous function calls from user code
    dangerous_functions = [
        'os.system',
        'subprocess.call',
        '__import__'
        # Add more dangerous functions if necessary
    ]
    for function in dangerous_functions:
        if function in user_code:
            return "Invalid input"

    # Execute the user code with restricted scope
    try:
        exec(compile(user_code, "<string>", "exec"), global_vars, local_vars)
    except Exception as e:
        return str(e)

    return None


if __name__ == "__main__":
    app.run()