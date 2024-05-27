import tarfile
import os
import tempfile

def extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents in a temporary directory
    '''
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Open the specified tar file in read mode
        with tarfile.open(file_name, 'r') as tar:
            # Iterate over each member in the tar file
            for member in tar.getmembers():
                # Extract each member to the temporary directory
                tar.extract(member, path=temp_dir)
                print(f"Extracted: {member.name}")
            
# Example usage:
# extract_tar('example.tar')