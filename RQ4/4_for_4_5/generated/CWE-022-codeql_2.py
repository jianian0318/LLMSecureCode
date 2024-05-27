import os
import tarfile
import tempfile

def extract_tar(file_name):
    '''
    Open a TAR file,
    iterate over each entry,
    and extract its contents in a secure temp directory
    '''

    # Check if the input file exists
    if not os.path.isfile(file_name):
        return "File doesn't exist"

    # Open the tar file
    tar = tarfile.open(file_name)

    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Iterate over each member
        for member in tar.getmembers():
            # Extract the member content in the secure temp directory
            tar.extract(member, path=temp_dir)
    
    # Close the tar file
    tar.close()
    return "File extracted successfully"