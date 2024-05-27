import subprocess
import shlex

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it.
    '''
    command = input("Enter a command: ")
    if not command.strip():
        return "Invalid command"

    try:
        # split the command string into a sequence.
        command = shlex.split(command)
        result = subprocess.run(command, shell=False, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr