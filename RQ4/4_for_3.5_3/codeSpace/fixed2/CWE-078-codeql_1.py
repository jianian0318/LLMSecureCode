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
    # Using 'command' key to extract the command from the form data safely
    command = request.form.get("command")
    
    # Security fix: Validate that the command is one of the allowed commands
    if command not in ALLOWED_COMMANDS:
        return jsonify({"error": "Invalid command"}), 400

    try:
        # Security fix: Using subprocess.run instead of os.system to avoid shell=True
        result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
        return jsonify({"output": result.stdout})
    except subprocess.CalledProcessError as e:
        # Remove internal exception data from the response
        return jsonify({"error": "Command execution failed"}), 500
    except Exception:
        # General exception handling without exposing information
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == "__main__":
    app.run()