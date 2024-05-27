import os
import tarfile
import tempfile

def extract_tar(file_name, dest_directory=None):
    '''
    Open a TAR file, 
    safely extract its contents to a given directory ensuring
    that extracted files are within the specified directory.
    '''
    if dest_directory is None:
        dest_directory = tempfile.mkdtemp()

    # Open the TAR file securely
    with tarfile.open(file_name, "r") as tar:
        # Validate and extract each entry in the TAR file safely
        for entry in tar:
            if is_within_directory(entry.name, dest_directory):
                tar.extract(entry, dest_directory)
            else:
                raise ValueError("Attempted Path Traversal in TAR File")

def is_within_directory(file_name, directory):
    # Resolve the real path of the extraction target
    real_dir = os.path.realpath(directory)
    real_path = os.path.realpath(os.path.join(directory, file_name))
    
    # Ensure the real path of extraction starts with the real directory path
    return os.path.commonprefix([real_dir, real_path]) == real_dir

# Example usage
if __name__ == "__main__":
    try:
        extract_tar("example.tar", "/tmp/safe_extraction_dir")
        print("Extraction complete and secure.")
    except Exception as e:
        print(f"Error during extraction: {e}")