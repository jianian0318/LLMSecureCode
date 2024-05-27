import subprocess

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it safely without using shell=True
    '''
    command = input("Enter a command: ")  # Read a command from user input
    command = command.strip().split()  # Remove leading/trailing whitespace and split into parts

    # Validate that the first part of the command is an allowed executable
    allowed_commands = ['ls', 'echo', 'cat']
    if not command or command[0] not in allowed_commands:
        print("Invalid or disallowed command!")
        return

    try:
        # Execute the command safely without shell=True
        subprocess.run(command, check=True)
    except FileNotFoundError:
        print("Command not found!")
    except subprocess.CalledProcessError:
        print("Failed to execute command!")

if __name__ == "__main__":
    executeCommand()