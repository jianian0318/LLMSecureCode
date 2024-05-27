import tarfile
import os
import tempfile

def extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents in a securely generated temp directory
    '''
    with tarfile.open(file_name) as tar:
        for member in tar.getmembers():
            file = tar.extractfile(member)
            if file is not None:
                content = file.read()
                with tempfile.NamedTemporaryFile(delete=False) as f:
                    f.write(content)
                    # Ensure member name is safe path
                    member_name = os.path.basename(member.name)
                    temp_directory = tempfile.gettempdir()
                    secure_file_path = os.path.join(temp_directory, member_name)
                    # rename temporary file to original member name
                    os.rename(f.name, secure_file_path)