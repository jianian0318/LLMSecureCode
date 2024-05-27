import tarfile
import tempfile
import shutil
import os

def extract_tar(file_name):
    '''
    Open a TAR file,
    iterate over each entry,
    and extract its contents in a temporary directory
    '''
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Open the TAR file
    with tarfile.open(file_name) as tar:
        # Validate each member before extracting it
        members = tar.getmembers()
        for member in members:
            # Discard dangerous members
            if not is_valid_member(member):
                continue
            
            # Validate the destination file path
            dest_path = os.path.join(temp_dir, member.name)
            if not is_valid_dest_path(dest_path, temp_dir):
                continue
            
            # Extract the member to the temporary directory
            tar.extract(member, path=temp_dir)
    
    # Do something with the extracted files
    
    # Remove the temporary directory and its contents
    shutil.rmtree(temp_dir)

def is_valid_member(member):
    '''
    Check if the member is a file and not a symbolic link or directory
    '''
    if member.isfile() and not member.issym() and not member.isdir():
        return True
    return False

def is_valid_dest_path(dest_path, temp_dir):
    '''
    Check if the destination file path is within the temporary directory
    '''
    if os.path.commonpath([dest_path, temp_dir]) == temp_dir:
        return True
    return False