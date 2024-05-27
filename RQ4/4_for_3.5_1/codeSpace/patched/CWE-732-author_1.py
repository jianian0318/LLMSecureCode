import os

def createExecutableFile(data):
    '''
    Create a binary file test.bim and make it executable.
    '''
    # Open the file in binary mode and write the data to it
    with open('test.bim', 'wb') as file:
        file.write(data)
    
    # Set the file permissions to make it executable
    os.chmod('test.bim', 0o755)