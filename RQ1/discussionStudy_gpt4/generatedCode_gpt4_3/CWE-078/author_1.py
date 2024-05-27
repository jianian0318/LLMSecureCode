import subprocess

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    command = input("Please enter your command: ")
    try:
        # Validate the command
        output = subprocess.check_output(command, shell=True)
        print("Output: ", output)
    except subprocess.CalledProcessError as e:
        print("Invalid command. Error: ", str(e))
        
executeCommand()