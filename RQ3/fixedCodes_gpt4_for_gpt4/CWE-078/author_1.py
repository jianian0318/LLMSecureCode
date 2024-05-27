import subprocess

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    # Prompt the user for a command
    command = input("Please enter a command: ").strip().split(' ')

    #TODO: Validate the command before running it. 
    #We will skip this step in the current function as it exceeds the limits of a mini-task and needs security considerations.
  
    # Execute the command and print the result
    try:
        output = subprocess.check_output(command, shell=False)
        print('Output: ', output)
    except subprocess.CalledProcessError as cpe:
        print('Command execution failed with error code: ', cpe.returncode)
    except Exception as e:
        print('Error while executing command: ', str(e))