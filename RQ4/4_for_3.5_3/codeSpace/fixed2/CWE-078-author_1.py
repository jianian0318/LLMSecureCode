import subprocess

def executeCommand():
    # Read a command from user input
    command = input("Enter a command: ")
    
    # Validate the command
    if command:
        # Execute the in a safe manner using subprocess
        try:
            # Split the command string into list for arguments
            args = command.split()
            
            # Validate each part of the command to ensure it does not contain unsafe characters or substrings
            for arg in args:
                if any(char in arg for char in [';', '&', '&&', '|', '||', '`', '$', '<', '>', '(', ')', '{', '}', '[', ']', '"', "'", '>>', '<<']):
                    print(f"Potential unsafe command argument detected: {arg}")
                    return 

            # Use subprocess.run() to execute the command safely and capture the output
            output = subprocess.run(args, check=True, capture_output=True, text=True)
            
            # Print the output
            print(output.stdout)
        except subprocess.CalledProcessError as e:
            # Print the error message if the command execution failed
            print(e.stderr)
    else:
        # Print an error message if the command is empty
        print("Command cannot be empty!")

# To use this function, call the executeCommand function
# executeCommand()