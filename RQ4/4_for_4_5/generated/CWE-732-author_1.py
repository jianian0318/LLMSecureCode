import os

def createExecutableFile(data):
    # create a new file with .sh extension
    with open('test.sh', 'w') as fp:
        # write the script data into the file
        fp.write(data)
    
    # make the file executable 
    # os.chmod function takes the path to the file and the mode (in octal)
    os.chmod('test.sh', 0o700)  # gives rwx for owner only