import os
import tarfile

def safe_extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents in the /tmp/ directory
    '''
    with tarfile.open(file_name) as tar:
        for member in tar.getmembers():
            if os.path.commonprefix(('/tmp/', os.path.abspath(member.name))) == '/tmp/':
                tar.extract(member, '/tmp/')