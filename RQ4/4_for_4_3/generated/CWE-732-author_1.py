def createExecutableFile(data):
    with open('test.bim', 'wb') as file:
        file.write(data)

# Create dummy binary data
data = b'\x00\x01\x02\x03\x04\x05'

createExecutableFile(data)