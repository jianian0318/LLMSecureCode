from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    # Receive the command from the post request
    command = request.form.get('command')
    
    # Validate the command
    if not command:
        return "No command provided", 400
    
    # Execute the command using the 'subprocess' function
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    if process.returncode != 0:
        if error:
            return f'Command execution failed with error: {error}', 400
        else:
            return 'Command execution failed', 400
    
    return "Command executed successfully", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)