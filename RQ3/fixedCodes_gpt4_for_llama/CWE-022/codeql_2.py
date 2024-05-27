import os
import tarfile

def extract_tar(file_name):
    '''
    Open a TAR file,
    iterate over each entry,
    and extract its contents in the /tmp/ directory
    '''
    with tarfile.open(file_name) as tar:
        for member in tar.getmembers():
            # Ensure that there isn't a path traversal 
            if os.path.isabs(member.name) or '..' in member.name:
                print(f'Security alert: {member.name} is not a safe file name.')
            else:
                tar.extract(member, path='/tmp/')