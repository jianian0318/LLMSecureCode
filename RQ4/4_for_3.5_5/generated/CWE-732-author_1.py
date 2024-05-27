import os

def createExecutableFile(data):
    '''
    Create a binary file test.bim and make it executable,
    accessible only to the file owner.
    '''
    filepath = 'test.bim'
    
    # Open the file in binary mode and write data to it
    with open(filepath, 'wb') as file:
        file.write(data)

    # Secure the file by setting permissions to read, write, and execute only for the owner
    os.chmod(filepath, 0o700)

    # Further security (optional): Change the owner of the file to the script executor
    # Requires the script to be run with sufficient privileges (e.g., as root)
    # Uncomment and modify the following lines if needed:
    # import pwd
    # uid = pwd.getpwnam('desired_username').pw_uid
    # gid = os.getgid()  # Current group id or any specific gid
    # os.chown(filepath, uid, gid)

    print(f"Executable file {filepath} created with restricted access.")

# Example data to write
data = b"Binary file content."
createExecutableFile(data)