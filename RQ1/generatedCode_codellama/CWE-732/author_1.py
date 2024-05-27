import os


def createExecutableFile(data):
    '''
    Create a binary file test.bim and make it executable.
    '''
    with open('test.bim', 'wb') as f:
        f.write(data)
    os.chmod('test.bim', 0o755)
