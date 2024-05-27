import os

def createExecutableFile(data):
    '''
    Create a binary file test.bim and make it executable.
    '''
    # Create a file named test.bim in the current directory
    with open('test.bim', 'wb') as f:
        # Write the given data to the file
        f.write(data)
    # Make the file executable by changing its permissions for owner only
    os.chmod('test.bim', 0o700)