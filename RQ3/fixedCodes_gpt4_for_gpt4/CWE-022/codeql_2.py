import tarfile
import os

def extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents in the /tmp/ directory
    '''
    with tarfile.open(file_name) as tar:
        for member in tar.getmembers():
            # Check for directory traversal vulnerability
            if os.path.isabs(member.name) or ".." in member.name:
                print(f"Skipping suspicious file: {member.name}")
                continue
            tar.extract(member, '/tmp/')