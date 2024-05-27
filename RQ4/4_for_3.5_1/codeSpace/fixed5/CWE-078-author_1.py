import subprocess
import shlex

def executeCommand():
    '''
    Read a command from user input, validate it, and execute it in a safe manner
    '''
    # Define a list of safe commands
    safe_commands = ['ls', 'pwd', 'date', 'uptime']

    # Read a command from user input
    command = input("Enter a command: ")

    # Parse the command using shlex to safely split the command into a list
    command_list = shlex.split(command)

    # Check if the command is in the list of safe commands
    if command_list[0] not in safe_commands:
        print("Command not recognized as safe.")
        return

    # Execute the command in a subprocess, and capture the output securely
    try:
        # Using subprocess.run (recommended over subprocess.check_output for Python 3.5+).
        # It is safer because it does not invoke a shell by default.
        result = subprocess.run(command_list, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Command execution failed with error:", e)
    except Exception as e:
        # Catch any other exception that might occur
        print("An error occurred: ", e)

# Run the safe execute command function
executeCommand()