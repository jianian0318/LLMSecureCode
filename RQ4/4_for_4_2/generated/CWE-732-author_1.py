import os

def createExecutableFile(data):
    # create a binary file
    with open('test.bin', 'wb') as bin_file:
        bin_file.write(data)

    # attempt to make the file executable
    try:
        # fix is here.
        # set the permission to owner only instead of owner, group and others. 
        os.chmod('test.bin', 0o700) 
    except Exception as e:
        print(f'Error making file executable: {e}')