import subprocess

def executeCommand():
    # Read a command from user input
    command = input("Enter a command: ")
    
    # Validate the command
    if command:
        # Execute the command using subprocess
        try:
            # Use subprocess.run() to execute the command and capture the output
            output = subprocess.run(command, check=True, shell=True, capture_output=True, text=True)
            
            # Print the output
            print(output.stdout)
        except subprocess.CalledProcessError as e:
            # Print the error message if the command execution failed
            print(e.stderr)
    else:
        # Print an error message if the command is empty
        print("Command cannot be empty!")