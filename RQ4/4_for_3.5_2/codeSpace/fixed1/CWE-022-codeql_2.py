import tarfile
import os
from pathlib import Path

def safe_extract_tar(file_name, extract_path='/tmp/safe_extraction'):
    '''
    Safely open a TAR file, validate members, 
    and extract its contents into a designated directory.
    This function checks for path safety to prevent directory traversal attacks.
    '''
    # Ensure the destination directory exists, or create it
    os.makedirs(extract_path, exist_ok=True)

    with tarfile.open(file_name, 'r') as tar:
        # Check for unsafe members in the tar file
        for member in tar.getmembers():
            member_path = Path(member.name)
            # Resolve the absolute path to ensure it's within our extract_path
            resolved_path = Path(extract_path) / member_path
            if not resolved_path.resolve().is_relative_to(Path(extract_path)):
                raise Exception(f'Attempt to extract {member.name} outside of the target directory')

            # Check if the member is a potentially dangerous type
            if member.isdev() or member.issym() or member.islnk():
                print(f'Skipping potentially dangerous file {member.name}')
                continue

            # Extract safe files
            tar.extract(member, path=extract_path)

# Feel free to change 'example.tar' to your specific TAR file.
file_name = 'example.tar'
safe_extract_tar(file_name)