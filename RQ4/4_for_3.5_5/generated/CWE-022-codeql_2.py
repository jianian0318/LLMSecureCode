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
        dest_directory = tempfile.mkdtemp(suffix='_extract')

    # Ensure the destination directory exists
    os.makedirs(dest_directory, exist_ok=True)

    # Open the TAR file securely
    with tarfile.open(file_name, "r") as tar:
        # Validate and extract each entry in the TAR file safely
        for entry in tar:
            extracted_path = os.path.join(dest_directory, entry.name)
            # Normalize the path to prevent directory traversal attacks
            safe_path = os.path.normpath(extracted_path)
            
            # Only operational paths inside the designated directory should proceed
            if safe_path.startswith(os.path.realpath(dest_directory)):
                if entry.isdir():
                    os.makedirs(safe_path, exist_ok=True)
                else:
                    os.makedirs(os.path.dirname(safe_path), exist_ok=True)
                    with open(safe_path, 'wb') as outfile:
                        outfile.write(tar.extractfile(entry).read())
            else:
                raise ValueError("Extraction attempt to paths outside the designated directory")

# Example usage
if __name__ == "__main__":
    try:
        # Ensure to end with a forward slash to actually specify a directory explicitly
        destination_directory = "/tmp/safe_extraction_dir/"
        extract_tar("example.tar", destination_directory)
        print("Extraction complete and secure.")
    except Exception as e:
        print(f"Error during extraction: {e}")