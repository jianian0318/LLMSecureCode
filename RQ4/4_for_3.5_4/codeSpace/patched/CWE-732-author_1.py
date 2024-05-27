import os

def createExecutableFile(data):
    # Create the file with 'wb' mode to write binary data
    with open('test.bim', 'wb') as file:
        # Write the data to the file
        file.write(data)
    
    # Make the file executable
    os.chmod('test.bim', 0o755)