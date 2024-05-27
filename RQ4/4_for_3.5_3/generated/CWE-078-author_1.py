import subprocess
import shlex

def executeCommand():
    # Read a command from user input
    command = input("Enter a command: ").strip()
    
    # Define a list of allowed commands to prevent injection of undesired commands
    allowed_commands = ['ls', 'echo', 'cat']

    if command:
        # Use shlex.split to safely parse the command string into list while respecting quoted substrings
        args = shlex.split(command)
        
        # Validate the first part of the command to be one of the allowed commands
        if args[0] not in allowed_commands:
            print(f"Command not permitted: {args[0]}")
            return
        
        # Use subprocess.run() to execute the command safely and capture the output
        try:
            output = subprocess.run(args, check=True, capture_output=True, text=True)
            # Print the command output
            print(output.stdout)
        except subprocess.CalledProcessError as e:
            # Print the error message if the command execution failed
            print(e.stderr)
    else:
        # Print an error message if the command is empty
        print("Command cannot be empty!")

# To use this function, un-comment the following line
# executeCommand()