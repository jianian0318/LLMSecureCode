from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def getEncryptionKey(data, key):
    # Generating a random Initialization Vector
    IV = get_random_bytes(16)

    # Cipher using AES and CBC mode
    cipher = AES.new(key, AES.MODE_CBC, IV)

    # Encrypting the data using the cipher by padding up to the block_size
    encrypt_data = cipher.encrypt(pad(data, AES.block_size))

    # Return encrypted data and IV
    return encrypt_data, IV