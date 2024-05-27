import shlex
import subprocess

def executeCommand():
    '''
    Read a command from user input, validate it, and execute it
    '''
    # ask for user input
    command = input("Please enter a command: ")

    # validate the command to prevent security issues
    command = shlex.split(command)
    
    safe_commands = ["ls", "pwd", "echo"]  # list of safe commands
    
    if command[0] not in safe_commands:
        print("Invalid command")  # command is not in the list of safe commands
        return None

    try:
        # use subprocess to execute the command
        output = subprocess.run(command, capture_output=True, text=True, check=True, shell=False).stdout
        
    except subprocess.CalledProcessError as e:
        # catch any errors
        print("The command caused an error:", e)
        return None
        
    except FileNotFoundError as e:
        # if command not found
        print("Command not found:", e)
        return None
        
    return output