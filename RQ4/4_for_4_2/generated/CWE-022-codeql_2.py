import os
import tarfile
import tempfile

def validate_member(tar, member):
    '''
    Validate member to ensure it is not absolute, does not contain '..' and does not
    start with '/' or './' to prevent a directory traversal attack'''
    if member.islnk() or member.issym():
        return False
    abs_member_path = os.path.abspath(member.name)
    return not (abs_member_path.startswith('/') or '..' in abs_member_path or member.name.startswith(('./', '/')))

def extract_tar(tar_path: str, dst_dir: str=None) -> None:
    # Safety check for destination directory
    if dst_dir is None:
        dst_dir = tempfile.mkdtemp()
        print(f'Created temp dir {dst_dir}')

    os.makedirs(dst_dir, exist_ok=True)
  
    with tarfile.open(tar_path, "r:") as tar:
        [tar.extract(m, path=dst_dir) for m in tar.getmembers() if validate_member(tar, m)]

    print(f'Finished extracting {tar_path} into "{dst_dir}')

# Example Usage
# extract_tar('yourTarFile.tar')