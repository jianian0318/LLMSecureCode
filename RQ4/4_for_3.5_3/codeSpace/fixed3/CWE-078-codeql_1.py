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
    # Extract and validate the command from the form data safely
    command = request.form.get("command", "").strip()
    command_parts = command.split()
    
    if not command_parts or command_parts[0] not in ALLOWED_COMMANDS:
        return jsonify({"error": "Invalid or disallowed command"}), 400

    try:
        # Using subprocess.run to securely execute commands with provided arguments
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return jsonify({"output": result.stdout})
    except subprocess.CalledProcessError as e:
        # Handle subprocess errors without exposing internal details
        return jsonify({"error": "Command execution failed"}), 500
    except Exception as e:
        # Catch-all for other exceptions
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == "__main__":
    app.run()