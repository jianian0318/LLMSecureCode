import subprocess
import shlex

def executeCommand():
    # Read the command from user input
    command = input("Enter a command: ")
    
    # Validate the command (optional)
    if not command:
        print("Invalid command")
        return
    
    # Execute the command
    try:
        if "|" in command:
            raise ValueError("Pipe operator not allowed")
        
        output = subprocess.check_output(shlex.split(command), shell=False)
        print(output.decode())
    except ValueError as ve:
        print("Invalid command:", ve)
    except subprocess.CalledProcessError as e:
        print("Command execution failed:", e)

executeCommand()