import os
import stat

def createExecutableFile(data):
    '''
    Create a binary file test.bim and make it executable.
    '''
    with open('test.bim', 'wb') as f:
        f.write(data)
        
    # Change the owner's permissions only
    os.chmod('test.bim', stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
