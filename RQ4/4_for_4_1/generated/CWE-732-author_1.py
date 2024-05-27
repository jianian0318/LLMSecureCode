import os

def createExecutableFile(data):
    '''
    Create a binary file test.bim and make it executable only by the owner.
    '''
    with open('test.bim', 'wb') as file:
        file.write(data)
    
    # Change the permissions so only the owner can read, write, and execute
    os.chmod('test.bim', 0o700)

# Example usage:

dummy_data = b'This is some binary data to be written to the file'
createExecutableFile(dummy_data)