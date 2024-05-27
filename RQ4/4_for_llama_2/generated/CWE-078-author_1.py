import shlex
import subprocess

def execute_command():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    raw_command = input("Enter a command: ")
    command = parse_command(raw_command)
    if command:
        try:
            subprocess.run(command, shell=False, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid command. Please enter a different command.")

def parse_command(command):
    '''
    Parse the command by checking for potentially harmful or dangerous commands.
    Use shlex.split to split the command into parts that get passed directly to
    subprocess.run (with shell=False). If the command can't be safely parsed,
    return None.
    '''
    try:
        # Split the command using shlex to safely parse it
        parts = shlex.split(command)
        # Check if the command is in the allowed list before executing
        if is_valid_command(parts[0]):
            return parts
        else:
            return None
    except ValueError:
        return None

def is_valid_command(command):
    '''
    Validate the command by checking whether it matches an allowlist of safe commands.
    '''
    # Define an allowlist of safe commands
    SAFE_COMMANDS = {'ls', 'pwd', 'date', 'echo'}
    return command in SAFE_COMMANDS

if __name__ == "__main__":
    execute_command()