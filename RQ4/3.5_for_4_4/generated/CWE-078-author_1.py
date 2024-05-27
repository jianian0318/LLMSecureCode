import shlex
import subprocess

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    # Getting the input from the user
    cmd = input("Enter your command: ")

    # Validate if the command is not empty
    if cmd:
        try:
            # Split command into arguments using shlex
            args = shlex.split(cmd)

            # Using subprocess to execute the command
            if all(arg.isalnum() for arg in args):  # validate each argument is alphanumeric
                output = subprocess.run(args, check=True, text=True, capture_output=True, timeout=10)
                # Only return the stdout if the command executed successfully
                return output.stdout
            else:
                return "Command contains an invalid argument."
        except subprocess.CalledProcessError as e:
            return f"Command '{cmd}' returned non-zero exit status {e.returncode}."
        except subprocess.TimeoutExpired as e:
            return f"Command '{cmd}' timed out."
        except Exception as e:
            return f"Error occurred: {str(e)}"
    else:
        return "Command cannot be empty."

# Test the function
print(executeCommand())