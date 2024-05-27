import tarfile
import os

def extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents  in the /tmp/ directory
    '''
    # Open the TAR file
    with tarfile.open(file_name) as tar:
        # Iterate over each entry
        for member in tar.getmembers():
            # Extract its contents in the /tmp/ directory
            tar.extract(member, '/tmp/')
    print(f'Extraction of {file_name} Complete') 

# Example usage
# extract_tar('my_tar_file.tar')