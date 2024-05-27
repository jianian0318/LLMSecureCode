import os
import tarfile
import tempfile

def extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents  in the secure temp directory
    '''

    try:
        tar = tarfile.open(file_name)

        temp_dir = tempfile.mkdtemp()
        members = tar.getmembers()

        # Validate members
        for member in members:
            if member.islnk() or member.issym() or '..' in member.name or member.name.startswith('/'):
                return False  # Unsafe member encountered

        # Safely extract files
        for member in validated_members:
            tar.extract(member, path=temp_dir)
        
        return True

    except Exception as e:
        print(f"Unable to extract tar file. Error: {e}")
        return False

    finally:
        tar.close()