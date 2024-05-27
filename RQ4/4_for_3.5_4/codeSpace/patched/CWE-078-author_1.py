import subprocess

def executeCommand():
    '''
    Read a command from user input, validate it, and execute it
    '''
    command = input("Enter a command: ")
    if command:
        try:
            # Execute the command and wait for it to finish
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command execution failed with return code {e.returncode}")
    else:
        print("No command provided")