import subprocess
import shlex

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''

    # Whitelisted commands
    WHITELIST = ['ls', 'cd', 'pwd', 'top', 'date', 'whoami']

    # Get command from user
    command = input('Enter the command you want to execute: ')

    # Validate command
    # Real command validation should depend on the actual commands you're expecting and should be more thorough.
    if command is None or command.strip() == '':
        print('Command cannot be empty.')
        return

    # Split the command into a list using shlex
    # This safely preserves command arguments if there are spaces in the arguments
    command_list = shlex.split(command)

    # Make sure the base command is in the whitelist
    if command_list[0] not in WHITELIST:
        print('Command not recognized or not allowed.')
        return

    # Execute the command
    try:
        # It's more secure to use subprocess.run; it's recommended over subprocess.check_output
        result = subprocess.run(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print('Command executed successfully: \n', result.stdout)
        else:
            print('Command resulted in an error: \n', result.stderr)
    except subprocess.CalledProcessError as e:
        print('Error occurred while executing the command: ', e)

# Note: 'cd' command won't work as expected because each subprocess call creates a new shell session.
executeCommand()