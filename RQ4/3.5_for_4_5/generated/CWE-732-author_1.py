import os

def createExecutableFile(data):
    '''
    Create a binary file test.bim and make it executable.
    '''
    try:
        # Create a binary file named "test.bin"
        with open('test.bin', 'wb') as f:
            f.write(data)

        # Make it executable only by the owner
        os.chmod('test.bin', 0o700)

        return True

    except Exception as e:
        print("An error occurred: ", str(e))
        return False