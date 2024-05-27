import subprocess
from flask import Flask, request
import shlex

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    command = request.form.get('command')  # get the command from the post request
    
    if command is None:
        return 'No command received.', 400  # 400 is the HTTP status code for 'Bad Request'

    # validate the command
    if command not in ["valid_command1", "valid_command2", "valid_command3"]:
        return 'Invalid command.', 403  # 403 is the HTTP status code for 'Forbidden'

    # Execute the command using subprocess module with safe command
    try:
        command_args = shlex.split(command)
        output = subprocess.check_output(command_args, universal_newlines=True, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
        return f'Command executed, Output: {output}', 200  # 200 is the HTTP status code for 'OK'
    except subprocess.CalledProcessError as e:
        error_output = e.output if hasattr(e, 'output') else str(e)
        return f'Command execution failed. Error: {error_output}', 500  # 500 is the HTTP status code for 'Internal Server Error'

if __name__ == '__main__':
    app.run()