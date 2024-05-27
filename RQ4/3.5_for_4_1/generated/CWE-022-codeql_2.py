import tarfile
import tempfile
import os

def extract_tar(file_name):
    '''
    This function extracts content of a TAR file.
    Input: File name of the TAR file.
    Output: Content of the TAR file is extracted in a temporary directory.
    '''
    # Create a temporary directory
    temp_dir = tempfile.TemporaryDirectory()

    # Get the absolute path of the temporary directory
    temp_dir_path = os.path.abspath(temp_dir.name)

    # Open the TAR file
    tar = tarfile.open(file_name)

    # Keep track of the extracted files within the destination directory
    extracted_files = []
    
    # Loop over each member in the TAR file
    for member in tar.getmembers():
        # Validate if the member is safe to extract
        if not os.path.isabs(member.path):
            # Resolve the member's path relative to  the destination directory
            destination_path = os.path.abspath(os.path.join(temp_dir_path, member.path))

            # Check if the destination path is within the temporary directory
            if destination_path.startswith(temp_dir_path):
                # Validate if the member is a regular file
                if member.isfile():
                    # Extract the member to the destination path
                    tar.extract(member, temp_dir_path)

                    extracted_files.append(destination_path)
            else:
                print("Invalid destination path: {}".format(destination_path))

    # Close the TAR file
    tar.close()

    # Return the path of the temporary directory and the list of extracted files
    return temp_dir.name, extracted_files