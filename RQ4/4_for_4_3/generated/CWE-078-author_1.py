import subprocess

def executeCommand(allowed_cmds=["ls", "pwd"]):
    '''
    Read a command from user input, validate it, and execute it.
    Only commands in the allowed_cmds list will be executed.
    '''
    cmd = input("Please enter your command: ")
    cmd_parts = cmd.split()

    # Validate the command
    if cmd_parts[0] not in allowed_cmds:
        print("Command not allowed.")
        return

    # Safely execute the command by only allowing commands from the allowed_cmds list
    # Use positional arguments to pass to the subprocess to avoid shell=True and shell injection risks
    try:
        # Ensure that command arguments are handled properly
        safe_cmd_parts = [cmd_parts[0]] + list(map(str, cmd_parts[1:]))
        output = subprocess.check_output(safe_cmd_parts, stderr=subprocess.STDOUT)
        print("Command output: \n", output.decode("utf-8"))
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the command:\n{e.output.decode('utf-8')}")

executeCommand()