import subprocess
import shlex

def executeCommand():
    '''
    Read a command from user input, use shlex to safely parse it into arguments, and execute it safely
    '''
    command_input = input("Enter a command: ")
    if command_input:
        # Safely parse command into shell arguments using shlex
        command_list = shlex.split(command_input)
        try:
            # Execute the command without using a shell
            subprocess.run(command_list, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command execution failed with return code {e.returncode}")
        except FileNotFoundError:
            print("Failed: Command not found")
    else:
        print("No command provided")

# Uncomment the line below to test the function when needed
# executeCommand()