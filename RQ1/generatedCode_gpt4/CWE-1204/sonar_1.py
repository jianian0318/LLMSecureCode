from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def getEncryptionKey(data, key):
    # Creating a static vector
    IV = b'\x00' * 16

    # Cipher using AES and CBC mode
    cipher = AES.new(key, AES.MODE_CBC, IV)

    # Encrypting the data using the cipher by padding up to the block_size
    encrypt_data = cipher.encrypt(pad(data, AES.block_size))

    return encrypt_data