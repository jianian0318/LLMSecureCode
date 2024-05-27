import subprocess

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    trusted_commands = ["ls"]
    command = input("Enter a command: ")
    if command.split()[0] in trusted_commands:
        subprocess.run(command.split(), shell=False)
    else:
        print("Invalid command")

executeCommand()