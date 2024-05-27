import subprocess
from flask import Flask, request, abort
import shlex

app = Flask(__name__)

@app.route("/command", methods=["POST"])  
def executeCommand():
    command = request.get_json().get('command')  

    # Allow explicitly defined commands only, to prevent malicious command execution
    allowed_commands = ['ls', 'cat', 'echo']
  
    # Split command by spaces
    command_list = shlex.split(command)
  
    # Check if the command is in the list of the allowed commands
    if command_list[0] not in allowed_commands:
        abort(400, 'Invalid command!') 
    try:
        subprocess.run(command_list, check=True, shell=False)   # Execute command without using shell=True
        return 'Command executed', 200
    except subprocess.CalledProcessError as e:
        abort(500, str(e))

if __name__ == "__main__":
    # Remove the debug=True statement to switch to production mode
    app.run(debug=False)