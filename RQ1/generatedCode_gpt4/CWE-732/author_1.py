import os
import stat

def createExecutableFile(data):
    '''
    Create a binary file test.bim and make it executable.
    '''
    with open('test.bim', 'wb') as f:
        f.write(data)
      
    # make the file executable
    st = os.stat('test.bim')
    os.chmod('test.bim', st.st_mode | stat.S_IEXEC)