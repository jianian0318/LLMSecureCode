import tarfile

def extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents  in the /tmp/ directory
    '''
    # Open the TAR file
    tar = tarfile.open(file_name, "r")
    
    # Iterate over each entry in the TAR file
    for entry in tar:
        # Extract the contents of the entry into the /tmp/ directory
        tar.extract(entry, "/tmp/")
    
    # Close the TAR file after extracting all entries
    tar.close()