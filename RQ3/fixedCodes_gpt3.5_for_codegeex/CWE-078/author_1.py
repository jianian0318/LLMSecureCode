import subprocess

def executeCommand():
    command = input("Enter a command: ")
    if not command.strip():
        return "Invalid command"

    try:
        result = subprocess.run(args=command.split(), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr