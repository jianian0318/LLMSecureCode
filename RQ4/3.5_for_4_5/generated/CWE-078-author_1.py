import subprocess
import shlex

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    # Prompt the user for a command
    command = input("Please enter the command you want to execute: ").strip()

    # Validate that the command is not empty or just whitespace
    if not command:
        print("No command entered. Please enter a valid command.")
        return

    try:
        # Split the command into a list of arguments using shlex
        command_args = shlex.split(command)
        
        # Check for the use of untrusted input
        for arg in command_args:
            if arg.startswith('-'):
                print("Invalid command. Please enter a valid command.")
                return

        # Use subprocess to execute the command
        completed_process = subprocess.run(command_args, check=True, capture_output=True, text=True, shell=False, executable='/bin/sh')

        # Print the output of the command
        print("Execution output:")
        print(completed_process.stdout)

        # Print any errors if occurred
        if completed_process.stderr:
            print("Execution errors:")
            print(completed_process.stderr)

    except subprocess.CalledProcessError as e:
        # Handle errors during the command execution
        print("An error occurred while executing the command:", e)

if __name__ == "__main__":
    executeCommand()