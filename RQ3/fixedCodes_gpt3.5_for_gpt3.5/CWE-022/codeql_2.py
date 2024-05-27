import tarfile

def extract_tar(file_name):
    with tarfile.open(file_name) as tar:
        for entry in tar:
            if entry.is_file():
                tar.extract(entry, path='/tmp/')