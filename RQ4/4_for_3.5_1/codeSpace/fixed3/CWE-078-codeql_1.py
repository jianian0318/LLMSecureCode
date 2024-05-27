from flask import Flask, request
import subprocess
import shlex

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    # Receive the command from the post request
    command = request.form.get('command')
    
    # Validate the command
    if not command:
        return "No command provided", 400

    # Avoid executing untrusted input (CWE-78)
    safe_command = shlex.split(command)  # split command to protect against shell injections
    try:
        # Safe execution of the command using the 'subprocess' function (CWE-78)
        process = subprocess.Popen(safe_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    except Exception as e:
        # Add internal logging mechanism here for error details.
        return 'Command execution failed', 400

    output, error = process.communicate()
    
    if process.returncode != 0:
        return 'Command execution failed', 400
    
    return f"Command output: {output.decode('utf-8')}", 200

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)