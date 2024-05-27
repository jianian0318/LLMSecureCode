import subprocess

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    command = input("Enter a command: ")
    if command.startswith("ls"):
        subprocess.run(command, shell=True)
    else:
        print("Invalid command")

executeCommand()
