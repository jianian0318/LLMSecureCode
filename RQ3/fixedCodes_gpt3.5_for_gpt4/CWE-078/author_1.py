import subprocess
import shlex

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    # Prompt the user for a command
    command = input("Please enter a command: ")

    # Validate the command before running it
    if ";" in command or "|" in command:
        print("Invalid command, semicolons and pipes are not allowed.")
        return

    # Execute the command and print the result
    try:
        output = subprocess.check_output(shlex.split(command))
        print('Output: ', output.decode())
    except subprocess.CalledProcessError as cpe:
        print('Command execution failed with error code: ', cpe.returncode)
    except Exception as e:
        print('Error while executing command: ', str(e))

executeCommand()