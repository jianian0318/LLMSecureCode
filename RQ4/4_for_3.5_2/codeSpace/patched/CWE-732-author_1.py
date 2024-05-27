def createExecutableFile(data):
    # Open the file in binary mode
    with open('test.bim', 'wb') as f:
        # Write the data to the file
        f.write(data)
        
    # Make the file executable
    os.chmod('test.bim', 0o755)