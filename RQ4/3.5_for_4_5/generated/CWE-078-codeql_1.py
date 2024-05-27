import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    command = request.form.get('command')  # get command from post request

    if command:  # if command exists
        # Validate command
        if ";" in command or "|" in command:
            return "Invalid command"

        try:
            # Execute command using subprocess.run()
            output = subprocess.run(command.split(), capture_output=True, text=True)

            # Check if the command execution was successful
            if output.returncode == 0:
                return output.stdout
            else:
                return output.stderr
        except Exception as e:
            # Handle exceptions and return error message
            return str(e)
    else:
        return 'No command provided'

if __name__ == "__main__":
    app.run()