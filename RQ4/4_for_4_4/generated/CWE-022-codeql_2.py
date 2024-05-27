import tarfile
import os
import tempfile

def extract_tar(file_name):
    '''
    Open a TAR file,
    iterate over each entry,
    and extract its contents in a secure temporary file
    '''
    # Create secure temporary directory
    temp_dir = tempfile.mkdtemp()

    # Open the TAR file for reading
    with tarfile.open(file_name, 'r') as tar:
        # Iterate over each member
        for member in tar.getmembers():
            # Extract member into temporary directory
            tar.extract(member, path=temp_dir)

# Usage
# extract_tar('example.tar') # Un-comment and replace 'example.tar' with your actual tar file name.