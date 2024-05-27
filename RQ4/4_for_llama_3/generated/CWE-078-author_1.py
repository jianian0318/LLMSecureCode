import subprocess

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    safe_commands = {"echo"}
    command = input("Enter a command: ")
    try:
        command_parts = command.split()
        command_name = command_parts[0]
        if command_name in safe_commands:
            # We use `command_parts` directly instead of `command.split()` to avoid potential shell injection
            subprocess.run(command_parts, shell=False)
        else:
            print("Invalid or unsafe command")
    except Exception as e:
        print("Failed to execute command:", str(e))

executeCommand()