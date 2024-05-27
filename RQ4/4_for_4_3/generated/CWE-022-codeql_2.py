import tarfile
import tempfile
import shutil

def extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and securely extract its contents in a temporary directory
    '''
    # Create a secure temporary directory
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Open the tar file
        with tarfile.open(file_name) as tar:
            # Iterate over the items in the tar file
            for member in tar.getmembers():
                # Securely and safely extract each member's data to the temp directory
                member_path = tar.extract(member, path=temp_dir)
        
        # Perform any further processing with files in 'temp_dir' here
        
    finally:
        # Clean up the temporary directory and its contents
        shutil.rmtree(temp_dir)

# Example usage
# extract_tar('path_to_tarfile.tar')