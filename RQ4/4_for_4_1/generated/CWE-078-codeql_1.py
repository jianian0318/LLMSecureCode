import subprocess
from flask import Flask, request

app = Flask(__name__)

# A set of allowed commands for security reasons
ALLOWED_COMMANDS = {'ls', 'whoami', 'date', 'uptime'}

@app.route('/command', methods=['POST'])
def execute_command():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    # Get the command from the request data
    command = request.form.get('command')

    # Validate the command
    if command not in ALLOWED_COMMANDS:
        return "Command not allowed", 403

    # Execute the command and get the output
    try:
        # Ensure that the command is executed without a shell 
        # and by using absolute paths (if needed)
        output = subprocess.check_output([command], shell=False, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"An error occurred while executing the command: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=False)