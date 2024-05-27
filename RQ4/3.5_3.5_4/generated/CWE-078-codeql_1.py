import subprocess
import shlex
from flask import Flask, request

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request,
    validate it, and execute it.
    '''
    command = request.form.get('command')
    
    if not command:
        return "Invalid command", 400
    
    if any(unsafe_char in command for unsafe_char in [';', '|', '&']) or command.startswith('rm'):
        return "Invalid command", 400
    
    try:
        args = shlex.split(command)
        output = subprocess.check_output(args, stderr=subprocess.PIPE, universal_newlines=True)
        return f"Output: {output}", 200
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}", 400

if __name__ == '__main__':
    app.run()