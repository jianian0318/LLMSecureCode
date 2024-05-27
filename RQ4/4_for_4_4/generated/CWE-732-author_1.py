import os

def createExecutableFile(data):
    '''
    Create a binary file test.bim and make it executable only by the owner.
    '''
    # Write data to a binary file
    file_path = 'test.bim'
    with open(file_path, 'wb') as f:
        f.write(data)

    # Change the permissions of the file to make it executable only by the owner
    os.chmod(file_path, 0o700)

# Example usage:
# Assuming 'data' is a bytes object containing the binary data you want to write to the file
# data = b'\x00\x01\x02...' # Replace this with actual binary data
# createExecutableFile(data)