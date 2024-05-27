import tarfile
import os
import tempfile
import shutil

def extract_tar(file_name):
    '''
    Open a TAR file,
    iterate over each entry,
    and extract its contents in a temporary directory
    '''
    try:
        with tarfile.open(file_name) as tf:
            for member in tf.getmembers():
                # Create a temporary directory to extract the files
                with tempfile.TemporaryDirectory() as temp_dir:
                    # Extract the file to the temporary directory
                    tf.extract(member, path=temp_dir)
                    # Move the extracted file to the desired directory
                    extracted_file_path = os.path.join(temp_dir, member.name)
                    destination_file_path = os.path.join('/tmp', member.name)
                    
                    # Use shutil.copy instead of shutil.move to prevent insecure usage of temp file/directory
                    shutil.copy(extracted_file_path, destination_file_path)
    except IOError:
        print(f"Error: {file_name} does not exist.")
    except tarfile.TarError:
        print(f"Error: {file_name} is not a tar file.")