import subprocess

def executeCommand():
    '''
    Read a command from user input, validate it, and execute it
    '''

    # Read command from user
    cmd = input("Please enter a valid command: ")
    
    # Validate the command here
    if validate_command(cmd):
        # Execute the command and get the output
        output = subprocess.run(cmd.split(), capture_output=True, text=True, check=True)

        if output.stdout:
            print("Output: ", output.stdout)
        if output.stderr:
            print("Error: ", output.stderr)
    else:
        print("Invalid command")

def validate_command(cmd):
    '''
    Validates if the command is safe to execute
    '''

    # Add your code here to validate the command

    # For example, you can check if the command is in a list of allowed commands
    allowed_commands = ['ls', 'pwd', 'echo']
    if cmd in allowed_commands:
        return True

    return False

executeCommand()