import os
import tarfile
import tempfile

def is_within_directory(file_path, directory):
    # Normalize paths to absolute version for accurate comparison
    absolute_path = os.path.abspath(file_path)
    absolute_directory = os.path.abspath(directory)
    common_prefix = os.path.commonpath([absolute_path, absolute_directory])
    return common_prefix == absolute_directory

def securely_extract_tar(file_name, dir_path):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents securely in a given directory
    '''
    # Ensure the directory exists and is a secure temp directory
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path, exist_ok=True)
        
    with tarfile.open(file_name, 'r') as tar:
        # Check each member for safety before extraction
        for member in tar.getmembers():
            member_path = os.path.join(dir_path, member.name)
            if is_within_directory(member_path, dir_path):
                tar.extract(member, path=dir_path)
            else:
                print(f"Skipping potentially unsafe tar entry: {member.name}")

# Example usage:
with tempfile.TemporaryDirectory() as tmpdirname:
    securely_extract_tar('example.tar', tmpdirname)