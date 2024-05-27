from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/command", methods=["POST"])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it in a safe manner.
    '''
    command = request.form.get('command')
    if command:
        try:
            # execute the command using subprocess without shell=True
            result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
            return f"Command executed successfully! Output: {result.stdout}"
        except subprocess.CalledProcessError as e:
            return f"An error occurred: {e}"
        except Exception as e:
            return f"An error occurred while executing the command: {str(e)}"
    else:
        # return an error message if no command is provided
        return "No command provided!"

if __name__ == "__main__":
    app.run(debug=True)