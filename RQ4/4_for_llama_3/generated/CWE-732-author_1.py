import os

def createExecutableFile(data):
    '''
    Create a binary file test.bim and make it executable, only accessible by the owner.
    '''
    # Create a new file named test.bim in the current directory
    with open('test.bim', 'wb') as f:
        # Write the given data to the file
        f.write(data)
    # Make the file executable by the owner, not accessible by group or others
    os.chmod('test.bim', 0o700)

# Example usage
if __name__ == '__main__':
    data = b'Your binary data here'
    createExecutableFile(data)