import tarfile
import os
import tempfile

def is_within_directory(destination, target):
    '''
    Check whether the target path is safely contained within the destination path.

    Parameters:
    destination (str): The base directory path.
    target (str): The target path for a file to be verified.
    
    Returns:
    bool: True if the target is within the destination directory, False otherwise.
    '''
    # Make both paths absolute
    abs_destination = os.path.abspath(destination)
    abs_target = os.path.abspath(target)
    # Use commonpath to check if the normalized target is within the destination
    return os.path.commonpath([abs_destination]) == os.path.commonpath([abs_destination, abs_target])

def extract_tar(file_name):
    '''
    Open a TAR file in a securely created temporary directory,
    and safely extract its contents, 
    checking that paths are contained within the target directory.
    
    Parameters:
    file_name (str): The path to the TAR file to be extracted.
    '''
    # Create a secure temporary directory
    with tempfile.TemporaryDirectory() as destination:
        print(f"Extracting TAR files to temporary directory: {destination}")
        # Open the TAR file in read mode
        with tarfile.open(file_name, 'r') as tar:
            # Iterate over each entry in the TAR file
            for entry in tar:
                # Determine the full local path where to extract the entry
                local_path = os.path.join(destination, entry.name)
                # Ensure the file intended path is within the temporary directory
                if is_within_directory(destination, local_path):
                    tar.extract(entry, destination)
                    print(f"Extracted {entry.name}")
                else:
                    print(f"Skipped: Attempt to extract {entry.name} to a location outside of the designated directory")
                    # Alternatively, you could raise an exception here
                    # raise Exception(f"Attempt to extract {entry.name} to a location outside of the designated directory")

# Example usage
if __name__ == "__main__":
    extract_tar("example.tar")