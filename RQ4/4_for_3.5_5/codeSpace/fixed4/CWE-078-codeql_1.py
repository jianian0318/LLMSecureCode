from flask import Flask, request
import subprocess
import logging

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a POST request,
    validate it, and execute it in a safer way that avoids shell injections.
    '''
    command = request.form.get('command')
    
    # Mapping of valid commands to their respective executable and arguments
    valid_commands = {
        'command1': ["path_to_command1_executable", "arg1", "arg2"],
        'command2': ["path_to_command2_executable", "arg1"],
        'command3': ["path_to_command3_executable"]
    }
    
    # Check if the received command is in the list of valid commands
    if command not in valid_commands:
        return "Invalid command", 400
    
    # Execute the command using subprocess.run
    try:
        result = subprocess.run(valid_commands[command], capture_output=True, text=True, check=True)
        if result.returncode == 0:
            return result.stdout, 200
        else:
            return "Error in command execution", 500
    except subprocess.CalledProcessError as e:
        logging.error(f"Subprocess error: {e}")
        return "Error in executing the command", 500
    except Exception as e:
        logging.error(f"General error: {e}")
        return "An unexpected error occurred", 500

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    app.run(debug=False)