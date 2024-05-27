import subprocess
import shlex

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    command = input("Please input the command to execute: ")  # Read command from user
    try:
        args = shlex.split(command) # Tokenize the command string
        
        # Validate command before executing
        allowed_commands = ('ls', 'cd', 'echo', 'cat') # Specify allowed commands
        if any(command.startswith(prefix) for prefix in allowed_commands):
            # Execute the validated command
            result = subprocess.run(args, stdout=subprocess.PIPE)
            print(result.stdout.decode())  # Print the results
        else:
            print("Invalid command") # If the command is not allowed, print an error message
    except Exception as e:
        print("Error occurred:", e)  # If something goes wrong, print the error