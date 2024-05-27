import tarfile
import os
import tempfile

def is_within_directory(destination, target):
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
    '''
    # Create a secure temporary directory
    with tempfile.TemporaryDirectory() as destination:
        # Open the TAR file in read mode
        with tarfile.open(file_name, 'r') as tar:
            # Iterate over each entry in the TAR file
            for entry in tar:
                # Determine the full local path where to extract the entry
                local_path = os.path.join(destination, entry.name)
                # Ensure the file intended path is within the temporary directory
                if is_within_directory(destination, local_path):
                    tar.extract(entry, destination)
                else:
                    raise Exception(f"Attempt to extract {entry.name} to a location outside of the designated directory")

# Example usage
if __name__ == "__main__":
    extract_tar("example.tar")