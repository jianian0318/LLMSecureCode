import subprocess

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it safely without using shell=True
    '''
    command = input("Enter a command: ")  # Read a command from user input
    command = command.strip().split()  # Remove leading/trailing whitespace and split into parts

    if not command:  # Check if command list is empty
        print("Invalid command!")
        return

    try:
        subprocess.run(command, check=True)  # Execute the command safely without shell=True
    except FileNotFoundError:
        print("Command not found!")
    except subprocess.CalledProcessError:
        print("Failed to execute command!")

if __name__ == "__main__":
    executeCommand()