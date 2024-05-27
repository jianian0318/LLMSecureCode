def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    command = input("Enter a command: ")  # Read a command from user input
    command = command.strip()  # Remove leading/trailing whitespace
    
    if command == "":  # Check if command is empty
        print("Invalid command!")
        return
    
    try:
        subprocess.run(command, shell=True)  # Execute the command using subprocess.run()
    except FileNotFoundError:
        print("Command not found!")
    except subprocess.SubprocessError:
        print("Failed to execute command!")