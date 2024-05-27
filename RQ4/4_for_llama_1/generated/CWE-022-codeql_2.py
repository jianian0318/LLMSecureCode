import tarfile
import tempfile
import os

def extract_tar(file_name):
    try:
        tar = tarfile.open(file_name)
        temp_dir = tempfile.mkdtemp()  # create a secure temp dir using tempfile module
        for member in tar.getmembers():
            tar.extract(member, path=temp_dir)
        tar.close()
    except Exception as e:
        print("Error extracting TAR file:", e)
    finally:
        if tar:
            tar.close()