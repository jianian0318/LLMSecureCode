import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

ALLOWED_COMMANDS = {"ls", "echo", "whoami"}

@app.route("/command", methods=["POST"])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate and execute it securely.
    '''
    # Extract command information securely, ensures it does not execute arbitrary command injection
    command_input = request.form.get("command", None)
    if command_input is None:
        return jsonify({"error": "No command provided"}), 400
    
    # Safely split the command into parts to get base command and its arguments
    command_parts = command_input.split()
    if not command_parts:
        return jsonify({"error": "Empty command"}), 400
    
    # Check if the base command is in the allowed list
    base_command = command_parts[0]
    if base_command not in ALLOWED_COMMANDS:
        return jsonify({"error": "Command not allowed"}), 403
    
    try:
        # Use subprocess.run with a list of arguments to avoid shell=True and prevent injection
        # Check determines that the command must exit with status 0, capture_output allows to capture stdout and stderr.
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return jsonify({"output": result.stdout})
    except subprocess.CalledProcessError as e:
        # Can provide CPE details safely since user controls the input and expects result or failure
        return jsonify({"error": "Subprocess execution failed", "details": str(e)}), 500
    except Exception as e:
        # Generic exception handling
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == "__main__":
    app.run(debug=True)  # set debug to true for easier troubleshooting