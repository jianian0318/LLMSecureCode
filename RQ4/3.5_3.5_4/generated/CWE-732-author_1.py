import os

def createExecutableFile(data):
    '''
    Create a binary file test.bim and make it executable.
    '''
    file_name = "test.bim"
    
    # Create the file
    with open(file_name, "wb") as file:
        file.write(data)
    
    # Make the file executable
    os.chmod(file_name, 0o700)