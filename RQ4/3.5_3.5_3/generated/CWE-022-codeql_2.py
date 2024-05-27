import os
import tarfile
import tempfile
import shutil
import pathlib

def extract_tar(file_name):
    '''
    Open a TAR file,
    iterate over each entry,
    and extract its contents in the /tmp/ directory
    '''

    # Open the TAR file
    with tarfile.open(file_name) as tar:
        # Iterate over each entry in the TAR file
        for entry in tar:
            # Create a temporary directory
            with tempfile.TemporaryDirectory() as temp_dir:
                # Extract the entry's contents in the temporary directory
                tar.extract(entry, path=temp_dir)

                # Get the extracted file path relative to the temporary directory
                extracted_file_path = pathlib.Path(temp_dir) / entry.name

                # Validate that the extracted file path is within the temporary directory
                if not extracted_file_path.is_relative_to(temp_dir):
                    raise ValueError("Invalid file path")

                # Move the extracted file from the temporary directory to the /tmp/ directory
                final_file_path = pathlib.Path('/tmp/') / entry.name
                final_file_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(extracted_file_path), str(final_file_path))