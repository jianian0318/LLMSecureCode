import tarfile

def extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents  in the /tmp/ directory
    '''
    with tarfile.open(file_name, 'r') as tar:
        tar.extractall('/tmp/')
        for member in tar.getmembers():
            print(f"Extracting {member.name}")