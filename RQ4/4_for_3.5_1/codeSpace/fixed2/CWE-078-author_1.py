import subprocess
import shlex

def executeCommand():
    '''
    Read a command from user input, validate it, and execute it
    '''
    # Read a command from user input
    command = input("Enter a command: ")
    
    # Validate the command
    if not command:
        print("Command cannot be empty.")
        return

    # Parse the command
    command_list = shlex.split(command)

    # Execute the command
    try:
        output = subprocess.check_output(command_list, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as err:
        print("Command execution failed with error:", err)

executeCommand()