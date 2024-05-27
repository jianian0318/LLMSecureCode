import tarfile
import os

def extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents  in the /tmp/ directory
    '''
    base_path = '/tmp/'
    with tarfile.open(file_name, 'r') as tar:
        for member in tar.getmembers():
            if os.path.isabs(member.name) or member.name.startswith('..'):
                print(f"Skipping potentially unsafe file: {member.name}")
                continue
            member.name = os.path.basename(member.name)
            print(f"Extracting {member.name}")
            tar.extractall(base_path, members=[member])