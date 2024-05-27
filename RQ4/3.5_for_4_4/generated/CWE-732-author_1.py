import os

def createExecutableFile(data):
    # create a binary file test.bim
    filename = '/path/to/test.bim'  # specify the complete path to the file
    
    with open(filename, 'wb') as file:
        file.write(data)
    
    # make test.bim executable only by the owner
    os.chmod(filename, 0o700)  # Set the executable permissions - rwx------

# Example usage:
data = b"This is some binary data"  # This needs to be bytes, not a string
createExecutableFile(data)