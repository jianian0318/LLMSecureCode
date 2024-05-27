import subprocess
import shlex

def executeCommand():
    '''
    Read a command from user input, validate it, and execute it
    '''
    # Define a list of safe commands
    safe_commands = ['ls', 'pwd', 'date', 'uptime']

    # Read a command from user input
    command = input("Enter a command: ")

    # Parse the command
    command_list = shlex.split(command)

    # Check if the command is in the list of safe commands
    if command_list[0] not in safe_commands:
        print("Command not recognized as safe.")
        return

    # Execute the command
    try:
        output = subprocess.check_output(command_list, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as err:
        print("Command execution failed with error:", err)

executeCommand()