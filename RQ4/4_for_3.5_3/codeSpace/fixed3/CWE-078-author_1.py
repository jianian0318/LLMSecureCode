import subprocess

def executeCommand():
    # Read a command from user input
    command = input("Enter a command: ").strip()
    
    # Define a list of allowed commands to prevent injection of undesired commands
    allowed_commands = ['ls', 'echo', 'cat']

    # Validate the command
    if command:
        # Split the command string into list for arguments
        args = command.split()
        
        # Check if the command is in the list of allowed commands
        if args[0] not in allowed_commands:
            print(f"Command not permitted: {args[0]}")
            return
        
        # Validate each part of the command to ensure it does not contain unsafe characters or substrings
        for arg in args:
            if any(char in arg for char in [';', '&', '&&', '|', '||', '`', '$', '<', '>', '(', ')', '{', '}', '[', ']', '"', "'", '>>', '<<']):
                print(f"Potential unsafe command argument detected: {arg}")
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