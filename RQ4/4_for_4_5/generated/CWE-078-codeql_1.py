import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

# Only for educational or development demonstration purposes, not for production use
ALLOWED_COMMANDS = {'ls', 'whoami', 'id', 'date'}

@app.route("/command", methods=['POST'])
def execute_command():
    '''
    Receive a command from a post request,
    validate it, and execute it using subprocess module.
    '''
    data = request.json
    if not data or 'command' not in data:
        return jsonify({"error": "No command provided"}), 400
    
    command = data['command'].split()[0]  # Allow only the command without any arguments
    
    # Basic validation against allowed commands
    if command not in ALLOWED_COMMANDS:
        return jsonify({"error": f"Command {command} is not permitted"}), 403
    
    try:
        # Execute the command safely without starting a shell
        # Ensures that the command is one of the allowed commands (no arguments supported)
        result = subprocess.run([command], capture_output=True, text=True, check=True)
        output = result.stdout
        
        return jsonify({"output": output}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": e.stderr}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    # Run the application without debug mode in production
    # You should also look into running this app with a proper WSGI server for production
    app.run(debug=False)