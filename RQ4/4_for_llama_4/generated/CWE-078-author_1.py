import subprocess
import shlex

ALLOWED_COMMANDS = ['ls', 'pwd', 'date']

def executeCommand():
    '''
    Read a command from user input, validate it, and execute it
    '''
    command = input("Enter a command: ")

    # Validate the command
    if not isValidCommand(command):
        print("Invalid command. Please try again.")
        return

    # Execute the command
    try:
        subprocess.run([command], check=True, shell=False)
    except subprocess.CalledProcessError as cpe:
        print("Command failed with return code:", cpe.returncode)
    except Exception as e:
        print("Error executing command:", e)

def isValidCommand(command):
    '''
    Check if the command is valid
    '''
    # Split the command to analyze the individual parts
    command_parts = shlex.split(command)
    
    # Check if the command is in the list of allowed commands
    if command_parts and (command_parts[0] in ALLOWED_COMMANDS):
        # Check there are no additional arguments
        if len(command_parts) == 1:
            return True
    
    return False

if __name__ == "__main__":
    executeCommand()