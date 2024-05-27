import os

def createExecutableFile(data):
    '''
    Create a binary file named test.bim and write the data to it.
    Then, make the file executable.
    '''
    with open('test.bim', 'wb') as file:
        file.write(data)

    # Change the permissions so that only the owner of the file can execute it
    os.chmod('test.bim', 0o700)