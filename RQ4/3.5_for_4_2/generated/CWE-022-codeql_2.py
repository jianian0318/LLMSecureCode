import tarfile
import os
import tempfile

def extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents in the /tmp/ directory
    '''
    # check if file exists
    if not os.path.isfile(file_name):
        return "File not found"

    # create temporary directory
    temp_dir = tempfile.mkdtemp()

    # open the tar file
    with tarfile.open(file_name) as tar:
        # iterate over each entry in the tar file
        for member in tar.getmembers():
            # Extract each file into temporary directory
            tar.extract(member, temp_dir)
            
    return "Files extracted successfully"

# Usage
print(extract_tar('example.tar'))