import subprocess
import shlex

def executeCommand():
    """
    Read a command from user input, validate it, and execute it
    """
    command = input("Enter a command: ")  # Read a command from user input

    # Validate the command
    if not command:
        print("Invalid command. Please enter a valid command.")
        return

    try:
        # Execute the command using the subprocess module
        args = shlex.split(command)  # Split the command into arguments
        if args[0] in ['ls', 'dir']:  # Check if the command is allowed
            process = subprocess.Popen(args, shell=False, 
                                       stdin=subprocess.PIPE, 
                                       stdout=subprocess.PIPE)
            output, error = process.communicate()
            print(output.decode())
        else:
            print("Invalid command. Only 'ls' and 'dir' commands are allowed.")
    except Exception as e:
        print(f"Error executing the command: {str(e)}")

executeCommand()