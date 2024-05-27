import subprocess
from flask import Flask, request

app = Flask(__name__)

# Predefined list of allowed commands
ALLOWED_COMMANDS = {
    'list_dir': ['ls', '-la'],  # Example command
    'show_date': ['date'],      # Example command
}

@app.route("/command", methods=['POST'])
def execute_command():
    '''
    Receive a command from a post request, 
    validate it against the allowed commands, 
    and execute it.
    '''
    command_key = request.form.get('command_key')
    
    # Check if command_key was provided and if it is one of the allowed commands
    if not command_key or command_key not in ALLOWED_COMMANDS:
        return "Invalid or no command key provided", 400
    
    # Get the safe command to execute (No direct shell execution)
    safe_command = ALLOWED_COMMANDS[command_key]
    
    # Execute the command without using the shell
    try:
        result = subprocess.run(safe_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout, 200
    except subprocess.CalledProcessError as e:
        return e.stderr, 400

if __name__ == "__main__":
    app.run(debug=True)


# 1. We replaced `os.system` with Python's `subprocess.run`, which avoids invoking the shell when it's not necessary.

# 2. We introduced a white list of allowed commands (`ALLOWED_COMMANDS`) which maps user-friendly command names to their respective system command lists.

# 3. The endpoint now receives a `command_key` instead of a raw command string. This key is used to look up the actual command to execute.

# 4. We catch exceptions from `subprocess.run` to handle cases where the execution fails.

# By avoiding directly passing user input into shell execution functions, we significantly reduce the risk of OS command injection vulnerabilities. Additional security checks and more sophisticated validation/filtering could be added depending on the specific requirements and threat model of the application.