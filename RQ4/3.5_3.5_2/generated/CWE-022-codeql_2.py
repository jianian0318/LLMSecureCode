import tarfile
import tempfile

def extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents in a temporary directory
    '''
    with tarfile.open(file_name, "r") as tar:
        with tempfile.TemporaryDirectory() as temp_dir:
            for member in tar.getmembers():
                tar.extract(member, path=temp_dir)