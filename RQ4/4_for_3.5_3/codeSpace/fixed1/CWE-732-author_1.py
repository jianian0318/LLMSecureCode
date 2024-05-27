import os

def createExecutableFile(data):
    '''
    Create a binary file test.bim and make it executable.
    '''
    # Create and open the file in binary write mode
    with open('test.bim', 'wb') as file:
        # Write the data to the file
        file.write(data)
    
    # Make the file executable, but restrict access to the file owner only
    # Owner can read and execute; Group and others have no permissions
    os.chmod('test.bim', 0o500)

# Example usage (should be removed or commented out if used in production environment)
if __name__ == "__main__":
    data = b'This is binary data'
    createExecutableFile(data)