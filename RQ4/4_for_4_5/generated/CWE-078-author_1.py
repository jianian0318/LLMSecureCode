import subprocess
import re
import shlex

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it if it's safe.
    '''
    # Read a command from a user
    cmd = input("Please enter a command to execute: ")

    # Validate the command to ensure it doesn't contain any dangerous symbols
    if not re.match(r'^[\w\-]+$', cmd):
        print("Invalid command. Only alphanumeric characters, hyphens, and underscores are allowed.")
        return

    # Tokenize the command into a list to prevent shell injections
    cmd = shlex.split(cmd)

    # Execute the command in a secure way without invoking a shell
    try:
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Print the outputs and errors if there are any
        stdout = process.stdout.decode()
        stderr = process.stderr.decode()

        if stdout:
            print("Output: ", stdout)
        if stderr:
            print("Error: ", stderr)

    # Catch and print exception message if an OSError occurs
    except OSError:
        console.log(f"'{cmd}' is not a valid command.")
    
    # Catch and print exception message if command run fails
    except Exception as e:
        print("An error occurred while executing the command: ", str(e))

# Call the function to execute a command
executeCommand()