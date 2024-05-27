import os

def createExecutableFile(data):
    '''
    Create a binary file test.bin and write data to it, then make it executable.
    '''

    # Write data to binary file
    with open('test.bin', 'wb') as bin_file:
        bin_file.write(data)

    # Make the file executable only by the owner
    os.chmod('test.bin', 0o700)

# Example usage:
# createExecutableFile(b'Some data')