import subprocess

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    command_input = input("Enter your command: ")

    try:
        # validate the command
        command = command_input.split()
        if not command:
            print("You did not enter anything.")
            return
        
        # execute command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        print("Output: ", stdout.decode())
        print("Error (if any): ", stderr.decode())
        
    except Exception as ex:
        print("An exception occurred: ", ex)

executeCommand()