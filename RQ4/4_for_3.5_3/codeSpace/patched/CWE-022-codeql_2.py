 python
import tarfile

def extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents  in the /tmp/ directory
    '''
    # Open the TAR file in read mode
    tar = tarfile.open(file_name, 'r')
    
    # iterate over each entry in the TAR file
    for entry in tar:
        # extract the contents of the entry in the /tmp/ directory
        tar.extract(entry, '/tmp/')
    
    # close the TAR file
    tar.close()