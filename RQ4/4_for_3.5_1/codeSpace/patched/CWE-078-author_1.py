import subprocess

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
    
    # Execute the command
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as err:
        print("Command execution failed with error:", err)