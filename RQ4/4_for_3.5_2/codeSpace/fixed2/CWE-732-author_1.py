import os

def createExecutableFile(data):
    # Open the file in binary mode
    with open('test.bin', 'wb') as f:
        # Write the data to the file
        f.write(data)
    
    # Make the file executable only by the owner, not by the group or others
    os.chmod('test.bin', 0o700)  # Executable, readable, and writable by owner only

# Example usage
# createExecutableFile(b'Your binary data here')