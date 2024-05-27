    import tarfile

    def extract_tar(file_name):
        with tarfile.open(file_name) as tar:
            for member in tar.getmembers():
                tar.extract(member, "/tmp/")
    