import os

def createExecutableFile(data):
    # Open the file in binary mode
    with open('test.bim', 'wb') as f:
        # Write the data to the file
        f.write(data)
        
    # Make the file executable with more restrictive permissions
    os.chmod('test.bim', 0o755)  # Executable by owner, read and execute for others

# Example usage
# createExecutableFile(b'Your binary data here')