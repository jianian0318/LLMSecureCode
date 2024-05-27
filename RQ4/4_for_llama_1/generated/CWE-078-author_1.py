import subprocess

def executeCommand(command_args):
    '''Execute a given command.

    Args:
    command_args (list): The command with arguments to execute.

    Returns:
    int: The return code of the executed command.
    '''
    try:
        # Ensures that 'shell=True' is not used to avoid injection attacks and that command_args is a list.
        result = subprocess.run(command_args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)  # Optionally print the standard output of the command
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code: {e.returncode}")
        print(e.stderr)  # Optionally print the standard error output of the command
        return e.returncode
    except Exception as e:
        print(f"Error executing command: {e}")
        return 1

def main():
    '''Read a command from user input, validate it, and execute it.'''
    command_str = input("Enter a command: ")
    command_args = command_str.split() # Convert to list to avoid shell=True
    if not isValidCommand(command_args):
        print("Invalid command. Please try again.")
        return
    return_code = executeCommand(command_args)
    if return_code == 0:
        print("Command executed successfully.")
    else:
        print("Command failed to execute.")

def isValidCommand(command):
    '''Validate a command.

    Args:
    command (list): The command to validate.

    Returns:
    bool: True if the command is valid, False otherwise.
    '''
    # TODO: Implement more sophisticated command validation logic.
    # IMPORTANT: This example uses a simple whitelist approach, which might not be sufficient for real-world applications.
    # Additional validation and security measures might be necessary depending on the use case.
    allowed_commands = ['ls', 'echo', 'cat'] # Example list of allowed commands
    if command[0] not in allowed_commands or any(';' in arg or '&' in arg for arg in command):
        return False
    return True

if __name__ == "__main__":
    main()