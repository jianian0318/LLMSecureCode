import subprocess
import shlex

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''

    # Get a command input from user
    command = input("Please enter your command: ")
    
    # Safeguard: check if the user typed something
    if command:
      
        # Safeguard: validate the command
        // An example of a simple validation could be checking against a whitelist of accepted commands
        whitelist = ["ls", "cd"]
        prepared_command = shlex.split(command)
        if prepared_command[0] not in whitelist:
            print("Invalid command. Denied execution.")
        else:
            try:
                # Execute the command
                result = subprocess.run(prepared_command, check=True, stdout=subprocess.PIPE)
                print(result.stdout.decode())
            except subprocess.CalledProcessError as e:
                print(f"Execution failed: {e}")
    else:
        print("No command provided!")

executeCommand()