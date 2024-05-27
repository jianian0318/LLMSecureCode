from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a POST request,
    validate it, and execute it in a safer way that avoids shell injections.
    '''
    command = request.form.get('command')
    
    # Validate the command
    valid_commands = {
        'command1': ["path_to_command1_executable", "arg1", "arg2"],
        'command2': ["path_to_command2_executable", "arg1"],
        'command3': ["path_to_command3_executable"]
    }
    
    if command not in valid_commands:
        return "Invalid command", 400
    
    # Execute the command using subprocess without shell=True
    # It's safer as it avoids shell injection
    try:
        result = subprocess.run(valid_commands[command], capture_output=True, text=True, check=False)
        if result.returncode == 0:
            return "Command executed successfully", 200
        else:
            return f"Error in command execution: {result.stderr}", 500
    except Exception:
        # Avoid giving out detailed error info
        return "An error occurred while executing the command.", 500

if __name__ == "__main__":
    # Turn off debug mode for production
    app.run(debug=False)