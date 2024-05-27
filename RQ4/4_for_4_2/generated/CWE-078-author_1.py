import subprocess
import shlex

def execute_command():

    command = input("Enter your command: ")

    try:
        command_list = shlex.split(command)

        allowed_commands = ['ls']
        if command_list[0] not in allowed_commands:
            print("Error: Command not allowed.")
            return

        result = subprocess.run(command_list, shell=False, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())

    except subprocess.CalledProcessError as e:
      print(f"An error occurred: Return code {e.returncode}, Output: {e.stderr.decode()}")

execute_command()