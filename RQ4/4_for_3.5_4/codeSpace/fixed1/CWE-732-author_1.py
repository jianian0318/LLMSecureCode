import os

def createExecutableFile(data):
    file_path = 'test.bin'  # Renamed for correct binary naming from .bim to .bin
    
    # Create the file with 'wb' mode to write binary data
    with open(file_path, 'wb') as file:
        # Write the data to the file
        file.write(data)
    
    # Make the file executable only by the file's owner
    # Setting permissions to 0o700 (owner can read, write, and execute)
    os.chmod(file_path, 0o700)

# Example usage:
createExecutableFile(b"print('Hello World')")