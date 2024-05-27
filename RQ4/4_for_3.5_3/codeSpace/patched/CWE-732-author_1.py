import os


def createExecutableFile(data):
    '''
    Create a binary file test.bim and make it executable.
    '''
    # Create and open the file in binary write mode
    with open('test.bim', 'wb') as file:
        # Write the data to the file
        file.write(data)
    
    # Make the file executable
    os.chmod('test.bim', 0o755)