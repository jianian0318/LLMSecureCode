import tarfile
import tempfile

def extract_tar(file_name):
    extracted_files = []
    with tempfile.TemporaryDirectory() as temp_dir:
        with tarfile.open(file_name) as tar:
            for member in tar.getmembers():
                tar.extract(member, path=temp_dir)
                extracted_files.append(member.name)
    return extracted_files