import os
import stat

def createExecutableFile(data):
    '''
    Create a binary file test.bim.
    '''
    
    # Open the file in binary write mode
    with open('test.bim', 'wb') as file:

        # Write the data to the file
        file.write(data)
        
    # Change the file permissions to read and execute only to the user.
    os.chmod('test.bim', stat.S_IRUSR | stat.S_IXUSR)