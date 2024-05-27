from flask import Flask, request
import subprocess

app = Flask(__name__)

def is_valid_command(command):
    # Add your validation logic here
    # Example validation: only allow specific commands
    allowed_commands = {'ls', 'echo', 'date'}
    return command.split()[0] in allowed_commands

@app.route("/command", methods=["POST"])
def execute_command():
    command = request.data.decode().strip().split()  # Split into command and arguments

    # Validate the command
    if not is_valid_command(command[0]):
        return "Invalid command"
    
    # Execute the command securely without shell=True
    try:
        output = subprocess.run(command, text=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return f"Command executed successfully: {output.stdout}"
    except subprocess.CalledProcessError as e:
        return f"Command failed: {e.stderr}"
    except Exception as e:
        return "An error occurred while processing the request"

if __name__ == "__main__":
    app.run(debug=False)  # Ensure debug mode is off in production