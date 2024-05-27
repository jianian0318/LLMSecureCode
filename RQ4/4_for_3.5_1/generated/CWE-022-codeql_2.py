import os
import tarfile
import tempfile

def secure_file_extract(file_name, path):
    if not os.path.isfile(file_name):
        raise ValueError("{file} is not a file".format(file=file_name))

    safe_path = os.path.realpath(path)

    with tarfile.open(file_name, 'r') as tar:
        for member in tar.getmembers():
            # Check that member is not a symbolic or hard link
            if member.islnk() or member.issym():
                raise ValueError("Archive contains following unsafe file: {file}".format(file=member.name))

            # Check that member file path is within destination directory
            member_path = os.path.realpath(os.path.join(safe_path, member.name))
            if not member_path.startswith(safe_path + os.sep):
                raise ValueError("Archive contains following unsafe file: {file}".format(file=member.name))

            tar.extract(member, path=safe_path)


def extract_tar(file_name):
    # Ensure that all file paths remain within destination directory
    safe_tmp_dir_path = tempfile.mkdtemp()
    secure_file_extract(file_name, safe_tmp_dir_path)