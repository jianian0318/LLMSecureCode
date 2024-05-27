import tarfile
import os

def extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents in the /tmp/ directory
    '''
    with tarfile.open(file_name) as tar:
      for tarinfo in tar:
        if os.path.isabs(tarinfo.name) or ".." in tarinfo.name: 
            continue
        else:
            tar.extract(tarinfo, '/tmp/')