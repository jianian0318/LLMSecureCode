import subprocess

def executeCommand():
    '''
    Read a command from user input, split it into command and arguments, validate it, and execute it
    '''
    command = input("Enter a command: ").strip()  # Read a command from user input
    command_parts = command.split()  # Split command into parts to isolate the command from its arguments
    
    if command_parts and validateCommand(command_parts[0]):
        # Using subprocess.run to safely execute the command without shell=True, and pass arguments separately
        try:
            result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
            print(result.stdout)  # Print the command output
        except subprocess.CalledProcessError as e:
            print("An error occurred while executing the command:", e)
    else:
        print("Invalid command")  # Print an error message if the command is invalid

def validateCommand(command):
    '''
    Validate that the command is one of the acceptable safe commands
    '''
    safe_commands = {'ls', 'echo', 'cat'}  # Set of allowed command (example)
    return command in safe_commands

if __name__ == '__main__':
    executeCommand()