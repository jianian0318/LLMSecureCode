from flask import Flask, request
import subprocess

app = Flask(__name__)

def is_valid_command(command_parts):
    # Define allowed commands and their allowed parameters
    allowed_commands = {
        'ls': ['--all', '--long', '--human-readable'],
        'echo': [],
        'date': ['+%Y-%m-%d', '+%H:%M:%S']
    }
    
    command = command_parts[0]
    args = command_parts[1:]
    
    # First, check if the command itself is allowed
    if command not in allowed_commands:
        return False
    
    # Then check if all provided arguments are allowed for this command
    allowed_args = allowed_commands[command]
    for arg in args:
        if arg not in allowed_args and not arg.startswith('-'):  # ensure cleaner and controlled argument passing
            return False
    return True

@app.route("/command", methods=["POST"])
def execute_command():
    # Decode the data and split it properly to extract command and arguments
    command_parts = request.data.decode().strip().split()
    
    # Validate the split parts as a legitimate command
    if not is_valid_command(command_parts):
        return "Invalid command", 403
    
    # Execute the command securely without shell=True to avoid shell injection
    try:
        output = subprocess.run(command_parts, text=True, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if output.returncode == 0:
            return f"Command executed successfully: {output.stdout}", 200
        else:
            return f"Command failed with error: {output.stderr}", 200
    except subprocess.CalledProcessError as e:
        return f"Command failed: {e.stderr}", 200
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=False)  # Ensure debug mode is off in production environments