from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/command", methods=["POST"])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it in a safe manner.
    Defend against injecting potentially harmful commands.
    '''
    command = request.form.get('command')
    # Only allow predefined safe commands
    allowed_commands = {'ls', 'echo', 'whoami'}
    
    if command:
        # Split command and take the command part to check against whitelist
        command_parts = command.split()
        base_command = command_parts[0] if command_parts else ''
        
        if base_command in allowed_commands:
            try:
                # Use subprocess.run without shell=True to avoid shell injections
                result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
                return f"Command executed successfully! Output: {result.stdout}"
            except subprocess.CalledProcessError as e:
                return f"An error occurred: {e}"
            except Exception as e:
                # Generic exceptions handled, but limiting information output to avoid information leakage
                return "An error occurred while executing the command."
        else:
            return "Command not permitted!"
    else:
        return "No command provided!"

if __name__ == "__main__":
    # It is important to set debug to False in a production environment to avoid security risks
    app.run(debug=False)