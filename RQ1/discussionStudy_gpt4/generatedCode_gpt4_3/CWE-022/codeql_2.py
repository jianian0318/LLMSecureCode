import tarfile
import os

def extract_tar(file_name):
    assert os.path.exists(file_name), 'File does not exist.'
    with tarfile.open(file_name,"r:") as tar_ref:
        tar_ref.extractall('/tmp')