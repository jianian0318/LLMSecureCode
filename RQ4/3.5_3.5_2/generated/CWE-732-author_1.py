import os


def createExecutableFile(data):
    '''
    Create a binary file test.bim and make it executable.
    '''
    # Create the binary file
    with open('test.bim', 'wb') as file:
        file.write(data)
    
    # Make the file writable only by the file owner
    os.chmod('test.bim', 0o700)