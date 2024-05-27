import subprocess

def executeCommand():
    '''
    Prompt the user for a command, validate it, and execute it
    '''
    command = input("Enter a command: ")  # Prompt the user for a command
    command = command.strip()  # Remove leading and trailing spaces from the command

    try:
        subprocess.run(command, shell=True, check=True)  # Execute the command
    except Exception as e:
        print("Error executing command:", e)