import subprocess

def executeCommand():
    """
    Read a command from a user input, validate it, and execute it
    """
    # Get the command input and split it into a list
    command_input = input("Enter a command: ")
    command = command_input.split()
    
    # Only allow 'echo' command to run
    if command[0] == 'echo':
        try:
            # Join the arguments safely and construct the command without using shell=True
            safe_command = ['echo'] + command[1:]
            subprocess.run(safe_command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command execution failed with error {e.returncode}")
    else:
        print("Invalid command. Only 'echo' is allowed.")

if __name__ == "__main__":
    executeCommand()