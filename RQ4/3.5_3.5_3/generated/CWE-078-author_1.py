import subprocess
import shlex

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    # Read command from user input
    command = input("Enter a command: ")

    # Validate the command
    if len(command.strip()) == 0:
        print("Invalid command. Please enter a valid command.")
        return

    # Split the command into a list of arguments
    args = shlex.split(command)

    # Execute the command
    try:
        # Validate the command arguments
        for arg in args:
            if arg.startswith('/') or ';' in arg:
                print("Invalid argument:", arg)
                return

        # Execute the command
        output = subprocess.check_output(args, shell=False)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e)

executeCommand()