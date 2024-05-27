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

    # Ensure the destination directory exists
    os.makedirs(dest_directory, exist_ok=True)

    # Open the TAR file securely
    with tarfile.open(file_name, "r") as tar:
        # Validate and extract each entry in the TAR file safely
        for entry in tar:
            extracted_path = os.path.join(dest_directory, entry.name)
            # Create directory structure within specified destination directory only
            if entry.isdir():
                os.makedirs(extracted_path, exist_ok=True)
            else:
                # Before extracting files, validate paths to prevent directory traversal
                if is_within_directory(extracted_path, dest_directory):
                    tar.extract(entry, dest_directory)
                else:
                    raise ValueError("Attempted Path Traversal in TAR File")

def is_within_directory(file_path, directory):
    # Resolve the real path of the extraction target
    real_dir = os.path.realpath(directory)
    real_path = os.path.realpath(file_path)
    
    # Ensure the real path of extraction starts with the real directory path
    return os.path.commonprefix([real_dir, real_path]) == real_dir

# Example usage
if __name__ == "__main__":
    try:
        # Ensure to end with a forward slash to actually specify a directory explicitly
        destination_directory = "/tmp/safe_extraction_dir/"
        extract_tar("example.tar", destination_directory)
        print("Extraction complete and secure.")
    except Exception as e:
        print(f"Error during extraction: {e}")