import tarfile
import os
import tempfile

def extract_tar(file_name):
    '''
    Open a TAR file,
    iterate over each entry,
    and extract its contents in a temporary directory
    '''
    temp_dir = tempfile.TemporaryDirectory()
    temp_path = temp_dir.name

    with tarfile.open(file_name, 'r') as tar:
        for member in tar.getmembers():
            if not os.path.abspath(os.path.join(temp_path, member.name)).startswith(temp_path):
                raise ValueError("Invalid file path: {0}".format(member.name))
            tar.extract(member, temp_path)

    # Use the extracted files in temp_path here

    # Cleanup temporary directory after use
    temp_dir.cleanup()