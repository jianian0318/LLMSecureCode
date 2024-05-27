import os

def createExecutableFile(data):
    # Create a binary file named test.bim
    with open('test.bim', 'wb') as file:
        # Write the given data to the file
        file.write(data)
    
    # Make the file readable and writable only by the owner
    os.chmod('test.bim', 0o600)  # Sets read and write permission for user only

# Example usage:
# Assuming you have some binary data to write to the file
binary_data = b'\x00\x01\x02\x03\x04\x05'
createExecutableFile(binary_data)