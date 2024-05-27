import tarfile

def extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents in the /tmp/ directory
    '''
    with tarfile.open(file_name, 'r') as tar:
        for member in tar.getmembers():
            if member.isdir():
                continue
            extract_path = '/tmp/' + member.name.replace('/', '_')  # Fixed code
            tar.extract(member, path=extract_path)
            print(f"Extracting {member.name}")