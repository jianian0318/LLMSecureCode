import os

def createExecutableFile(data):
    '''
    Create a binary file test.bim and make it executable.
    '''
    with open('test.bin', 'wb') as file:
        file.write(data)

    # Change the permissions of the file to make it only readable and writable by the owner
    os.chmod('test.bin', 0o700)